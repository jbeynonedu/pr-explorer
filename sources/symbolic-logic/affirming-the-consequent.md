# Source pack: affirming the consequent

## bland-reason-ch2-ac
Bland, *Reason* (Revised Edition), ch. 2, pp. 31–32. CC BY-NC 4.0. Project file.
> Errors in deductive reasoning that lead to invalid arguments are known as formal fallacies, and they occur not because of a mistake in the content of an argument, but rather because of a mistake in the argument's structure. (p. 31)

Example (p. 31): "If Mary studies hard, then she will pass her Philosophy test. Mary passed her Philosophy test, therefore she must have studied hard." S, P. 1. If S then P. 2. P. C. Therefore, S.
> Instead of affirming the antecedent in the second premise, we are instead affirming the consequent (hence the name of this fallacy). (p. 32)

Royal family example (p. 32): 1. If R then W. 2. W. C. Therefore, R. "It's quite possible for the premises of this argument to be true and the conclusion to be false, hence the argument is invalid."
Form box (p. 32): AFFIRMING THE CONSEQUENT (FORMAL FALLACY) 1. If P then Q. 2. Q. C. Therefore, P.
Variations (Exercise 2.2, pp. 33–34): (b) "1. R if S. 2. R. C. Therefore, S."; (e) "1. M. 2. If N, then M. C. Therefore, N."; (g) "1. Y only if X. 2. X. C. Therefore, Y."

## bland-reason-ch3-ac-table
Bland, ch. 3, pp. 52–53: 1. R ⊃ W 2. W C. R. "This row gives us a counterexample to the argument: 'R = FALSE and W = TRUE'." "A counterexample is simply a case where the argument breaks down". (Bland names real billionaires as counterexamples; not used.)

## forallx-5-5-iff
forall x: Calgary (Fall 2025), §5.5, p. 41. CC BY 4.0.
> Ordinary speakers of English often use 'if . . . , then. . . ' when they really mean to use something more like '. . . if and only if . . . '. Perhaps your parents told you, when you were a child: 'if you don't eat your greens, you won't get any dessert'.

"So, be aware of this when interpreting people; but in your own writing, make sure you use the biconditional iff you mean to."

## sep-confirmation
Crupi, V., "Confirmation", *Stanford Encyclopedia of Philosophy*, first published 30 May 2013; substantive revision 4 Aug 2025. https://plato.stanford.edu/entries/confirmation/ (Chrome, 26 Nov 2026).
Introduction:
> As emphasized in a joke attributed to American philosopher Morris Raphael Cohen (1880–1947), logic textbooks had to be divided in two parts: in the first part, on deductive logic, unwarranted forms of inference (deductive fallacies) are exposed; in the second part, on inductive logic, they are endorsed (see Meehl 1990, 110).

§2 "Hypothetico-deductivism": HD confirmation is "roughly described as 'deduction-in-reverse': evidence is said to confirm a hypothesis in case the latter, while not entailed by the former, is able to entail it, with the help of suitable auxiliary hypotheses and assumptions."
Use: if hypothesis H (with auxiliaries) entails prediction E, and E is observed, concluding H would be affirming the consequent; HD treats E as confirming (supporting) H, not proving it. Phrase without "prove" for inductive conclusions (style guide). One line; link hypothetico-deductive method entry.

## Logic checks (code, 26 Nov 2026)
`P ⊃ Q, Q ∴ P` invalid; counterexample P 0, Q 1. With biconditional premise `(P ⊃ Q) & (Q ⊃ P), Q ∴ P`: valid (checked).
