import {readFileSync} from 'node:fs';import assert from 'node:assert/strict';import {runInNewContext} from 'node:vm';
const html=readFileSync('one-interaction-demo.html','utf8');const page=readFileSync('one.html','utf8');
assert.match(page,/href="one-interaction-demo\.html"/);
assert.match(html,/NO LIVE AI/);
assert.match(html,/No audio, camera, microphone/);
const script=html.match(/<script>([\s\S]*?)<\/script>/);assert.ok(script);
const ids=['heading','intro','back','status','notice','footer','statement','language'];
const els=Object.fromEntries(ids.map(k=>[k,{textContent:'',handlers:{},addEventListener(type,fn){this.handlers[type]=fn;}}]));
const buttons=['greet','uncertain','privacy'].map(scene=>({dataset:{scene},textContent:'',pressed:'',handlers:{},setAttribute(k,v){if(k==='aria-pressed')this.pressed=v;},addEventListener(type,fn){this.handlers[type]=fn;}}));
const document={documentElement:{lang:'en'},getElementById(k){assert.ok(els[k],k);return els[k];},querySelectorAll(s){assert.equal(s,'button[data-scene]');return buttons;}};
runInNewContext(script[1],{document},{timeout:1000});
assert.equal(document.documentElement.lang,'en');assert.equal(buttons[0].pressed,'true');
buttons[2].handlers.click();assert.match(els.statement.textContent,/Camera and microphone/);
els.language.handlers.click();assert.equal(document.documentElement.lang,'el');assert.match(els.statement.textContent,/Κάμερα/);assert.equal(buttons[2].pressed,'true');
buttons[1].handlers.click();assert.match(els.statement.textContent,/αβεβαιότητα/);
console.log('NOVERA ONE bilingual scripted interaction checks passed.');

const other=readFileSync('other-robots.html','utf8');const homepage=readFileSync('index.html','utf8');
assert.match(homepage,/href="other-robots\.html"/);assert.match(other,/NOVERA HOME/);assert.match(other,/NOVERA SCOUT/);assert.match(other,/NOVERA FIELD/);assert.match(other,/NOVERA ACCESS/);
assert.match(other,/Άλλα ρομπότ/);assert.match(other,/No performance, autonomy or safety claims/);

const catalog=readFileSync('other-robots.html','utf8');
for(const model of ['HOME','SCOUT','FIELD','ACCESS','BUDDY','CARGO','MED','AGRI','SERVE','GUARD'])assert.match(catalog,new RegExp('NOVERA '+model));
assert.match(catalog,/const photos=\[/);assert.match(catalog,/loading="lazy"/);assert.match(catalog,/third-party photographs/);
assert.equal((catalog.match(/https:\/\/images\.unsplash\.com\/photo-/g)||[]).length,10);

const specialized=readFileSync('specialized-robots.html','utf8');
for(const name of ['SILENT GUIDE','MEMORY','QUIET CARE','MICRO-MUSEUM','RESET','TRANSIT','CALM ROOM','COURTESY','WINDOW','FIELD NOTE','RECEPTION PLUS','KID SAFE','STUDIO BOT','AFTERCARE','ETHOS'])assert.match(specialized,new RegExp('NOVERA '+name));
assert.match(specialized,/filter robot concepts/i);assert.match(specialized,/not built or validated products/);assert.match(specialized,/third-party photographic/);
assert.match(readFileSync('index.html','utf8'),/href="specialized-robots\.html"/);
assert.match(readFileSync('other-robots.html','utf8'),/href="specialized-robots\.html"/);
