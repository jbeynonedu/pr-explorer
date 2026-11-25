---
id: denying-the-antecedent
title: Denying the antecedent
type: logic-form
units: [1]
section: symbolic-logic
status: drafted
related: [modus-tollens, affirming-the-consequent, modus-ponens, valid, necessary-sufficient, hidden-premise]
sources: [bland-reason-ch2-da, forallx-5-5-iff]
---

# Denying the antecedent

**Denying the antecedent is a formal fallacy: an invalid argument form that takes a conditional, denies its antecedent, and concludes that its consequent is false.** It is a mistake in the argument's structure, not its content: the form alone never guarantees the conclusion.

## The form

| Standard form | Symbolic form |
| --- | --- |
| 1. If P, then Q. | `P ⊃ Q` |
| 2. Not P. | `~P` |
| C. Therefore, not Q. | `∴ ~Q` |

Line form: `P ⊃ Q, ~P ∴ ~Q`

## Example

```sf
1. If it is a public holiday, then the library is closed.
2. It is not a public holiday.
C. Therefore, the library is not closed.
```

Dictionary:

- `H = "It is a public holiday."`
- `L = "The library is closed."`

```sf
1. H ⊃ L
2. ~H
C. ~L
```

Premise 1 says that a public holiday is enough to close the library. It does not say that nothing else can. The library might be closed for renovations on an ordinary day: the premises would be true and the conclusion false. That **counterexample** shows the argument is invalid.

## Why it is invalid

A truth table tests whether an argument form is valid: if any row has all true premises and a false conclusion, the form is invalid (1 = true, 0 = false).

<!-- interactive: truth-table; premises: P ⊃ Q, ~P; conclusion: ~Q -->

| P | Q | Premise 1: `P ⊃ Q` | Premise 2: `~P` | Conclusion: `~Q` |
| --- | --- | --- | --- | --- |
| 1 | 1 | 1 | 0 | 0 |
| 1 | 0 | 0 | 0 | 1 |
| **0** | **1** | **1** | **1** | **0** |
| 0 | 0 | 1 | 1 | 1 |

In the third row (in bold: P false, Q true), both premises are true and the conclusion is false. That row is the counterexample.

## Variations you will meet
- **"Only if" wording.**

```sf
1. You can enter only if you have a ticket.
2. You cannot enter.
C. Therefore, you do not have a ticket.
```

Dictionary:

- `E = "You can enter."`
- `T = "You have a ticket."`

```sf
1. E ⊃ T
2. ~E
C. ~T
```

Premise 2 denies the antecedent E. You might have a ticket but arrive after the doors close.
- **Negated parts.**

```sf
1. If the power is out, then the lights do not work.
2. The power is not out.
C. Therefore, the lights work.
```

Dictionary:

- `O = "The power is out."`
- `W = "The lights work."`

```sf
1. O ⊃ ~W
2. ~O
C. W
```

Premise 2 denies the antecedent O. The lights might be broken for another reason.

Treating a sufficient condition as if it were necessary is this fallacy; see [necessary and sufficient conditions](necessary-sufficient).

## Look-alike forms

| Form | Symbolic | Valid? |
| --- | --- | --- |
| Denying the antecedent | `P ⊃ Q, ~P ∴ ~Q` | Invalid |
| [Modus tollens](modus-tollens) (denies the consequent) | `P ⊃ Q, ~Q ∴ ~P` | Valid |
| [Affirming the consequent](affirming-the-consequent) | `P ⊃ Q, Q ∴ P` | Invalid |
| [Modus ponens](modus-ponens) (affirms the antecedent) | `P ⊃ Q, P ∴ Q` | Valid |

Denying the antecedent is easily confused with modus tollens. The two share the same conditional; only the denied part differs.

## When similar reasoning is acceptable
Speakers sometimes say "if" when they mean "if and only if". A parent might tell a child that if they don't eat their greens, they won't get any dessert. The child who eats the greens expects dessert, and usually the parent meant that too.

```sf
1. If you don't eat your greens, then you won't get dessert.
2. You eat your greens.
C. Therefore, you get dessert.
```

Dictionary:

- `G = "You eat your greens."`
- `D = "You get dessert."`

```sf
1. ~G ⊃ ~D
2. G
C. D
```

As it stands, this denies the antecedent `~G`, so it is invalid: the parent could keep their word and still give no dessert. If the context shows that the parent also meant "if you don't get dessert, it's because you didn't eat your greens", add `~D ⊃ ~G` as a [hidden premise](hidden-premise). Then the argument is valid (it becomes a modus tollens), but it is a different argument, and the extra premise must itself be true.

## Related concepts
[Modus tollens](modus-tollens) · [Affirming the consequent](affirming-the-consequent) · [Modus ponens](modus-ponens) · [Deductively valid and invalid](valid) · [Necessary and sufficient conditions](necessary-sufficient) · [Hidden premise](hidden-premise)

## Sources
- Bland, *Reason* (Revised Edition), ch. 2, pp. 32–34. CC BY-NC 4.0.
- Magnus, Button, Trueman and Zach, *forall x: Calgary* (Fall 2025), ch. 5, §5.5, pp. 41–42. CC BY 4.0.
