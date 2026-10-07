---
name: write-items
description: Write a sealed delayed test for one concept, before any teaching happens.
argument-hint: "[concept]"
disable-model-invocation: true
---

Concept: $ARGUMENTS

Write eight test items for this concept and save them to `data/sealed/<slug>.md`. The person reading this conversation is the person who will sit the test, so do not print the items, the answers or the scoring guide. When you are done, report only the file path and that eight items were written.

Who the test is for: a working software engineer who studied this concept once, about a week earlier, for about 25 minutes. Target depth: can predict and explain, including where it stops working. Each item must be answerable closed book in two to four minutes without running code.

Write one item of each type, in this order:

1. Recall. Say what it is and how it works, from memory.
2. Prediction. A concrete case they have not seen: what happens?
3. Explanation. Why does a given behavior occur?
4. Discrimination. Two similar cases or tools: which applies, and what decides it?
5. Transfer. The same structure in a different setting, with different surface details.
6. Boundary. Where does it stop working, and what breaks?
7. Unfamiliar problem. A problem that needs the concept, in a form not usually taught.
8. Non-applicability. A case that looks like it calls for the concept and does not.

For each item write the prompt, what a full-credit answer contains (2 points), what earns partial credit (1 point), and the common wrong answers that score 0 with the reason.

Rules:

- Do not build items around the standard textbook example. A session may have used it, and then the item tests memory of the example.
- No trick questions and no trivia.
- Where an item depends on how code behaves, verify it by running the code in `data/scratch/` and put the observed output in the scoring guide. Do not show that output in the conversation.
- Do not read the learner's notes and lab in `~/understanding/`, or any session transcript.
