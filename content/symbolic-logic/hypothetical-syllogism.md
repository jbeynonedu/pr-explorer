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
1. If it rains on Saturday, then the cross-country is postponed.
2. If the cross-country is postponed, then the cross-country clashes with the debating final.
C. Therefore, if it rains on Saturday, then the cross-country clashes with the debating final.
```

Dictionary:

- `S = "It rains on Saturday."`
- `T = "The cross-country is postponed."`
- `D = "The cross-country clashes with the debating final."`

```sf
1. S ⊃ T
2. T ⊃ D
C. S ⊃ D
```

The two premises share a link, T: it is the consequent of the first and the antecedent of the second. The conclusion does not say that it will rain, or that there will be a clash. It says only that if it rains on Saturday, there will be a clash.

## Why it is valid

With three letters, the truth table has eight rows (1 = true, 0 = false).

<!-- interactive: truth-table; premises: P ⊃ Q, Q ⊃ R; conclusion: P ⊃ R -->

| Row | P | Q | R | Premise 1: `P ⊃ Q` | Premise 2: `Q ⊃ R` | Conclusion: `P ⊃ R` |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 2 | 1 | 1 | 0 | 1 | 0 | 0 |
| 3 | 1 | 0 | 1 | 0 | 1 | 1 |
| 4 | 1 | 0 | 0 | 0 | 1 | 0 |
| 5 | 0 | 1 | 1 | 1 | 1 | 1 |
| 6 | 0 | 1 | 0 | 1 | 0 | 1 |
| 7 | 0 | 0 | 1 | 1 | 1 | 1 |
| 8 | 0 | 0 | 0 | 1 | 1 | 1 |

A counterexample needs a false conclusion, so only the rows where the conclusion is false need checking. `P ⊃ R` is false only when P is true and R is false (rows 2 and 4). In each of those rows one premise is false. No row has true premises and a false conclusion, so the form is valid.

## Variations you will meet

- **Longer chains.** The chain can have any number of links, as long as each consequent is the next antecedent: `P ⊃ Q, Q ⊃ R, R ⊃ S ∴ P ⊃ S`.
- **Order.** The premises may be given in either order.
- **Negated parts.**

```sf
1. If the canteen does not open, then Sam buys lunch at the shop.
2. If Sam buys lunch at the shop, then Sam is late to class.
C. Therefore, if the canteen does not open, then Sam is late to class.
```

Dictionary:

- `O = "The canteen opens."`
- `B = "Sam buys lunch at the shop."`
- `L = "Sam is late to class."`

```sf
1. ~O ⊃ B
2. B ⊃ L
C. ~O ⊃ L
```

## Look-alike forms

The links must join, end to end. These look similar but are invalid:

| Form | Symbolic | Valid? | Counterexample |
| --- | --- | --- | --- |
| Hypothetical syllogism | `P ⊃ Q, Q ⊃ R ∴ P ⊃ R` | Valid | None |
| Two conditionals sharing a consequent | `P ⊃ Q, R ⊃ Q ∴ P ⊃ R` | Invalid | P true, Q true, R false |
| Two conditionals sharing an antecedent | `P ⊃ Q, P ⊃ R ∴ Q ⊃ R` | Invalid | P false, Q true, R false |
| Conclusion reversed | `P ⊃ Q, Q ⊃ R ∴ R ⊃ P` | Invalid | P false, R true |

## Where it matters

A [slippery slope](slippery-slope) argument is often a chain of conditionals. The chain's form is valid; whether the argument is sound depends on whether every link is true.

## Related concepts
[Modus ponens](modus-ponens) · [Modus tollens](modus-tollens) · [Constructive dilemma](constructive-dilemma) · [Slippery slope](slippery-slope) · [Deductively valid and invalid](valid) · [Logical operators](logical-operators)

## Sources
- Bland, *Reason* (Revised Edition), ch. 2, pp. 27–28; ch. 3, p. 52. CC BY-NC 4.0.
- Klement, K. C., "Propositional Logic", *Internet Encyclopedia of Philosophy*, §5.b. https://iep.utm.edu/propositional-logic-sentential-logic/
