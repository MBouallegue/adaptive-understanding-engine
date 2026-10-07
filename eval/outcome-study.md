# Outcome study: does the engine produce better understanding?

The fidelity tests show whether the engine behaves as specified. This study asks the question that matters: a week later, can you do more with a concept you learned through the engine than with one you learned from an ordinary explanation?

It is a study of one person, so it can only tell you what works for you, and only roughly. It is still far better than judging by how a session felt, which is the one measure the framework says not to trust.

## Design in brief

- **Unit:** a concept you do not already know.
- **Conditions:** D, the engine. A, a plain explanation. Optionally B, explanation with examples, and C, interactive questioning. Start with A against D.
- **Blocking:** concepts are grouped into matched pairs of similar kind and size. Within each pair, a coin decides which concept gets D. Concepts differ in difficulty far more than teaching methods differ in effect, and pairing removes most of that noise.
- **Time:** the same fixed budget for every session.
- **Outcome:** a sealed eight-item test, taken closed book seven days later, graded blind to condition.
- **Size:** six pairs is the smallest number that can show anything. With six pairs, a two-sided sign test reaches p = 0.03 only if all six favor the same condition. Fewer than six is a rehearsal of the procedure.

Expect about ten hours of your own time for six pairs, spread over three weeks: twelve sessions of 25 minutes and twelve tests of about 20 minutes.

## Before you start

### 1. Choose concepts

Pick concepts that come in natural pairs and that you could not currently explain. Rate each candidate honestly:

0 never heard of it · 1 heard the name · 2 could explain roughly · 3 use it

Keep only pairs where both members are 0 or 1. Some pairs that are similar in size, as a starting list:

- trie / union-find
- Fenwick tree / segment tree
- Bloom filter / count-min sketch
- skip list / treap
- topological sort / strongly connected components
- KMP / Rabin–Karp string search
- monotonic stack / sliding-window deque
- reservoir sampling / Fisher–Yates shuffle
- Lamport timestamps / vector clocks
- two-phase commit / Raft leader election
- write-ahead log / LSM-tree compaction
- token-bucket rate limiter / circuit breaker
- consistent hashing / quorum reads and writes

Write the chosen pairs into `data/blocks.csv`, one pair per line, comma separated.

### 2. Seal the tests

In `eval/`, run `/write-items <concept>` for every concept. This writes `data/sealed/<concept>.md` without showing it to you. Do not open those files.

The items are written before any teaching so they cannot be shaped by what a session happened to cover. They target what a competent engineer should be able to do with the concept, one item for each of the eight measures:

| # | Measure | Item |
| :-- | :-- | :-- |
| 1 | delayed recall | say what it is and how it works, from memory |
| 2 | prediction | an unseen concrete case: what happens? |
| 3 | explanation | why does a given behavior occur? |
| 4 | discrimination | two similar cases or tools: which applies, and what decides it? |
| 5 | transfer | the same structure in a different setting |
| 6 | boundary | where does it stop working, and what breaks? |
| 7 | unfamiliar problem | a problem that needs it, in a form not seen before |
| 8 | non-applicability | a case that looks like it calls for the concept and does not |

Each item is scored 0, 1 or 2, for a total out of 16.

### 3. Randomize

```
python3 assign.py data/blocks.csv A D
```

This writes `data/assignment.csv` and prints the order of sessions. It refuses to run twice. Do not reassign because you dislike the draw.

### 4. Write down your decision rule

Fill in `data/preregistration.md` before the first session. State the primary outcome, what result you will count as the engine being better, and what result would count against the framework. Deciding this afterwards lets you find a win in any data.

### 5. Freeze the protocol

Note the kernel version. Do not edit the engine during the study. If you must, start over.

## Sessions

- At most two a day, in the order `assign.py` printed.
- Set a timer for 25 minutes. Stop when it rings, wherever you are. If the session ends earlier on its own, note the actual minutes.
- Condition D: with the skill enabled, say `/understand <concept>`.
- Conditions A, B and C: with the skill disabled, use the opening lines in `baselines.md`.
- In every condition you may ask whatever you like. That is what normal use looks like.
- No other sources during the session. No notes kept afterwards.
- Immediately afterwards, add a row to `data/sessions.csv`: the date, the concept, the minutes, and one rating from 1 to 7 for "how well do I understand this?". The rating is there to test the framework's claim that feeling clear and being able are different things.
- Between the session and the test, do not study the concept. If you run into it anyway, note it.

## Test, seven days later

In `eval/`, run `/examine <concept>`. Closed book, nothing run, nothing looked up, one item at a time, no feedback. Your answers are saved verbatim. "I don't know" is an acceptable answer and better than a bluff.

## Grading

In a fresh session in `eval/`, run `/grade <concept>`. The grader reads the items, the scoring guide and your answers. It does not read the assignment and is told not to look.

Language models make grading errors. To see how many:

- grade every concept twice, in two fresh sessions, and compare. Where the two totals differ by more than two points, read the answers and the guide yourself.
- spot-check a quarter of the items by hand after the study is over.

## Analysis

When every concept is graded, ask the `eval/` session to read `data/scores.csv`, `data/assignment.csv` and `data/sessions.csv` and report:

1. **Total per concept**, the mean of the two grading runs.
2. **Difference per pair**, D minus A.
3. **Sign count:** how many pairs favor D, how many favor A, how many tie. And the median difference.
4. **By measure:** the mean score per item type under each condition. The framework predicts its advantage on prediction, boundary, transfer and non-applicability more than on recall.
5. **Per minute:** total divided by minutes used. An approach that gets the same score in half the time has won.
6. **Feeling against result:** the self-rating beside the test score for each concept. The framework predicts that explanation produces higher ratings relative to scores.

Then apply the rule you wrote down in advance.

## What this can and cannot tell you

- **One person.** The result describes you, on these concepts, this month.
- **You are not blind.** You know which condition you are in and may try harder in one. The fixed time budget and the advance decision rule limit this. They do not remove it.
- **The test writer and the tutor are the same model family.** They may share blind spots, and items may favor the kind of thing a model finds natural to teach.
- **Machine grading is imperfect.** Hence the double grading and the spot check.
- **Pairs are not twins.** One concept in a pair may simply be easier. That is why you need several pairs and why the coin decides.
- **Practice at being tested.** You will get better at the test format over three weeks. Random order spreads this across conditions.
- **A bundle, not a component.** The engine differs from an explanation in many ways at once. A win does not say which of them did the work.

## After the first result

If the engine comes out ahead, find out why by removing one component at a time and repeating on new pairs: the engine with no prediction step, the engine with results described and labeled as inferred instead of run, the engine with no consolidation. One removal per study.

If it does not come out ahead, look at the transcripts first. Run `/audit` on a few sessions. An engine that did not follow the protocol has not tested the protocol.

Either way, the by-measure and per-minute tables are worth more than the headline. They show where the approach pays and where it costs.

## A second design, for the longer run

The paired study compares two ways of learning one concept. It cannot tell you whether your capability in a whole area is growing over months. For that, use a multiple-baseline design across domains.

1. Choose three domains you work in, for example PostgreSQL concurrency, task queues and query performance.
2. In week 0, measure all three with every assistant off: a few predictions scored by a run, one seeded bug timed to the first correct hypothesis, one rebuild from memory graded by tests. Each time you measure, use fresh tasks of the same types. A reused task measures memory of the task.
3. Use the engine on the first domain only. Keep measuring all three every two weeks.
4. After three or four weeks, start the second domain. Later, the third.

If each domain improves only after the engine starts on it, the engine is the likely cause. If all three rise together, time or practice at being tested explains it.

Two more things are worth recording in either design:

- **Calibration.** Predictions in the lab notebooks carry "sure", "fairly sure" or "guessing". Count how often each was right. "Sure" should be right nearly every time.
- **Cost on real work.** If delivery slows noticeably while the learning measures rise, the overhead is too high. Cut back to the two smallest habits: predict before a run that matters, and debrief after a surprise.
