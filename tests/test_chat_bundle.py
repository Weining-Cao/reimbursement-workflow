import importlib.util
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/export_chat_bundle.py"
SPEC = importlib.util.spec_from_file_location("export_chat_bundle", SCRIPT)
bundle = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(bundle)


class ChatBundleTests(unittest.TestCase):
    def test_export_is_complete_and_excludes_unrelated_case_files(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            for relative in bundle.SOURCES:
                copy = root / relative
                copy.parent.mkdir(parents=True, exist_ok=True)
                copy.write_bytes((ROOT / relative).read_bytes())
            (root / "private-case.txt").write_text("PRIVATE_SENTINEL", encoding="utf-8")
            destination = root / "START_CHAT.txt"
            bundle.export(root, destination)
            text = destination.read_text(encoding="utf-8")
            self.assertNotIn("PRIVATE_SENTINEL", text)
            for relative in bundle.SOURCES:
                self.assertIn((root / relative).read_text(encoding="utf-8").rstrip(), text)
                for target in re.findall(r"\]\(([^)]+)\)", (root / relative).read_text(encoding="utf-8")):
                    if "://" in target or target.startswith("#"):
                        continue
                    target_path = (root / relative.parent / target.split("#", 1)[0]).resolve()
                    self.assertIn(target_path, {(root / p).resolve() for p in bundle.SOURCES})

    def test_cli_works_outside_repo_and_refuses_overwrite(self):
        with tempfile.TemporaryDirectory(prefix="chat trial ") as folder:
            destination = Path(folder) / "chat instructions.txt"
            args = [sys.executable, str(SCRIPT), str(destination)]
            result = subprocess.run(args, cwd=folder, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            original = destination.read_bytes()
            result = subprocess.run(args, cwd=folder, capture_output=True, text=True)
            self.assertEqual(result.returncode, 2)
            self.assertEqual(destination.read_bytes(), original)

    def test_missing_source_leaves_no_partial_export(self):
        with tempfile.TemporaryDirectory() as folder:
            destination = Path(folder) / "START_CHAT.txt"
            with self.assertRaises(FileNotFoundError):
                bundle.export(Path(folder), destination)
            self.assertFalse(destination.exists())


if __name__ == "__main__":
    unittest.main()
