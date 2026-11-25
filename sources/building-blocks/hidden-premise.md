# Source pack: hidden-premise

## bland-reason-ch1-hidden
Bland, *Reason* (Revised Edition), The Glennie School, Oct 2026. CC BY-NC 4.0. Project file `Reason Revised Edition.pdf`; text copied from the Project file by script (whitespace normalised).
> A hidden premise, otherwise known as a tacit premise, is an assumption in an argument that is not explicitly stated but is necessary for the argument to work. Often, hidden premises are unstated because they are considered obvious or contain widely shared and agreed knowledge, but occasionally these hidden premises are more controversial and are subject to challenge. When converting a prose argument to standard form, it is important to be able to identify hidden premises and then include these premises in the standard form construction, allowing the truth value of such premises to be discussed and evaluated. (p. 16)

Example (p. 16): "Those biscuits must be good because Jessica baked them." → `1. Jessica baked the biscuits.` `C. Therefore, the biscuits are good.` → with `2. Jessica is skilled at baking biscuits. (HP)`.
> Sometimes, you may encounter an argument where the premises are clearly laid out but the conclusion is not directly stated, rather it is inferred or implied. In this case, the argument can be said to contain a hidden conclusion (HC). Be careful with these – sometimes the implied conclusion is obvious, but other times it is vague. It’s always good practice to state a conclusion clearly and explicitly rather than have your listeners jump to the conclusion themselves. However, if you do encounter an argument with a hidden conclusion, do your best to identify what it is and include it in your standard form. (p. 16)

Example (p. 16): junk food → `C. Therefore, you should avoid eating junk food every day. (HC)`.
> Articulated by 18th Century Scottish philosopher David Hume, the is-ought problem concerns the fact that there is a logical gap when trying to argue for a normative conclusion based on descriptive premises or statements. For example, consider the following argument: 1) Cigarette smoking causes ill health. C) Therefore, the government should ban cigarette smoking. Can you see the problem here? Even if the first premise is factually correct, it is a descriptive proposition that tells you what something is. On the other hand, the conclusion is a normative proposition which talks about what the government ought to do. This problem can be solved by including an additional premise that bridges the gap between the descriptive premise and the normative conclusion: (p. 14)

Added premise (p. 14): "2) The government has a duty to protect public health."

## syllabus-p7
QCAA, *Philosophy & Reason 2025 v1.3*, January 2026. CC BY 4.0, © State of Queensland (QCAA) 2026 www.qcaa.qld.edu.au/copyright. Project file.

> When examining the reasoning of others, the deconstruction of arguments is a key tool of interpretation and analysis. This involves breaking down arguments into their constituent components of premise/s and conclusion/s, including assumed premises necessary for an argument to cohere. The structured setting out of this information in standard form is a feature of philosophical analysis. It provides a basis for the evaluation of both the inferential quality of an argument, and the truth of its premises. (p. 7)

> When creating responses in Philosophy & Reason, an analytical essay is connected prose that has the purpose of establishing a claim or assertion (central thesis) through careful reasoning. In this respect, essays present an argument. As part of this process, key concepts, arguments and assumptions are clarified, and counterarguments identified and responded to, applying the principle of charity. (p. 7)

## vancleave-1-9
Matthew Van Cleave, *Introduction to Logic and Critical Thinking*, 2nd edn, §1.9 "Arguments with Missing Premises". CC BY 4.0. https://human.libretexts.org/Bookshelves/Philosophy/Logic_and_Reasoning/Introduction_to_Logic_and_Critical_Thinking_2e_(van_Cleave)/01:_Reconstructing_and_Analyzing_Arguments/1.09:_Arguments_with_Missing_Premises (fetched 25 Nov 2026; short quotations only).

> The principle of charity states that when reconstructing an argument, you should try to make that argument [as strong as possible] 

(Bracketed completion from the fetch summary; verify the exact ending before quoting, or paraphrase.)

> supplying the most plausible premises needed in order to make the argument either valid [(for deductive arguments) or inductively strong (for inductive arguments)]

> there is never just one correct way of doing it

Supports: choose the most plausible premise; more than one reconstruction is possible.

## trivial-conditional (logic, verified by code)
Adding the premise "If P1 and P2, then C" to any argument with premises P1, P2 and conclusion C makes it valid: checked over all 8 truth-value assignments, 25 Nov 2026 (`{P1, P2, (P1 & P2) ⊃ C} ⊨ C`). No external source needed; re-verify at the Checked stage.

## bland-reason-ch1-junkfood
Bland p. 16, prose: "Eating junk food every day leads to health problems like obesity and diabetes. These foods are high in fat, sugar, and salt."
Bland's standard form (p. 16): "1. Eating junk food every day leads to health problems like obesity and diabetes." "2. Junk food is high in fat, sugar, and salt." "C. Therefore, you should avoid eating junk food every day. (HC)"
