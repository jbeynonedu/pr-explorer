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

## Where the next chat picks up (26 Nov 2026)
1. **Phase 1, Sections 1–5: complete.** All entries approved by John. Not yet live: publish with `--public` at launch.
2. **Section 5: Induction — complete** (26 Nov 2026): induction, strong-weak, generalisation, analogy, problem-of-induction (uniformity of nature merged into it). The problem of induction is split into tabs (style guide §8).
3. **Site features:** full-screen view for argument maps (zoom, fit, Esc); entry tabs via `<!-- tab: Label -->` / `<!-- tabs-end -->` (`scripts/tabs.py`, shared by both builds); a Back button in the app.
4. **Workflow:** shared checker prompt in `briefs/_checker-prompt.md`; run one checker per entry in parallel, then one re-checker. Without a browser, WebFetch gives only short exact snippets: ask John to paste full pages (select all) for key secondary sources; commit only the extracts needed (the repo is public), keep full copies out of the repo.
5. **Open items:** (a) ~~IEP (Shanahan) lines~~ verified word for word against the page John pasted (26 Nov 2026), in all source packs. (b) ~~map colour~~ decided: argument maps follow the entry's branch (Reason cobalt, Philosophy coral), done in both templates.
6. **Section 6: Claims and reason in the real world** — Briefed (26 Nov 2026). Scope approved by John; all decisions in `briefs/_section-06-claims-real-world.md`. Next chat: Sourced (ask John to paste SEP "Truth", Nickerson's opening, the ACCC advertising page).
