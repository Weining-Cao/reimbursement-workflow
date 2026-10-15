---
name: reimbursement-workflow
description: Help complete travel reimbursement from missing materials to finance review. Find applicable rules, guide website steps, retrieve invoices from authorized mailboxes, fill the original form, and review the final PDF for avoidable rejection. Not general accounting or tax advice.
---

# Reimbursement Workflow

Read [the canonical workflow](references/workflow.md) before handling case files. Follow the requested scope; resume from the current case state instead of restarting intake.

Use [case.md](assets/case.md), [expenses.csv](assets/expenses.csv), and [review.md](assets/review.md) as working templates in the private case directory. Keep resources in this skill folder unchanged during case work.

Discover available browser/search, mailbox, file, and document tools. Use [collection.md](references/collection.md) to close missing-material gaps through those tools and targeted user handoffs. Reuse existing scoped access; do not ask the user to manually find files the agent can already retrieve. Report unavailable capabilities precisely. If workspace document dependencies are exposed, inspect them before editing.

After assembly, use [finance-review.md](references/finance-review.md) to assess the actual packet against the applicable requirement matrix, repair failures, and repeat affected checks. A completed download or generated PDF is not the acceptance criterion. Do not install software or call external services merely because they appear in an example.

For optional file freshness checks, read [integrity.md](references/integrity.md), then run `scripts/check_packet.py` with explicit manifest and lock paths. A successful check is only an unchanged-file result.

Return links to the completed case artifacts and a concise review outcome. Do not open applications in the foreground unless requested.
