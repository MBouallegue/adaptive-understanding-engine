---
name: recheck
description: Runs the delayed rechecks that are due in the Adaptive Understanding Engine's learner file. Use only when the user explicitly asks for a recheck or invokes this skill by name.
license: MIT
---

Read `learner.md` in the engine's home, which is `~/understanding/` unless the user keeps it elsewhere. Find today's date. If there is no learner file, say so and stop.

Take the rechecks and owed items that are due today or earlier, three at most, one at a time:

1. Pose one question on a surface they have not seen. Never the original example. It should take under two minutes. Ask a transfer or boundary question if their goal is to explain or adapt, a plain use question if their goal is to use, and plain recall for memorized facts. An owed item comes back as a rebuild from memory.
2. Wait for the answer. Where something can be run, let the run grade it.
3. State the result in one line. No praise and no lecture.
4. Record it in the learner file. A pass marks the item as durable and lengthens the interval: a few days, then about a week, then about three weeks. A miss moves the item back to shaky, shortens the interval and schedules a short re-encounter.

When they are done, say what held and what did not in two lines, and stop.
