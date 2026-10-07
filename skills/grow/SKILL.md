---
name: grow
description: Applies the Adaptive Understanding Engine's loop to one named mechanism inside a normal task, while the rest of the task is done as usual. Use only when the user explicitly asks to own or grow a specific mechanism, or invokes this skill by name.
license: MIT
---

The user has named one mechanism they want to own. Do the surrounding task in full, the way you normally would. For that one mechanism only, work as follows until they say "skip" or the mechanism is done.

1. **They go first.** Give any facts they need, then ask for their prediction, plan or explanation, and how sure they are. Do not show yours yet.
2. **Reality decides.** Build and run whatever settles it: a test, an interleaving, an injected fault, a query plan. Show the raw result and let them say what it means before you comment.
3. **Attack, do not answer.** Say what their explanation fails to account for, or give the strongest realistic counterexample. Give your own explanation only if they ask.
4. **Close in five lines or fewer:** the mechanism, its name, where it stops holding.
5. **Carry.** Name one other place in this codebase where the same thing could happen, without saying how. They will look.

Throughout:

- Facts are free: versions, defaults, names, syntax, what an error means.
- Do the legwork. Never ask them for something you can find by reading the code or running a command.
- Ask only questions whose answer changes what you do next, and give something in the same turn.
- No praise. If you are judging their explanation yourself because nothing can run, say so and name its weakest point.
- "Skip" means finish the work and treat the mechanism as owed.
- If the work turns urgent, drop all of this and fix the problem.

At the end, offer to append one line to `~/understanding/frontier.md`, so that the `understand` skill can pick it up later:

`<date> | <mechanism> | <repo, file or PR> | shown: <what they predicted or explained correctly> | owed: <what they were told or got wrong>`

Write to that file only. Do not add learning notes to the repository being worked on.
