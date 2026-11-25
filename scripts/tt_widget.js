// ---------- truth tables (shared by site_template.html and preview_template.html) ----------
// Each form: name, group (forms in the same group are offered as comparison buttons),
// letters, premises [[label, fn]], conclusion [label, fn]. Rows follow the house convention:
// all 1s first, the right-most letter alternating 1, 0.
const imp=(a,b)=>!a||b;
const FORMS={
 mt:{name:'Modus tollens',g:'cond',v:'PQ',p:[['P ⊃ Q',(P,Q)=>imp(P,Q)],['~Q',(P,Q)=>!Q]],c:['~P',(P,Q)=>!P]},
 mp:{name:'Modus ponens',g:'cond',v:'PQ',p:[['P ⊃ Q',(P,Q)=>imp(P,Q)],['P',(P,Q)=>P]],c:['Q',(P,Q)=>Q]},
 da:{name:'Denying the antecedent',g:'cond',v:'PQ',p:[['P ⊃ Q',(P,Q)=>imp(P,Q)],['~P',(P,Q)=>!P]],c:['~Q',(P,Q)=>!Q]},
 ac:{name:'Affirming the consequent',g:'cond',v:'PQ',p:[['P ⊃ Q',(P,Q)=>imp(P,Q)],['Q',(P,Q)=>Q]],c:['P',(P,Q)=>P]},
 ds:{name:'Disjunctive syllogism',g:'disj',v:'PQ',p:[['P ∨ Q',(P,Q)=>P||Q],['~P',(P,Q)=>!P]],c:['Q',(P,Q)=>Q]},
 ad:{name:'Affirming a disjunct',g:'disj',v:'PQ',p:[['P ∨ Q',(P,Q)=>P||Q],['P',(P,Q)=>P]],c:['~Q',(P,Q)=>!Q]},
 hs:{name:'Hypothetical syllogism',g:'chain',v:'PQR',p:[['P ⊃ Q',(P,Q,R)=>imp(P,Q)],['Q ⊃ R',(P,Q,R)=>imp(Q,R)]],c:['P ⊃ R',(P,Q,R)=>imp(P,R)]},
 hx:{name:'P ⊃ Q, R ⊃ Q ∴ P ⊃ R',g:'chain',v:'PQR',p:[['P ⊃ Q',(P,Q,R)=>imp(P,Q)],['R ⊃ Q',(P,Q,R)=>imp(R,Q)]],c:['P ⊃ R',(P,Q,R)=>imp(P,R)]},
 cd:{name:'Constructive dilemma',g:'dil',v:'PQRS',p:[['P ⊃ Q',(P,Q,R,S)=>imp(P,Q)],['R ⊃ S',(P,Q,R,S)=>imp(R,S)],['P ∨ R',(P,Q,R,S)=>P||R]],c:['Q ∨ S',(P,Q,R,S)=>Q||S]},
 dd:{name:'Destructive dilemma',g:'dil',v:'PQRS',p:[['P ⊃ Q',(P,Q,R,S)=>imp(P,Q)],['R ⊃ S',(P,Q,R,S)=>imp(R,S)],['~Q ∨ ~S',(P,Q,R,S)=>!Q||!S]],c:['~P ∨ ~R',(P,Q,R,S)=>!P||!R]},
 ax:{name:'P ⊃ Q, R ⊃ S, Q ∨ S ∴ P ∨ R',g:'dil',v:'PQRS',p:[['P ⊃ Q',(P,Q,R,S)=>imp(P,Q)],['R ⊃ S',(P,Q,R,S)=>imp(R,S)],['Q ∨ S',(P,Q,R,S)=>Q||S]],c:['P ∨ R',(P,Q,R,S)=>P||R]}
};
function drawTT(box,key){
 const F=FORMS[key],b=v=>v?1:0,bad=[],n=F.v.length,big=n>2,vs=[...F.v];
 const combos=[...Array(2**n).keys()].map(i=>vs.map((_,j)=>((i>>(n-1-j))&1)?0:1));
 const rows=combos.map(vals=>{
  const a=vals.map(x=>!!x),ps=F.p.map(([,f])=>f(...a)),c=F.c[1](...a);
  const live=ps.every(Boolean),ce=live&&!c;if(ce)bad.push(vs.map((x,j)=>`${x} = ${vals[j]}`).join(', '));
  const cls=[ce?'ce':live?'live':'',big&&!c?'chk':''].filter(Boolean).join(' ');
  return `<tr class="${cls}">${vals.map(x=>`<td>${x}</td>`).join('')}${ps.map(x=>`<td>${b(x)}</td>`).join('')}<td>${b(c)}</td></tr>`}).join('');
 const head=vs.map(x=>`<th>${x}</th>`).join('')+F.p.map(([l],i)=>`<th>Premise ${i+1}: ${l}</th>`).join('')+`<th>Conclusion: ${F.c[0]}</th>`;
 box.querySelector('.out').innerHTML=`<div class="scroll"><table><thead><tr>${head}</tr></thead><tbody>${rows}</tbody></table></div>`+
  (bad.length?`<p class="verdict no">${F.name} is invalid: true premises and a false conclusion in the row${bad.length>1?'s':''} ${bad.join('; ')}.</p>`:`<p class="verdict ok">${F.name} is valid: no row has true premises and a false conclusion.</p>`);
 box.querySelector('.key').textContent='1 = true, 0 = false. Shaded rows: all premises true. Red rows: true premises with a false conclusion (a counterexample).'+(big?' Outlined rows: the conclusion is false. Only these rows can be counterexamples, so they are the ones to check.':'');
 box.querySelectorAll('.forms button').forEach(x=>x.setAttribute('aria-pressed',x.dataset.k===key));
}
function truthTable(box){
 const key=box.dataset.form||'mt',g=FORMS[key].g,peers=Object.entries(FORMS).filter(([,v])=>v.g===g);
 box.innerHTML=`<div class="forms" role="group" aria-label="Compare argument forms">${peers.map(([k,v])=>`<button type="button" data-k="${k}">${v.name}</button>`).join('')}</div><div class="out" aria-live="polite"></div><p class="key"></p>`;
 box.querySelectorAll('.forms button').forEach(x=>x.addEventListener('click',()=>drawTT(box,x.dataset.k)));
 drawTT(box,key);
}
