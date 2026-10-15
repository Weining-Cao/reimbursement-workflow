# First-use package check

Checked on 2026-10-15 using the v4 share ZIP, then a freshly extracted v5 candidate.
This was a maintainer-run onboarding rehearsal, not an independent novice study
or a new Codex client session. Only public files and synthetic case data were used.

## Observed friction and fixes

| First-use step | Observed friction | Change |
| --- | --- | --- |
| Give the workflow to a chat without filesystem access | The reader had to collect several linked references and templates manually | The share ZIP now includes `START_CHAT.txt`, generated from the canonical sources; one attachment or full-text paste carries the resources |
| Use the starter prompt after installing only the Skill folder | The old prompt's repository-relative workflow path did not exist in the new case directory | The prompt resolves resources from the supplied Skill folder or included chat sections |
| Choose where to put case files and how to begin | The README did not show a complete no-install prompt or installed-folder layout | Separate local-file, chat, and installed-Skill routes with explicit locations and a small starting request |
| Run the optional commands from the case directory | The repository-relative example path failed there | State the required working directory and separate developer checks from reimbursement intake |
| Repeat the example record command | Exclusive creation correctly returned an existing-lock error, but the recovery was easy to miss | Explain expected output, use `check` for the same snapshot, and choose a new lock for a new revision |
| Try the example without running code | The example explained expected decisions but did not supply a starting request | Add a text-only trial prompt using three existing synthetic inputs and a concrete next action |

## Executed checks

- Extracted the share package into a fresh temporary directory; copied the whole
  Skill into a separate case directory whose name contains spaces. Its entrypoint
  and linked resources resolved without relying on the original repository.
- Checked local Markdown links in both the extracted package and installed Skill.
- Generated the chat export from an unrelated working directory and compared it
  byte-for-byte with the copy in the candidate share ZIP. All source sections were
  present; no separately requested reference was needed to read the workflow.
- Ran the README's record/check commands from the documented package root; observed
  recorded and unchanged results. Repeating record was rejected without overwrite.
- Copied the entire synthetic example to a scratch case, recorded it, changed only
  the scratch summary, and observed the expected stale result and exit code 1.
- Reviewed the three synthetic inputs and independently recomputed USD 145.50 and
  EUR 64.20 with decimal arithmetic. The scratch review retained the date conflict,
  intentional blank, and user-confirmed paper status; it did not assert PDF readiness.
- Ran 13 standard-library tests from the extracted package, covering freshness and
  chat-export completeness, exclusion of unrelated case data, execution outside
  the repository, overwrite refusal, and missing-source failure without partial output.
- Verified the supplied package files remained unchanged after the trial. Skill
  frontmatter validation also passed.

The recorded rehearsal used macOS and Python 3.9.6; the same 13-test suite also
passed on Python 3.14.7. The documentation recommends Python 3.10+ for optional
helpers; no Python installation is needed to consume the prebuilt chat export
or follow the workflow in a capable agent.

## Limits

This checked extraction, paths, bundled resources, commands, and a text-only first
review. It did not launch a fresh Codex UI, verify Skill auto-discovery in a new
client, upload the attachment to another chat provider, or test every operating
system. Installation guidance was checked against the [official skills documentation](https://learn.chatgpt.com/docs/build-skills).
The synthetic trial did not exercise mail connection, authenticated portals, Word
editing, PDF rendering/assembly, or finance acceptance. Those paths require their
own host capabilities and applicable evidence; a successful start is not a completed
claim.
