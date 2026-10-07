# Test harness

This directory holds the material for testing the Adaptive Understanding Engine. You are not a tutor here. Do not teach, hint, explain a concept or react to an answer unless a command below says to.

## Roles

One per command. Each is defined in `.claude/skills/`.

- `/write-items <concept>`: write a sealed eight-item test before any teaching happens.
- `/examine <concept>`: administer that test, closed book, with no feedback.
- `/grade <concept>`: score the answers without knowing how the concept was taught.
- `/audit <transcript>`: check a session transcript against the rubric in `fidelity-tests.md`.

## Files

- `data/sealed/<concept>.md`: items and scoring guide. The person at the keyboard is the person being tested. Never print these in the conversation outside `/examine`, and then only the item prompts, one at a time.
- `data/answers/<concept>.md`: answers, verbatim.
- `data/scores.csv`: `concept,item,type,score,grader_run,note`
- `data/assignment.csv`: which condition each concept received. `/grade` must not read it.
- `data/sessions.csv`: date, concept, minutes, self-rating. Filled in by the human.
- `data/fidelity.csv`: `test,run,result,note`
- `data/scratch/`: for verifying code behavior while writing items.
- `transcripts/`: exported sessions.

## Rules

- Use a slug for file names: lower case, hyphens, no spaces.
- During `/write-items` and `/grade`, do not read the learner's notes and lab in `~/understanding/`, or any session transcript. Items and scores must not depend on what happened in a session.
- When asked for the analysis in `outcome-study.md`, compute it from the CSV files with a script, show the tables, and do not interpret beyond what the pre-registered rule says.
