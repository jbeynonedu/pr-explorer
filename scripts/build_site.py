"""Build the Explorer site (one self-contained index.html) from tracker.csv and content/.

Usage:
  python3 scripts/build_site.py OUT.html            # review preview: checked + approved + live entries
  python3 scripts/build_site.py OUT.html --public   # public site: approved + live entries only

Bubble tree: Reason (sections 1-6) and Philosophy (sections 7-14) -> sections -> entries,
in tracker order. In Philosophy sections, `term` entries are grouped under a "Key terms"
bubble. Entries without a published file show as dashed placeholder bubbles.
Entry bodies are rendered as in build_preview.py: `sf` blocks, an interactive truth table
where an `<!-- interactive: truth-table ... -->` marker appears, and Mermaid maps.
"""
import csv, glob, html, json, os, re, sys
import markdown, yaml
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tt_forms import TT_FORMS, WIDGET

ROOT = __file__.rsplit('/scripts/', 1)[0]
out = sys.argv[1]
public = '--public' in sys.argv
SHOW = {'approved', 'live'} if public else {'checked', 'approved', 'live'}

rows = list(csv.DictReader(open(f'{ROOT}/tracker.csv', encoding='utf-8')))
slug = lambda s: re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')

# Section blurbs shown under bubbles and cards (navigation text only, not entry content).
BLURB = {
    'Building blocks': 'What an argument is made of, and how to set it out.',
    'Deduction': 'Arguments that aim to guarantee their conclusion.',
    'Symbolic logic': 'Operators, valid forms and formal fallacies.',
    'Informal fallacies': 'Flaws in the content of reasoning, not its form.',
    'Induction': 'Arguments that aim to make their conclusion probable.',
    'Claims and reason in the real world': 'Judging claims, bias, and argument in the wild.',
    'Philosophy of religion': 'Arguments about the existence and nature of God.',
    'Philosophy of science': 'How science produces knowledge, and how sure it can be.',
    'Philosophy of mind': 'Consciousness, minds and machines.',
    'Moral philosophy': 'Key moral concepts and ethical theories.',
    'Consequentialism (school)': 'A school of thought: judging actions by their outcomes.',
    'Feminist philosophy (school)': 'A school of thought: philosophy and the position of women.',
    'Rights': 'Where rights come from and how far they reach.',
    'Political philosophy': 'How best to arrange our collective life.',
}
ROOTS = [
    ('reason', 'Reason', 'How arguments work and how to judge them.', 'r', range(1, 7)),
    ('philosophy', 'Philosophy', 'The big questions, and the arguments philosophers use to answer them.', 'p', range(7, 15)),
]

# ---------- entry files ----------
files = {}
for p in glob.glob(f'{ROOT}/content/*/*.md'):
    fm, body = open(p, encoding='utf-8').read().split('---', 2)[1:]
    meta = yaml.safe_load(fm)
    files[meta['id']] = (meta, body)
status = {r['id']: r['status'] for r in rows}
published = {i for i, (m, _) in files.items() if status.get(i, m['status']) in SHOW}


def render(eid):
    meta, body = files[eid]
    body = re.sub(r'^# .*\n', '', body.strip(), count=1).lstrip()
    lead = re.match(r'\*\*(.+?)\*\*', body)
    lead = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', lead.group(1)) if lead else ''
    lead = re.sub(r'[*_`]', '', lead)
    mermaid, sfs = [], []
    def keep(m):
        mermaid.append(m.group(1)); return f'\n\nMERMAID{len(mermaid)-1}\n\n'
    body = re.sub(r'```mermaid\n(.*?)```', keep, body, flags=re.S)
    def keep_sf(m):
        sfs.append(m.group(1)); return f'\n\nSFBLOCK{len(sfs)-1}\n\n'
    body = re.sub(r'```sf\n(.*?)```', keep_sf, body, flags=re.S)
    body = body.replace('<!-- interactive: coin-sim -->', '\n\nCOINSIM\n\n')
    tt = re.search(r'<!-- interactive: truth-table; premises: (.*?); conclusion: (.*?) -->', body)
    if tt:
        body = body.replace(tt.group(0), '\n\nTTMARK\n\n', 1)
    body = re.sub(r'<!--.*?-->\n?', '', body, flags=re.S)
    h = markdown.markdown(body, extensions=['tables'])
    h = re.sub(r'<(/?)h([2-5])', lambda m: f'<{m.group(1)}h{int(m.group(2))+1}', h)  # title is the only h2
    h = h.replace('<p>COINSIM</p>', '<div class="coinsim"></div>')
    for i, code in enumerate(mermaid):
        h = h.replace(f'<p>MERMAID{i}</p>', f'<div class="map"><button type="button" class="map-expand" aria-label="Open the argument map full screen">⤢ Full screen</button><pre class="mermaid">{html.escape(code)}</pre></div>')
    for i, block in enumerate(sfs):
        out_rows = []
        for line in block.strip().splitlines():
            m = re.match(r'(\d+\.|C\.|IC\d*\.|\(HP\d*\))\s+(.*)', line)
            lab, txt = (m.group(1), m.group(2)) if m else ('', line)
            txt = re.sub(r'`([^`]+)`', r'<code>\1</code>', html.escape(txt))
            cls = ' class="c"' if lab == 'C.' else ''
            out_rows.append(f'<div{cls}><span>{html.escape(lab)}</span><span>{txt}</span></div>')
        h = h.replace(f'<p>SFBLOCK{i}</p>', '<div class="sf" role="group" aria-label="Standard form">' + ''.join(out_rows) + '</div>')
    if tt:  # replace the first static truth table with an interactive one
        want = (tt.group(1).strip(), tt.group(2).strip())
        form = next((k for k, v in TT_FORMS.items() if v == want), None)
        if form:
            # replace the first table after the marker
            h = re.sub(r'<p>TTMARK</p>(.*?)<table>.*?</table>', lambda m: m.group(1) + f'<div class="tt" data-form="{form}"></div>', h, count=1, flags=re.S)
        h = h.replace('<p>TTMARK</p>', '')
        if not form:
            print(f'warning: {eid}: truth-table marker {want} matches no known form; static table kept')
    def link(m):
        target, text = m.group(1), m.group(2)
        if target in published:
            return f'<a href="#{target}" data-go="{target}">{text}</a>'
        st = status.get(target, 'planned')
        return f'<span class="xref" title="Entry not yet written ({st})">{text}</span>'
    h = re.sub(r'<a href="([a-z0-9-]+)">(.*?)</a>', link, h)
    h = h.replace('<table>', '<div class="scroll"><table>').replace('</table>', '</table></div>')
    return h, lead

# ---------- tree ----------
def leaf(r):
    n = {'id': r['id'], 't': r['title'], 'u': [int(x) for x in r['units'].split(';')], 'ty': r['type']}
    if r['id'] in published:
        n['html'], n['def'] = render(r['id'])
        n['st'] = status[r['id']]
    else:
        n['stub'] = 1
    return n

tree = {'id': 'home', 't': 'Home', 'c': []}
for rid, title, blurb, br, nos in ROOTS:
    root = {'id': rid, 't': title, 'b': blurb, 'br': br, 'c': []}
    for no in nos:
        sec_rows = [r for r in rows if int(r['section_no']) == no]
        if not sec_rows:
            continue
        name = sec_rows[0]['section']
        sid = 's-' + slug(name)
        units = sorted({int(u) for r in sec_rows for u in r['units'].split(';')})
        sec = {'id': sid, 't': name, 'b': BLURB.get(name, ''), 'u': units, 'c': []}
        terms = [r for r in sec_rows if r['type'] == 'term']
        if br == 'p' and terms and len(terms) < len(sec_rows):
            sec['c'].append({'id': sid + '-terms', 't': 'Key terms', 'b': f'Key terms for {name.lower()}.',
                             'c': [leaf(r) for r in terms]})
            sec['c'] += [leaf(r) for r in sec_rows if r['type'] != 'term']
        else:
            sec['c'] = [leaf(r) for r in sec_rows]
        root['c'].append(sec)
    tree['c'].append(root)

missing = set(files) - {r['id'] for r in rows}
if missing:
    print('warning: content files not in tracker:', sorted(missing))

data = json.dumps({'tree': tree, 'preview': not public}, ensure_ascii=False).replace('</', '<\\/')
page = open(f'{ROOT}/scripts/site_template.html', encoding='utf-8').read().replace('{{DATA}}', data).replace('{{TT_WIDGET}}', WIDGET)
open(out, 'w', encoding='utf-8').write(page)
print('wrote', out, len(page), 'bytes;', len(published), 'of', len(rows), 'entries published', '(public)' if public else '(preview)')
