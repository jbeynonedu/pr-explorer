# Source pack: valid

## bland-reason-validity
Greg Bland, *Reason: A Guide to Argument and Critical Reasoning*, Revised Edition, Oct 2026. CC BY-NC 4.0. Project file `Reason Revised Edition.pdf`; text copied from the Project file by script (whitespace normalised). Page numbers are the book's own ("Reason Page N" markers).

> Valid argument – a deductive argument is valid if and only if the truth of the premises guarantees the truth of the conclusion. In other words, if the premises are true, then the conclusion must also be true. (p. 18)

> It’s important to note that the validity of a deductive argument has nothing to do with the factual content that is presented in the argument. Validity is only concerned with the structure of the argument. (p. 18)

> The premises in this argument are clearly ridiculous – scientific observations have demonstrated that premise 2 is false, and there is certainly no causal link between the composition of celestial bodies and the existence of aliens (premise 1), at least asfar as we know. However, this deductive argument is still valid – if the premises were true, then the conclusion is inescapable. (p. 18)

(Argument, p. 18: "1. If the moon is made of cheese, then aliens exist. 2. The moon is made of cheese. C. Therefore, aliens exist.")

> As we have already discussed, the first and most important criterion for evaluating a deductive argument is whether the argument is valid or invalid. All deductive arguments fall into one of these two categories – it is impossible for a deductive argument to be “partially valid”, or for one argument to be “more valid” than another. For these arguments, validity is a black and white construct. You will recall that the criterion for deductive validity is that the truth of the premises guarantees the truth of the conclusion. In other words, a valid deductive argument cannot have true premises and false conclusion. (p. 36)

> If you see an argument that fits one of these well-known patterns, then you can confidently state whether the argument is valid or invalid with no further justification. In your philosophy essays, you should identify the argument type and state whether the argument is valid or invalid. (p. 36)

> To test for validity, construct a truth table for each of the premises and the conclusion in an argument. Examine the truth table closely: • If you cannot find any rows of the table that have all true premises and a false conclusion, then the argument is VALID. • If you can find at least one row containing all true premises and a false conclusion, then the argument is INVALID. The combination of propositional truth values in this row can be given as a counterexample – that is, an example of the scenario that demonstrates the invalidity of the argument. (p. 50)

> Validity and soundness are all-or-nothing properties. An argument cannot be partially valid or sound, nor can one argument be more valid or more sound than another. An argument is either valid or it's not. If the argument is valid, then test for soundness — at this point, the argument is either sound or it's not. There are no grey areas. (p. 19)


## forallx-ch2-validity
P. D. Magnus, Tim Button, Robert Trueman, Richard Zach, *forall x: Calgary*, Fall 2025 edition. CC BY 4.0. Text copied by script from the LaTeX source, github.com/rzach/forallx-yyc, commit bb86fe9 (22 Oct 2026); LaTeX markup removed; **notation converted** to syllabus symbols (`⊃`, `&`). Wording and page numbers checked by script against the Fall 2025 PDF in the Project (`forallxyyc.pdf`), 25 Nov 2026; chapter numbers confirmed from its running heads.

> How did we determine that the second argument is invalid? We pointed to a case in which the premises are true and in which the conclusion is not. This was the scenario where neither the driver nor the maid did it, but some third person did. Let’s call such a case a counterexample to the argument. If there is a counterexample to an argument, the conclusion cannot be a consequence of the premises. For the conclusion to be a consequence of the premises, the truth of the premises must guarantee the truth of the conclusion. If there is a counterexample, the truth of the premises does not guarantee the truth of the conclusion. (ch. 2 §2.2 'Cases and types of validity', pp. 8–9)

> An argument is valid if and only if the conclusion is a consequence of the premises. An argument is invalid if and only if it is not valid, i.e., it has a counterexample. (ch. 2 §2.2, definition box, p. 10)

> Arguments in this sense are used all the time in everyday and scientific discourse. When they are, arguments are given to support or even prove their conclusions. Now, if an argument is valid, it will support its conclusion, but only if its premises are all true. Validity rules out the possibility that the premises are true and the conclusion is not true at the same time. It does not, by itself, rule out the possibility that the conclusion is not true, period. In other words, it is perfectly possibly for a valid argument to have a conclusion that isn’t true! (ch. 2 §2.4 'Sound arguments', p. 14)

Example (§2.4, p. 14): "Oranges are either fruit or musical instruments. Oranges are not fruit. ∴ Oranges are musical instruments." Valid, absurd conclusion.
> Conversely, having true premises and a true conclusion is not enough to make an argument valid. Consider this example: (ch. 2 §2.4, p. 15)

Example (§2.4, p. 15): "London is in England. Beijing is in China. ∴ Paris is in France."
> The premises and conclusion of this argument are, as a matter of fact, all true, but the argument is invalid. If Paris were to declare independence from the rest of France, then the conclusion would no longer be true, even though both of the premises would remain true. Thus, there is a case where the premises of this argument are true without the conclusion being true. So the argument is invalid. (ch. 2 §2.4, p. 15)

For brief Q1 ("invalid is not necessarily bad", approved): "Many good arguments are invalid." (ch. 2 §2.5, p. 16). Use with the terminology flag: the entry's line should say that an argument that is really inductive is judged as strong or weak, not that inductive arguments are invalid.

## Four combinations (for the table)
Derived from the definitions above: a valid argument can have true premises/true conclusion, false premises/false conclusion (cheese, oranges), false premises/true conclusion; never true premises/false conclusion. An invalid argument can have all true premises and a true conclusion (London/Beijing/Paris). False-premises/true-conclusion valid example to be constructed in drafting and checked by code.

## forallx-ch2-validity-by-meaning
forall x: Calgary (details as above), ch. 2. Checked by script against the Fall 2025 PDF.

Example (§2.2, p. 11): "Priya is an ophthalmologist. ∴ Priya is an eye doctor."
> If we’re allowing only conceivable scenarios, this is also a valid argument. If you imagine Priya being an ophthalmologist, you thereby imagine Priya being an eye doctor. That’s just what “ophthalmologist” and “eye doctor” mean. A scenario where Priya is an ophthalmologist but not an eye doctor is ruled out by the conceptual connection between these words. (ch. 2 §2.2, p. 11)

Examples (§2.3 'Formal validity', p. 12): "Priya is either an ophthalmologist or a dentist. Priya isn’t a dentist. ∴ Priya is an eye doctor." and "... ∴ Priya is an ophthalmologist."
> [...] are valid arguments. But while the validity of the first depends on the content (i.e., the meaning of “ophthalmologist” and “eye doctor”), the second does not. The second argument is formally valid. (ch. 2 §2.3, p. 12)

Supports the qualifier (checker, 25 Nov 2026): some arguments are valid because of what their words mean; the arguments studied at this level are valid or invalid because of their form.
