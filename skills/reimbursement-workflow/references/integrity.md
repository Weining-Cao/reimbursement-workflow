# File freshness utility

`scripts/check_packet.py` uses only Python 3.10+ standard libraries. It hashes an explicit set of files. It does not build, parse, or visually review Word/PDF documents, prove that outputs correspond to inputs, or determine claim eligibility. It cannot detect an omitted dependency. The snapshot is a local change detector, not a signed audit log.

Create a JSON manifest in the private case directory:

```json
{
  "version": 1,
  "inputs": [
    "case.md",
    "expenses.csv",
    "rules.md",
    "original-template.docx",
    "working-summary.docx",
    "evidence/hotel-invoice.pdf"
  ],
  "outputs": [
    "summary.pdf",
    "packet.pdf",
    "review.md"
  ]
}
```

Paths are relative to the manifest directory. Include every dependency that could invalidate the handoff, including the current editable Word file and the page manifest (which may be part of `review.md`). Paper items belong in `case.md`, not as nonexistent paths. Both lists must be nonempty. Duplicate resolved paths, parent traversal, absolute paths, missing files, directories, and symlinks escaping the case directory are rejected. The manifest and lock must not list themselves.

1. Finish editing, rebuilding, and visually reviewing the actual packet. Complete the review report.
2. Pause edits and run `record MANIFEST --lock NEW_LOCK`. The lock must not already exist. Record it only after checking the build, never to silence a stale result.
3. Run `check MANIFEST --lock LOCK` before handoff. Keep source files quiescent during hashing; there is no filesystem transaction or concurrent-writer protection.
4. If stale, identify the change, regenerate affected outputs, repeat the affected review, and record a new revision with a new lock path.

Exit codes: `0` = recorded or unchanged; `1` = changed manifest or file hashes; `2` = invalid data, missing/unreadable file, or other I/O error. Neither `1` nor `2` is a passing check. The tool never updates case status. A PDF can be wrong even when the command returns `0`.
