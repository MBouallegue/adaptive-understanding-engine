#!/usr/bin/env python3
"""Regenerate the two generated files from their sources.

Run from the repository root:   python3 scripts/build.py

    output-styles/adaptive-understanding-engine.md   the kernel as a Claude Code output style
    docs/PROTOCOL.md                        everything in one file, for reading

Edit the sources, never these two files.
"""
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
SKILL = "skills/understand/SKILL.md"
REF = "skills/understand/references/"


def strip_frontmatter(text):
    if text.startswith("---\n"):
        return text.split("\n---\n", 1)[1]
    return text


def body(path, demote=1, drop_title=False):
    text = strip_frontmatter((ROOT / path).read_text())
    out, in_fence, dropped = [], False, False
    for line in text.strip("\n").split("\n"):
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
        elif not in_fence and re.match(r"#{1,5} ", line):
            if drop_title and not dropped and line.startswith("# "):
                dropped = True
                continue
            line = "#" * demote + line
        out.append(line)
    return "\n".join(out).strip("\n") + "\n"


def fenced(path):
    return f"`{path}`\n\n````text\n{(ROOT / path).read_text().strip()}\n````\n"


# 1. The output style: the kernel, sent with every request.
kernel = strip_frontmatter((ROOT / SKILL).read_text()).strip("\n")
style = f"""---
name: adaptive-understanding-engine
description: Always-on mode for the Adaptive Understanding Engine. The kernel of the understand skill, sent with every request.
---

{kernel}

## 8. In this mode

This text is the kernel of the `understand` skill, loaded as an output style so that it applies to every message. The reference modules live in that skill's folder. If you do not know where that is, invoke the `understand` skill once at the start of the session.
"""
(ROOT / "output-styles/adaptive-understanding-engine.md").write_text(style)

# 2. The reading copy.
INTRO = """# Adaptive Understanding Engine: protocol v1.2

One file containing everything in the repository, in reading order. It is generated. To change the protocol, edit the source files and run `python3 scripts/build.py`.

```
message -> gate -> lookup:        answer in a few lines
                -> task:          do it (it may carry one mechanism to own)
                -> understanding: pick the gap
                                  -> choose the smallest encounter that separates models
                                  -> get a prediction, if one is worth making
                                  -> let reality answer
                                  -> they read the result, then you do
                                  -> consolidate in five lines
                                  -> update the model of the learner
                                  -> stop, or go round again
```

## How to read this

- **Changes** come first, newest at the top.
- **Part I, the kernel,** is what the model reads whenever the skill is used. About 1,700 words. If you read one part, read this.
- **Part II, the reference modules,** is what the model opens when it needs it: intake, encounters, the lab, the learner model, and the domain packs.
- **Part III, testing,** is for you: 31 behavioral tests, then a paired randomized study with a delayed test.
- **Part IV, design notes,** says what was decided and why, and separates what the research supports from what is still a bet.
- **The appendices** hold the README and the small files.
"""

parts = [
    INTRO,
    "# Changes\n\nSource: `CHANGELOG.md`.\n",
    body("CHANGELOG.md", demote=0, drop_title=True),
    f"# Part I · The kernel\n\nSource: `{SKILL}`.\n",
    body(SKILL),
    f"# Part II · Reference modules\n\nSource: `{REF}`. Each is read when the kernel calls for it.\n",
    body(REF + "intake.md"),
    body(REF + "encounters.md"),
    body(REF + "lab.md"),
    body(REF + "learner-model.md"),
    body(REF + "domains/software.md"),
    body(REF + "domains/other-domains.md"),
    body(REF + "domains/_template.md"),
    "# Part III · Testing\n\nSource: `eval/`. Fidelity first, then outcomes.\n",
    body("eval/fidelity-tests.md"),
    body("eval/outcome-study.md"),
    body("eval/baselines.md"),
    "# Part IV · Design notes\n\nSource: `docs/DESIGN.md`.\n",
    body("docs/DESIGN.md", demote=0, drop_title=True),
    "# Appendix A · README\n\nSource: `README.md`.\n",
    body("README.md", demote=0, drop_title=True),
    "# Appendix B · The small files\n\nShort enough to show whole.\n",
    "## Skills\n",
    fenced("skills/recheck/SKILL.md"),
    fenced("skills/grow/SKILL.md"),
    fenced("skills/exit-ticket/SKILL.md"),
    "## Claude Code plugin\n",
    fenced("agents/dry-run.md"),
    fenced(".claude-plugin/plugin.json"),
    fenced(".claude-plugin/marketplace.json"),
    "## Test harness\n",
    fenced("eval/CLAUDE.md"),
    fenced("eval/.claude/skills/write-items/SKILL.md"),
    fenced("eval/.claude/skills/examine/SKILL.md"),
    fenced("eval/.claude/skills/grade/SKILL.md"),
    fenced("eval/.claude/skills/audit/SKILL.md"),
]
out = ROOT / "docs/PROTOCOL.md"
out.write_text("\n".join(parts))
print(f"wrote output-styles/adaptive-understanding-engine.md and docs/PROTOCOL.md ({len(out.read_text().split()):,} words)")
