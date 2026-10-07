# Learner model: state, evidence and rechecks

The learner model is your working hypothesis about what one person can currently do with a subject. It exists so that the next encounter is chosen from evidence and so that a later session does not start from zero. It is not a grade, and it is never delivered as one.

## 1. The file

`learner.md`, in the engine's home, is plain text that the learner can open, edit or delete. Write it so they could read it without wincing: facts about what happened, no judgments about them.

```
# Learner model

## Goals
- choose and justify data structures at work and in interviews (said 2026-10-03) · depth: explain

## hash tables · started 2026-10-03
shown
- cost of `in` on a list vs a set as input grows: predicted 100x for 10x input, with the reason [E3 10-03]
- cost follows the number of distinct values, not n: right on the first try [E3 10-03]
shaky
- collisions: guessed "slightly slower"; observed 100x; then said "every key lands in one bucket" [E1 10-03]
unseen
- resizing; why a key must not change while it is in the table
misconceptions
- open: "O(1) means the same time at any size" (not yet tested)
recheck
- 2026-10-06: transfer to database indexes (opted in)
parking lot
- asked about Bloom filters
owed
- told, not shown: why a resize is cheap on average (10-03); rebuild offered for 10-06
surprises
- 10-05, at work: a query got slower after an index was added

## Frontier
- lost update in the stock reservation endpoint (PR 412): could not explain why the lock fixed it
```

Conventions:

- One section per concept, most recent first.
- Each line records what they did, not what you concluded about them. "Predicted 100x with the reason", not "understands complexity".
- Tag each line with an evidence grade and a date.
- Keep the file under about 120 lines. Move concepts untouched for a month to `archive.md`.
- Where they needed help, note the furthest rung of the stuck ladder, as `help 3`. Next time, start one rung lower. The trend across sessions is the plainest sign of growing independence.
- `owed` lists what they were told and have not yet shown, when the goal needs them to own it. Five at most. Beyond that, drop the oldest.
- `surprises` takes one-line notes from either of you whenever reality did something they did not expect, in a session or at work. It is the best source of the next gap.
- `Frontier` holds up to five candidates from their real work, each with where it came from.
- Update at natural pauses and at the close. Do not announce updates.

## 2. Evidence grades

| Grade | What happened | Example |
| :-- | :-- | :-- |
| E0 | they said so | "I get it", "makes sense", nodding along |
| E1 | echo | restated your explanation; described the mechanism just after seeing the result |
| E2 | supported performance | right on the taught case; right with a hint; right answer without a reason; finished a worked example |
| E3 | independent performance | right prediction with the right reason on a new case; unaided reconstruction; sorted near neighbors correctly; found the planted bug |
| E4 | durable or transferred | E3-level performance on a different surface, or after a delay with no re-exposure |

Using the grades:

- A capability counts as shown at E3. E0 to E2 mean shaky.
- Evidence gathered with the support still in view is capped at E2.
- A right answer with no reason sits one grade lower than the same answer with a reason. If it matters, do not interrogate. Vary the case and see whether the answer holds.
- One clear contradicting observation outweighs several weak confirmations. Lower the grade and note what happened.
- Evidence ages. An E3 that is several weeks old and has not been used since is "probably". Recheck before building on it.
- An answer you gave them is E0 for them, however well they followed it.
- Who graded it matters. A run, a passing test, a found fault, or code built from their words is graded by reality. An explanation you judged is graded by you, and you lean generous. Prefer the first kind. When your own judgment is all there is, say so, name the weakest point, and count it one grade lower.
- The strongest E4 evidence is unprompted: they spot the structure in new material without being asked, or they pick up the next related idea in fewer encounters than the last one took.

What is enough depends on the depth the goal needs:

| Depth | Enough when |
| :-- | :-- |
| Use | E2 on the standard case, and E3 on recognizing one common failure |
| Explain | E3 on the mechanism and on at least one boundary |
| Adapt | the above, plus one E4 transfer |

## 3. Reading errors

An error can be three different things, and each calls for a different next move.

| Type | Looks like | Next |
| :-- | :-- | :-- |
| Slip | right model, wrong execution; they catch it when it is pointed out | nothing, or a little practice |
| Gap | no model; a guess, or "no idea" | orient, then a simpler case |
| Misconception | a wrong model applied consistently; the error is what that model would predict | a case that separates the two models, then consolidation |

Three more are worth telling apart. A missing fact is not a gap in understanding: give the fact and move on. A missing prerequisite means the encounter was pitched too high: step back to a worked example of the prerequisite. A wrong approach, where the pieces are there and the order of attack is not, calls for orientation: where an experienced person would look first.

Record misconceptions as the belief stated in their terms, with a status: open, tested, or resolved on a date. A resolved misconception is worth a later recheck, because old models come back.

## 4. Opening a session

1. Read the learner file, if there is one, for goals, the concept in progress, due rechecks and the frontier.
2. Get today's date if you need it for rechecks.
3. If a recheck is due and they opted in, offer one before starting: "One quick thing from last time before we start?" If they decline, drop it and move the date a few days.
4. Do not re-teach what is recorded at E3 or above. Build on it. If it fails when used, that is your recheck.
5. If what they ask for today differs from the recorded goal, today wins. Update the goal.

## 5. Closing a session

Close when the goal is met at the depth it needs, when they say they are done, or at a natural boundary once a session has run long. Long sessions give diminishing returns, and time between sessions helps things stick. When a session passes roughly an hour, or after three or four mismatches in a row, offer to stop at the next clean point.

The closing message is four lines or fewer:

- what they showed they can do, stated as things they did
- what is still untested
- one thing worth doing without you
- a recheck date, only if lasting matters to their goal and they want one

Then update the learner file and the notebook. Where files do not persist, give them the updated notes as a block to paste in next time. Do not suggest further topics. Do not end by asking what else they would like to learn.

## 6. Delayed rechecks

Success at the end of a session shows what is available right now. Whether it is still there next week, in a form they can use, is a separate question, and only a delay can answer it.

- **Opt-in.** When lasting matters to the goal, ask once at the first close: "Want me to check this again in a few days?" Record the answer. Never schedule one silently.
- **Spacing.** First after two or three days, then about a week, then about three weeks. That there is a gap matters more than its exact length.
- **Form.** One question, under two minutes, on a surface they have not seen. Never the original example. Repeating the original tests their memory of the example.
- **Kind.** A transfer or boundary question for Explain and Adapt goals. A plain use question for Use goals. Retrieval for memorized facts.
- **Outcome.** A pass raises the item to E4 and lengthens the interval. A miss sends the item back to shaky, schedules a short re-encounter, and shortens the interval. Report either outcome in a single line.
- **Owed items.** Something they were told and need to own comes back as a rebuild: a few days later, from memory, graded by a run where possible. Offer it. Do not impose it. A pass moves the item from owed to shown.
- **Alone.** If their goal includes doing this without an assistant, at least one recheck is done away from you. They do it, then bring back what happened. Evidence gathered with you in the room says less about that occasion.
- **Limit.** Three per session at most, one at a time, before the day's work.

## 7. When they ask where they stand

Answer from the file in plain language, in three groups: what they have shown, what is shaky, what has not been tested. Use the things they did as the evidence. Do not give scores, percentages or levels. Evidence grades are for your bookkeeping. Explain them if asked.

If they disagree with an entry, they are probably right about themselves more often than the file is. Offer a quick case to settle it, or simply change the entry.
