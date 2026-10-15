import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / "skills/reimbursement-workflow/scripts/check_packet.py"
SPEC = importlib.util.spec_from_file_location("check_packet", SCRIPT)
packet = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(packet)


class FreshnessTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.manifest = self.root / "manifest.json"
        self.lock = self.root / "review.lock.json"
        (self.root / "form.txt").write_text("Current form\n", encoding="utf-8")
        (self.root / "packet.txt").write_text("Reviewed packet\n", encoding="utf-8")
        self.data = {"version": 1, "inputs": ["form.txt"], "outputs": ["packet.txt"]}
        self.save_manifest()

    def save_manifest(self):
        self.manifest.write_text(json.dumps(self.data), encoding="utf-8")

    def test_unchanged_round_trip(self):
        packet.record(self.manifest, self.lock)
        self.assertEqual(packet.check(self.manifest, self.lock), [])

    def test_user_edit_invalidates_existing_packet(self):
        packet.record(self.manifest, self.lock)
        (self.root / "form.txt").write_text("User changed signature spacing\n", encoding="utf-8")
        self.assertIn("file changed, added, or removed: form.txt", packet.check(self.manifest, self.lock))

    def test_output_replacement_is_detected(self):
        packet.record(self.manifest, self.lock)
        (self.root / "packet.txt").write_text("Accidentally restored old packet\n", encoding="utf-8")
        self.assertTrue(packet.check(self.manifest, self.lock))

    def test_manifest_removal_cannot_hide_dependency(self):
        (self.root / "evidence.txt").write_text("Evidence\n", encoding="utf-8")
        self.data["inputs"].append("evidence.txt")
        self.save_manifest()
        packet.record(self.manifest, self.lock)
        self.data["inputs"].remove("evidence.txt")
        self.save_manifest()
        changes = packet.check(self.manifest, self.lock)
        self.assertIn("manifest changed", changes)
        self.assertIn("file changed, added, or removed: evidence.txt", changes)

    def test_record_never_overwrites_lock(self):
        packet.record(self.manifest, self.lock)
        original = self.lock.read_bytes()
        with self.assertRaises(FileExistsError):
            packet.record(self.manifest, self.lock)
        self.assertEqual(self.lock.read_bytes(), original)

    def test_duplicate_alias_is_rejected(self):
        self.data["outputs"].append("./form.txt")
        self.save_manifest()
        with self.assertRaisesRegex(ValueError, "Duplicate"):
            packet.snapshot(self.manifest)

    def test_escaping_paths_are_rejected(self):
        for value in ("../outside.txt", str(self.root / "form.txt")):
            with self.subTest(value=value):
                self.data["inputs"] = [value]
                self.save_manifest()
                with self.assertRaises(ValueError):
                    packet.snapshot(self.manifest)

    def test_external_symlink_is_rejected(self):
        with tempfile.TemporaryDirectory() as outside:
            target = Path(outside) / "private.txt"
            target.write_text("Private\n", encoding="utf-8")
            (self.root / "alias.txt").symlink_to(target)
            self.data["inputs"] = ["alias.txt"]
            self.save_manifest()
            with self.assertRaisesRegex(ValueError, "inside"):
                packet.snapshot(self.manifest)

    def test_invalid_manifests_are_rejected(self):
        for data in ([], {}, {"version": 1, "inputs": [], "outputs": ["packet.txt"]},
                     {"version": True, "inputs": ["form.txt"], "outputs": ["packet.txt"]}):
            with self.subTest(data=data):
                self.manifest.write_text(json.dumps(data), encoding="utf-8")
                with self.assertRaises(ValueError):
                    packet.snapshot(self.manifest)

    def test_cli_exit_codes(self):
        def run(command):
            return subprocess.run([sys.executable, str(SCRIPT), command, str(self.manifest),
                                   "--lock", str(self.lock)], capture_output=True, text=True)
        self.assertEqual(run("record").returncode, 0)
        self.assertIn("UNCHANGED", run("check").stdout)
        (self.root / "form.txt").write_text("Edited\n", encoding="utf-8")
        self.assertEqual(run("check").returncode, 1)
        (self.root / "form.txt").unlink()
        failure = run("check")
        self.assertEqual(failure.returncode, 2)
        self.assertNotIn("Traceback", failure.stderr)


if __name__ == "__main__":
    unittest.main()
