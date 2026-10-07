---
name: exit-ticket
description: Before a merge, names the mechanisms the current diff depends on and records the ones the user cannot explain, for the Adaptive Understanding Engine. Use only when the user explicitly asks for an exit ticket or invokes this skill by name.
license: MIT
---

Look at the current diff: the changes against the base branch, or the staged changes.

1. Name the one to three mechanisms the change depends on to be correct. Mechanisms, not files: "the row lock taken before the balance check", "the retry is safe because the handler is idempotent".
2. List any consequential choice you made that the user did not review: an isolation level, a timeout, a retry policy, an authorization check, a deletion.
3. For each item ask one thing only: "could explain" or "could not". Take their word for it. Do not quiz them.
4. Offer to append each "could not" as a line in `~/understanding/frontier.md`:

`<date> | <mechanism> | <repo, file or PR> | could not explain`

Keep it under a minute. If they say "skip", stop. Do not add learning notes to the repository being worked on.
