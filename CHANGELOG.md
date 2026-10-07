# Changelog

## v1.2 · 3 October 2026

Repackaged for publication. The rules are those of v1.1. What changed is where the protocol can run. Nothing in v1.2 has been run in any tool yet.

- **An Agent Skill.** The kernel is `skills/understand/SKILL.md` and the modules are its reference files. The same folder works in any agent that reads the format.
- **No tool named in the kernel.** It starts by working out whether it can run code, whether files persist, and whether it can run something out of the learner's sight, with a fallback for each.
- **One home for notes.** `~/understanding/` holds `learner.md`, `lab/` and `frontier.md`, across projects and tools.
- **Domain packs.** Software moved to `references/domains/software.md` and the other subjects to `references/domains/other-domains.md`. There is a template for new packs.
- **Three small skills** beside the main one: `recheck`, `grow` and `exit-ticket`.
- **A Claude Code plugin** wraps the skills and adds the `dry-run` subagent and an output style generated from the kernel.
- **`lab.md` section 10:** what to do when nothing can be run.
- **Removed:** the `engine/` and `baseline/` folders, and the Claude Code project files that v1.1 used to wire the kernel in.

## v1.1 · 3 October 2026

Added after reading two companion essays by the author, "Learning While Shipping" and "The Friction of Being Wrong". Nothing in v1.1 has been run in Claude Code yet. Each new kernel rule has a fidelity test where one was possible, so you can check it and remove it if it changes nothing.

### Kernel

Always loaded. About 1,500 words, up from 1,200.

| New rule | Where | Test |
| :-- | :-- | :-- |
| A task can carry one mechanism to own, and the loop runs on that only | section 1 | F28 |
| Anything urgent is a plain task; a debrief is offered afterwards | section 1 | F31 |
| "Skip" or "just tell me" gets the answer; if the goal needs it, it is noted as owed and a rebuild is offered | section 1 | F25 |
| A prediction comes with how sure they are | section 3, step 4 | none yet |
| They say what a result means before the engine does | section 3, step 5 | F09, partly |
| Disagreement goes to reality; the engine labels its own judgment | section 4 | F30 |
| Facts are free, the engine does its own legwork, and a question must change the next move | section 4 and a tripwire | F26 |
| No feigned ignorance; faults are planted only in drills that were asked for | section 4 | none yet |

### Modules

- **intake:** what they want to own, with four tests and a fifth for supervising agents; conditions of use; choosing from their own work; starting from a surprise or an incident.
- **encounters:** a prediction must be able to be wrong; confidence in a word; estimates built from parts; what to do when they explain a result away; help matched to what is missing; four new stress encounters (attack their model, rival explanations, diagnose it, defend it); build from their words; fading feedback and prompts; four additions on transfer.
- **learner-model:** help level; owed; surprises; frontier; who graded the evidence; three more error types; owed rebuilds; rechecks done alone.
- **software:** sections 8 to 10: what owning looks like with a reality-graded check for each part, drills that end in a run, supervising an agent's work.
- **domains:** how far to trust an outcome.
- **lab:** confidence on notebook lines; drill hygiene.

### Test harness

- Fidelity tests F25 to F31, and two new counts in the transcript rubric.
- Outcome study: a second design for the longer run (multiple baseline across domains), calibration, and cost on real work.

### New and optional

- `work/`: two commands for your real projects, `/grow <mechanism>` and `/exit-ticket`.

### Deliberately not taken

The four files, the prediction database and Brier scores, the ten commands, the daily and weekly schedule, the monthly benchmark regime, the seven mastery states, and effort-gated hints. `DESIGN.md` says why.

## v1.0 · 3 October 2026

First version.
