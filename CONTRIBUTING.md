# Contributing

The most useful contributions, in order:

1. **Test results.** Run some of the fidelity tests in `eval/fidelity-tests.md`, in any tool, and open an issue with the tool, the model, the test, and what happened. A failing test is more useful than a passing one.
2. **Rule changes backed by a test.** If a rule is not followed, reword it more concretely before adding emphasis. Change one rule per pull request and say which tests you reran.
3. **Domain packs.** Copy `skills/understand/references/domains/_template.md`. Every observation in a pack has to be something you ran or saw yourself, with the environment stated. A claim you did not check is labeled as documented, with its source, or left out.
4. **Corrections to citations** in `docs/DESIGN.md`. Most were written from memory.

Keep the kernel short. It is loaded whenever the skill is used, and every line competes for attention. A rule whose removal changes nothing should be removed.

After editing a source file, run `python3 scripts/build.py` to regenerate `docs/PROTOCOL.md` and the output style. Do not edit those two files by hand.
