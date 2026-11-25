# PR Explorer

The Philosophy & Reason Explorer: a free, public reference for every key term, method and theory in the QCAA Philosophy & Reason syllabus (2025 v1.3), for Year 11 and 12 students in Queensland.

## Layout
- `tracker.csv` — every entry and its stage: not-started → briefed → sourced → drafted → checked → approved → live. Only John approves.
- `briefs/<id>.md` — syllabus dot points (verbatim), scope, planned sources, questions. John approves scope before sourcing.
- `sources/<section>/` — fetched extracts with author, work, edition or translator, URL and locator. Quotations come only from here.
- `content/<section>/<id>.md` — entries, with front matter as in `STYLE_GUIDE.md` §10.
- `STYLE_GUIDE.md` — binding house style.

## Licences
Syllabus extracts © State of Queensland (QCAA) 2026, CC BY 4.0. Material adapted from Bland, *Reason*, is CC BY-NC 4.0; forall x: Calgary is CC BY 4.0. The Explorer is non-commercial.

## Site
`python3 scripts/build_site.py OUT.html` builds the whole Explorer as one self-contained page from `tracker.csv` and `content/` (template: `scripts/site_template.html`). Bubbles: Reason (sections 1–6) and Philosophy (sections 7–14) → sections → entries, in tracker order; Philosophy sections group `term` entries under "Key terms". Default is the review preview (checked, approved and live entries, with status tags). `--public` includes approved and live entries only: use it for GitHub Pages. Review preview: https://claude.ai/artifact/69doPgZ34TYgy5yASkWhYY (private to John). Rebuild and republish it whenever an entry reaches checked or approved.

## Preview (single entries)
`python3 scripts/build_preview.py .work/preview.html <id> ...` builds a single review page (interactive truth tables, Mermaid argument maps) from `content/`. Phase 0 exemplar preview: https://claude.ai/artifact/WuKi8KEsjgzTUge826Uys2 (private to John).

## Where the next chat picks up (25 Nov 2026)
1. **Site shell: built.** Preview republished at the bubble prototype's link. John to look it over (layout, section blurbs in `build_site.py`, footer wording). GitHub Pages at launch: build with `--public` to `docs/index.html` and enable Pages from `/docs`.
2. **Phase 1, Section 1: Building blocks — complete.** All nine entries approved by John (25 Nov 2026). Not yet live: publish with `--public` at launch.
3. **Next: Phase 1, Section 2: Deduction.** Start at the Briefed stage (seven entries; see `tracker.csv`).
