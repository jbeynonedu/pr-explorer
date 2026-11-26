"""Truth-table marker forms: (premises, conclusion) as written in an entry's
`<!-- interactive: truth-table; premises: ...; conclusion: ... -->` marker -> widget key
(see scripts/tt_widget.js)."""
TT_FORMS = {
    'mt': ('P ⊃ Q, ~Q', '~P'), 'mp': ('P ⊃ Q, P', 'Q'),
    'da': ('P ⊃ Q, ~P', '~Q'), 'ac': ('P ⊃ Q, Q', 'P'),
    'ds': ('P ∨ Q, ~P', 'Q'), 'ad': ('P ∨ Q, P', '~Q'),
    'hs': ('P ⊃ Q, Q ⊃ R', 'P ⊃ R'),
    'cd': ('P ⊃ Q, R ⊃ S, P ∨ R', 'Q ∨ S'), 'dd': ('P ⊃ Q, R ⊃ S, ~Q ∨ ~S', '~P ∨ ~R'),
}
WIDGET = (open(__file__.replace('tt_forms.py', 'tt_widget.js'), encoding='utf-8').read()
          + '\n' + open(__file__.replace('tt_forms.py', 'coin_sim.js'), encoding='utf-8').read()
          + '\n' + open(__file__.replace('tt_forms.py', 'rule_task.js'), encoding='utf-8').read())
