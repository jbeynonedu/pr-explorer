---
id: affirming-the-consequent
title: Affirming the consequent
type: logic-form
units: [1]
section: symbolic-logic
status: approved
related: [modus-ponens, denying-the-antecedent, modus-tollens, valid, necessary-sufficient, hidden-premise, hypothetico-deductive]
sources: [bland-reason-ch2-ac, bland-reason-ch3-ac-table, forallx-5-5-iff, sep-confirmation]
---

# Affirming the consequent

**Affirming the consequent is a formal fallacy: an invalid argument form that takes a conditional, affirms its consequent, and concludes its antecedent.** It is a mistake in the argument's structure, not its content: the form alone never guarantees the conclusion.

## The form

| Standard form | Symbolic form |
| --- | --- |
| 1. If P, then Q. | `P ⊃ Q` |
| 2. Q. | `Q` |
| C. Therefore, P. | `∴ P` |

Line form: `P ⊃ Q, Q ∴ P`

## Example

```sf
1. If there is a power outage across the suburb, then the traffic lights at the school crossing are off.
2. The traffic lights at the school crossing are off.
C. Therefore, there is a power outage across the suburb.
```

Dictionary:

- `O = "There is a power outage across the suburb."`
- `L = "The traffic lights at the school crossing are off."`

```sf
1. O ⊃ L
2. L
C. O
```

Both premises could be true while the conclusion is false: the lights might be off because of a fault at that crossing alone. That possibility is a **counterexample**, and it shows the argument is invalid.

## Why it is invalid

A truth table tests whether an argument form is valid: if any row has all true premises and a false conclusion, the form is invalid (1 = true, 0 = false).

<!-- interactive: truth-table; premises: P ⊃ Q, Q; conclusion: P -->

| P | Q | Premise 1: `P ⊃ Q` | Premise 2: `Q` | Conclusion: `P` |
| --- | --- | --- | --- | --- |
| 1 | 1 | 1 | 1 | 1 |
| 1 | 0 | 0 | 0 | 1 |
| **0** | **1** | **1** | **1** | **0** |
| 0 | 0 | 1 | 0 | 0 |

In the third row (in bold: P false, Q true), both premises are true and the conclusion is false. That row is the counterexample.

## Variations you will meet
The conditional may be worded in other ways, and its parts may be negated. Each of these still affirms the consequent and concludes the antecedent.

**"Q if P."** "The bus is late if it rains" has the antecedent "it rains". Affirming "the bus is late" and concluding "it rains" is the fallacy.

**"P only if Q."**

```sf
1. You can enter only if you have a ticket.
2. You have a ticket.
C. Therefore, you can enter.
```

Dictionary:

- `E = "You can enter."`
- `T = "You have a ticket."`

```sf
1. E ⊃ T
2. T
C. E
```

Having a ticket is necessary for entry, not sufficient: the venue might be full.

**Negated parts.**

```sf
1. If the shop is closed, then the lights are not on.
2. The lights are not on.
C. Therefore, the shop is closed.
```

Dictionary:

- `S = "The shop is closed."`
- `N = "The lights are on."`

```sf
1. S ⊃ ~N
2. ~N
C. S
```

The consequent is `~N`, and premise 2 affirms it. The lights might simply be broken.

Treating a necessary condition as if it were sufficient is this fallacy; see [necessary and sufficient conditions](necessary-sufficient).

## Look-alike forms

| Form | Symbolic | Valid? |
| --- | --- | --- |
| Affirming the consequent | `P ⊃ Q, Q ∴ P` | Invalid |
| [Modus ponens](modus-ponens) (affirms the antecedent) | `P ⊃ Q, P ∴ Q` | Valid |
| [Denying the antecedent](denying-the-antecedent) | `P ⊃ Q, ~P ∴ ~Q` | Invalid |
| [Modus tollens](modus-tollens) (denies the consequent) | `P ⊃ Q, ~Q ∴ ~P` | Valid |

Affirming the consequent is easily confused with modus ponens.

## When similar reasoning is acceptable

**"If" meaning "if and only if".** Speakers sometimes say "if" when they mean "if and only if". If the context shows that the conditional also runs the other way, add `Q ⊃ P` as a [hidden premise](hidden-premise). Then concluding P from Q is valid, but it is a different argument, and the extra premise must itself be true.

**As inductive support.** Testing a hypothesis by its predictions has this shape:

```sf
1. If the hypothesis is true, then the prediction comes true.
2. The prediction comes true.
C. Therefore, the hypothesis is true.
```

Dictionary:

- `H = "The hypothesis is true."`
- `E = "The prediction comes true."`

```sf
1. H ⊃ E
2. E
C. H
```

As a deduction this is invalid, so a successful prediction cannot prove a hypothesis. On the [hypothetico-deductive](hypothetico-deductive) view, it confirms (supports) the hypothesis instead.

## Related concepts
[Modus ponens](modus-ponens) · [Denying the antecedent](denying-the-antecedent) · [Modus tollens](modus-tollens) · [Deductively valid and invalid](valid) · [Necessary and sufficient conditions](necessary-sufficient) · [Hidden premise](hidden-premise) · [The hypothetico-deductive method](hypothetico-deductive)

## Sources
- Bland, *Reason* (Revised Edition), ch. 2, pp. 31–34; ch. 3, pp. 52–53. CC BY-NC 4.0.
- Magnus, Button, Trueman and Zach, *forall x: Calgary* (Fall 2025), ch. 5, §5.5, pp. 41–42. CC BY 4.0.
- Crupi, V., "Confirmation", *Stanford Encyclopedia of Philosophy* (rev. 4 Aug 2025), §2. https://plato.stanford.edu/entries/confirmation/
