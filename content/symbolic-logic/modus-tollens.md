---
id: modus-tollens
title: Modus tollens
type: logic-form
units: [1]
section: symbolic-logic
status: checked
related: [modus-ponens, denying-the-antecedent, affirming-the-consequent, valid, logical-operators, popper-demarcation]
sources: [bland-reason-ch2, bland-reason-ch3-truth-table, bland-reason-ch3-wording, bland-reason-answers, popper-link]
---

# Modus tollens

**Modus tollens is a valid deductive argument form: it takes a conditional, denies its consequent, and concludes that its antecedent is false.** The Latin is short for *modus tollendo tollens*, "the method of denying by denying".

## The form

In a conditional "If P, then Q", P is the *antecedent* and Q is the *consequent*.

| Standard form | Symbolic form |
| --- | --- |
| 1. If P, then Q. | `P ⊃ Q` |
| 2. Not Q. | `~Q` |
| C. Therefore, not P. | `∴ ~P` |

Line form: `P ⊃ Q, ~Q ∴ ~P`

## Example

> If the oval is waterlogged, then Saturday's game is cancelled. Saturday's game is not cancelled. Therefore, the oval is not waterlogged.

Dictionary: `O = "The oval is waterlogged."` `C = "Saturday's game is cancelled."`

```sf
1. O ⊃ C
2. ~C
C. ~O
```

The argument is valid: if both premises are true, the conclusion must be true. It is [sound](sound) only if the premises are also true; the first is false if a waterlogged game would be moved to another ground.

## Why it is valid

A truth table tests whether an argument form is valid: if no row has all true premises and a false conclusion, the form is valid (1 = true, 0 = false).

<!-- interactive: truth-table; premises: P ⊃ Q, ~Q; conclusion: ~P -->

| P | Q | Premise 1: `P ⊃ Q` | Premise 2: `~Q` | Conclusion: `~P` |
| --- | --- | --- | --- | --- |
| 1 | 1 | 1 | 0 | 0 |
| 1 | 0 | 0 | 1 | 0 |
| 0 | 1 | 1 | 0 | 1 |
| 0 | 0 | 1 | 1 | 1 |

*Text alternative:* both premises are true only in the last row (P false, Q false), and there the conclusion is also true. No row has true premises and a false conclusion, so the form is valid.

## Variations you will meet

- **Negated parts.** The consequent may already be negative. For example: "The car can't be out of fuel because if it were, the engine wouldn't start. The engine started just fine, so the car has fuel." With `F = "The car is out of fuel."` and `E = "The engine starts."`, this is `F ⊃ ~E, E ∴ ~F`. Asserting E denies the consequent `~E`, so it is still modus tollens.
- **Exact wording.** The second premise must deny the same proposition as the consequent. Consider: "If a person is compassionate, then they donate to charity. Maria does not give money to charity..." the argument only looks like modus tollens. "Donating to charity" and "giving money to charity" may not mean the same thing (Maria may volunteer her time), so the argument is not deductively valid. (Applying a premise about "a person" to Maria is a generalised modus tollens, which is accepted at this level.) A dictionary of propositions helps you catch this.

## Look-alike forms

| Form | Symbolic | Valid? |
| --- | --- | --- |
| Modus tollens (denies the consequent) | `P ⊃ Q, ~Q ∴ ~P` | Valid |
| [Modus ponens](modus-ponens) (affirms the antecedent) | `P ⊃ Q, P ∴ Q` | Valid |
| [Denying the antecedent](denying-the-antecedent) | `P ⊃ Q, ~P ∴ ~Q` | Invalid |
| [Affirming the consequent](affirming-the-consequent) | `P ⊃ Q, Q ∴ P` | Invalid |

Both formal fallacies fail in the same row: P false and Q true. For example, the oval might be dry (not waterlogged) while the game is cancelled for another reason, such as a storm warning.

## Where it matters

Karl Popper (1902–1994) built his account of science on a logical asymmetry: no number of observations can verify a universal law, but a single genuine counter-instance falsifies it. The falsifying step has the form of modus tollens: if the law is true, no counter-instance occurs; one occurs; so the law is false. Popper also held that, in practice, one conflicting observation is never methodologically sufficient for falsification, because deciding whether an apparent counter-instance is genuine can be problematic. See [Popper's demarcation problem](popper-demarcation).

## Related concepts
[Modus ponens](modus-ponens) · [Denying the antecedent](denying-the-antecedent) · [Affirming the consequent](affirming-the-consequent) · [Deductively valid and invalid](valid) · [Logical operators](logical-operators) · [Popper's demarcation problem](popper-demarcation)

## Sources
- Bland, *Reason* (Revised Edition), ch. 2, pp. 26–27, 31 (exercise i); ch. 3, pp. 50–51, 68–69; answers, p. 121. CC BY-NC 4.0.
- Thornton, S., "Karl Popper", *Stanford Encyclopedia of Philosophy* (rev. 31 Jul 2026), §§1, 3–4. https://plato.stanford.edu/entries/popper/
