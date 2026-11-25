# Source pack: modus ponens

## bland-reason-ch2-mp
Bland, *Reason* (Revised Edition), ch. 2, p. 26. CC BY-NC 4.0. Project file.
> Now, the modus ponens argument involves setting up a conditional statement and then affirming the truth of the antecedent of that statement. In Latin, modus ponens literally translates as "the method of affirming". It is short for modus ponendo ponens which translates as "the method of affirming by affirming". (p. 26)

> This is a valid argument because if the premises are true, then the conclusion must also be true. It affirms the truth of the conclusion by affirming the antecedent of the conditional. (p. 26)

Example (p. 26): "If it's Monday, then I will go to school. It's Monday. Therefore, I will go to school." M = "It is Monday." S = "I will go to school." 1. If M, then S. 2. M. C. Therefore, S.
Form box: MODUS PONENS 1. If P, then Q. 2. P. C. Therefore, Q.
Wordings (p. 26): If R, then W / If R, W / W if R / R only if W / R is sufficient for W / W is necessary for R. Footnote 6 on "only if" (Glennie School).
Truth-table method: Bland ch. 3 pp. 50–51 (rule: no row with all true premises and a false conclusion → valid). Exercise 3.4 Q1(a) tests this example.

## bland-reason-confusion
Bland, ch. 2, pp. 31–32: affirming the consequent "bears a strong resemblance to a valid argument form that we considered in the previous section – the form of modus ponens"; "Instead of affirming the antecedent in the second premise, we are instead affirming the consequent".

## forallx-17-4
forall x: Calgary (Fall 2025), ch. 17.4, p. 121. CC BY 4.0. Conditional elimination (→E): from A → B and A, infer B.
> This rule is also sometimes called modus ponens.

"the conditional A → B and the antecedent A can be separated from one another in the proof, and they can appear in any order."

## carroll-1895
Carroll, L. (1895), "What the Tortoise Said to Achilles", *Mind*, New Series, vol. IV, no. 14 (April 1895), pp. 278–280. Public domain (Carroll d. 1898). Text read in full: https://math.dartmouth.edu/~matc/Readers/HowManyAngels/Tortoise.html (transcription of *Mind* 1895; Chrome, 26 Nov 2026). Pagination from JSTOR record (stable 2254477) as cited in search results; page of each line not yet located.

Propositions (verbatim):
> (A) Things that are equal to the same are equal to each other.
> (B) The two sides of this Triangle are things that are equal to the same.
> (Z) The two sides of this Triangle are equal to each other.
> (C) If A and B are true, Z must be true.

The Tortoise accepts A and B but not the "Hypothetical" C; Achilles writes C down; the Tortoise then asks for (D) "If A and B and C are true, Z must be true." Achilles:
> "Then Logic would take you by the throat, and force you to do it!"

Tortoise: "Whatever Logic is good enough to tell me is worth writing down," then (E) "If A and B and C and D are true, Z must be true." Months later the notebook holds "a thousand and one" steps, "There are several millions more to come."

**Accuracy notes for drafting:**
- A, B ∴ Z is not itself modus ponens. With C added, the step "A and B; if A and B then Z; so Z" has the form of modus ponens (with a conjunction as antecedent): `(A & B) ⊃ Z, A & B ∴ Z`. Each new premise (D, E, ...) is a further conditional; the regress is that writing the rule down as a premise never removes the need to apply it.
- The standard reading (a rule of inference is not another premise) is interpretation, not Carroll's own statement. Present it as how the dialogue is usually read; source for that reading: Wikipedia "What the Tortoise Said to Achilles" (search snippet: "a regressive problem that arises from modus ponens deductions") — tertiary; prefer to phrase as the entry's own explanation and attribute only the dialogue to Carroll.

## Logic checks (code, 26 Nov 2026)
`P ⊃ Q, P ∴ Q` valid; variant `~P ⊃ Q, ~P ∴ Q` valid.
