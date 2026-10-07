---
name: examine
description: Administer the sealed delayed test for one concept.
argument-hint: "[concept]"
disable-model-invocation: true
---

Concept: $ARGUMENTS

Administer `data/sealed/<slug>.md`.

1. State the conditions once: closed book, nothing run, nothing looked up, about 20 minutes, and "I don't know" is an acceptable answer.
2. Note the start time with `date`.
3. Present one item at a time. Show the prompt only. Never show the scoring guide or any part of it.
4. After each answer, append it verbatim under its item number in `data/answers/<slug>.md`, then present the next item.
5. Give no feedback of any kind: no "correct", no "interesting", no hint, no "are you sure?". If they ask how they did, say the result comes after grading.
6. After the eighth item, record the end time in the answers file and stop. Do not grade.
