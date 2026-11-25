---
id: constructive-dilemma
title: Constructive dilemma
type: logic-form
units: [1]
section: symbolic-logic
status: approved
related: [modus-ponens, disjunctive-syllogism, hypothetical-syllogism, modus-tollens, sound, hidden-premise, valid]
sources: [bland-reason-ch2-cd, iep-prop-logic-cd, wilson-good-reasoning-12-3]
---

# Constructive dilemma

**Constructive dilemma is a valid deductive argument form: from two conditionals and a disjunction of their antecedents, it concludes the disjunction of their consequents.** It works like two [modus ponens](modus-ponens) arguments at once: whichever antecedent is true, its consequent follows.

## The form

| Standard form | Symbolic form |
| --- | --- |
| 1. If P, then Q. | `P ⊃ Q` |
| 2. If R, then S. | `R ⊃ S` |
| 3. P or R. | `P ∨ R` |
| C. Therefore, Q or S. | `∴ Q ∨ S` |

Line form: `P ⊃ Q, R ⊃ S, P ∨ R ∴ Q ∨ S`. Like the destructive dilemma below, it has three premises; the other named valid forms have two in their basic versions.

## Example

```sf
1. If the athletics carnival is held on Friday, then Year 12 will miss a practice exam.
2. If the athletics carnival is held on Saturday, then fewer families will be able to attend.
3. The athletics carnival is held on Friday or on Saturday.
C. Therefore, Year 12 will miss a practice exam or fewer families will be able to attend.
```

Dictionary:

- `F = "The athletics carnival is held on Friday."`
- `M = "Year 12 will miss a practice exam."`
- `S = "The athletics carnival is held on Saturday."`
- `W = "Fewer families will be able to attend."`

```sf
1. F ⊃ M
2. S ⊃ W
3. F ∨ S
C. M ∨ W
```

## Why it is valid

With four letters, the truth table has 16 rows (1 = true, 0 = false).

<!-- interactive: truth-table; premises: P ⊃ Q, R ⊃ S, P ∨ R; conclusion: Q ∨ S -->

| Row | P | Q | R | S | Premise 1: `P ⊃ Q` | Premise 2: `R ⊃ S` | Premise 3: `P ∨ R` | Conclusion: `Q ∨ S` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 2 | 1 | 1 | 1 | 0 | 1 | 0 | 1 | 1 |
| 3 | 1 | 1 | 0 | 1 | 1 | 1 | 1 | 1 |
| 4 | 1 | 1 | 0 | 0 | 1 | 1 | 1 | 1 |
| 5 | 1 | 0 | 1 | 1 | 0 | 1 | 1 | 1 |
| 6 | 1 | 0 | 1 | 0 | 0 | 0 | 1 | 0 |
| 7 | 1 | 0 | 0 | 1 | 0 | 1 | 1 | 1 |
| 8 | 1 | 0 | 0 | 0 | 0 | 1 | 1 | 0 |
| 9 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 10 | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 1 |
| 11 | 0 | 1 | 0 | 1 | 1 | 1 | 0 | 1 |
| 12 | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 1 |
| 13 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 |
| 14 | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| 15 | 0 | 0 | 0 | 1 | 1 | 1 | 0 | 1 |
| 16 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 |

A counterexample needs a false conclusion, so only the rows where the conclusion is false need checking. `Q ∨ S` is false only when Q and S are both false: rows 6, 8, 14 and 16. In each of these, at least one premise is false. No row has true premises and a false conclusion, so the form is valid.

## Variations you will meet

- **Order.** The disjunction, or the conclusion, may list the parts in the other order: `P ⊃ Q, R ⊃ S, R ∨ P ∴ S ∨ Q` is still a constructive dilemma, because the order of disjuncts makes no difference to the truth of a disjunction.
- **One shared consequent.** When both conditionals have the same consequent, the conclusion is that consequent alone: `P ⊃ Q, R ⊃ Q, P ∨ R ∴ Q`. This is also valid.
- **Unstated parts.** Dilemmas in ordinary speech often leave parts unstated: the disjunction, the conditionals, or the conclusion. Supplying a missing premise is a matter of identifying a [hidden premise](hidden-premise); a missing conclusion must also be stated before the argument is evaluated.

## Look-alike forms

| Form | Symbolic | Valid? |
| --- | --- | --- |
| Constructive dilemma (affirms one antecedent or the other) | `P ⊃ Q, R ⊃ S, P ∨ R ∴ Q ∨ S` | Valid |
| Destructive dilemma (denies one consequent or the other) | `P ⊃ Q, R ⊃ S, ~Q ∨ ~S ∴ ~P ∨ ~R` | Valid |
| Affirms the consequents | `P ⊃ Q, R ⊃ S, Q ∨ S ∴ P ∨ R` | Invalid |

The destructive dilemma relates to [modus tollens](modus-tollens) as the constructive dilemma relates to modus ponens. The invalid form affirms the consequents: it fails, for example, when Q is true but P and R are both false.

## Evaluating a dilemma

Because the form is valid, the only way to resist the argument is to challenge a premise: show that it is false, or that it has not been shown to be true. This does not show that the conclusion is false, only that the argument has not established it. The two options in the disjunction are called the *horns* of the dilemma.

- **Escaping between the horns**: showing that the disjunction is false, because there is another option. If the carnival will in fact be held on Thursday, premise 3 is false.
- **Attacking a horn**: showing that one of the conditionals is false. If the carnival is held on Friday but the practice exam is moved to another day, Year 12 will not miss it, and premise 1 is false.

## Related concepts
[Modus ponens](modus-ponens) · [Modus tollens](modus-tollens) · [Disjunctive syllogism](disjunctive-syllogism) · [Hypothetical syllogism](hypothetical-syllogism) · [Deductively valid and invalid](valid) · [Sound and unsound](sound) · [Hidden premise](hidden-premise)

## Sources
- Bland, *Reason* (Revised Edition), ch. 2, pp. 29–30 (incl. Exercise 2.1 d). CC BY-NC 4.0.
- Klement, K. C., "Propositional Logic", *Internet Encyclopedia of Philosophy*, §5.b. https://iep.utm.edu/propositional-logic-sentential-logic/
- Wilson, D. C., *A Guide to Good Reasoning: Cultivating Intellectual Virtues*, ch. 12, §12.3. University of Minnesota Libraries. CC BY-NC 4.0. https://open.lib.umn.edu/goodreasoning/chapter/chapter-12-either-or-arguments-and-more/
