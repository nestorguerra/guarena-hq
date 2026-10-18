import fs from'node:fs';import assert from'node:assert/strict';import crypto from'node:crypto';
const file='.cache/calidad/tanda17/preview_final_r3/tools/interiores/fotos_casa.py',source=fs.readFileSync(file,'utf8');
const start=source.indexOf("      if(window.__errs?.length)throw Error('errores antes de captura:"),end=source.indexOf('      vistas[vistas.length-1].clearance.afterRender',start);assert(start>0&&end>start);
const segment=source.slice(start,end),fn=new Function('window','g','r',segment+';return "eligible_to_save";');
const rows=[];
for(const spec of[{name:'clean',pre:[],post:[],programs:[{}],pass:true},{name:'before_console_error',pre:['shader error'],post:[],programs:[],pass:false},{name:'render_console_error',pre:[],post:['shader error'],programs:[],pass:false},{name:'link_failure_without_console',pre:[],post:[],programs:[{diagnostics:{runnable:false}}],pass:false}]){
 const window={__errs:[...spec.pre]},g={render(){window.__errs.push(...spec.post);}},r={info:{programs:spec.programs}};let result,error;try{result=fn(window,g,r);}catch(e){error=e.message;}assert.equal(result==='eligible_to_save',spec.pass,spec.name);rows.push({name:spec.name,eligible:!!result,error:error??null});
}
fs.writeFileSync('.cache/calidad/tanda17/revision_shader_r3/guardas_cpu.json',JSON.stringify({state:'PASS_EXACT_CAPTURE_GUARDS_CPU',scope:'Exact added guard block with controlled doubles, no rendering/GLSL compilation.',sourceSha256:crypto.createHash('sha256').update(source).digest('hex'),rows},null,2)+'\n');console.log(rows);
