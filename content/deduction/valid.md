---
id: valid
title: Deductively valid and invalid
type: term
units: [1]
section: deduction
status: checked
related: [deduction, sound, modus-ponens, modus-tollens, affirming-the-consequent, denying-the-antecedent, logical-operators, classifying-arguments, hidden-premise]
sources: [bland-reason-validity, forallx-ch2-validity]
---

# Deductively valid and invalid

**A deductive argument is valid if and only if the truth of its premises guarantees the truth of its conclusion.** In other words, it is impossible for all the premises to be true and the conclusion false. A deductive argument that is not valid is invalid.

## Form, not truth

For the arguments studied at this level, validity depends on an argument's structure, not on whether its premises are actually true. Some arguments are valid because of what their words mean: "Priya is an ophthalmologist, so Priya is an eye doctor." These are not covered here.

```sf
1. If the moon is made of cheese, then aliens exist.
2. The moon is made of cheese.
C. Therefore, aliens exist.
```

Premise 2 is false, but the argument is valid: *if* both premises were true, the conclusion could not be false. Whether they are true is a question of [soundness](sound).

## The four combinations

| Premises | Conclusion | Possible in a valid argument? | Example |
| --- | --- | --- | --- |
| All true | True | Yes | If Brisbane is in Queensland, then Brisbane is in Australia. Brisbane is in Queensland. Therefore, Brisbane is in Australia. |
| At least one false | False | Yes | Oranges are either fruit or musical instruments. Oranges are not fruit. Therefore, oranges are musical instruments. |
| At least one false | True | Yes | If Sydney is in Queensland, then Sydney is in Australia. Sydney is in Queensland. Therefore, Sydney is in Australia. |
| All true | False | **No** | This is exactly what validity rules out. |

So a true conclusion does not make an argument valid. This argument has true premises and a true conclusion, but it is invalid: nothing in the premises guarantees where Hobart is.

```sf
1. Brisbane is in Queensland.
2. Perth is in Western Australia.
C. Therefore, Hobart is in Tasmania.
```

## Testing validity

If an argument fits one of the valid named forms (see [classifying arguments](classifying-arguments)), you can state that it is valid. Otherwise, [symbolise](translating-symbolising) the argument and build a truth table. If no row has all true premises and a false conclusion, the argument is valid. If a row does, the argument is invalid. That row is a **counterexample**: a case in which the premises are true and the conclusion is false.

A truth table tests validity that depends on the logical operators (`~`, `&`, `∨`, `⊃`). It cannot test arguments whose validity depends on words such as "all" and "some", or on what words mean; see [classifying arguments](classifying-arguments).

> If it is raining, then the oval is wet. The oval is wet. Therefore, it is raining.

Dictionary: `R = "It is raining."` `W = "The oval is wet."` Form: `R ⊃ W, W ∴ R`. This is the formal fallacy of [affirming the consequent](affirming-the-consequent). In the table, 1 = true and 0 = false.

| R | W | Premise 1: `R ⊃ W` | Premise 2: `W` | Conclusion: `R` |
| --- | --- | --- | --- | --- |
| 1 | 1 | 1 | 1 | 1 |
| 1 | 0 | 0 | 0 | 1 |
| **0** | **1** | **1** | **1** | **0** |
| 0 | 0 | 1 | 0 | 0 |

*Text alternative:* in the third row (in bold: R false, W true), both premises are true and the conclusion is false. The oval is wet, but it is not raining (the sprinklers were on). That counterexample makes the argument invalid. The other formal fallacy, [denying the antecedent](denying-the-antecedent) (`R ⊃ W, ~R ∴ ~W`), fails in the same row.

## All or nothing

Validity has no degrees: an argument is never "partly valid" or "more valid" than another.

An argument that lacks this guarantee is not necessarily a poor one. If it aims only to make its conclusion probable, it is [inductive](induction), and is judged as [strong or weak](strong-weak) instead.

## Related concepts
[Deduction](deduction) · [Sound and unsound](sound) · [Modus ponens](modus-ponens) · [Modus tollens](modus-tollens) · [Affirming the consequent](affirming-the-consequent) · [Denying the antecedent](denying-the-antecedent) · [Logical operators](logical-operators) · [Classifying arguments](classifying-arguments) · [Hidden premise](hidden-premise)

## Sources
- Bland, *Reason* (Revised Edition), ch. 1, §1.4 pp. 18–19; ch. 3, pp. 36, 50. CC BY-NC 4.0.
- Magnus, Button, Trueman and Zach, *forall x: Calgary* (Fall 2025), ch. 2, §§2.2–2.5, pp. 8–16. CC BY 4.0.
