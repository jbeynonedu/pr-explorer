"""Build a single-page review preview of entries from content/*.md.

Usage: python3 scripts/build_preview.py OUT.html id1 id2 ...
Renders each entry's markdown, an interactive truth table where an
`<!-- interactive: truth-table ... -->` marker appears, and Mermaid
argument maps. Links to entries not yet written are shown as plain text.
"""
import html, json, os, re, sys, glob, csv
import markdown, yaml
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tt_forms import TT_FORMS, WIDGET

ROOT = __file__.rsplit('/scripts/', 1)[0]
out, ids = sys.argv[1], sys.argv[2:]
tracker = {r['id']: r for r in csv.DictReader(open(f'{ROOT}/tracker.csv'))}
files = {}
for p in glob.glob(f'{ROOT}/content/*/*.md'):
    fm, body = open(p).read().split('---', 2)[1:]
    meta = yaml.safe_load(fm)
    files[meta['id']] = (meta, body)

BRANCH = {'building-blocks': 'r', 'symbolic-logic': 'r', 'deduction': 'r', 'informal-fallacies': 'r',
          'induction': 'r'}

def render(eid):
    meta, body = files[eid]
    body = re.sub(r'^# .*\n', '', body.strip(), count=1)
    mermaid = []
    def keep(m):
        mermaid.append(m.group(1)); return f'\n\nMERMAID{len(mermaid)-1}\n\n'
    body = re.sub(r'```mermaid\n(.*?)```', keep, body, flags=re.S)
    sfs = []
    def keep_sf(m):
        sfs.append(m.group(1)); return f'\n\nSFBLOCK{len(sfs)-1}\n\n'
    body = re.sub(r'```sf\n(.*?)```', keep_sf, body, flags=re.S)
    body = body.replace('<!-- interactive: coin-sim -->', '\n\nCOINSIM\n\n')
    tt = re.search(r'<!-- interactive: truth-table; premises: (.*?); conclusion: (.*?) -->', body)
    if tt:
        body = body.replace(tt.group(0), '\n\nTTMARK\n\n', 1)
    body = re.sub(r'<!--.*?-->\n?', '', body)
    h = markdown.markdown(body, extensions=['tables'])
    h = h.replace('<p>COINSIM</p>', '<div class="coinsim"></div>')
    for i, code in enumerate(mermaid):
        h = h.replace(f'<p>MERMAID{i}</p>', f'<div class="map"><pre class="mermaid">{html.escape(code)}</pre></div>')
    for i, block in enumerate(sfs):
        rows = []
        for line in block.strip().splitlines():
            m = re.match(r'(\d+\.|C\.|IC\d*\.|\(HP\d*\))\s+(.*)', line)
            lab, txt = (m.group(1), m.group(2)) if m else ('', line)
            txt = re.sub(r'`([^`]+)`', r'<code>\1</code>', html.escape(txt))
            cls = ' class="c"' if lab == 'C.' else ''
            rows.append(f'<div{cls}><span>{html.escape(lab)}</span><span>{txt}</span></div>')
        h = h.replace(f'<p>SFBLOCK{i}</p>', '<div class="sf" role="group" aria-label="Standard form">' + ''.join(rows) + '</div>')
    form = None
    if tt:
        want = (tt.group(1).strip(), tt.group(2).strip())
        form = next((k for k, v in TT_FORMS.items() if v == want), None)
        if not form:
            print(f'warning: {meta["id"]}: truth-table marker {want} matches no known form; static table kept')
            h = h.replace('<p>TTMARK</p>', '')
    if tt and form:  # replace the first static table after the marker with an interactive one
        h = re.sub(r'<p>TTMARK</p>(.*?)<table>.*?</table>', lambda m: m.group(1) + f'<div class="tt" data-form="{form}"></div>', h, count=1, flags=re.S)
    def link(m):
        target, text = m.group(1), m.group(2)
        if target in ids:
            return f'<a href="#{target}">{text}</a>'
        status = tracker.get(target, {}).get('status', 'planned')
        return f'<span class="xref" title="Entry not yet written ({status})">{text}</span>'
    h = re.sub(r'<a href="([a-z0-9-]+)">(.*?)</a>', link, h)
    h = h.replace('<table>', '<div class="scroll"><table>').replace('</table>', '</table></div>')
    br = BRANCH.get(meta['section'], 'p')
    tags = f'<span class="tag">{html.escape(meta["type"])}</span><span class="tag">Unit {", ".join(map(str, meta["units"]))}</span><span class="tag">{html.escape(meta["section"].replace("-", " "))}</span><span class="tag st">{html.escape(meta["status"])}</span>'
    return (f'<article class="entry" id="{eid}" style="--c:var(--{br});--soft:var(--{br}-soft)">'
            f'<div class="tags">{tags}</div><h2>{html.escape(meta["title"])}</h2>{h}</article>')

nav = ''.join(f'<a href="#{i}">{html.escape(files[i][0]["title"])}</a>' for i in ids)
arts = '\n'.join(render(i) for i in ids)
page = open(f'{ROOT}/scripts/preview_template.html').read().replace('{{NAV}}', nav).replace('{{ENTRIES}}', arts).replace('{{TT_WIDGET}}', WIDGET)
open(out, 'w').write(page)
print('wrote', out, len(page))
