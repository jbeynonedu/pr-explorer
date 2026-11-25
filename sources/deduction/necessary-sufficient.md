# Source pack: necessary-sufficient

## bland-reason-3-2
Greg Bland, *Reason: A Guide to Argument and Critical Reasoning*, Revised Edition, Oct 2026. CC BY-NC 4.0. Project file `Reason Revised Edition.pdf`; text copied from the Project file by script (whitespace normalised). Page numbers are the book's own ("Reason Page N" markers).

> In logic, words such as necessary and sufficient indicate a logical and conditional relationship, and have very precise meanings. (p. 42)

> So what do the terms necessary and sufficient actually mean? And how can we symbolise them? Let's start with the concept of necessity. If A is necessary for B, then A is one of the required conditions for B to hold. It may not be the only condition – there could be others – but without A, B simply cannot be the case. In terms of symbolised logical relationships, if A is necessary for B, that means: "If B is true, then A must also be true." In symbolic form, we express this as "B ⊃ A". This indicates that B guarantees A — or put another way, A is required for B. (p. 42)

> Now, we can say that having water is necessary for the plant to grow. Is water enough to guarantee that the plant will grow? No – if we put the plant in our basement without any sunlight, or if we don’t give the plant nutrients through the soil, then the plant won’t grow regardless of how much water we give it. But flip the scenario around – if you see a plant that is growing and thriving, then you can guarantee that the plant must have access to water. Access to water is necessary for plant growth. In other words, if a plant is growing, then it has access to water. (p. 43)

> Let’s now consider sufficiency. If event A is sufficient for event B, then it means that A guarantees B – if we know that A is true, then B must also be true. Consider a first-aid scenario where you respond to an emergency and find a person lying on the floor. You assess the situation and notice that although the patient appears to be unconscious, they are clearly breathing. What does this mean? Well, the fact that the person is breathing is a good sign – a very good sign indeed! It guarantees that the person is alive… if they were dead, then surely they couldn’t be breathing! We can say that “breathing is sufficient to know that a person is alive”. In other words, if a person is breathing, then they are alive. (p. 43)

> Necessity and sufficiency aren’t separate relationships – they’re the same logical conditional read in opposite directions. To say “A is necessary for B” is just to say “B is sufficient for A”. Both statements correspond with the same symbolic expression: B ⊃ A. There is one last relationship to consider, and that is the relationship of “necessary and sufficient”. Occasionally, you will see a relationship between two events that is “necessary and sufficient”. This means that the two events are equivalent in every way – each condition guarantees the other. In this case, we can use a tribar (≡) to symbolise the relationship. For example, you could say that “A number is divisible by 2” is necessary and sufficient for “A number is even.” These two conditions go together at all times – you can’t have one without the other. (p. 43)

> Sometimes the relationship is causal – rooted in a physical or biological mechanism (water enables plant growth, or dropping a ball causes it to fall). Sometimes it’s a matter of definition (a triangle, by definition, is a 3-sided polygon). Sometimes it’s a rule or convention (only Year 12 students can attend the Formal). Sometimes it’s evidential (if a person is breathing, we can be confident that they are alive). (p. 42)

Boxes (pp. 42–43): NECESSITY "If A is necessary for B, then we can say: B ⊃ A"; SUFFICIENCY "If A is sufficient for B, then we can say: A ⊃ B"; NECESSITY AND SUFFICIENCY "If A is necessary and sufficient for B, then A ≡ B".

**Flags:**
- Not used (John, 25 Nov 2026): you might say that water is necessary for plants to grow, or that holding a current Australian passport is sufficient for becoming an Australian citizen. (p. 42) A passport is issued to someone who is already a citizen.
- "equivalent in every way" (p. 43) overstates: the two conditions always have the same truth value; they need not mean the same thing. Paraphrase as "each guarantees the other".
- `≡` not a syllabus operator. John's decision: `(A ⊃ B) & (B ⊃ A)`, with `≡` in a note. forall x supports this form (below).

## forallx-ch5-conditional-biconditional
P. D. Magnus, Tim Button, Robert Trueman, Richard Zach, *forall x: Calgary*, Fall 2025 edition. CC BY 4.0. Text copied by script from the LaTeX source, github.com/rzach/forallx-yyc, commit bb86fe9 (22 Oct 2026); LaTeX markup removed; **notation converted** to syllabus symbols (`⊃`, `&`). Wording and page numbers checked by script against the Fall 2025 PDF in the Project (`forallxyyc.pdf`), 25 Nov 2026; chapter numbers confirmed from its running heads.

Example sentences (ch. 5 §5.4 'Conditional', pp. 39–40): "25. If Jean is in Paris, then Jean is in France." / "26. Jean is in France only if Jean is in Paris."
> In fact, sentence 26 can be paraphrased as ‘If Jean is in France, then Jean is in Paris’. So we can symbolize it by ‘(F ⊃ P)’. A sentence can be symbolized as (A ⊃ B) if it can be paraphrased in English as ‘If A, then B’ or ‘A only if B’. (ch. 5 §5.4, p. 40)

Sentences (§5.4, pp. 40–41): "27. For Jean to be in Paris, it is necessary that Jean be in France." "28. It is a necessary condition on Jean’s being in Paris that she be in France." "29. For Jean to be in France, it is sufficient that Jean be in Paris." "30. It is a sufficient condition on Jean’s being in France that she be in Paris."
> If we think about it, all four of these sentences mean the same as ‘If Jean is in Paris, then Jean is in France’. So they can all be symbolized by ‘(P ⊃ F)’. It is important to bear in mind that the connective ‘⊃’ tells us only that, if the antecedent is true, then the consequent is true. It says nothing about a causal connection between two events (for example). In fact, we lose a huge amount when we use ‘⊃’ to symbolize English conditionals. [...] (ch. 5 §5.4, p. 41)

(The last sentence supports a caveat on Bland's "causal" kind: the conditional itself does not express causation.)

Sentences (ch. 5 §5.5 'Biconditional', p. 41): "31. Laika is a dog only if she is a mammal. 32. Laika is a dog if she is a mammal. 33. Laika is a dog if and only if she is a mammal."
> Sentence 33 says something stronger than either sentence 31 or sentence 32. It can be paraphrased as ‘Laika is a dog if Laika is a mammal, and Laika is a dog only if Laika is a mammal’. This is just the conjunction of sentences 31 and 32. So we can symbolize it as ‘(D ⊃ M) & (M ⊃ D)’. We call this a biconditional, because it amounts to stating both directions of the conditional. (ch. 5 §5.5, p. 41)


## Searle link
Existing entry `content/philosophy-of-mind/searle-chinese-room.md` (checked, not yet approved): "Searle argues that running a program is not a sufficient condition for a mind." Link only.

## Dropped
SEP "Necessary and Sufficient Conditions": not needed; Bland p. 42 covers the kinds of connection and forall x covers the causal caveat.

## searle-dates
John Searle (1932–2025): Cole, D., "The Chinese Room Argument", *Stanford Encyclopedia of Philosophy* (rev. 23 Oct 2024), live page fetched 25 Nov 2026; recorded in `sources/philosophy-of-mind/searle-chinese-room.md`. Syllabus p. 16: "John Searle’s Chinese room argument".
