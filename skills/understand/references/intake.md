# Intake: from a topic to a first encounter

The aim is to reach a real encounter within two exchanges. Everything here happens in your head unless marked otherwise. The learner should experience a quick start, not an interview.

## 1. Confirm it is a learning request

Run the gate from the kernel on the first message. People often describe a subject area when what they want is a task done in that area. "I want to test this", "write me", "set up", "review" and "fix" are tasks. If you are unsure, do the literal thing and offer the other in one line.

## 2. Establish the goal

You need two things: what they want to be able to do, and how deep it has to go.

- If they said it, restate it in half a line inside your first move. Do not stop to ask for confirmation.
- If the topic is clear and the purpose is not, infer the most likely purpose, say the assumption in passing, and start. They will correct you if it is wrong.
- If the topic itself is too broad to act on ("algorithms", "system design", "get better at backend"), you may ask one question. Make it cheap to answer: offer two or three concrete directions rather than an open "what do you want to learn?". If they ignore the question or answer loosely, pick the entry point yourself and begin.

One clarifying question is the ceiling. A second question before any encounter is an interview.

### Depth

| Depth | They can | Typical reason |
| :-- | :-- | :-- |
| Use | apply it correctly in the standard case and recognize the two or three ways it goes wrong | needs it for work this week |
| Explain | predict what it does in cases they have not seen, say why, and say where it stops working | interviews, code review, debugging, teaching others |
| Adapt | modify it, combine it, or re-derive it for a problem that does not look like the examples | designing something new around it |

Take the depth from the goal. Do not push past it. Someone who needs Use and gets a tour of the internals has been given a lesson they did not ask for.

### What they want to own

Most of what a working person touches does not need to be understood. It can be delegated and spot-checked. The loop is for the part they have chosen to own: what they will have to judge, decide or do when no assistant is there, or when the assistant is wrong. If they have not said which part that is, take the narrowest reading of the goal. Do not widen it for them.

An idea is owned when four things hold. They can predict a new case before checking. They can explain it to someone who pushes back. They know where it breaks. They could rebuild it without the source. For anything at depth Explain or above, these four give the target its shape.

For someone who works with coding agents there is a fifth: they can supervise. Given work an agent produced in this area, they know what to check and they catch what is wrong. `domains/software.md` section 10 covers it.

### Conditions of use

Work out where they will use this. With an assistant beside them or without one. Under time pressure or not. Spoken aloud, as in an interview or an incident call, or written. People perform best under the conditions they practiced in, so the last encounters and the rechecks should resemble the real occasion. If they will have to do it alone, at least one check happens alone.

## 3. Build the target

A private note of about a dozen lines:

- **Capabilities**, three to seven, phrased as things you could watch them do. "Given a query and a schema, say whether the planner will use the index" is a capability. "Understands indexes" is not.
- **Load-bearing ideas**, one to three. The ideas the rest follows from.
- **Boundaries.** Where it stops applying, and what breaks first.
- **Neighbors.** What it is commonly confused with.
- **Likely misconceptions**, each written as the prediction it would produce.
- **Prerequisites.** What has to be in place already.
- **Kinds of knowledge involved.** Most real subjects mix several, and each kind is learned and evidenced differently:

| Kind | Question it answers | Evidence looks like |
| :-- | :-- | :-- |
| Declarative | what is it? | recall, recognition |
| Causal | why does it happen? | predictions that hold when one thing changes |
| Structural | how do the parts relate? | drawing it, tracing a path through it |
| Procedural | how do I do it? | doing it unaided, at a reasonable speed |
| Perceptual | what does it look like? | spotting it in unlabeled examples |
| Strategic | when should I use it? | choosing between options and defending the choice |
| Conditional | when does it stop working? | naming or constructing a case that breaks it |
| Social | how does this work between people? | reading a situation, anticipating a response |
| Embodied | how does the body do it? | performance |
| Tacit | what comes only from repetition? | judgment that improves with exposure |

The target is a map. It implies no route. You will visit only the parts the evidence says need visiting.

## 4. Find where they are

Probe, do not survey. One well-chosen case tells you more than a self-rating or a list of "have you heard of" questions.

A good opening probe:

- takes under a minute to answer;
- can be checked against reality straight afterwards;
- separates models: someone with no model, a partial model and a full model would give three different answers;
- is pitched at your best guess of their level, erring slightly high.

Read the response:

| Response | Meaning | Next |
| :-- | :-- | :-- |
| Right, with the right reason | they are past this | jump to a boundary or the next capability |
| Right, no reason | maybe luck, maybe fluency | a second case that changes one thing |
| Wrong, with a reason | a model you can work with | run it, then the mismatch procedure in `encounters.md` |
| "No idea" | no footing | orient first: a concrete instance, then its name |
| Irritation or "can you just explain it" | they wanted a different mode | explain briefly, then offer one thing to try |

Skip the probe when they have already shown their level: a precise question in the field's own terms, their code, a description of exactly where they got stuck.

## 5. Starting mode by experience

How much guidance helps depends on what the person already has. The same encounter that suits an experienced learner wastes a beginner's effort, and the reverse.

- **New to it.** They have nothing to predict with. Start with a concrete instance, then a worked example with the reasoning shown, then a small variation they complete. Predictions begin once there is a model to predict from.
- **Some experience.** Predict-then-observe on cases that separate models. This is the default.
- **Experienced.** Go straight to boundaries, failure cases, trade-offs and transfer. Do not re-establish what they already use daily.

## 6. Broad goals

For a goal that spans many topics, do not lay out a curriculum.

1. Choose one entry point that many of the other ideas reuse. In data structures, the cost of a single operation as input grows is such an idea. In databases, "the engine has to find the rows somehow" is another.
2. Start there with a real case.
3. Keep the rest of the map in the learner file under "parking lot".
4. Let later encounters depend on earlier ideas, so earlier ideas get re-tested by being used.

Share the map only if they ask what else there is.

### Choosing from their own work

When the question is "what should I work on?", the best candidates are gaps their own work exposed. Look for these, strongest first:

- a prediction they were sure of that turned out wrong
- something they shipped and could not explain
- the cause of an incident or a bug
- a consequential choice an agent made for them that they did not review: an isolation level, a retry policy, a timeout, an authorization check
- the same concept turning up for the third time in a month
- a place where their plan and the agent's plan differed

Rank by four questions. How bad is it to get this wrong? How often does it come up? Are the prerequisites in place? How many other things share its structure? Take a candidate that does well on all four and sits just beyond what they already know. The hardest unknown is rarely the best next step.

Keep at most five candidates in the learner file, each with the piece of real work it came from. Drop any that has not come up again in two months.

## 7. The first reply

It contains the first encounter or the single allowed question. It does not contain a description of your approach, a list of what you will cover, or a request to rate their own knowledge.

## 8. Starting from a surprise or an incident

Sometimes they arrive with reality's answer already in hand: something broke, a result surprised them, a decision turned out badly. This is the best starting material there is, because the contact has already happened.

1. Get what happened in a line or two. Read the logs or the code yourself if they are available.
2. Ask what they expected, and why. This recovers the prediction they never wrote down.
3. Let them explain the gap first. Then attack the explanation: what does it not account for? Offer a rival explanation only if theirs does not survive.
4. Where it can be reproduced, reproduce it in `lab/`, so that a run checks the explanation and agreement does not have to.
5. Consolidate, then ask where else the same thing could happen. Check one of those places for real.

If the surprise came from a decision with slow or noisy feedback, judge the reasoning as well as the outcome: what was known at the time, and what was considered. A good decision can turn out badly.
