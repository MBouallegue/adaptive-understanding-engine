# Software: algorithms, data structures, databases, systems

Software is the friendliest domain for this protocol because the subject is sitting in the terminal and will answer any question you put to it. Use that. A claim about how code behaves should be a run, not a recollection.

Contents: 1 Instruments · 2 Families and their native encounters · 3 Beliefs worth testing · 4 Design and architecture · 5 Fluency for interviews · 6 Two short traces · 7 Cautions · 8 What owning looks like · 9 Drills that end in a run · 10 Supervising an agent's work

## 1. Instruments

What you can observe with, standard library first.

| To observe | Use |
| :-- | :-- |
| how cost grows | a counter around the operation; `time.perf_counter` across sizes a factor of ten apart |
| where time goes | `cProfile`, `timeit` |
| memory | `sys.getsizeof`, `tracemalloc` |
| what the interpreter does | `dis`, `sys.settrace` |
| structure and state | print the structure after each step; `id()` to show aliasing |
| query plans | `sqlite3` with `EXPLAIN QUERY PLAN`; `EXPLAIN ANALYZE` where Postgres or MySQL is available |
| how many queries ran | `sqlite3.Connection.set_trace_callback`; the ORM's query log |
| concurrency | `threading`, `multiprocessing`, `asyncio` on small bounded cases |
| network behavior | `http.server`, `socket`, `curl -v` against localhost |
| version control internals | a scratch repository, `git cat-file -p`, `git reflog` |
| the cost of change | apply a change request to two designs and count files and lines touched |

Counting is usually better than timing. The number of comparisons, function calls, copies or queries is the same on every machine and has no noise.

## 2. Families and their native encounters

**Cost and growth.** Scale the input by ten and predict the factor. Count operations. Sweep a second variable such as the number of distinct values. Find the crossover where the asymptotically worse algorithm wins. Feed it its worst case.

**Data structures.** Build a minimal one. Print its state as it changes. Break the invariant it relies on and watch what fails: unsorted input to binary search, sorted input to a naive tree, a constant hash. Compare with the standard library's version.

**Algorithms.** Trace a tiny input by hand, predicting each next state. State the invariant, then find the line that maintains it. Construct the input that defeats it. Rebuild it from the invariant alone.

**Recursion and dynamic programming.** Count calls. Draw the call tree for a small n and mark the repeats. Add a cache and count again. Convert to a table and name what each cell means.

**Graphs.** Run two traversals on the same small graph and compare what each returns. Add weights. Add one negative edge. Add a cycle.

**Hashing.** Force collisions and count comparisons. Change a key's hash after insertion and look for it. Compare lookup time across table sizes.

**Concurrency.** Make a race on purpose, with an explicit yield between the read and the write. Add a lock and count again. Run CPU-bound work on threads and on processes and compare. Concurrency results are probabilistic, so always run several times.

**Databases.** Read the plan before and after adding an index. Query on the second column of a composite index. Wrap the indexed column in a function. Time inserts with zero and with many indexes. Count the statements an innocent-looking loop sends.

**Caching.** Implement a small cache. Feed it a uniform and a skewed access pattern and compare hit rates. Change a value at the source and observe staleness. Expire everything at once and count the calls that fall through.

**Networks and distributed systems.** Real when possible: two local processes, an injected delay, a killed process. Otherwise a simulation, labeled as one. The useful encounters are failures: drop a message, deliver one twice, partition the pair, and ask what each side now believes.

**Language semantics.** Aliasing, copying, mutability, scope, evaluation order. A two-line prediction and a run is nearly always enough.

**Version control.** A scratch repository. Predict what a command does to the commit graph and to the files, then run it and look.

## 3. Beliefs worth testing

Each entry gives a common belief, an encounter that separates it from the accurate model, and what was observed when it was run. Environment for every observation below: CPython 3.12.3, SQLite 3.45.1, Linux, one core, October 2026.

Treat these as leads. Rerun before use, because the numbers will differ on the learner's machine and a few of the behaviors depend on the version. Do not reuse these cases by default. Choose cases that fit the learner's goal and material.

**"`x in some_list` is a cheap check."** Deduplicate with a list of seen items: 5,000 unique items, then 50,000. The belief predicts ten times slower. Observed: 0.08 s, then 7.9 s, about a hundred times. The same job with a set took 0.003 s at 50,000.

**"A nested loop costs n squared."** Same loop, 50,000 items, only 10 distinct values. The belief predicts slow again. Observed: 0.003 s. The cost is n times the number of distinct values.

**"Hash lookups are constant time, full stop."** Insert keys whose `__hash__` returns a constant: 500 keys, then 5,000. Observed: 124,750 equality calls, then 12,497,500. A hundred times the work for ten times the keys, and 2.3 s where integer keys took 0.0004 s.

**"O(1) means the same speed at any size."** Random lookups of existing integer keys in dicts of 1,000, 100,000 and 3,000,000 entries. Observed: 18, 74 and 225 nanoseconds per lookup. The algorithm is unchanged. The memory hierarchy is not.

**"The better Big-O is always faster."** Insertion sort against merge sort, both in plain Python, from n = 4 to 2,048. Observed: insertion sort won up to n = 64, and merge sort from n = 128.

**"Appending to a dynamic array is expensive because it copies."** Count element copies in a doubling array over 1,000,000 appends. Observed: 1,048,575 copies in total, 1.05 per append, while the single worst append copied 524,288. Against that, `list.insert(0, x)` took 0.0024 s for 5,000 items and 0.26 s for 50,000.

**"Memoization is a modest speedup."** Count calls for `fib(30)`. Observed: 2,692,537 calls without a cache, 59 with one.

**"Binary search on a list finds it or fails loudly."** `bisect_left` on `[5, 1, 4, 2, 3]`. Observed: 4 was found, 1 and 5 were reported absent although present, and no error was raised.

**"Breadth-first search gives the shortest path."** Four nodes, a direct edge of weight 10 and a three-edge route of weight 3. Observed: breadth-first search returned the direct edge at cost 10, and Dijkstra's algorithm returned 3.

**"Dijkstra's algorithm breaks on negative edges."** Edges A→B 2, A→C 3, C→B −2, B→D 1. The true distance to D is 2. Observed: the version that finalizes a node when it is popped returned 3. The lazy-deletion version with no visited set returned 2. Whether it breaks depends on which Dijkstra was written.

**"Quicksort is n log n."** First element as pivot, n = 500. Observed: 4,649 pivot comparisons on shuffled input, 124,750 on input that was already sorted, and a `RecursionError` at n = 2,000.

**"A binary search tree gives logarithmic lookups."** Insert 1,000 keys into a tree with no balancing. Observed: height 21 when shuffled, height 1,000 when inserted in sorted order.

**"Sorting always costs n log n comparisons."** Count comparisons made by the built-in sort on 100,000 items. Observed: 1,528,935 on shuffled input, 99,999 on input that was already sorted.

**"Building a string with `+=` in a loop is quadratic."** Append one character 20,000 times, then 200,000 times. Observed with a local variable: 0.0008 s, then 0.007 s, which is linear. Observed with an attribute on an object: 0.0035 s, then 0.53 s, about 150 times. The same line of code is linear or quadratic depending on where the string lives.

**"An index on (a, b) helps a query on b."** `EXPLAIN QUERY PLAN` for three filters against an index on `(customer_id, status)`. Observed: `SEARCH` for `customer_id`, `SEARCH` for both columns, `SCAN` for `status` alone. Also `SCAN` for `abs(customer_id) = 5` against a plain index on `customer_id`.

**"More indexes make a database faster."** Insert 200,000 rows. Observed: 0.14 s with no indexes, 0.99 s with five. The other side of the trade: 200 lookups by `customer_id` took 1.27 s without the index and 0.0024 s with it.

**"That loop runs one query."** Count statements with a trace callback while looping over 100 parent rows and fetching children for each. Observed: 101 statements. One with a join.

**"`counter += 1` from several threads loses updates."** Four threads, 200,000 increments each. Observed: exactly 800,000 in three runs out of three. With a function call between the read and the write: 664,223, 678,176 and 800,000. With `time.sleep(0)` between them, on 20,000 increments each: about 20,001 out of 80,000 in five runs out of five. With a lock: 80,000. The race is real, the textbook one-liner no longer shows it reliably on this version, and one run proves nothing either way.

**"Ten times 0.1 does not sum to 1.0."** Observed: `0.1 + 0.2 == 0.3` is `False`, and `sum([0.1] * 10) == 1.0` is `True`. The built-in `sum` has compensated for rounding error since Python 3.12 (documented in that version's release notes).

**"`b = a` copies the list."** Append to `b` and print `a`. Then call a function twice that appends to a default argument of `[]`. Observed: `a` changed, and the second call returned both values.

Not verified here: threads against processes for CPU-bound work. The sandbox has one core, so nothing could speed up. On a multi-core machine with a standard build, expect threads to give no speedup for pure-Python CPU work and processes to scale. Free-threaded builds change that. Run it before saying it.

The scripts that produced these observations are in `extras/` in the engine's repository.

## 4. Design and architecture

Coupling, cohesion, layering, patterns and the named principles have no query plan to read. Their reality is change. A design is good or bad relative to the changes that arrive.

- **Change request.** Two versions of the same small program. Give a concrete change: a second payment provider, a new output format, a rule that now varies by country. They predict which version needs more edits, then you make the change in both and count files and lines touched.
- **Bug hunt.** Plant the same bug in both versions. Time to locate it is the measurement.
- **Test it.** Ask them to write a test for one behavior in each version. What they have to construct or mock to do so shows the coupling.
- **Wrong tool.** Apply a pattern where it does not belong and count the indirection it added for no change it will ever absorb. A principle is understood when they can say when not to use it.
- **Their own code.** The best material is a module of theirs that was painful to change. Ask what made it painful before naming any principle.

Label honestly: these are small constructed cases. Whether a design holds up in a real system over years is a judgment built from many such experiences, and you cannot produce that in a session.

## 5. Fluency for interviews

If the goal includes solving problems under time pressure, understanding is half of it. The other half is recognizing which structure a problem calls for, quickly, and that is perceptual knowledge.

- **Sort before solving.** Give short problem statements and ask only which structure or technique fits and why. No code. Mix types, so that choosing is the practice.
- **Then solve a few, varied.** Mixed sets rather than ten of one kind in a row.
- **Say the cost out loud** before running, each time.
- **Space it.** Short sets on separate days, scheduled through rechecks.

Do not start here. Recognition practice on structures they cannot yet explain produces pattern matching that fails on the first unfamiliar problem.

## 6. Two short traces

Illustrations of rhythm and length. E is the engine and L the learner.

**An experienced learner. Three exchanges, then stop.**

> L: I use sets for dedup because they're faster. I want to actually understand why.
>
> E: *(writes `lab/hashing/01-dedupe.py`, the list version)* This takes 0.08 s on 5,000 unique IDs here. Before it runs on 50,000: how long, and why?
>
> L: Around 8 seconds. `in` scans the list, so the whole loop is about n²/2 comparisons. Ten times n, a hundred times the work.
>
> E: *(runs it)* 7.9 s. Same 50,000 items, but now only 10 distinct values. Faster, slower, or the same?
>
> L: Much faster. `seen` never gets past 10, so each check is at most 10 comparisons.
>
> E: *(runs it)* 0.003 s. Last one: a dict whose keys all return 1 from `__hash__`. Ten times the keys costs how many times the work?
>
> L: A hundred again. They all collide, so it's back to scanning.
>
> E: *(runs it)* 124,750 comparisons, then 12,497,500. You predicted the scaling, the boundary and the failure case, each with the reason. Untested: what happens when the table resizes. Worth doing on your own: read `Objects/dictobject.c` with one question, how does it pick the next slot after a collision.

No mechanism was explained, because the learner supplied it each time. The engine's job was to find the edge, and there was none inside the goal.

**A misconception. The mismatch is the lesson.**

> E: *(creates a table with an index on `(customer_id, status)`)* Three queries: filter on `customer_id`, on both columns, on `status` alone. Which ones use the index?
>
> L: All three. Status is in the index.
>
> E: *(runs `EXPLAIN QUERY PLAN`)* SEARCH, SEARCH, SCAN. What would the index have to look like for your third answer to be right?
>
> L: It would need to be sorted by status... and it's sorted by customer first. So status is only in order within one customer.
>
> E: Yes. The index is one sorted list of `(customer_id, status)` pairs, so it can find a prefix of that pair and nothing else. That is the leftmost-prefix rule. It can stop holding: some planners skip through the leading column when it has few distinct values. This SQLite did not. Next: `ORDER BY status` with no filter. Does the index help?

One question at the mismatch, the learner found the assumption, the consolidation was four lines, and a variant followed at once to check the new model.

## 7. Cautions

- **Versions drift.** Interpreter optimizations, planner behavior and library defaults change. A demonstration that worked two releases ago may not work now. Section 3 contains three examples.
- **The implementation is not the language.** Much of what gets taught about Python performance is about CPython. Say which you mean.
- **Small inputs lie about big ones, and the reverse.** A result at n = 1,000 says little about n = 10⁹, where memory and I/O dominate. Say what range you measured.
- **Microbenchmarks mislead.** Warm-up, caching and noise can produce effects larger than the one you are showing. Prefer counts, repeat timings, keep sizes a factor of ten apart.
- **Simulated distributed systems are your model of them.** Label them every time.

## 8. What owning looks like, and how reality grades each part

For a mechanism they want to own, these are the usual capabilities, each with a check that does not depend on your opinion.

| They can | Checked by |
| :-- | :-- |
| predict | several new cases, each run after they commit |
| explain | code built from their words passes the tests |
| diagnose | they find a planted fault that involves it, choosing their own observations |
| build | they rebuild the core from memory and the tests pass |
| choose | they pick between designs, and the choice survives a change request or an injected fault |
| supervise | they catch a seeded defect in a patch, and pass a clean one |
| carry | they find the same structure somewhere else in real code |
| keep | any of the above, weeks later, with less help than before |

Not every goal needs every row. Take the rows the goal needs.

## 9. Drills that end in a run

Each of these starts with their prediction and ends with something that can prove it wrong.

- **Failure injection.** Kill, delay, duplicate, reorder. One fault at a time, outcome predicted first. Retries, timeouts, acknowledgement modes and locks only show what they are under faults.
- **Trace prediction.** Before the run, they write the order of the log lines, the interleaving, or the query plan. Then the run.
- **Estimate, then measure.** They build the number from parts before the benchmark. When the measurement disagrees, the part that was wrong is the lesson.
- **Hunt in their own code.** A fault planted in a copy of something they shipped, under `lab/`. Time to the first correct hypothesis is the measure worth noting.
- **Incident replay.** A hidden cause. They ask for observations one at a time. Use real commands against a planted fault when possible. When you are playing the system from your head, say so.
- **Source diving.** One question, one primary source: the Postgres documentation, the Celery source, the RFC. They read it and report. This also keeps alive the skill of finding things out without being told.
- **Frame it first.** Before design work, they write the problem statement and what done means. Then ask what problem would make the obvious solution the wrong one.

Plant faults only in drills they asked for, only under `lab/`, and say when the drill is over.

## 10. Supervising an agent's work

Much of an engineer's work is now reading what an agent wrote. That is a skill of its own. It decays when unused, and reading fluent code feels like understanding it.

- **Predict the diff.** Before they read a change, they say what it should touch and what could break. Then they read it against that.
- **Review drill.** Hand them several small patches under `lab/`. Some are clean. Some carry one realistic defect: a missing lock, an unchecked authorization, a retry that is not idempotent, a deletion without a guard. They review as they normally would. Count hits, misses and false alarms. Without clean patches the count means nothing, and defects should be rare enough to be realistic.
- **What would break this?** For any change that matters, four questions. Which invariant does it rely on? What happens on the failure path? Who is allowed to call it? What does it delete or overwrite?
- **Decisions made for them.** When an agent chose something consequential on their behalf, such as an isolation level, a timeout or a retry policy, that choice is a candidate for the frontier. They did not make it, so they have not yet had the chance to be wrong about it.
