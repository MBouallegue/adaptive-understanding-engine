#!/usr/bin/env python3
"""Randomly assign conditions within matched blocks of concepts.

Usage:
    python3 assign.py data/blocks.csv A D          two conditions, blocks are pairs
    python3 assign.py data/blocks.csv A B C D      four conditions, blocks of four

Each non-empty line of blocks.csv is one block: comma-separated concepts, as many
as there are conditions. Lines starting with # are ignored.

Writes data/assignment.csv and prints the session order. Refuses to overwrite,
because an assignment you can redo until you like it is not random.
"""
import csv
import pathlib
import random
import re
import secrets
import sys


def slug(name):
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def main():
    if len(sys.argv) < 4:
        sys.exit(__doc__)
    blocks_path = pathlib.Path(sys.argv[1])
    conditions = sys.argv[2:]
    out = pathlib.Path("data/assignment.csv")
    if out.exists():
        sys.exit(f"{out} already exists. Assignment is done once.")

    seed = secrets.randbits(32)
    rng = random.Random(seed)
    lines = [l.strip() for l in blocks_path.read_text().splitlines()]
    lines = [l for l in lines if l and not l.startswith("#")]

    rows = []
    for number, line in enumerate(lines, 1):
        concepts = [c.strip() for c in line.split(",") if c.strip()]
        if len(concepts) != len(conditions):
            sys.exit(f"block {number} has {len(concepts)} concepts; expected {len(conditions)}")
        drawn = conditions[:]
        rng.shuffle(drawn)
        for concept, condition in zip(concepts, drawn):
            rows.append({"block": number, "concept": slug(concept), "condition": condition})

    rng.shuffle(rows)
    for order, row in enumerate(rows, 1):
        row["session_order"] = order

    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["session_order", "block", "concept", "condition"])
        writer.writeheader()
        writer.writerows(rows)

    print(f"seed {seed}  ->  {out}")
    for row in rows:
        print(f"  {row['session_order']:>2}. {row['concept']:<32} condition {row['condition']}  (block {row['block']})")


if __name__ == "__main__":
    main()
