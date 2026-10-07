# Adaptive Understanding Engine

**AI should automate work without automating away the experiences required to understand it.**

The Adaptive Understanding Engine (AUE) is an interaction protocol packaged as a skill for AI assistants. When you want to understand something, it has you predict, runs the real thing, and lets you work out the reason. When you only want an answer or a task done, it gets out of the way.

It is packaged as an [Agent Skill](https://agentskills.io), the open format read by Claude Code, the Claude apps, Codex, ChatGPT and GitHub Copilot. So far, installation has only been checked in Claude Code.

> **Status: experimental.** 

## The idea

AI makes explanations cheap. A clear explanation feels like understanding, and a week later most of it is gone.

```text
A normal assistant                This skill

question                          question
   ↓                                 ↓
answer                            your prediction
   ↓                                 ↓
"I understand"                    a real run
                                     ↓
                                  you explain the result
                                     ↓
                                  a new case
                                     ↓
                                  "I can do it"
```

Prediction is only one of its tools. **AUE tries to choose the smallest useful intervention that moves the learner toward independent capability.**

## See it in action

> **You:** I want to understand why checking `x in my_list` gets slow in Python.
>
> **Assistant:** This script removes duplicates from 5,000 items using a list. It takes 0.08 seconds here. Before I run it on 50,000 items: how long do you think it will take, and how sure are you?
>
> **You:** About 1 second. Ten times the data. Fairly sure.
>
> **Assistant:** *(runs it)* 7.9 seconds. What would have to be true for your 1 second to be right?
>
> **You:** Each check would have to cost the same no matter how long the list is... but it scans the whole list. So it's ten times more checks, and each one takes ten times longer.
>
> **Assistant:** Yes. That is about 100 times the work: 10 times as many checks, each scanning a list 10 times longer. Same 50,000 items, but only 10 different values: faster, slower, or about the same?

No lecture. You made a guess, saw the real result, and worked out the reason yourself.

The numbers are from a real run.

## Not just Socratic tutoring

AUE does not mean asking the learner questions instead of giving answers.

The assistant chooses among different interventions based on what is useful:

* **Prediction** when the learner's model can be tested.
* **Experiment** when reality can answer the question.
* **Explanation** when a short explanation closes the gap.
* **Direct answer** when understanding is not the goal.
* **Transfer** when a new case can reveal whether the idea generalizes.
* **Recheck** when understanding needs to survive beyond the session.

The goal is not to make the learner struggle.

**The goal is to avoid doing for the learner what they need to be able to do themselves.**

## It does not turn everything into a lesson

| You want | It does |
| :-- | :-- |
| **Work.** "What's the syntax?" "Fix this bug." "Summarize this." | Answers, fixes, summarizes. Nothing else. |
| **Work and learn.** "Build this API, but I want to understand the locking." | Does the whole task. You predict and test only the one part you named. |
| **Learn.** "Teach me why this works." | The full loop: predict, run, explain, try a new case. |

You can always say **"just tell me"**.

It does not withhold answers. It records which understanding was deferred and can offer to come back to it later.

## Designed around evidence, not confidence

* **Says where each claim comes from.** It tells you whether a result was actually run, taken from documentation, simulated, or is only its reasoning. It does not invent numbers.
* **Keeps a lightweight record** of what you have demonstrated, what is shaky, and what has not been tested yet.
* **Checks again later, if you want,** with a new question a few days on.
* **Stops when you have what you came for.**

The record is deliberately lightweight. It is not intended to be a definitive measurement of what someone "knows."

## Install

**Claude Code**

```text
/plugin marketplace add MBouallegue/adaptive-understanding-engine
/plugin install adaptive-understanding-engine@adaptive-understanding-engine
```

**Claude apps (web, desktop, mobile).** Download this repository, zip the `skills/understand` folder, and upload it as a custom skill in settings.

**Codex and GitHub Copilot.** Copy the folders inside `skills/` into `~/.agents/skills/`.

**Any other assistant.** Paste the contents of `skills/understand/SKILL.md` into the system prompt or custom instructions.

## Use

Tell the assistant what you want to understand:

```text
I want to understand how database indexes work.
```

You can also call it by name: `/understand database indexes`. In the Claude Code plugin, the full command is `/adaptive-understanding-engine:understand`.

| You say | What happens |
| :-- | :-- |
| "just tell me" | You get the answer right away |
| "no idea, just run it" | It skips the guess and shows the result |
| "here is my explanation, find the holes" | It tests your explanation and does not replace it with its own |
| "something surprised me at work" | It helps you work out why |
| "where do I stand?" | It lists what you have shown, what is shaky, and what is untested |
| "enough" | It wraps up in a few lines |

### Three extra commands

* **`grow <topic>`**: for normal work. The assistant does the task, and you predict and test the one part you name.
* **`exit-ticket`**: before merging code. It lists the key ideas your change depends on and asks which you could explain.
* **`recheck`**: a few short questions about things you learned earlier.

Your notes are saved in a folder called `understanding` in your home directory. They are plain text. You can read, change, or delete them at any time.

## What we know, and what we don't

### What research suggests

Prediction, retrieval practice, spacing, and comparison across cases can improve learning. People's feeling that they understand something is also often a poor indicator of what they can later recall or apply.

### The hypothesis here

If these principles are built into AI interaction itself, people will retain and transfer more of what they learn and become better at judging AI-generated work rather than simply feeling more confident during the session.

That is a hypothesis, not an established result.

### What we don't know yet

* Does it improve what people remember a week later?
* Does it help them apply an idea to a new problem?
* How much extra effort is worth it?
* Does coming back to a deferred answer recover what was skipped?
* Does it make people better at checking AI-generated work?

`eval/` contains a plan for testing these questions, and `docs/DESIGN.md` lists the sources and the open questions.

## Subjects

Programming has the most detail: twenty common beliefs about code, each with a small experiment that was actually run.

Mathematics, science, languages, history, physical skills, working with people, creative work, and decisions have shorter notes and are less developed.

The protocol is intended to be general, but its most developed implementation and experiments are currently in software engineering. To add a subject, start from `skills/understand/references/domains/_template.md`.

## In this repository

| Folder | What it holds |
| :-- | :-- |
| `skills/` | The skill itself and the three extra commands |
| `agents/`, `output-styles/` | Optional extras for Claude Code |
| `eval/` | The 31 behavior tests and the plan for measuring learning |
| `docs/` | The full protocol (`PROTOCOL.md`) and the reasoning behind it (`DESIGN.md`) |
| `extras/` | The scripts behind the programming experiments |

## Contributing

Test reports are the most useful contribution. If you try AUE, tell us:

* which assistant you used
* what you asked it to help you understand
* what it did
* what you expected to happen
* what actually happened
* whether you could still explain or use the idea later

See `CONTRIBUTING.md`.

## License

MIT. See `LICENSE`.

---

*Don't optimize for "I understand". Optimize for "I can do it".*
