# PR Explorer

The Philosophy & Reason Explorer: a free, public reference for every key term, method and theory in the QCAA Philosophy & Reason syllabus (2025 v1.3), for Year 11 and 12 students in Queensland.

## Layout
- `tracker.csv` — every entry and its stage: not-started → briefed → sourced → drafted → checked → approved → live. Only John approves.
- `briefs/<id>.md` — syllabus dot points (verbatim), scope, planned sources, questions. John approves scope before sourcing. `briefs/README.md` lists them in tracker order (rebuild with `python3 scripts/build_brief_index.py`).
- `sources/<section>/` — fetched extracts with author, work, edition or translator, URL and locator. Quotations come only from here.
- `content/<section>/<id>.md` — entries, with front matter as in `STYLE_GUIDE.md` §10.
- `STYLE_GUIDE.md` — binding house style.

## Licences
Syllabus extracts © State of Queensland (QCAA) 2026, CC BY 4.0. Material adapted from Bland, *Reason*, is CC BY-NC 4.0; forall x: Calgary is CC BY 4.0. The Explorer is non-commercial.

## Site
`python3 scripts/build_site.py OUT.html` builds the whole Explorer as one self-contained page from `tracker.csv` and `content/` (template: `scripts/site_template.html`). Bubbles: Reason (sections 1–6) and Philosophy (sections 7–14) → sections → entries, in tracker order; Philosophy sections group `term` entries under "Key terms". Default is the review preview (checked, approved and live entries, with status tags). `--public` includes approved and live entries only: use it for GitHub Pages. Review preview: https://claude.ai/artifact/69doPgZ34TYgy5yASkWhYY (private to John). Rebuild and republish it whenever an entry reaches checked or approved.

## Preview (single entries)
`python3 scripts/build_preview.py .work/preview.html <id> ...` builds a single review page (interactive truth tables, Mermaid argument maps) from `content/`. Phase 0 exemplar preview: https://claude.ai/artifact/WuKi8KEsjgzTUge826Uys2 (private to John).

## Where the next chat picks up (27 Nov 2026)
1. **Phase 1, Sections 1–6: complete.** All entries approved by John. Not yet live: publish with `--public` at launch.
2. **Section 6: Claims and reason in the real world — complete** (27 Nov 2026): true-false, plausible, credible, justification-persuasion, cognitive-bias, confirmation-bias, misuse-of-argument (tabs; one question per context tab). Check log: `briefs/_section-06-check-log.md`.
3. **Site features:** full-screen argument maps (button above the map; maps take the entry's branch colour); entry tabs (`<!-- tab: Label -->` / `<!-- tabs-end -->`); Back button; interactives: truth tables, coin simulator, number-rule task (`scripts/rule_task.js`, marker `<!-- interactive: rule-246 -->`).
4. **Workflow:** John's Chrome is available (Claude in Chrome): fetch pages, PDFs in viewers and scans directly rather than asking John to paste. Shared checker prompt in `briefs/_checker-prompt.md`; one checker per entry in parallel, then one re-checker. Commit only the extracts needed (the repo is public). Shell `git clone` of public GitHub repos (e.g. Standard Ebooks) works for script-copied primary texts.
5. **Style decisions this section:** plausible vs credible (§2); researchers cited for a study get full name and study year, no life dates (§4); "Questions to explore" for "Generate questions and theses" entries (§8).
6. **Section 7: Philosophy of religion — scope approved, Sourced in progress** (27 Nov 2026). Section note `briefs/_section-07-philosophy-of-religion.md` has John's unit material (Religion OneNote, Project) and his scope decisions: two-layer tabs (a renderer change in `scripts/tabs.py`, to preview at Drafted); modal ontological argument in English only by default; "Questions to explore" only where genuinely interesting; Pascal, Flew and Kierkegaard in a "Faith and reason" part of `religion` (to confirm at drafting).
7. **Sourced** (27 Nov 2026): all seven terms (`religion`, `god`, `omnipotence`, `omniscience`, `benevolence`, `good`, `evil`); packs in `sources/philosophy-of-religion/` (Aquinas; Plato; Augustine; Boethius; Descartes V; Pascal (Krailsheimer) and SEP Wager; Kierkegaard (Lowrie) and SEP; Flew; ABS 2021; SEP Concept of Religion, Concepts of God, Omnipotence, Omniscience, Theological Voluntarism, Concept of Evil, Problem of Evil). **Flags:** "leap of faith" is not in *Fear and Trembling* or the SEP Kierkegaard entry (don't quote it as his); *Fear and Trembling* is pseudonymous (Johannes de silentio); SEP "Problem of Evil" (Tooley) argues for one side, use it for structure only. **Still to source at drafting:** thinker dates (Plato, Augustine, Boethius, Anselm, Aquinas, Pascal) by WebSearch; SEP authors of three entries from their copyright lines. **Next: Drafted**, in order religion → god → omnipotence → omniscience → benevolence → good → evil; then source the four arguments (Anselm/Gaunilo, Kant, Leibniz, Paley ch. 1, Hume *Dialogues*, SEP Ontological/Cosmological/Teleological/Fine-Tuning, IEP logical and evidential problem of evil: John to print to the Project).
