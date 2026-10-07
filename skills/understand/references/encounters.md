# Encounters: choosing, designing and reading them

An encounter is anything that puts the learner in contact with the subject and produces a response you can read: a prediction, a run, a trace, a choice, something built, something broken. This module covers how to pick one, how to make it informative, and what to do with the result.

Contents: 1 Selecting · 2 Designing · 3 Predictions · 4 Reading the result · 5 When they are stuck · 6 Catalog · 7 Changing representation · 8 Fading support · 9 Transfer and lasting · 10 Leaving them alone with it · 11 Questions and curiosity

## 1. Selecting

Work down this list and stop at the first line that settles it.

1. They asked for something specific. Do that.
2. Which shaky or unseen capability matters most for the goal?
3. What kind of gap is it? Use the table below.
4. Which encounters could close that kind of gap?
5. Of those, which would come out differently depending on the model they hold?
6. Of those, which costs them the least time? Break ties toward the real system, then toward them acting rather than watching.
7. If the cheapest option is a short explanation, give the short explanation.

| Kind of gap | What you see | Encounter | Closed when they |
| :-- | :-- | :-- | :-- |
| No footing | cannot guess; asks what the words mean | orient: one concrete instance, then its name, then a worked example | can make a reasoned guess on a simple case |
| Words without mechanism | defines it correctly; predictions are guesses | predict then observe on a small case; a trace | predict a new case and give the cause |
| Wrong boundary | right on the standard case; applies it where it fails, or avoids it where it holds | edge case, counterexample, break-it | name the condition and predict both sides of the edge |
| Confused with a neighbor | swaps two terms or tools | minimal contrast pair, differing in one feature | sort unlabeled cases and say which feature decided |
| Can explain, cannot do | accurate description; stalls when performing | worked example, then completion, then independent attempt | perform unaided on a fresh case |
| Slow or error-prone | gets there with effort | short sets of varied practice, spaced | are fluent at the speed the goal needs |
| Stuck in the taught context | solves the original; misses the same structure elsewhere | same structure on a new surface, then compare the two | spot the structure in a third case unprompted |
| Cannot see it | knows the idea; misses instances in real material | many short unlabeled examples and non-examples, quick sorting | find instances in real code or data |
| No stakes | understands; would not choose it | a decision with consequences; a change of observer; the failure it prevents | make a choice and defend it |
| Needs memorizing | arbitrary facts | a reference card, then retrieval practice | recall without the card |
| Had it, lost it | fails a recheck | a shorter re-encounter on a new surface | pass the next recheck |
| Sure and untested | "obviously" | a specific prediction on a case where the naive model fails | have been checked against reality once |

## 2. Designing

Before you build an encounter, fill this in privately. Keep it out of files and out of the conversation until after the reveal, because it contains the answer.

```
gap:            which capability, which kind of gap
models:         correct model predicts ...
                suspected model predicts ...
                no model predicts ...
encounter:      what they will see and what they will do
separates:      the outcomes above differ in a way anyone can see
my prediction:  fixed before anything runs
cost:           about N minutes of their time
branches:       if correct -> ...   if suspected -> ...   if neither -> ...
```

What makes an encounter informative:

- **Different models predict different outcomes.** If every model predicts the same thing, you have a demonstration. It may still be worth showing, but it tells you nothing about them.
- **Wrong models leave fingerprints.** Choose cases where each plausible wrong model gives its own wrong answer. Then the answer tells you which model they hold, not only that they missed.
- **One thing changes.** Between a case and its variant, alter a single feature.
- **The outcome needs no interpretation.** A count, an ordering, an error, a line of a query plan. Not "notice how it feels slower".
- **Deterministic beats timed.** Where both can show the effect, count operations instead of measuring seconds. Counts do not depend on the machine.
- **It is small.** Under five minutes. If it will take longer, say how long and let them decide.
- **It is honest.** Never build a trick case to manufacture a failure. A person who was tricked learns to distrust the next question.

## 3. Predictions

A prediction turns a result into feedback on their model. Without one, a result is a fact they watched go by.

Ask for the cheapest form that still separates models:

- a direction: faster, slower, or the same
- a rough magnitude: about how many times
- a number
- a ranking
- which one breaks first
- the next state in a trace
- the output
- an estimate built from parts, such as three round trips at about 2 ms each plus one 40 ms call

Add "and why, in a few words" once. The reason is what separates a model from a lucky guess. Do not insist on it.

A prediction has to be able to be wrong. "It depends" and "probably slower" cannot be scored. If the answer is too loose to be wrong, ask once for a number, a direction, or a yes or no.

Ask how sure they are in the same breath, in a word: sure, fairly sure, guessing. A confident miss is the most useful result a session can produce, and over time the notebook shows whether their "sure" means sure.

Do not ask for a prediction when they have no footing, when the outcome is arbitrary and there is nothing to reason from, when they are exploring freely, or when they have said they want it straight.

Mechanics:

1. Show the setup with nothing run. If it is a script, it carries no comments that give away the result.
2. Ask once.
3. Whatever they answer, including "no idea" or "just run it", proceed.
4. The result is revealed only after they have answered.

## 4. Reading the result

**Match, with the right reason.** Confirm in one line. Do not re-explain what they just told you. Move to a boundary, a transfer, or stop.

**Match, with no reason or the wrong one.** Run a variant that changes one thing. If the model is real it will survive.

**"No idea."** This is missing footing, not a wrong model. Run it, show it, orient briefly, and try a simpler case.

**Mismatch.** This is the most valuable moment in a session and the easiest to waste.

1. Show the raw result in a line. No explanation yet.
2. Ask one question aimed at the assumption behind their prediction. "What would have to be true for your number to be right?" works in most cases. A more concrete version is better when you can see the assumption: "What did you expect `seen` to contain by the end?"
3. If they find the assumption, confirm it. If one attempt does not get there, give the mechanism yourself. Do not make them dig.
4. Consolidate.
5. Close the loop with a near variant where the corrected model predicts something definite. Until you have seen the new model predict correctly, the update is a hope.

**When they explain the result away.** People protect a model they like: the run was a fluke, the case is special, the measurement is off. Do not argue. Run it again, or run a second case that the same excuse cannot cover, and ask what their model predicts now.

**They read it first.** Whatever the outcome, they say what the result means before you do. If you interpret every result for them, they stop checking their own.

**Consolidation** is five lines or fewer:

- what happened and why, in terms of what they just saw
- the name the field uses for it
- the general rule in one sentence
- where it stops being true
- optionally, where the primary source is

Experience first and names second. The name sticks when it attaches to something they have already seen.

## 5. When they are stuck

One rung per failed attempt. Skip rungs if they are frustrated. Nobody should make more than two attempts without getting something solid to stand on.

1. Restate the question more concretely, or shrink the case.
2. Narrow the space: offer two or three outcomes to choose between.
3. Point at the feature that matters. "Look at what the list holds on the last pass."
4. Work a parallel, simpler case in full, then come back.
5. Tell them, plainly.

Match the help to what is missing. A missing fact gets the fact at once. A slip gets a pointer to the line. A wrong approach gets rung 3: where to look. A wrong model gets a case that exposes it. A missing prerequisite gets a worked example of the prerequisite.

Note the furthest rung you reached in the learner file. The next time the idea comes up, start one rung lower.

A hint that contains the whole answer is rung 5 pretending to be rung 3. If you are going to tell them, tell them.

## 6. Catalog

Each entry: when it fits, how to run it, what it shows, how it goes wrong.

### Orient

- **Concrete instance.** For no footing. Show one real case before any definition. Shows nothing about them yet. Goes wrong when the instance is exotic. Pick the plainest one.
- **Worked example.** For beginners and for procedures. Solve one case with the reasoning visible at each step. Follow it at once with a near-identical case for them to finish. Goes wrong when it stands alone, because watching feels like learning.
- **Picture or state dump.** For structure and for change over time. Print the data structure after each step, or draw the parts and their links. Goes wrong as decoration. It must answer a question such as what is where, what changed, or what causes what.
- **Definition.** For lookups and for naming something they have already seen.

### Probe

- **Predict then observe.** The default for causal and conditional knowledge. Sections 3 and 4 describe it.
- **Trace.** For algorithms and processes. They step through a tiny input by hand, predicting the next state each time, and you run it to check. Shows whether the mechanism is in their head or only its description. Keep the input tiny.
- **Sweep.** Change one variable across a range and watch the output: input size, number of distinct values, number of threads. Shows the shape of a relationship and where it bends.
- **Measurement.** When the question is "how much". Decide what to measure before running, and say what it was measured on.

### Stress

- **Contrast pair.** Two cases identical except for one feature, with different outcomes. For confusion and for boundaries. Ask what changed and why the outcome followed.
- **Break it.** Remove a component or violate a rule the structure depends on, then observe: unsorted input to a binary search, a key whose hash changes after insertion. Shows what each part was for.
- **Edge case.** Empty, one element, all equal, already sorted, enormous, adversarial. Shows the boundary of their model.
- **Find the bug.** A version that is subtly wrong. For perceptual and conditional knowledge. Shows whether they can notice a violation, which is harder than explaining the rule.
- **Counterfactual.** "What if the opposite were true?" Run it when you can. When you cannot, label it imagined.

- **Attack their model.** They go first: a plan, an explanation or a design, with how sure they are. You answer with the strongest realistic counterexample, the question that exposes the weakest assumption, and a cheap way to test it for real. You do not answer with your own solution unless they ask. For anything they want to own, this is the default way to respond to their work.
- **Rival explanations.** After a result, give two or three explanations that fit it, theirs among them, and ask which observation would tell them apart. Then make that observation. Choosing the test is harder than explaining the result, and debugging and science both rest on it.
- **Diagnose it.** A fault with a hidden cause, in a drill they asked for. Plant it in a copy of real code under `lab/` and let them investigate with real commands. If that is not possible, hold the cause yourself and answer only the observations they request, and say that you are simulating. What they choose to look at, and in what order, is the evidence.
- **Defend it.** Push back on a correct answer the way a skeptical colleague would, mixing objections that are sound with objections that only sound sound. They hold the position or concede, with reasons. Afterwards, say which objections were which. Someone who abandons a right answer under confident pressure does not own it yet.

### Construct

- **Build it.** A minimal implementation with a failing test and a marked gap for them to fill in their own editor. For procedural and structural knowledge. Keep it to the part that carries the idea and write the scaffolding yourself.
- **Reconstruct.** Take the support away and ask for the idea back in a form the domain suits: draw it, implement it from the invariant, solve a new case, state where it fails. Do not default to "explain it in your own words". A paraphrase is weak evidence.
- **Decide and live with it.** A realistic choice with constraints. They choose and give a reason, then you play a concrete consequence forward: a change request, ten times the load, a node failing. With code, apply the change to both designs and count what had to move.
- **Teach it to someone else.** Useful only when the audience or the case differs from the one they learned on. Otherwise it is recitation.

- **Build from their words.** They state the mechanism or the rule in plain language. You implement exactly what they said, and nothing they left out, then run the tests. Whatever the explanation omitted shows up as a failure. A run grades the explanation, which you would otherwise have to judge yourself, and it costs them no typing.

### Move

- **Transfer case.** The same structure under a different surface. Section 9.
- **Side by side.** Two instances they have already met, set next to each other, with the question "what is the same?"
- **Change the observer.** The same event as seen by the user, the operator, the attacker, the database, the network. Use it to expose a variable that was invisible from where they stood. It is not role-play for its own sake.
- **Field assignment.** Section 10.

### Keep

- **Retrieval.** For facts that have to be remembered. Recall from memory, then check. Brief, and spaced out.
- **Varied practice.** For fluency. Mix problem types so that choosing the method is part of the practice.
- **Delayed recheck.** See `learner-model.md`.

## 7. Changing representation

Each new representation costs the learner something. They must learn to read it and connect it to the last one. So change representation for a reason:

| The gap is about | Move to |
| :-- | :-- |
| how parts relate | a picture or a printed state |
| what changes over time | a trace, or a table of steps |
| how much | a measurement, or a sweep |
| the general rule | a formal statement, after they have seen instances |
| why it matters | a consequence, or another observer's view |
| doing it | their hands on it |

When you add a representation, have them map it onto the previous one: "which line of the code is this arrow?" That mapping is strong evidence in its own right.

Choose by what the content hides in its current form. Do not choose by what kind of learner someone says they are.

Two representations of one idea is the limit unless new evidence shows a gap the first two did not reach.

## 8. Fading support

For anything they must be able to do:

1. a full worked example with reasons
2. the same structure with the last step left for them
3. only the first step given
4. an independent attempt
5. an independent attempt on a different surface

Move forward the moment they succeed. Move back one step after two failures. Staying on worked examples after they can do it alone slows them down. So does starting a beginner at step 4.

Fade your feedback as well as your help. Correction that always comes from outside tends to stop people detecting their own errors. Once they are mostly right, ask them to check their own result against the run before you confirm it. And when you have asked the same kind of question three times, such as "what must stay true here?", stop asking it and watch whether they now ask it themselves. Doing so unprompted is strong evidence.

## 9. Transfer and lasting

Success on the original example shows they can do the original example.

- Go near before far: the same domain with different values, then a different surface, then a different domain.
- After two instances, ask what stayed the same. Comparing two cases builds the general idea more reliably than a third example does.
- Let them see the link before you name it. "This is just like caching" said too early replaces the noticing.
- Interleave by dependence. Design later encounters so they need earlier ideas. The earlier ideas get retrieved and retested through use, without a quiz.
- For anything that has to last, schedule a recheck.

- After a consolidation, ask where else this would show up. Their own candidate is worth more than yours. Then check one for real.
- When you supply the case, name the place and not the mapping. "The same thing happens somewhere in the webhook handler" leaves the finding to them.
- Check your own far cases. A far case changes the technology or the domain and keeps the structure. Renamed variables make a near case.
- The strongest signs of transfer cannot be staged: they spot the structure unprompted in new material, or they pick up the next related idea in fewer encounters. Note both when you see them.

Use transfer when the goal needs it. A person who wants one specific thing working by Friday has not asked to be tested on a second domain.

## 10. Leaving them alone with it

Some contact has to happen without you in the middle. Set it up, then get out of the way.

Forms:

- read a primary source with one question in hand: the documentation page, the PEP, the function in the source tree
- look at their own system: the slowest query in their own application, the real log, the real profile
- build something with a failing test and no help
- explain it to a colleague and notice where the explanation stalls
- make the real decision and note what happens

Give them four things: what to look at, the question to carry, how they will know they are done, and what to bring back. Then stop writing. When they return, ask what they saw before you tell them anything.

## 11. Questions and curiosity

A question from the learner outranks the encounter you had planned. Answer it, or turn it into the next experiment. Their questions show where the edge of their model is more precisely than your probes do.

When there is no goal yet, start from something worth being curious about: a surprising result, an odd failure, a case that should not work and does. Show it with as little framing as possible and follow what they ask.

If a tangent does not serve the goal and they want it anyway, follow it. The goal is theirs. If they would rather stay on course, note the tangent in the parking lot of the learner file.
