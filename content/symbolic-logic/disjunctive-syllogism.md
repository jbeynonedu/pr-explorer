---
id: disjunctive-syllogism
title: Disjunctive syllogism
type: logic-form
units: [1]
section: symbolic-logic
status: checked
related: [logical-operators, constructive-dilemma, modus-ponens, valid, sound, hidden-premise]
sources: [bland-reason-ch2-ds, forallx-19-1, iep-prop-logic-ds, wilson-good-reasoning-12, fallacy-files-affirming-a-disjunct, conan-doyle-1890, conan-doyle-dates]
---

# Disjunctive syllogism

**Disjunctive syllogism is a valid deductive argument form: from a disjunction and the denial of one disjunct, it concludes the other disjunct.** It is the formal name for the process of elimination. (Its traditional Latin name is *modus tollendo ponens*.)

## The form

A disjunction "P or Q" has two *disjuncts*, P and Q. Here "or" is [inclusive](logical-operators): the disjunction is true if at least one disjunct is true.

| Standard form | Symbolic form |
| --- | --- |
| 1. P or Q. | `P ∨ Q` |
| 2. Not P. | `~P` |
| C. Therefore, Q. | `∴ Q` |

Line form: `P ∨ Q, ~P ∴ Q`. Either disjunct may be denied: `P ∨ Q, ~Q ∴ P` is also a disjunctive syllogism.

## Example

```sf
1. The missing permission note is in Mia's bag or in Mia's locker.
2. The missing permission note is not in Mia's bag.
C. Therefore, the missing permission note is in Mia's locker.
```

Dictionary:

- `B = "The missing permission note is in Mia's bag."`
- `L = "The missing permission note is in Mia's locker."`

```sf
1. B ∨ L
2. ~B
C. L
```

## Why it is valid

A truth table tests whether an argument form is valid: if no row has all true premises and a false conclusion, the form is valid (1 = true, 0 = false).

<!-- interactive: truth-table; premises: P ∨ Q, ~P; conclusion: Q -->

| P | Q | Premise 1: `P ∨ Q` | Premise 2: `~P` | Conclusion: `Q` |
| --- | --- | --- | --- | --- |
| 1 | 1 | 1 | 0 | 1 |
| 1 | 0 | 1 | 0 | 0 |
| 0 | 1 | 1 | 1 | 1 |
| 0 | 0 | 0 | 1 | 0 |

Both premises are true only in the third row (P false, Q true), and there the conclusion is also true. So the form is valid.

## Variations you will meet

- **More than two disjuncts.** Options can be eliminated one at a time until one remains: `(P ∨ Q) ∨ R, ~P, ~Q ∴ R`.

**Negated disjuncts.** Asserting a proposition denies its negation, so this is also a disjunctive syllogism:

```sf
1. Either the canteen is not open, or there is a queue.
2. The canteen is open.
C. Therefore, there is a queue.
```

Dictionary:

- `O = "The canteen is open."`
- `U = "There is a queue."`

```sf
1. ~O ∨ U
2. O
C. U
```

## Look-alike forms

| Form | Symbolic | Valid? |
| --- | --- | --- |
| Disjunctive syllogism (denies a disjunct) | `P ∨ Q, ~P ∴ Q` | Valid |
| Affirming a disjunct | `P ∨ Q, P ∴ ~Q` | Invalid |

**Affirming a disjunct** (also called affirming an alternative) concludes that one disjunct is false because the other is true.

```sf
1. Ella studies Philosophy or Ella studies Physics.
2. Ella studies Philosophy.
C. Therefore, Ella does not study Physics.
```

Dictionary:

- `H = "Ella studies Philosophy."`
- `Y = "Ella studies Physics."`

```sf
1. H ∨ Y
2. H
C. ~Y
```

Because "or" is inclusive, Ella may study both. That is the counterexample: H true, Y true.

If the "or" really is exclusive ("one or the other, but not both"), the argument needs that as a further premise: here `~(H & Y)`. With it, the inference is valid, but it is a different argument. Check whether the context supports the extra premise before adding it.

## Where it matters

In *The Sign of Four* (1890), by Arthur Conan Doyle (1859–1930), Sherlock Holmes reasons about how an accomplice, "the ally", got into a locked room:

> How often have I said to you that when you have eliminated the impossible, whatever remains, however improbable, must be the truth? We know that he did not come through the door, the window, or the chimney.

Arthur Conan Doyle, *The Sign of Four* (London: Spencer Blackett, 1890), ch. 6.

Holmes also rules out hiding in the room, and Watson concludes that the ally came through the hole in the roof. The reasoning is a disjunctive syllogism with five disjuncts, so it is valid. It is [sound](sound) only if every premise is true, and the first premise, the list of options, is the one to check most carefully. If the list leaves an option out, the conclusion may be false.

## Related concepts
[Logical operators](logical-operators) · [Constructive dilemma](constructive-dilemma) · [Modus ponens](modus-ponens) · [Deductively valid and invalid](valid) · [Sound and unsound](sound) · [Hidden premise](hidden-premise)

## Sources
- Bland, *Reason* (Revised Edition), ch. 2, pp. 25, 28–29; ch. 3, p. 38. CC BY-NC 4.0.
- Magnus, Button, Trueman and Zach, *forall x: Calgary* (Fall 2025), ch. 5, §5.3, p. 38; ch. 19, §19.1, pp. 162–163. CC BY 4.0.
- Klement, K. C., "Propositional Logic", *Internet Encyclopedia of Philosophy*, §5.b. https://iep.utm.edu/propositional-logic-sentential-logic/
- Wilson, D. C., *A Guide to Good Reasoning: Cultivating Intellectual Virtues*, ch. 12, §§12.1, 12.1.2. University of Minnesota Libraries. CC BY-NC 4.0. https://open.lib.umn.edu/goodreasoning/chapter/chapter-12-either-or-arguments-and-more/
- Curtis, G. N., "Affirming a Disjunct", *The Fallacy Files*. https://fallacyfiles.org/afonedis.html
- Conan Doyle, A., *The Sign of Four* (London: Spencer Blackett, 1890), ch. 6 (also published as *The Sign of the Four*). Public domain. Text: https://en.wikisource.org/wiki/The_Sign_of_Four/Chapter_6
- "Arthur Conan Doyle", *Britannica* (dates). https://www.britannica.com/biography/Arthur-Conan-Doyle
