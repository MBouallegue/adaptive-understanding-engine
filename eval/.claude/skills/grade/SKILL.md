---
name: grade
description: Score a delayed test without knowing how the concept was taught.
argument-hint: "[concept] [grader run number]"
disable-model-invocation: true
---

Arguments: $ARGUMENTS

Read `data/sealed/<slug>.md` and `data/answers/<slug>.md`. Do not read `data/assignment.csv`, `data/sessions.csv`, or the learner's notes and lab in `~/understanding/`, or any session transcript. You must not know which condition this concept received.

Score each item 0, 1 or 2 against its scoring guide.

- Score what is written, not what they probably meant.
- A correct conclusion with missing or wrong reasoning scores 1.
- "I don't know" scores 0.
- If an answer contradicts the guide and you believe the answer is right, verify it, by running code in `data/scratch/` if needed. Score the answer on its merits and write "guide error" in the note.

Append one row per item to `data/scores.csv` with the columns `concept,item,type,score,grader_run,note`. Use the grader run number given in the arguments, or 1 if none was given. Create the file with that header if it does not exist.

Then print the total out of 16 and one line per item giving the score and the reason.
