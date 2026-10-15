# From partial materials to a finance-ready packet

This is an illustrative interaction for a separate fictional case, not a tool execution log, an institutional policy, or a claim of actual acceptance. It does not change the unresolved state of the neighboring text fixtures. Portal names, requirement IDs, and outcomes below are hypothetical; a live run must discover real sources and inspect real artifacts.

## Starting point

The user says: "I attended a workshop. I have the tickets and a hotel receipt, but I do not know what else finance needs. Help me finish the reimbursement."

The agent inspects those files, then asks only for missing context: which institution and traveler category apply, and which funding route if it affects the process. It discovers the available browser, mailbox, and document tools. The user has already authorized reading one mailbox; the agent reuses that scope.

The agent finds and reads the institution's official instructions and original form. In this fictional case, the sources establish these requirements:

| ID | Required result | Initial finding | Next action |
| --- | --- | --- | --- |
| R1 | Original form with required fields | No template supplied | Download the verified official template |
| R2 | Registration invoice and matching payment proof | No registration documents supplied | Search the authorized mailbox for merchant/order/date |
| R3 | Lodging receipt with stay details and payment proof | Receipt lacks stay dates | Find booking details and request the matching payment export |
| R4 | Stamped approval, separate paper permitted | User has only a portal preview | Locate the official pickup instructions |
| R5 | Required department review before finance submission | Not completed | Prepare the form for that office, then obtain the reviewed copy |

The agent does not stop at this table. It follows the next actions.

## Collection loop

1. **Registration:** search results include a "payment successful" email and another message containing an invoice link. The agent inspects both, validates the invoice link destination, downloads the existing invoice, and matches its amount and buyer title to the case. The payment notice is counted as supporting evidence only if it meets R2; neither email is a second expense. A link to the same invoice in a later email is deduplicated.
2. **Lodging:** the agent retrieves a booking statement showing the stay dates. The required payment record is in the user's bank app, which the agent cannot access. It asks the user to export that specific transaction with the fields R3 requires, while filling the form from verified information. When the export arrives, the agent checks the match before closing R3.
3. **Approval:** the agent opens the verified official collection page at the user's request and identifies the pickup step. The user completes the identity check and collects the stamped paper. The agent records user-confirmed-paper, the permitted delivery route, and that it has not inspected the paper digitally. It does not add a missing-upload blocker when separate paper is allowed.
4. **Department review:** the agent prepares and renders the form for the preceding office. It labels this an intermediate deliverable, not ready for final finance submission. The user returns the completed review; the agent verifies the required completion before closing R5.

If any acquired item has an incorrect title, missing field, or conflicting amount, the corresponding gap stays open. The agent locates the correction route and prepares a specific request; it sends or submits that request only if authorized. Waiting on an issuer does not block unrelated work.

## Assembly and rejection rehearsal

The agent fills the original form, verifies amounts by currency, exports and inspects the summary, and assembles the packet with a page map. It then reviews the combined PDF against R1–R5.

The first pass finds that the lodging payment proof was saved locally but omitted from the combined PDF. R3 is a fail despite a complete source folder. The agent inserts it beside the lodging evidence, rebuilds the packet, checks the updated page map, and repeats the affected checks. The final review locates each requirement's support in the exact packet or the permitted paper handoff.

Only then does the agent mark the case ready-for-user-submission and return the PDF plus the precise paper delivery steps. Its review states which physical documents were user-confirmed. It does not report that finance has already accepted anything.

## Actual outcome loop

After submission, a user report of "accepted without changes" supports accepted-without-rework. "Submitted" alone leaves outcome-unknown. If finance requests a correction, record returned-for-correction and the exact reason. Repair the case when requested and add a synthetic regression scenario if the cause could have been caught before submission.

For example, "the lodging payment proof existed but was omitted" becomes a permanent packet-level check. A new funding-specific requirement is recorded with its applicability instead of becoming a rule for every traveler.
