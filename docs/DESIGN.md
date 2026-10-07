# Design notes

## From framework to protocol

This protocol turns an earlier framework by the same author, the Adaptive Understanding Engine, into something an agent can run. The framework is a set of principles in 37 short sections. It is not reproduced here, and the table below lists its ideas.

The framework states what the engine should value and what it must avoid. A protocol has to go further: it says what state is kept, which decision is made at each point, and what the engine does next, precisely enough that two sessions behave alike and a transcript can be checked against it. Most of the work here was converting prohibitions ("do not over-explain") into procedures and tripwires ("more than about 150 words with no learner action since the last explanation: change course").

The framework repeats its central ideas many times. That is fine for a statement of intent. In a prompt it dilutes attention, so the protocol states each rule once, in the place where it is used.

## Where each part of the framework lives

| Framework idea | Where it lives now | What changed |
| :-- | :-- | :-- |
| Choose the next experience, not the next explanation | kernel 3; `encounters.md` 1 | became a seven-line selection procedure |
| Never optimize for "I understand" | kernel 2; `learner-model.md` 2 | became evidence grades E0 to E4, with "I get it" defined as E0 |
| Encounter, predict, act, observe, reconstruct, contrast, transfer | kernel 3 | eight steps, explicitly skippable; consolidation added |
| Representation rotation | `encounters.md` 7 | rotation needs a reason, costs are stated, limit of two |
| Internal hypothesis about the learner's model | kernel 2; `learner-model.md` | written to a plain file the learner can read |
| Discriminating experiences | `encounters.md` 2 | design card; "wrong models leave fingerprints" |
| Prediction before explanation | kernel 3.4; `encounters.md` 3 | commit-before-reveal mechanics; cases where no prediction is asked |
| Reality has priority; observed, simulated, inferred | kernel 4; `lab.md` 5 | five provenance labels; numbers only from runs |
| Do not manufacture struggle | `encounters.md` 5 | the stuck ladder, with a two-attempt limit |
| Do not force modes | kernel 3.3; `encounters.md` 1 | "if two lines of explanation close the gap, write two lines" |
| Explanation is a tool | kernel 3.7 | consolidation of five lines or fewer, after the experience |
| Reconstruction, contrast, transfer | `encounters.md` 6 and 9 | catalog entries with failure modes |
| Productive failure | `encounters.md` 4 | five-step mismatch procedure that ends by checking the new model |
| Perspective shifting, visuals | `encounters.md` 6 and 7 | used to expose a hidden variable, not for variety |
| Actions as evidence | `learner-model.md` 2 | grades describe what the person did |
| No bureaucracy | kernel 4 and 5 | one thing per turn; no narration; no scores shown |
| Memorization versus understanding; kinds of knowledge | `intake.md` 3; `domains.md` | table of kinds with what counts as evidence for each |
| The AI should sometimes disappear | `encounters.md` 10; `lab.md` 4 | field assignments; the learner runs commands with `!` |
| Avoid AI-generated closure | kernel 4; `lab.md` 6 | "run before you promise"; what to do when reality disagrees |
| Curiosity; creative and human domains | `encounters.md` 11; `domains.md` | per-domain notes on where reality is and what the engine cannot see |
| The user owns the goal; stopping; minimum effective experience | kernel 1 and 6; `learner-model.md` 5 | gate, depth dial, four-line close |
| Testing, section 34 | `eval/` | fidelity tests, then a paired randomized study with sealed items |
| Software engineering first, section 35 | `software.md` | instruments, families, twenty checked beliefs |

## Tensions the protocol had to settle

**Distrust "I understand", and do not quiz.** Evidence is gathered by making the next encounter depend on the previous idea. The learner experiences work, not a test. If they stop early, the close says once what was shown and what was not.

**Predict first, and do not manufacture struggle.** A prediction is only worth asking for when the person has something to predict with. Beginners get footing first. "No idea" and "just run it" are accepted without comment.

**Reality first, and minimum effective experience.** Reality wins among options of equal cost. A two-line explanation beats a ten-minute experiment when it closes the gap.

**A hidden hypothesis, and honesty.** The hypothesis is not narrated, and it is not hidden either. It sits in a text file the learner owns.

**Experience over explanation, and what is known about beginners.** Novices learn poorly from unguided discovery. The protocol starts beginners with worked examples and fades support as they succeed.

**Many representations, and their cost.** Each one has to be learned and connected to the last. The protocol asks for the connection explicitly and treats it as evidence.

**Answer on request, and the risk of becoming a crutch.** The framework says never withhold, and the protocol keeps that. An answer given is recorded as no evidence, and the next encounter still has to be passed. Whether this is enough is an open question, listed below.

## What was added

- **A gate.** Lookup, task or understanding, decided on every message. Most requests in a coding tool are tasks, and an engine that turns every task into a lesson is worse than no engine.
- **A depth dial.** Use, explain, adapt. It tells the engine when to stop.
- **Evidence grades with aging**, and the distinction between a slip, a gap and a misconception, because each calls for a different next move.
- **A table from kind of gap to kind of encounter**, with a closing condition for each.
- **Consolidation.** Experience without a short explanation afterwards leaves people with an event and no idea. The research on learning from failure is clear that the instruction that follows is part of the effect.
- **Run before you promise**, and a subagent that checks an experiment out of the learner's sight.
- **Delayed rechecks**, opt-in, on a new surface.
- **Tripwires** that can be counted in a transcript.
- **A test harness** that separates "does it follow the protocol" from "does the protocol work".

## What v1.1 took from two companion essays

v1.1 drew on two companion essays by the same author: "Learning While Shipping" (1 October 2026) and "The Friction of Being Wrong" (2 October 2026). Much of what they recommend the protocol already did: commit before the reveal, reality as the grader, consolidation after the experience, spacing, comparison for transfer, help that depends on expertise. What they added falls into four groups.

**The engine was a classroom, and the essays are about work.** v1.0 assumed a session whose purpose is learning. The essays assume a day whose purpose is shipping, with learning attached to one mechanism at a time. v1.1 adds: a task can carry one mechanism to own; urgency always wins; a session can start from a surprise or an incident; candidates for study come from their own work; and two optional commands bring the loop into real repositories.

**Who goes first, and who grades.** "Me first, AI second, reality decides." v1.1 adds encounters where the learner's model is attacked instead of replaced, where they choose the test that separates rival explanations, and where code is built from their words so that a run grades the explanation. It also adds the rule that evidence judged by the engine counts for less than evidence graded by a run, because a model judging an explanation leans generous.

**Help without toll booths.** Facts are free, the engine does its own legwork, and a question is asked only if the answer changes the next move. A told answer on something they want to own becomes an owed rebuild. This is the essays' "learning debt", and it is the first concrete response to the open question about answer on request.

**What decays.** Correction that always comes from outside stops people detecting their own errors, so v1.1 fades feedback and prompts as well as help. Unused skills decay, including the skill of supervising an agent, so `software.md` gains review drills, and a recheck can be done alone.

Left out on purpose: the four files, the prediction database with Brier scores, the ten commands, the daily and weekly schedule, the monthly benchmark regime, and a second scale of mastery states. The later essay makes the argument itself: keep the habits and drop the paperwork. The engine keeps one learner file and one notebook per topic, and confidence is a word on a notebook line.

One tension is worth naming. "Learning While Shipping" gates help on effort: a hint is earned by producing something new. The original framework says withholding is never the method. v1.1 keeps the framework's rule. Help rises when they are stuck, an answer is given when asked for, and what was told is noted as owed. Whether effort-gating would teach more is now on the list of open questions.

## How it is packaged

v1.2 is an Agent Skill, the open format described at https://agentskills.io. The kernel is `skills/understand/SKILL.md` and the modules are its reference files, read on demand. Nothing in them depends on one tool. The kernel begins by working out three things from the tools available: whether it can run code, whether files persist, and whether it can run something out of the learner's sight. Each has a fallback.

- **Why a skill.** One format is read by many agents, in coding tools and in chat applications, and a short file with references loaded when needed is the shape the protocol already had.
- **What that costs.** A skill is loaded on demand as instructions. It is not the system prompt, so in a long session it may hold less firmly than an always-loaded prompt would. For Claude Code, the plugin therefore also ships the kernel as an output style, generated from the same source, for people who want it sent with every request.
- **Claude Code extras.** The plugin adds a `dry-run` subagent, which runs an experiment in a fresh context and reports back without putting the output in front of the learner.
- **Where notes live.** `~/understanding/` by default: one place across projects and tools, and outside any team repository.
- **Domain packs.** Software is the only subject with a full pack. The others share one file of short notes. `references/domains/_template.md` is the shape a new pack takes.
- **The test harness** in `eval/` is written for Claude Code. The fidelity tests themselves are plain text and can be run by hand anywhere.

A format that travels does not guarantee behavior that travels. The kernel was worded for Claude. Other models may follow it differently, and the fidelity tests are how to find out.

## What the evidence supports

- **Feeling clear is a poor guide to being able.** People overrate how well they can explain everyday mechanisms until asked to do it (Rozenblit and Keil 2002). Physics students in active classes learned more and felt they had learned less than after polished lectures (Deslauriers et al. 2019).
- **Predicting first helps, even when the prediction is wrong.** Attempting an answer before being taught improves later learning (Richland, Kornell and Kao 2009; Kornell, Hays and Bjork 2009), and errors made with high confidence are especially likely to be corrected (Butterfield and Metcalfe 2001). Predict-observe-explain is a long-standing classroom technique (White and Gunstone 1992).
- **Experience, then explanation.** Working with contrasting cases prepares people to learn from a later explanation (Schwartz and Bransford 1998). Problem solving before instruction beats the reverse order for conceptual understanding and transfer, provided instruction follows and builds on the attempts (Kapur 2008; Sinha and Kapur 2021).
- **Retrieval and spacing make learning last** (Roediger and Karpicke 2006; Cepeda et al. 2006).
- **Doing beats watching.** Constructive and interactive engagement outperform passive and merely active engagement (Chi and Wylie 2014). Explaining steps to oneself improves learning from examples (Chi et al. 1989).
- **Comparison drives transfer.** Comparing two analogous cases produces transfer that a single case does not (Gick and Holyoak 1983). Far transfer remains hard (Barnett and Ceci 2002).
- **The right amount of guidance depends on expertise** (Kalyuga et al. 2003; Kirschner, Sweller and Clark 2006).
- **Different kinds of knowledge need different instruction** (Koedinger, Corbett and Perfetti 2012).
- **Design decides whether an AI tutor helps.** In a field experiment with about a thousand high-school students, unrestricted GPT-4 access improved practice scores and lowered later unassisted exam scores by 17% relative to no access, while a version with guardrails largely avoided the harm (Bastani et al. 2025). A tutor built on active-learning principles produced more than double the median learning gains of an active-learning class in less time, in a crossover trial with 194 students measured shortly after each lesson (Kestin et al. 2025).

## Where it is thin

- **"More kinds of contact" is not established as such.** What is supported is narrower: particular variations expose particular features (Marton and Booth 1997), and multiple representations help only when learners connect them (Ainsworth 2006). Matching instruction to a self-described learning style has no good support (Pashler et al. 2008). The protocol therefore chooses a representation by what the content hides, never by learner type.
- **Reality is not automatically the better teacher.** Virtual laboratories often match physical ones for conceptual learning (de Jong, Linn and Zacharia 2013). The protocol keeps reality first for a different reason: a real system can contradict the tutor, and a simulation written by the tutor cannot.
- **Answer on request may cost learning.** The Bastani result suggests so in a school setting. Self-directed adults with their own goals may differ. This protocol has not been tested either way.
- **The engine is a language model following instructions.** It will sometimes not follow them. That is why the fidelity tests come first.
- **The learner model rests on a handful of observations** and will be wrong in places.
- **A study of one person** shows what works for that person.

## Open questions for testing

1. Does answer-on-request reduce delayed performance compared with a version that gives a stronger hint first?
2. Does the prediction step earn its friction, or do real runs with no prediction do as well?
3. Does the dry run matter in practice, or do live surprises teach as much?
4. Do delayed rechecks change the result at three weeks?
5. Does the engine help more on prediction, boundary and transfer items than on recall, as the framework expects?
6. Does it cost more minutes per point than a good explanation?
7. Which kernel rules change behavior, and which could be deleted?
8. Do owed rebuilds actually get done, and do they recover what a told answer costs?
9. Would effort-gated hints, where a hint is earned by producing something new, teach more than help on request?
10. Does asking how sure they are add anything beyond the prediction itself?

## Known limitations

- Outside software the engine sees only what the learner reports.
- The checked examples in `software.md` are from one interpreter version on one machine. Three of them contradict what is usually taught, which is a warning about the others.
- Session transcripts in Claude Code are long. An audit by a model can miss things a careful reader would catch.
- Nothing enforces the rules. A skill is an instruction. If a rule has to hold without exception, the tool's own permission system or a hook is the place for it, and none is configured here.

## Two things that went wrong while writing this

**A misread request.** While this protocol was being drafted, a message that named a subject area, "software engineering concepts, DSA", was answered by starting to teach it. What was wanted was a document. A gate was always going to be needed, because most requests in a coding tool are tasks. The instruction to read the verb comes from this mistake.

**Two textbook demonstrations failed.** While checking examples for `software.md`, the standard thread race on `counter += 1` lost no updates on CPython 3.12, and `sum([0.1] * 10) == 1.0` returned `True`. Both would have been taught confidently from memory. That is why "run before you promise" sits in the kernel, where it is always loaded, and not only in the lab module.

## References

- Ainsworth, S. (2006). DeFT: A conceptual framework for considering learning with multiple representations. *Learning and Instruction*, 16(3).
- Barnett, S. M., and Ceci, S. J. (2002). When and where do we apply what we learn? A taxonomy for far transfer. *Psychological Bulletin*, 128(4).
- Bastani, H., Bastani, O., Sungu, A., Ge, H., Kabakcı, Ö., and Mariman, R. (2025). Generative AI without guardrails can harm learning: Evidence from high school mathematics. *PNAS*, 122(26). doi:10.1073/pnas.2422633122
- Butterfield, B., and Metcalfe, J. (2001). Errors committed with high confidence are hypercorrected. *Journal of Experimental Psychology: Learning, Memory, and Cognition*, 27(6).
- Cepeda, N. J., Pashler, H., Vul, E., Wixted, J. T., and Rohrer, D. (2006). Distributed practice in verbal recall tasks. *Psychological Bulletin*, 132(3).
- Chi, M. T. H., Bassok, M., Lewis, M. W., Reimann, P., and Glaser, R. (1989). Self-explanations. *Cognitive Science*, 13(2).
- Chi, M. T. H., and Wylie, R. (2014). The ICAP framework. *Educational Psychologist*, 49(4).
- de Jong, T., Linn, M. C., and Zacharia, Z. C. (2013). Physical and virtual laboratories in science and engineering education. *Science*, 340(6130).
- Deslauriers, L., McCarty, L. S., Miller, K., Callaghan, K., and Kestin, G. (2019). Measuring actual learning versus feeling of learning. *PNAS*, 116(39).
- Gick, M. L., and Holyoak, K. J. (1983). Schema induction and analogical transfer. *Cognitive Psychology*, 15(1).
- Kalyuga, S., Ayres, P., Chandler, P., and Sweller, J. (2003). The expertise reversal effect. *Educational Psychologist*, 38(1).
- Kapur, M. (2008). Productive failure. *Cognition and Instruction*, 26(3).
- Kestin, G., Miller, K., Klales, A., Milbourne, T., and Ponti, G. (2025). AI tutoring outperforms in-class active learning. *Scientific Reports*, 15, 17458.
- Kirschner, P. A., Sweller, J., and Clark, R. E. (2006). Why minimal guidance during instruction does not work. *Educational Psychologist*, 41(2).
- Koedinger, K. R., Corbett, A. T., and Perfetti, C. (2012). The Knowledge-Learning-Instruction framework. *Cognitive Science*, 36(5).
- Kornell, N., Hays, M. J., and Bjork, R. A. (2009). Unsuccessful retrieval attempts enhance subsequent learning. *Journal of Experimental Psychology: Learning, Memory, and Cognition*, 35(4).
- Marton, F., and Booth, S. (1997). *Learning and Awareness*. Lawrence Erlbaum.
- Pashler, H., McDaniel, M., Rohrer, D., and Bjork, R. (2008). Learning styles: Concepts and evidence. *Psychological Science in the Public Interest*, 9(3).
- Richland, L. E., Kornell, N., and Kao, L. S. (2009). The pretesting effect. *Journal of Experimental Psychology: Applied*, 15(3).
- Roediger, H. L., and Karpicke, J. D. (2006). Test-enhanced learning. *Psychological Science*, 17(3).
- Rozenblit, L., and Keil, F. (2002). The misunderstood limits of folk science: An illusion of explanatory depth. *Cognitive Science*, 26(5).
- Schwartz, D. L., and Bransford, J. D. (1998). A time for telling. *Cognition and Instruction*, 16(4).
- Sinha, T., and Kapur, M. (2021). When problem solving followed by instruction works: Evidence for productive failure. *Review of Educational Research*, 91(5).
- White, R., and Gunstone, R. (1992). *Probing Understanding*. Falmer Press.

Added for v1.1. These are taken from the two essays and from memory. They were not re-opened during drafting.

- Aleven, V., Stahl, E., Schworm, S., Fischer, F., and Wallace, R. (2003). Help seeking and help design in interactive learning environments. *Review of Educational Research*, 73(3).
- Buçinca, Z., Malaya, M. B., and Gajos, K. Z. (2021). To trust or to think: Cognitive forcing functions can reduce overreliance on AI in AI-assisted decision-making. *Proceedings of the ACM on Human-Computer Interaction*, 5(CSCW1).
- Chinn, C. A., and Brewer, W. F. (1993). The role of anomalous data in knowledge acquisition. *Review of Educational Research*, 63(1).
- Gajos, K. Z., and Mamykina, L. (2022). Do people engage cognitively with AI? Impact of AI assistance on incidental learning. *IUI 2022*.
- Hogarth, R. M., Lejarraga, T., and Soyer, E. (2015). The two settings of kind and wicked learning environments. *Current Directions in Psychological Science*, 24(5).
- Kratochwill, T. R., et al. (2010). *Single-case designs technical documentation*. What Works Clearinghouse.
- Morris, C. D., Bransford, J. D., and Franks, J. J. (1977). Levels of processing versus transfer appropriate processing. *Journal of Verbal Learning and Verbal Behavior*, 16(5).
- Salmoni, A. W., Schmidt, R. A., and Walter, C. B. (1984). Knowledge of results and motor learning: A review and critical reappraisal. *Psychological Bulletin*, 95(3).
- Sharma, M., et al. (2023). Towards understanding sycophancy in language models. arXiv:2310.13548.

Only the Bastani and Kestin papers were looked up while writing this. The rest are cited from memory and are worth checking before you rely on a detail.
