---
id: modus-ponens
title: Modus ponens
type: logic-form
units: [1]
section: symbolic-logic
status: approved
related: [modus-tollens, affirming-the-consequent, denying-the-antecedent, hypothetical-syllogism, valid, sound, logical-operators, translating-symbolising]
sources: [bland-reason-ch2-mp, bland-reason-confusion, forallx-17-4, carroll-1895, carroll-dates]
---

# Modus ponens

**Modus ponens is a valid deductive argument form: it takes a conditional, affirms its antecedent, and concludes its consequent.** The name is short for *modus ponendo ponens*, "the method of affirming by affirming".

## The form

In a conditional "If P, then Q", P is the *antecedent* and Q is the *consequent*.

| Standard form | Symbolic form |
| --- | --- |
| 1. If P, then Q. | `P ⊃ Q` |
| 2. P. | `P` |
| C. Therefore, Q. | `∴ Q` |

Line form: `P ⊃ Q, P ∴ Q`

## Example

```sf
1. If a bushfire warning is issued for the area, then the school camp will be cancelled.
2. A bushfire warning is issued for the area.
C. Therefore, the school camp will be cancelled.
```

Dictionary:

- `W = "A bushfire warning is issued for the area."`
- `K = "The school camp will be cancelled."`

```sf
1. W ⊃ K
2. W
C. K
```

The argument is valid: if both premises are true, the conclusion must be true. It is [sound](sound) only if the premises are also true. Premise 1 would be false if the school moved the camp to another site instead of cancelling it.

## Why it is valid

A truth table tests whether an argument form is valid: if no row has all true premises and a false conclusion, the form is valid (1 = true, 0 = false).

<!-- interactive: truth-table; premises: P ⊃ Q, P; conclusion: Q -->

| P | Q | Premise 1: `P ⊃ Q` | Premise 2: `P` | Conclusion: `Q` |
| --- | --- | --- | --- | --- |
| 1 | 1 | 1 | 1 | 1 |
| 1 | 0 | 0 | 1 | 0 |
| 0 | 1 | 1 | 0 | 1 |
| 0 | 0 | 1 | 0 | 0 |

Both premises are true only in the first row (P true, Q true), and there the conclusion is also true. No row has true premises and a false conclusion, so the form is valid.

## Variations you will meet
**Different wording.** "Q if P" and "P only if Q" both express `P ⊃ Q`.

```sf
1. You can sit the exam only if you have your student card.
2. You can sit the exam.
C. Therefore, you have your student card.
```

Dictionary:

- `E = "You can sit the exam."`
- `S = "You have your student card."`

```sf
1. E ⊃ S
2. E
C. S
```

**Negated parts.** The antecedent may itself be a negation.

```sf
1. If it is not a school day, then the canteen is closed.
2. It is not a school day.
C. Therefore, the canteen is closed.
```

Dictionary:

- `D = "It is a school day."`
- `L = "The canteen is closed."`

```sf
1. ~D ⊃ L
2. ~D
C. L
```

Premise 2 affirms the antecedent `~D`, so this is still modus ponens.

**Order.** The premises may come in either order; what matters is that one affirms the antecedent of the other.

## Look-alike forms

| Form | Symbolic | Valid? |
| --- | --- | --- |
| Modus ponens (affirms the antecedent) | `P ⊃ Q, P ∴ Q` | Valid |
| [Modus tollens](modus-tollens) (denies the consequent) | `P ⊃ Q, ~Q ∴ ~P` | Valid |
| [Affirming the consequent](affirming-the-consequent) | `P ⊃ Q, Q ∴ P` | Invalid |
| [Denying the antecedent](denying-the-antecedent) | `P ⊃ Q, ~P ∴ ~Q` | Invalid |

Affirming the consequent is the form that most resembles modus ponens. It fails in the row P false, Q true: the camp might be cancelled for another reason, such as a bus breakdown.

## Where it matters

In "What the Tortoise Said to Achilles" (1895), Lewis Carroll (1832–1898) has the Tortoise accept two premises, A and B, but refuse their conclusion, Z. Achilles adds a third premise:

> (C) If A and B are true, Z must be true.

Lewis Carroll, "What the Tortoise Said to Achilles", *Mind* 4 (1895), p. 279.

Carroll's A, B and Z are steps from Euclid's geometry:

- A: "Things that are equal to the same are equal to each other."
- B: "The two sides of this Triangle are things that are equal to the same."
- Z: "The two sides of this Triangle are equal to each other."

Carroll, "What the Tortoise Said to Achilles", p. 278.

With C, and taking A and B together, the step to Z has the form of modus ponens: `(A & B) ⊃ Z, A & B ∴ Z`.

## Related concepts
[Modus tollens](modus-tollens) · [Affirming the consequent](affirming-the-consequent) · [Denying the antecedent](denying-the-antecedent) · [Hypothetical syllogism](hypothetical-syllogism) · [Deductively valid and invalid](valid) · [Sound and unsound](sound) · [Logical operators](logical-operators) · [Translating and symbolising propositions](translating-symbolising)

## Sources
- Bland, *Reason* (Revised Edition), ch. 2, pp. 26, 31–32; ch. 3, p. 50. CC BY-NC 4.0.
- Magnus, Button, Trueman and Zach, *forall x: Calgary* (Fall 2025), ch. 17, §17.4, p. 121. CC BY 4.0.
- Carroll, L., "What the Tortoise Said to Achilles", *Mind*, New Series, 4(14) (1895), pp. 278–280 (C first appears on p. 279). Public domain. Text: https://math.dartmouth.edu/~matc/Readers/HowManyAngels/Tortoise.html
- "Lewis Carroll", *Britannica* (dates). https://www.britannica.com/biography/Lewis-Carroll
