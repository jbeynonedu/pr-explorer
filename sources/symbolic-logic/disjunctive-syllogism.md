# Source pack: disjunctive syllogism

## bland-reason-ch2-ds
Bland, *Reason* (Revised Edition), ch. 2, pp. 28–29. CC BY-NC 4.0. Project file.
> In logic, a disjunction is a compound proposition that links two or more simpler propositions together with the word "or". (p. 28)

> An inclusive disjunction is true as long as at least one of the component propositions (also known as disjuncts) is true. (p. 28)

> A disjunctive syllogism works by introducing a disjunction and then eliminating components until there is only one option remaining. (p. 28)

Example (p. 28): "I will go shopping or go to the movies. I won't go shopping; therefore, I will go to the movies." 1. S or M. 2. Not S. C. Therefore, M. "This argument form is deductively valid, as the premises guarantee the conclusion. It also works when you have more than one disjunct."
Cluedo (pp. 28–29): 1. C or R or W or D. 2. Not C. 3. Not R. 4. Not D. C. Therefore, W.
> The disjunctive syllogism is a formal name for what is commonly known as the process of elimination. (p. 29)

Form box (p. 29): DISJUNCTIVE SYLLOGISM 1. P or Q. 2. Not P. C. Therefore, Q.
Bland p. 25 cites the Holmes line (as "The Sign of the Four", Penguin Classics, 2014).

## forallx-19-1
forall x: Calgary (Fall 2025), ch. 19.1, pp. 162–163. CC BY 4.0. Example: "Elizabeth is either in Massachusetts or in DC. She is not in DC. ∴ She is in Massachusetts." "This is called disjunctive syllogism." Two versions: A ∨ B, ¬A ∴ B and A ∨ B, ¬B ∴ A; "the disjunction and the negation of one disjunct may occur in either order and need not be adjacent."
§5.3 p. 38: "The TFL symbol '∨' always symbolizes an inclusive or." (soup/salad menu as exclusive-or example).

## iep-prop-logic-ds
Klement, "Propositional Logic", IEP §5.b: DS in both versions (α ∨ β, ¬α ∴ β; α ∨ β, ¬β ∴ α). https://iep.utm.edu/propositional-logic-sentential-logic/ (Chrome, 26 Nov 2026).

## wilson-good-reasoning-12
Wilson, D. C., *A Guide to Good Reasoning: Cultivating Intellectual Virtues*, ch. 12 "Either–Or Arguments and More", §12.1.2 "The Exclusivity Premise". University of Minnesota Libraries open textbook, CC BY-NC 4.0. https://open.lib.umn.edu/goodreasoning/chapter/chapter-12-either-or-arguments-and-more/ (Chrome, 26 Nov 2026).
Form "P or Q. P ∴ Not Q": "This form is in fact invalid; the name of the invalid form is the fallacy of affirming an alternative." Exclusive alternatives: "paraphrase exclusive alternatives by including and only one as part of the standard constant" (Guideline); "Affirming an exclusive alternative" listed as valid. Also: "modus tollendo ponens (the formal Latin term, still in use, for the process of elimination)".

## fallacy-files-affirming-a-disjunct
Curtis, G. N., "Affirming a Disjunct", *The Fallacy Files*. https://fallacyfiles.org/afonedis.html (search result text, 26 Nov 2026). Aliases listed: Affirming One Disjunct; The Fallacy of the Alternative Syllogism; Asserting an Alternative; Improper Disjunctive Syllogism.
> Affirming a disjunct is a form of argument in which one disjunct of a disjunctive premiss is affirmed as a premiss, while the other disjunct is denied as a conclusion.

Exception noted: not every argument of the form is invalid; "check to see whether the second premiss implies the conclusion." Flag: search-result text only; checker to confirm against the page if possible. Name choice for entry: "affirming a disjunct" (John approved), with "affirming an alternative" as an alias.

## conan-doyle-1890
Conan Doyle, A., *The Sign of Four* (London: Spencer Blackett, 1890), ch. VI "Sherlock Holmes Gives a Demonstration", p. 89 ff. (chapter start per contents). Public domain (Conan Doyle d. 1930). Wikisource transcription of the 1890 Blackett edition: https://en.wikisource.org/wiki/The_Sign_of_Four/Chapter_6 (Chrome, 26 Nov 2026). Gutenberg unavailable (maintenance) at time of fetch. Serial title (*Lippincott's*, 1890): "The Sign of the Four".
> 'You will not apply my precept,' he said, shaking his head. 'How often have I said to you that when you have eliminated the impossible, whatever remains, however improbable, must be the truth? We know that he did not come through the door, the window, or the chimney. We also know that he could not have been concealed in the room, as there is no concealment possible. Whence, then, did he come?'

> 'He came through the hole in the roof!' I cried.

Context: a locked room; options door, window, chimney, concealment, roof. The passage itself is a disjunctive syllogism with five disjuncts. Its strength depends on the list being complete (first premise true).

## Logic checks (code, 26 Nov 2026)
- `P ∨ Q, ~P ∴ Q` valid; `P ∨ Q, ~Q ∴ P` valid; `~P ∨ Q, P ∴ Q` valid.
- Affirming a disjunct `P ∨ Q, P ∴ ~Q` invalid; counterexample P 1, Q 1.
- With exclusivity premise `P ∨ Q, ~(P & Q), P ∴ ~Q`: valid.
