#!/usr/bin/env python3
"""Record/check byte freshness only; never certify a reimbursement packet."""

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path, PurePosixPath
import sys


def digest(path):
    result = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            result.update(chunk)
    return result.hexdigest()


def snapshot(manifest_path):
    manifest_path = Path(manifest_path).resolve(strict=True)
    raw = manifest_path.read_bytes()
    manifest = json.loads(raw)
    if not isinstance(manifest, dict) or set(manifest) != {"version", "inputs", "outputs"}:
        raise ValueError("Manifest must contain only version, inputs, and outputs")
    if type(manifest["version"]) is not int or manifest["version"] != 1:
        raise ValueError("Unsupported manifest version")
    root = manifest_path.parent
    seen = {manifest_path}
    files = {}
    for role in ("inputs", "outputs"):
        entries = manifest[role]
        if not isinstance(entries, list) or not entries:
            raise ValueError(f"{role} must be a nonempty list of relative file paths")
        for name in entries:
            if not isinstance(name, str) or not name or "\\" in name:
                raise ValueError("Use nonempty relative paths with forward slashes")
            relative = PurePosixPath(name)
            if relative.is_absolute() or ".." in relative.parts or ":" in name:
                raise ValueError(f"Path must stay inside the case directory: {name}")
            path = (root / name).resolve(strict=True)
            if not path.is_relative_to(root) or not path.is_file():
                raise ValueError(f"Not a regular file inside the case directory: {name}")
            if path in seen:
                raise ValueError(f"Duplicate file or manifest self-reference: {name}")
            seen.add(path)
            files[name] = {"role": role, "sha256": digest(path)}
    return {
        "version": 1,
        "manifest_sha256": hashlib.sha256(raw).hexdigest(),
        "files": files,
    }


def record(manifest_path, lock_path):
    current = snapshot(manifest_path)
    current["recorded_at"] = datetime.now(timezone.utc).isoformat()
    payload = json.dumps(current, indent=2, sort_keys=True) + "\n"
    # Exclusive creation also protects existing documents from accidental overwrite.
    with Path(lock_path).open("x", encoding="utf-8") as stream:
        stream.write(payload)


def check(manifest_path, lock_path):
    saved = json.loads(Path(lock_path).read_text(encoding="utf-8"))
    if not isinstance(saved, dict) or set(saved) != {
        "version", "manifest_sha256", "files", "recorded_at"
    }:
        raise ValueError("Invalid lock structure")
    if type(saved["version"]) is not int or saved["version"] != 1:
        raise ValueError("Unsupported lock version")
    if not isinstance(saved["files"], dict):
        raise ValueError("Invalid lock file map")
    current = snapshot(manifest_path)
    changes = []
    if saved["manifest_sha256"] != current["manifest_sha256"]:
        changes.append("manifest changed")
    for name in sorted(set(saved["files"]) | set(current["files"])):
        if saved["files"].get(name) != current["files"].get(name):
            changes.append(f"file changed, added, or removed: {name}")
    return changes


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("record", "check"))
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--lock", type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        if args.command == "record":
            record(args.manifest, args.lock)
            print("Snapshot recorded. This does not establish build correctness or readiness.")
            return 0
        changes = check(args.manifest, args.lock)
        if changes:
            for change in changes:
                print(f"STALE: {change}")
            return 1
        print("UNCHANGED: listed files match the snapshot; content and visual review still required.")
        return 0
    except (OSError, ValueError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
