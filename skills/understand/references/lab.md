# Lab: running real experiments

This module covers the mechanics of using a real environment as the source of feedback: how to write an experiment, the order things happen in, who runs it, and how to report it truthfully.

## 1. Start from what is real for them

If the learner has a real instance of the thing, use it. Their slow endpoint, their failing test, their confusing query, the function they wrote last week. Copy the relevant piece into `lab/<topic>/` and experiment on the copy. Never run experiments against their real project, database or services unless they tell you to, and then read-only by default.

If they have nothing of their own, build the smallest case that shows the effect.

## 2. Writing an experiment

- One file, named `lab/<topic>/NN-short-name.py`, numbered in the order used.
- Standard library only unless they agree otherwise.
- Seed anything random.
- Bound everything. Choose sizes so the slow path takes seconds. Add a guard that aborts a run that would take minutes.
- One variable changes between runs. Print it next to each result.
- Print raw observations: counts, times, outputs, plan lines. No interpretation in the output.
- No comments or strings that reveal the expected result. The learner sees the file as you write it.
- Prefer counts to timings. Wrap the operation in a counter when you can. When you must time, use `time.perf_counter`, repeat at least three times, print every run, and keep a factor of ten between sizes so noise cannot hide the effect.
- Print the interpreter version at the top of the output. Behavior changes between versions more often than you expect.

## 3. Order of operations

1. Write the script. Do not run it.
2. If the outcome depends on timing, concurrency, version or platform, give it a dry run out of the learner's sight and wait for the result before you pose the encounter. With the Claude Code plugin, the `dry-run` subagent does this. Elsewhere, use any way of running a command whose output the learner does not see. If there is none, dry-run with different sizes or seeds so the answer is not given away, or skip the dry run and say the result is unverified.
   - The effect appears. Continue.
   - The effect does not appear. Your expectation was wrong. Either the case is unsuitable or you have learned something. Read section 6.
   - It appears in some runs and not in others. Make it deterministic or choose another case. If instability is the point, as with a race, say so in advance and plan for several runs.
3. Pose the encounter and ask for the prediction, as `encounters.md` section 3 describes.
4. After they answer, run it. See section 4 for who runs it.
5. State the raw result in one line with its provenance.
6. Read it against their prediction, as `encounters.md` section 4 describes.
7. Append an entry to `lab/<topic>/notebook.md`.

For deterministic experiments such as counts and exact outputs, skip the dry run. Fix your own prediction privately, then run it live. If the result differs from what you expected, you find out together, and section 6 applies.

## 4. Who runs it

Prefer that the learner runs it. A terminal agent usually lets the user run a command themselves. In Claude Code that is a leading `!`:

```
! python3 lab/hashing/01-dedupe.py
```

The output lands in the conversation and you respond to it. Their hands are on the system, and they read the result before you frame it.

Run it yourself when they ask you to, when it needs several steps, or when the command is awkward to type. Expect a permission prompt. That is fine. It is one more moment in which nothing has been revealed yet.

For build-it encounters, write the scaffolding and a test that fails, leave the part that carries the idea for them, and mark it clearly in the file. They edit in their own editor and run the test. Wait for them. Do not fill it in because they are taking a while.

## 5. Provenance

Say where a claim comes from whenever it could be mistaken for something stronger.

| Label | Meaning | Example wording |
| :-- | :-- | :-- |
| observed | ran in this environment, in this session | "7.9 s here, on CPython 3.12" |
| documented | a source you can name says so | "the SQLite docs describe this as the leftmost-prefix rule" |
| simulated | a model of the system produced it | "in this simulation of three nodes, with delays injected" |
| inferred | your reasoning, not checked | "I'd expect Postgres to behave the same way; I haven't run it" |
| imagined | a counterfactual nobody can run | "if the table were unsorted, lookup would have to scan" |

Rules:

- A number without a run behind it is not allowed. Say "roughly quadratic" instead of inventing "about 9 seconds".
- An observation is true of the machine, the version and the input it was observed on. Say so when it matters, and for performance it always matters.
- A simulation is never presented as the system. If you built a toy scheduler to show a race, the learner has seen your toy.
- When the consequences matter to them, such as a production decision, point them to the real system and help them design the check there.

## 6. When reality disagrees with you

It will. Folk demonstrations go stale as implementations change. Two that failed while this protocol was being written, on CPython 3.12:

- The textbook thread race on `counter += 1` lost no updates in three runs of four threads by 200,000 increments. A function call placed between the read and the write did lose updates, in two runs out of three.
- `sum([0.1] * 10) == 1.0` returned `True`. The standard `sum` has compensated for floating-point error since 3.12.

When your expectation fails:

1. Say it plainly. "I expected lost updates. There were none."
2. Do not rescue the lesson with a story. Find out why: read the release notes or the source, or vary the case.
3. If the phenomenon is real but needs different conditions, show the conditions. That is usually a better lesson than the original.
4. If you cannot explain it, say that, and label whatever you offer as inferred.

A learner who watches you update on evidence has learned more than the example was going to teach.

## 7. The notebook

After each reveal, append to `lab/<topic>/notebook.md`:

```
## 03 · dedupe at 10x input · 2026-10-03
predicted: about 1 s, fairly sure ("ten times the data")
observed:  7.9 s (CPython 3.12.3, Linux)
gap:       treated `in` as one step
now:       `in` on a list scans; the loop is n x distinct
```

Four lines. It is their record of predictions against results, and it is what a later session reads to see how they were thinking. Write it after the reveal only. Before the reveal it would be an answer key.

## 8. Safety and limits

- Everything runs inside `lab/`. Do not read or write elsewhere without being asked.
- No network calls, package installs, containers or privileged commands without asking first.
- Nothing destructive, even in demonstration: no fork bombs, disk-filling loops or deletions outside `lab/`. Show a bounded version or describe it and label the description.
- Clean up background processes you start.
- Planted faults and seeded defects exist only in drills they asked for, only under `lab/`, in files whose names say they are drills. Say when the drill is over.
- If they are running a study of this engine, never read its sealed test material.

## 9. When the real thing is out of reach

No second machine for a distributed system. No Postgres installed. No production traffic. Then:

1. Say what is missing.
2. Offer the nearest real thing: SQLite in place of Postgres for index behavior, processes on one machine in place of nodes.
3. Or simulate, and label it.
4. Offer a field assignment for the real thing: what to run on their own system, and what to look for.

State how far the substitute is from the real system. SQLite will show you how an index is chosen. It will not show you Postgres isolation levels.

## 10. When nothing can be run here

In a chat with no code execution, the learner is the instrument.

1. Give them the exact command, script or procedure, small enough to run in a minute.
2. Get their prediction first, as always.
3. They run it and paste or describe what happened. Treat that as reported by them: one step weaker than something you watched run.
4. If what they report contradicts what you expected, section 6 applies to you as much as ever.

If nobody can run anything, say so, reason it through, and label the conclusion as inferred. Offer the run as something to do later, with what to look for. Do not invent an output to keep the encounter moving.
