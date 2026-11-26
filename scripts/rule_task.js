// ---------- number-rule task (confirmation bias) ----------
// Marker in an entry: <!-- interactive: rule-246 -->. Based on Wason's (1960) 2-4-6 task as
// described by Nickerson (1998): the reader is told 2, 4, 6 fits a rule, proposes triples,
// is told whether each fits, then reveals the rule (any three numbers in ascending order).
function ruleTask(el){
  const tests=[];let shown=false;
  el.setAttribute('role','group');el.setAttribute('aria-label','Number rule task');
  el.innerHTML='<p class="simtitle">The number rule task</p>'+
   '<p>The numbers <b>2, 4, 6</b> fit a rule. Find the rule by testing other sets of three numbers. You will be told whether each set fits.</p>'+
   '<div class="rt-in"><label>First <input type="number" step="any" inputmode="decimal"></label><label>Second <input type="number" step="any" inputmode="decimal"></label><label>Third <input type="number" step="any" inputmode="decimal"></label></div>'+
   '<div class="simbtns"><button type="button" data-a="test">Test these numbers</button><button type="button" data-a="reveal">I think I know the rule</button><button type="button" data-a="reset">Reset</button></div>'+
   '<div class="simout" aria-live="polite"></div>'+
   '<p class="key">Based on a task devised by P. C. Wason (1960). This version is simplified.</p>';
  const ins=[...el.querySelectorAll('input')],out=el.querySelector('.simout');
  const fits=t=>t[0]<t[1]&&t[1]<t[2];
  function show(){
    let h=tests.length?'<ol class="rt-log">'+tests.map(t=>`<li>${t.join(', ')}: <b>${fits(t)?'fits':'does not fit'}</b></li>`).join('')+'</ol>':'<p>No sets tested yet.</p>';
    if(shown){
      const yes=tests.filter(fits).length,no=tests.length-yes;
      h+='<div class="rt-reveal"><p><b>The rule: any three numbers in ascending order</b> (each number larger than the one before).</p>'+
        `<p>You tested ${tests.length} set${tests.length===1?'':'s'}: ${yes} fitted and ${no} did not.</p>`+
        '<p>Many people guess a narrower rule, such as "successive even numbers", and test only sets that fit their guess. Every answer then comes back "fits", and the guess seems confirmed. The tests that can show a guess is wrong are the ones you expect to fail.</p></div>';
    }
    out.innerHTML=h;
  }
  el.querySelectorAll('button').forEach(b=>b.addEventListener('click',()=>{
    const a=b.dataset.a;
    if(a==='reset'){tests.length=0;shown=false;ins.forEach(i=>i.value='');show();return}
    if(a==='reveal'){shown=true;show();return}
    const v=ins.map(i=>i.value.trim());
    if(v.some(x=>x===''||!isFinite(+x))){out.insertAdjacentHTML('afterbegin','<p class="rt-err">Enter three numbers.</p>');return}
    tests.push(v.map(Number));show();
  }));
  show();
}
