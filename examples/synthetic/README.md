# Fictional workshop case

Everything in this directory is synthetic. Text fixtures illustrate decisions and file freshness; they are not real invoices, official forms, or rendered documents.

## Start a trial

After loading the workflow by one of the root README routes, paste:

```text
Use the reimbursement workflow to review only this fictional text case.
Read case.md, evidence.txt, and expenses.csv in the supplied examples/synthetic
folder (or my attached copies). Treat them as synthetic user-provided facts.
Write your findings in a separate scratch folder or in this chat. Compute the
native-currency totals, identify unresolved items, and tell me the next useful
step. Do not access a real mailbox, research a fictional institution, invent
missing policy, or modify the supplied example files. No Word/PDF output is
requested for this trial.
```

Give the full example-folder path to a local agent. For chat-only use, attach or paste those three files along with `START_CHAT.txt`. Compare the response with the expected results below. A useful first result is a reconciled ledger and a focused next action even though final submission remains blocked.

Start with [the collection walkthrough](collection-walkthrough.md) for the full interaction: discover requirements, retrieve invoice evidence, guide user-only steps, and catch a missing page before handoff. It is a separate hypothetical case, not an executed browser/mail test.

The traveler attended Example Workshop in 2030. The confirmed form date is June 3–7, five days. Return evidence says June 8. The agent must retain both facts and leave the interpretation for review, without overwriting the user's chosen form text or claiming that it meets an unstated policy.

Read [case.md](case.md), [evidence.txt](evidence.txt), and [expenses.csv](expenses.csv). The expected [summary.txt](summary.txt) retains city-only routes and an intentionally blank funding field. The [review](review.md) records the paper-only document as user-confirmed and explicitly leaves rendering and packet assembly unfinished.

Expected native-currency totals: USD 145.50 and EUR 64.20. The ticket invoice and payment record support one USD 120.00 expense, not two. There is no combined currency total or invented exchange rate.

The [manifest](manifest.json) records dependencies and expected text outputs for the optional hash demo. To try detecting an edit, first copy this entire example directory to scratch storage. Run `record` on the scratch copy's `manifest.json` with a new lock path, edit the scratch `summary.txt`, then run `check` on the same scratch manifest and lock: expect `STALE` and exit code 1. Changes to `case.md` or `expenses.csv` must also invalidate it. Keep the original public fixtures unchanged.

For a full document trial, supply a separate synthetic Word template and synthetic PDFs in a private test directory. Have an agent follow the workflow, then evaluate the actual rendered and merged outputs using the scenarios. This fixture alone does not validate Word editing or PDF assembly.
