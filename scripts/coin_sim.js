// ---------- coin-toss simulator (gambler's fallacy) ----------
// Marker in an entry: <!-- interactive: coin-sim -->. Tosses a fair virtual coin and reports
// how often the toss straight after a run of at least three heads comes up heads.
function coinSim(el){
  let n=0,h=0,run=0,after=0,afterH=0;
  el.innerHTML='<p class="simtitle">Coin-toss simulator</p>'+
   '<div class="simbtns"><button type="button" data-k="10">Toss 10</button><button type="button" data-k="1000">Toss 1,000</button><button type="button" data-k="100000">Toss 100,000</button><button type="button" data-k="0">Reset</button></div>'+
   '<div class="simout" aria-live="polite"></div>'+
   '<p class="key">Each toss is a fair 50–50 toss made by your browser. A "streak" means the three tosses just before were all heads.</p>';
  const out=el.querySelector('.simout');
  const pct=(a,b)=>b?(100*a/b).toFixed(1)+'%':'–';
  function show(){
    out.innerHTML=`<p>Tosses: <b>${n.toLocaleString()}</b> · Heads: <b>${h.toLocaleString()}</b> (${pct(h,n)})</p>`+
     `<p>Tosses straight after a streak of 3+ heads: <b>${after.toLocaleString()}</b> · of these, heads: <b>${afterH.toLocaleString()}</b> (${pct(afterH,after)})</p>`;
  }
  el.querySelectorAll('button').forEach(b=>b.addEventListener('click',()=>{
    const k=+b.dataset.k;
    if(!k){n=h=run=after=afterH=0;show();return}
    for(let i=0;i<k;i++){
      const heads=Math.random()<0.5;
      if(run>=3){after++;if(heads)afterH++}
      n++;if(heads){h++;run++}else run=0;
    }
    show();
  }));
  show();
}
