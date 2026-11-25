---
id: hypothetical-syllogism
title: Hypothetical syllogism
type: logic-form
units: [1]
section: symbolic-logic
status: drafted
related: [modus-ponens, modus-tollens, constructive-dilemma, slippery-slope, valid, logical-operators]
sources: [bland-reason-ch2-hs, bland-reason-ch3-hs-table, iep-prop-logic-hs]
---

# Hypothetical syllogism

**Hypothetical syllogism is a valid deductive argument form: from two conditionals, where the consequent of the first is the antecedent of the second, it concludes a conditional linking the first antecedent to the last consequent.** Its conclusion is itself a conditional. It is also called chain reasoning.

## The form

| Standard form | Symbolic form |
| --- | --- |
| 1. If P, then Q. | `P ⊃ Q` |
| 2. If Q, then R. | `Q ⊃ R` |
| C. Therefore, if P, then R. | `∴ P ⊃ R` |

Line form: `P ⊃ Q, Q ⊃ R ∴ P ⊃ R`

## Example

```sf
1. If it rains on Saturday, then the cross-country will be postponed.
2. If the cross-country is postponed, then it will clash with the debating final.
C. Therefore, if it rains on Saturday, then the cross-country will clash with the debating final.
```

Dictionary:

- `R = "It rains on Saturday."`
- `T = "The cross-country will be postponed."`
- `D = "The cross-country will clash with the debating final."`

```sf
1. R ⊃ T
2. T ⊃ D
C. R ⊃ D
```

The two premises share a link, T: it is the consequent of the first and the antecedent of the second. The conclusion does not say that it will rain, or that there will be a clash. It says only that rain would lead to a clash.

## Why it is valid

With three letters, the truth table has eight rows (1 = true, 0 = false).

<!-- interactive: truth-table; premises: P ⊃ Q, Q ⊃ R; conclusion: P ⊃ R -->

| P | Q | R | Premise 1: `P ⊃ Q` | Premise 2: `Q ⊃ R` | Conclusion: `P ⊃ R` |
| --- | --- | --- | --- | --- | --- |
| 1 | 1 | 1 | 1 | 1 | 1 |
| 1 | 1 | 0 | 1 | 0 | 0 |
| 1 | 0 | 1 | 0 | 1 | 1 |
| 1 | 0 | 0 | 0 | 1 | 0 |
| 0 | 1 | 1 | 1 | 1 | 1 |
| 0 | 1 | 0 | 1 | 0 | 1 |
| 0 | 0 | 1 | 1 | 1 | 1 |
| 0 | 0 | 0 | 1 | 1 | 1 |

A counterexample needs a false conclusion, so only the rows where the conclusion is false need checking. `P ⊃ R` is false only when P is true and R is false (rows 2 and 4). In each of those rows one premise is false. No row has true premises and a false conclusion, so the form is valid.

## Variations you will meet

- **Longer chains.** The chain can have any number of links, as long as each consequent is the next antecedent: `P ⊃ Q, Q ⊃ R, R ⊃ S ∴ P ⊃ S`.
- **Order.** The premises may be given in either order.
- **Negated parts.** "If the alarm doesn't go off, Izabella will wake up late. If she wakes up late, she will miss the bus. So if the alarm doesn't go off, she will miss the bus." With `A = "The alarm goes off."`, `L = "Izabella wakes up late."` and `B = "Izabella misses the bus."`: `~A ⊃ L, L ⊃ B ∴ ~A ⊃ B`.

## Look-alike forms

The links must join, end to end. These look similar but are invalid:

| Form | Symbolic | Valid? | Counterexample |
| --- | --- | --- | --- |
| Hypothetical syllogism | `P ⊃ Q, Q ⊃ R ∴ P ⊃ R` | Valid | None |
| Two conditionals sharing a consequent | `P ⊃ Q, R ⊃ Q ∴ P ⊃ R` | Invalid | P true, Q true, R false |
| Two conditionals sharing an antecedent | `P ⊃ Q, P ⊃ R ∴ Q ⊃ R` | Invalid | P false, Q true, R false |
| Conclusion reversed | `P ⊃ Q, Q ⊃ R ∴ R ⊃ P` | Invalid | P false, R true |

## Where it matters

A [slippery slope](slippery-slope) argument is often a chain of conditionals. The chain's form is valid; whether the argument is any good depends on whether every link is true.

## Related concepts
[Modus ponens](modus-ponens) · [Modus tollens](modus-tollens) · [Constructive dilemma](constructive-dilemma) · [Slippery slope](slippery-slope) · [Deductively valid and invalid](valid) · [Logical operators](logical-operators)

## Sources
- Bland, *Reason* (Revised Edition), ch. 2, pp. 27–28, 35 (Exercise 2.3 m); ch. 3, p. 52. CC BY-NC 4.0.
- Klement, K. C., "Propositional Logic", *Internet Encyclopedia of Philosophy*, §5.b. https://iep.utm.edu/propositional-logic-sentential-logic/
