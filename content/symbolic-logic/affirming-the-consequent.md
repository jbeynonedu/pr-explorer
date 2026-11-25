---
id: affirming-the-consequent
title: Affirming the consequent
type: logic-form
units: [1]
section: symbolic-logic
status: drafted
related: [modus-ponens, denying-the-antecedent, modus-tollens, valid, necessary-sufficient, hidden-premise, hypothetico-deductive]
sources: [bland-reason-ch2-ac, bland-reason-ch3-ac-table, forallx-5-5-iff, sep-confirmation]
---

# Affirming the consequent

**Affirming the consequent is a formal fallacy: an invalid argument form that takes a conditional, affirms its consequent, and concludes its antecedent.** It is a mistake in the argument's structure, not its content, so every argument of this form shares the flaw.

## The form

| Standard form | Symbolic form |
| --- | --- |
| 1. If P, then Q. | `P ⊃ Q` |
| 2. Q. | `Q` |
| C. Therefore, P. | `∴ P` |

Line form: `P ⊃ Q, Q ∴ P`

## Example

```sf
1. If there is a power outage across the suburb, then the traffic lights are off.
2. The traffic lights are off.
C. Therefore, there is a power outage across the suburb.
```

Dictionary:

- `O = "There is a power outage across the suburb."`
- `L = "The traffic lights are off."`

```sf
1. O ⊃ L
2. L
C. O
```

Both premises could be true while the conclusion is false: the lights might be off because of a fault at one intersection. That possibility is a **counterexample**, and it shows the argument is invalid.

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

The conditional may be worded in other ways. Each of these is `P ⊃ Q`, so affirming Q and concluding P is still the fallacy:

- "Q if P": "R if S. R. Therefore, S."
- "P only if Q": "Y only if X. X. Therefore, Y."
- "P is sufficient for Q", or "Q is necessary for P". Treating a necessary condition as if it were sufficient is this fallacy; see [necessary and sufficient conditions](necessary-sufficient).

## Look-alike forms

| Form | Symbolic | Valid? |
| --- | --- | --- |
| Affirming the consequent | `P ⊃ Q, Q ∴ P` | Invalid |
| [Modus ponens](modus-ponens) (affirms the antecedent) | `P ⊃ Q, P ∴ Q` | Valid |
| [Denying the antecedent](denying-the-antecedent) | `P ⊃ Q, ~P ∴ ~Q` | Invalid |
| [Modus tollens](modus-tollens) (denies the consequent) | `P ⊃ Q, ~Q ∴ ~P` | Valid |

Affirming the consequent is most often mistaken for modus ponens.

## When similar reasoning is acceptable

- **"If" meaning "if and only if".** Speakers sometimes say "if" when they mean "if and only if". If the context shows that the conditional runs both ways, `(P ⊃ Q) & (Q ⊃ P)`, then concluding P from Q is valid. But that is a different argument, with a stronger premise; state it as a [hidden premise](hidden-premise) if the context supports it.
- **As inductive support.** Testing a hypothesis by its predictions has this shape: if the hypothesis is true, the prediction will come true; it does; so the hypothesis is true. As a deduction this is invalid, so a successful prediction cannot prove a hypothesis. On the [hypothetico-deductive](hypothetico-deductive) view, it confirms (supports) the hypothesis instead.

## Related concepts
[Modus ponens](modus-ponens) · [Denying the antecedent](denying-the-antecedent) · [Modus tollens](modus-tollens) · [Deductively valid and invalid](valid) · [Necessary and sufficient conditions](necessary-sufficient) · [Hidden premise](hidden-premise) · [The hypothetico-deductive method](hypothetico-deductive)

## Sources
- Bland, *Reason* (Revised Edition), ch. 2, pp. 31–34; ch. 3, pp. 52–53. CC BY-NC 4.0.
- Magnus, Button, Trueman and Zach, *forall x: Calgary* (Fall 2025), ch. 5, §5.5, p. 41. CC BY 4.0.
- Crupi, V., "Confirmation", *Stanford Encyclopedia of Philosophy* (rev. 4 Aug 2025), introduction and §2. https://plato.stanford.edu/entries/confirmation/
