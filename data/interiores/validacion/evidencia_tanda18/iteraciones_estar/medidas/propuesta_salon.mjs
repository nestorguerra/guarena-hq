// Prototipo declarativo privado: reutiliza muebles y grupo_pared existentes.
export const OPTANTES=['artista','estudiante','familia','rico'];
const encaja=(lista,p)=>!lista||(lista.some(x=>x.startsWith('!'))?!lista.includes('!'+p):lista.includes(p));
export function proponer(K,perfiles){
 const old=structuredClone(K),rows=[];
 const legado=e=>{
  if(e.area_min!=null||e.area_max!=null)throw Error('La base ya contiene filtro de área');
  const otros=perfiles.filter(p=>!OPTANTES.includes(p)&&encaja(e.perfil,p));
  const out=[{...e,area_max:22}];if(otros.length)out.push({...e,area_min:22,perfil:otros});return out;
 };
 let libraries=0,modern=0,table=0,lamp=0,puff=0;
 for(const e of old.objetos){
  if(e.regla==='contra_pared'&&e.variantes?.includes('estanteria_libros_ancha')){
   libraries++;rows.push(...legado(e));
   rows.push({zona:'estancia',regla:'contra_pared',obj:'estanteria_libros_ancha',pared:'*',cantidad:[1,1],obligatorio:true,perfil:OPTANTES,area_min:22,grupo_pared:'lectura_salon'});
   for(const[obj,de]of[['sillon_moderno','estanteria_libros_ancha'],['mesita_auxiliar','sillon_moderno'],['lampara_pie','mesita_auxiliar']])rows.push({zona:'estancia',regla:'junto_a',obj,de,cantidad:[0,1],preferir:true,si_no:true,buscar_refs:true,perfil:OPTANTES,area_min:22,grupo_pared:'lectura_salon'});
  }else if(e.regla==='contra_pared'&&e.obj==='sillon_moderno'){modern++;rows.push(...legado(e));}
  else if(e.regla==='contra_pared'&&e.obj==='mesita_auxiliar'){table++;rows.push(...legado(e));}
  else if(e.regla==='esquina'&&e.obj==='lampara_pie'){lamp++;rows.push(...legado(e));}
  else if(e.regla==='suelo_libre'&&e.obj==='puff'){puff++;rows.push(...legado(e));}
  else rows.push(e);
 }
 if([libraries,modern,table,lamp,puff].some(n=>n!==1))throw Error('No coincide estructura T17 esperada');
 return{...old,objetos:rows};
}
