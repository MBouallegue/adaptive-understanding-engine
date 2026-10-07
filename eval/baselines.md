# Comparison conditions

The engine is condition D. These are the conditions it is compared against.

Run every baseline session with the skill switched off. If it is installed, the agent may pick it up unprompted the moment you say you want to understand something, and the baseline stops being a baseline. In Claude Code, run `claude plugin disable adaptive-understanding-engine` before a baseline session and `claude plugin enable adaptive-understanding-engine` afterwards.

Use the opening line exactly, replacing `<concept>`. After that, behave as you normally would: ask follow-up questions, ask for examples, say when you are lost. The time budget is the same in every condition and the timer decides when you stop.

## A · Plain explanation

```
Explain <concept> to me. I'm a backend engineer and I want to understand it properly.
```

## B · Explanation with examples

```
Explain <concept> to me with concrete examples and code I can read. I'm a backend engineer and I want to understand it properly.
```

## C · Interactive questioning

```
Teach me <concept> by asking me questions one at a time and responding to my answers. Don't lecture. I'm a backend engineer and I want to understand it properly.
```

## D · The engine

With the skill enabled:

```
/understand <concept>
```

## Keeping the comparison fair

- **Same tool and model** in every condition, so the tool is not what differs.
- **Same budget.** One timer, one length, every session.
- **Same freedom.** You may ask anything in any condition. Do not hold back in A to make D look good, and do not coast in D.
- **An empty folder.** Run every session in an empty folder so that no project instructions apply.
- **Check your global settings.** An output style or an instructions file in your home directory applies to every condition, including the baselines. Remove it for the study, or accept that it is part of all four.
- **The learner file.** Decide once whether the engine keeps its learner file between concepts. Keeping it is closer to real use and is part of what is being tested. Write the decision in the pre-registration.
