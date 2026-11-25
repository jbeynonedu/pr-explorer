---
id: deduction
title: Deduction
type: term
units: [1]
section: deduction
status: approved
related: [argument, induction, analogy, generalisation, deductive-vs-inductive, valid, sound, classifying-arguments, limits-of-deduction, modus-ponens, modus-tollens]
sources: [bland-reason-ch1-deduction, iep-shanahan-definitions, forallx-ch2-success-view]
---

# Deduction

**A deductive argument is an argument that aims to guarantee its conclusion: if the premises are true, the conclusion must be true.** Deduction is reasoning of this kind.

## What makes an argument deductive

In a well-built deductive argument, the [premises](premise) are linked by a logical process, and each premise contributes to the support for the [conclusion](conclusion). For the arguments studied at this level, whether that support works depends on the argument's *form* (its structure), not on what it is about.

Because a deductive argument is defined here by what it *aims* to do, it can fail. A deductive argument whose premises do not in fact guarantee its conclusion is still deductive, but it is [invalid](valid). An arguer's aim is not always stated, so it can be hard to tell; see [classifying arguments](classifying-arguments).

Some logic texts take a different approach. They sort every argument only by whether its premises do guarantee its conclusion. On that approach, even a good [inductive](induction) argument counts as invalid.

## Example

```sf
1. If a cyclone warning is issued for Cairns, then Cairns schools will close.
2. A cyclone warning has been issued for Cairns.
C. Therefore, Cairns schools will close.
```

Dictionary:

- `W = "A cyclone warning is issued for Cairns."`
- `S = "Cairns schools will close."`

```sf
1. W ⊃ S
2. W
C. S
```

This is [modus ponens](modus-ponens). The premises are linked: premise 2 matches the "if" part of premise 1. If both premises are true, the conclusion cannot be false. Whether premise 1 *is* true (do schools always close?) is a separate question.

## How deductive arguments are judged

A deductive argument is [valid or invalid](valid), and [sound or unsound](sound). Both judgements are all-or-nothing: no argument is "partly valid" or "more sound" than another. Inductive arguments, such as arguments from [analogy](analogy) and [generalisations](generalisation), are judged differently, as [strong or weak](strong-weak); see [the distinction between deductive and inductive arguments](deductive-vs-inductive).

## Where it is used

Mathematics relies mainly on deductive reasoning: a proof shows that a result follows from what is already accepted. At this level there are five named valid deductive forms: modus ponens, [modus tollens](modus-tollens), hypothetical syllogism, disjunctive syllogism and constructive dilemma. Two invalid forms look similar. Deduction also has [limitations](limits-of-deduction).

## Related concepts
[Argument](argument) · [Induction](induction) · [Deductive and inductive arguments](deductive-vs-inductive) · [Deductively valid and invalid](valid) · [Sound and unsound](sound) · [Classifying arguments](classifying-arguments) · [Limitations of deduction](limits-of-deduction) · [Modus ponens](modus-ponens) · [Modus tollens](modus-tollens)

## Sources
- Bland, *Reason* (Revised Edition), ch. 1, §1.4 pp. 17–21, 23. CC BY-NC 4.0.
- Magnus, Button, Trueman and Zach, *forall x: Calgary* (Fall 2025), ch. 2, §§2.2–2.3, 2.5, pp. 11–12, 16. CC BY 4.0.
- Shanahan, T., "Deductive and Inductive Arguments", *Internet Encyclopedia of Philosophy*, §§2, 4. https://iep.utm.edu/deductive-inductive-arguments/
