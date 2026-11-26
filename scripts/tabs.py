"""Tabs for long entries (shared by build_preview.py and build_site.py).

In an entry's markdown, put `<!-- tab: Label -->` on its own line where each tab starts,
and `<!-- tabs-end -->` where the tabbed part ends (usually before "Related concepts").
Everything before the first tab marker (the lead) and after the end marker stays outside the tabs.

Usage in a builder, before HTML comments are stripped:
    body, labels = tabs.mark(body)
and after markdown has been rendered to HTML `h`:
    h = tabs.build(h, labels, entry_id)
"""
import html, re

def mark(body):
    labels = []
    def rep(m):
        labels.append(m.group(1).strip())
        return f'\n\nTABMARK{len(labels)-1}\n\n'
    body = re.sub(r'<!--\s*tab:\s*(.*?)\s*-->', rep, body)
    body = re.sub(r'<!--\s*tabs-end\s*-->', '\n\nTABSEND\n\n', body)
    return body, labels

def build(h, labels, eid):
    if not labels:
        return h.replace('<p>TABSEND</p>', '')
    first = h.index('<p>TABMARK0</p>')
    end = h.find('<p>TABSEND</p>')
    if end < 0:
        end = len(h)
    before, middle, after = h[:first], h[first:end], h[end:].replace('<p>TABSEND</p>', '', 1)
    parts = re.split(r'<p>TABMARK(\d+)</p>', middle)[1:]
    tabs, panels = [], []
    for k in range(0, len(parts), 2):
        i, content = int(parts[k]), parts[k + 1]
        tid, pid = f'{eid}-tab-{i}', f'{eid}-panel-{i}'
        sel = 'true' if i == 0 else 'false'
        tabs.append(f'<button type="button" role="tab" id="{tid}" aria-controls="{pid}" aria-selected="{sel}" tabindex="{0 if i == 0 else -1}">{html.escape(labels[i])}</button>')
        panels.append(f'<div role="tabpanel" id="{pid}" aria-labelledby="{tid}" tabindex="0"{"" if i == 0 else " hidden"}>{content}</div>')
    return (before + '<div class="tabs"><div role="tablist" aria-label="Parts of this entry">' + ''.join(tabs)
            + '</div>' + ''.join(panels) + '</div>' + after)

CSS = """.tabs{margin:20px 0}
.tabs [role=tablist]{display:flex;flex-wrap:wrap;gap:6px;border-bottom:2px solid rgba(127,127,127,.3);margin-bottom:8px;position:sticky;top:0;background:var(--bg);z-index:2;padding-top:6px}
.tabs [role=tab]{font:inherit;font-weight:600;padding:8px 14px;border:0;border-bottom:3px solid transparent;margin-bottom:-2px;background:none;color:var(--mute);cursor:pointer;border-radius:8px 8px 0 0}
.tabs [role=tab][aria-selected=true]{color:var(--ink);border-bottom-color:currentColor}
.tabs [role=tab]:hover{color:var(--ink)}
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
