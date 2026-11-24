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

## Preview
`python3 scripts/build_preview.py .work/preview.html <id> ...` builds a single review page (interactive truth tables, Mermaid argument maps) from `content/`. Phase 0 exemplar preview: https://claude.ai/artifact/WuKi8KEsjgzTUge826Uys2 (private to John).
