# Adaptive Understanding Engine

A skill for AI assistants that teaches by letting you find out, not by lecturing.

Ask a normal assistant to explain something and you get a clear explanation. It feels good, and a week later most of it is gone. This skill works differently. It asks what you expect to happen, runs the real thing, and lets you compare. When your guess is wrong, that is where the learning happens.

It works for programming and for other subjects. It runs in Claude Code, the Claude apps, Codex, ChatGPT, GitHub Copilot, and any other assistant that supports [Agent Skills](https://agentskills.io).

## Status

This is an early version. It installs correctly, but it has not yet been tested in real learning sessions. If you try it, please open an issue and say what happened.

## A short example

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
> **Assistant:** Yes. That is a hundred times the work. Same 50,000 items, but only 10 different values: faster, slower, or the same?

No lecture. You made a guess, saw the real result, and worked out the reason yourself.

## What it does

- **Asks for your guess first.** Then it runs the real thing and shows you the result.
- **Answers directly when you want that.** Say "just tell me" and it will. It never holds an answer back.
- **Does not turn everything into a lesson.** Quick questions get quick answers. Tasks get done.
- **Is honest about what it knows.** It tells you whether a result was actually run or is only its reasoning. It does not invent numbers.
- **Remembers what you have shown you can do,** in a plain text file you can read and edit.
- **Checks again later, if you want,** with a new question a few days on, to see what stuck.
- **Stops when you have what you came for.**

## Install

**Claude Code**

```
/plugin marketplace add MBouallegue/adaptive-understanding-engine
/plugin install adaptive-understanding-engine@adaptive-understanding-engine
```

**Claude apps (web, desktop, mobile).** Download this repository, zip the `skills/understand` folder, and upload it as a custom skill in settings.

**Codex and GitHub Copilot.** Copy the folders inside `skills/` into `~/.agents/skills/`.

**Any other assistant.** Paste the contents of `skills/understand/SKILL.md` as the system prompt or custom instructions.

## How to use it

Tell the assistant what you want to understand:

```
I want to understand how database indexes work.
```

You can also call it by name: `/understand database indexes`. In the Claude Code plugin the full command is `/adaptive-understanding-engine:understand`.

Useful things to say during a session:

| You say | What happens |
| :-- | :-- |
| "just tell me" | You get the answer right away |
| "no idea, just run it" | It skips the guess and shows the result |
| "here is my explanation, find the holes" | It tests your explanation and does not replace it with its own |
| "something surprised me at work" | It helps you work out why |
| "where do I stand?" | It lists what you have shown, what is shaky, and what is untested |
| "enough" | It wraps up in a few lines |

Your notes are saved in a folder called `understanding` in your home directory. They are plain text. You can read, change or delete them at any time.

## Extra commands

- **`grow <topic>`**: use this during normal work. The assistant does the whole task, but for the one part you name, you guess first and a real run decides.
- **`exit-ticket`**: before you merge code, it lists the key ideas your change depends on and asks which ones you could explain.
- **`recheck`**: asks a few short questions about things you learned earlier.

## Subjects

Programming has the most detail: twenty common beliefs about code, each with a small experiment that was actually run. Mathematics, science, languages, history, physical skills, working with people, creative work and decisions have shorter notes. To add a subject, start from `skills/understand/references/domains/_template.md`.

## What is in this repository

| Folder | What it holds |
| :-- | :-- |
| `skills/` | The skill itself and the three extra commands |
| `agents/`, `output-styles/` | Optional extras for Claude Code |
| `eval/` | 31 test situations for checking that an assistant follows the rules, and a plan for measuring whether it helps people learn |
| `docs/` | The full text in one file (`PROTOCOL.md`) and the reasoning behind it (`DESIGN.md`) |
| `extras/` | The scripts behind the programming experiments |

## Contributing

Test reports are the most useful contribution: which assistant you used, what you asked, and what it did. See `CONTRIBUTING.md`.

## License

MIT. See `LICENSE`.
