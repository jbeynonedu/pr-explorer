"""Tabs for long entries (shared by build_preview.py and build_site.py).

In an entry's markdown, put `<!-- tab: Label -->` on its own line where each tab starts,
and `<!-- tabs-end -->` where the tabbed part ends (usually before "Related concepts").
For two layers (one outer tab per version of an argument), put `<!-- version: Label -->` where each
version starts and `<!-- versions-end -->` after the last; inside each version use `<!-- tab: ... -->` as usual.
Everything before the first tab marker (the lead) and after the end marker stays outside the tabs.

Usage in a builder, before HTML comments are stripped:
    body, labels = tabs.mark(body)
and after markdown has been rendered to HTML `h`:
    h = tabs.build(h, labels, entry_id)
"""
import html, re

class _Labels(list):
    """Inner tab labels; .outer holds version (outer tab) labels, if any."""
    outer = ()

def mark(body):
    labels, outer = _Labels(), []
    def rep(m):
        labels.append(m.group(1).strip())
        return f'\n\nTABMARK{len(labels)-1}\n\n'
    def rep_v(m):
        outer.append(m.group(1).strip())
        return f'\n\nVERMARK{len(outer)-1}\n\n'
    body = re.sub(r'<!--\s*version:\s*(.*?)\s*-->', rep_v, body)
    body = re.sub(r'<!--\s*versions-end\s*-->', '\n\nVERSEND\n\n', body)
    body = re.sub(r'<!--\s*tab:\s*(.*?)\s*-->', rep, body)
    body = re.sub(r'<!--\s*tabs-end\s*-->', '\n\nTABSEND\n\n', body)
    labels.outer = outer
    return body, labels

def _group(middle, mark, labels, pre, aria, cls):
    parts = re.split(rf'<p>{mark}(\d+)</p>', middle)
    lead, parts = parts[0], parts[1:]
    tabs, panels = [], []
    for n, k in enumerate(range(0, len(parts), 2)):
        i, content = int(parts[k]), parts[k + 1]
        tid, pid = f'{pre}-tab-{i}', f'{pre}-panel-{i}'
        sel = 'true' if n == 0 else 'false'
        tabs.append(f'<button type="button" role="tab" id="{tid}" aria-controls="{pid}" aria-selected="{sel}" tabindex="{0 if n == 0 else -1}">{html.escape(labels[i])}</button>')
        panels.append(f'<div role="tabpanel" id="{pid}" aria-labelledby="{tid}" tabindex="0"{"" if n == 0 else " hidden"}>{content}</div>')
    return (lead + f'<div class="{cls}"><div role="tablist" aria-label="{aria}">' + ''.join(tabs)
            + '</div>' + ''.join(panels) + '</div>')

def build(h, labels, eid):
    outer = getattr(labels, 'outer', ())
    if outer:
        # Two layers: each version panel holds its own inner tabs (no tabs-end needed inside).
        first = h.index('<p>VERMARK0</p>')
        end = h.find('<p>VERSEND</p>')
        if end < 0:
            end = len(h)
        before, middle, after = h[:first], h[first:end], h[end:].replace('<p>VERSEND</p>', '', 1)
        segs = re.split(r'(<p>VERMARK\d+</p>)', middle)[1:]
        out = ''
        for k in range(0, len(segs), 2):
            v = re.search(r'\d+', segs[k]).group()
            seg = segs[k + 1].replace('<p>TABSEND</p>', '')
            if '<p>TABMARK' in seg:
                j = seg.index('<p>TABMARK')
                seg = seg[:j] + _group(seg[j:], 'TABMARK', labels, f'{eid}-v{v}', 'Parts of this version', 'tabs inner')
            out += segs[k] + seg
        return before + _group(out, 'VERMARK', outer, eid + '-ver', 'Versions of this argument', 'tabs outer') + after
    if not labels:
        return h.replace('<p>TABSEND</p>', '')
    first = h.index('<p>TABMARK0</p>')
    end = h.find('<p>TABSEND</p>')
    if end < 0:
        end = len(h)
    before, middle, after = h[:first], h[first:end], h[end:].replace('<p>TABSEND</p>', '', 1)
    return before + _group(middle, 'TABMARK', labels, eid, 'Parts of this entry', 'tabs') + after

CSS = """.tabs{margin:20px 0}
.tabs [role=tablist]{display:flex;flex-wrap:wrap;gap:6px;border-bottom:2px solid rgba(127,127,127,.3);margin-bottom:8px;position:sticky;top:0;background:var(--bg);z-index:2;padding-top:6px}
.tabs [role=tab]{font:inherit;font-weight:600;padding:8px 14px;border:0;border-bottom:3px solid transparent;margin-bottom:-2px;background:none;color:var(--mute);cursor:pointer;border-radius:8px 8px 0 0}
.tabs [role=tab][aria-selected=true]{color:var(--ink);border-bottom-color:currentColor}
.tabs [role=tab]:hover{color:var(--ink)}
.tabs.inner{margin:12px 0}
.tabs.inner [role=tablist]{position:static;border-bottom-width:1px}
.tabs.inner [role=tab]{font-weight:500;padding:6px 12px}
.tabs [role=tabpanel]:focus-visible{outline:2px solid currentColor;outline-offset:4px}
"""

JS = """// ---------- entry tabs ----------
function prShowTab(t){
 const list=t.closest('[role=tablist]'),box=list.parentElement;
 list.querySelectorAll('[role=tab]').forEach(b=>{const on=b===t;b.setAttribute('aria-selected',on);b.tabIndex=on?0:-1;
  const p=box.querySelector('#'+CSS.escape(b.getAttribute('aria-controls')));if(p)p.hidden=!on});
 const p=box.querySelector('#'+CSS.escape(t.getAttribute('aria-controls')));
 if(p&&window.prRunMermaid){const m=p.querySelectorAll('pre.mermaid:not([data-processed])');if(m.length)window.prRunMermaid(m)}
 if(list.getBoundingClientRect().top<0)list.scrollIntoView({block:'start'});
}
document.addEventListener('click',e=>{const t=e.target.closest('[role=tab]');if(t)prShowTab(t)});
document.addEventListener('keydown',e=>{const t=e.target.closest&&e.target.closest('[role=tab]');if(!t)return;
 const all=[...t.parentElement.querySelectorAll('[role=tab]')],i=all.indexOf(t);
 const j=e.key==='ArrowRight'?(i+1)%all.length:e.key==='ArrowLeft'?(i-1+all.length)%all.length:e.key==='Home'?0:e.key==='End'?all.length-1:-1;
 if(j<0)return;e.preventDefault();all[j].focus();prShowTab(all[j])});
"""
