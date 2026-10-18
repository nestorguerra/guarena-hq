"""Private evidence v2: general front + complete consultation group.

No game/source mutation. Keeps 1.60m eye/FOV68/high/DPR1 and only CPU
positions proven free in BOTH builds, rechecked in the actual browser.
Projection and sparse actual-geometry rays complement human review.
"""
from pathlib import Path
import sys, json, importlib.util
r=Path(__file__).resolve().parents[3]; o=r/'.cache/calidad/tanda19'
base='--base' in sys.argv; p=o/('base_T18' if base else 'prototipo_r8')
f=p/'tools/interiores/fotos_casa.py'
spec=importlib.util.spec_from_file_location('consulta_completa',f)
photo=importlib.util.module_from_spec(spec);spec.loader.exec_module(photo)
def sub(old,new):
    assert photo.JS.count(old)==1,old
    photo.JS=photo.JS.replace(old,new)
sub('const {caja}=','const {caja,construir}=')
sub('const objetivos=puestosComedor.length?',"const consulta=k===1&&tipo==='trofeos'?[est.colocados.find(p=>p.obj==='vb_sillon_campo'),est.colocados.find(p=>p.obj==='vb_mesa_consulta_campo')].filter(Boolean):[];\n      if(k===1&&tipo==='trofeos'&&consulta.length!==2)throw Error('consulta incompleta');\n      const frente=k===0&&tipo==='trofeos'?est.colocados.filter(p=>['vb_armero','vb_guardado_campo','vb_banco_equipo_campo','vb_cornamenta'].includes(p.obj)):[];\n      const objetivos=frente.length?frente:consulta.length?consulta:puestosComedor.length?")
sub('const alturaObjetivo=k===0?',"const alturaObjetivo=objetivos.length?(Math.min(...objetivos.map(p=>(p.y||0)+caja(p.obj).y0))+Math.max(...objetivos.map(p=>(p.y||0)+caja(p.obj).y1)))/2:k===0?")
sub("const opacos=[];",r'''const consultaGhost=consulta.map(p=>{
        const ghost=construir([{...p,x:est.origen.x+p.x,y:y+(p.y||0),z:est.origen.z+p.z}]);
        ghost.updateMatrixWorld(true);return {p,ghost,bounds:new THREE.Box3().setFromObject(ghost)};
      });
      function visibilidadConsulta(pos){
        return consultaGhost.map(({p,ghost,bounds})=>{
          const c=bounds.getCenter(new THREE.Vector3()),size=bounds.getSize(new THREE.Vector3());let medidas=0,visibles=0;
          for(const [dx,dy] of [[0,0],[-.25,0],[.25,0],[0,-.25],[0,.25]]){
            const target=c.clone().add(new THREE.Vector3(size.x*dx,size.y*dy,0));
            const dir=target.clone().sub(pos).normalize(),ray=new THREE.Raycaster(pos,dir,0,100);
            const hit=ray.intersectObject(ghost,true)[0];if(!hit)continue;
            medidas++;ray.far=hit.distance-.005;
            if(!ray.intersectObjects(opacos,false).length)visibles++;
          }
          return {obj:p.obj,muestras:medidas,visibles,fraccion:medidas?visibles/medidas:0};
        });
      }
      const opacos=[];''')
commons=json.loads((o/'medidas/camaras_comunes_r8.json').read_text())['rows']
sub('        const clearance=cameraClearance(h,est,col,q);if(!clearance.free)continue;',
    '        if(!COMMON[String(s)]?.points.some(p=>Math.hypot(p.x-q.x,p.z-q.z)<1e-6))continue;\n'.replace('COMMON',json.dumps(commons))+
    '        const clearance=cameraClearance(h,est,col,q);if(!clearance.free)continue;')
sub('        let recortes=0,puertaPrimerPlano=0;',r'''        if(consulta.length){
          const seat=centros[0],dot=(Math.sin(seat.p.ry)*(q.x-seat.x)+Math.cos(seat.p.ry)*(q.z-seat.z))/Math.max(.001,Math.hypot(q.x-seat.x,q.z-seat.z));
          if(dot<Math.cos(65*Math.PI/180))continue;
          if(visibilidadConsulta(pos).some(v=>v.muestras<3||v.fraccion<.6))continue;
        }
        let recortes=0,puertaPrimerPlano=0;''')
sub('        const ray=new THREE.Raycaster(pos,dir.normalize(),0,dist);',
    '        if(objetivos.length&&recortes)continue;\n        const ray=new THREE.Raycaster(pos,dir.normalize(),0,dist);')
sub('      const clearanceAntes=requireCameraClearance',r'''      let coberturaConsulta=null;
      if(consulta.length){
        h.group.updateMatrixWorld(true);
        const recortes=esquinas.filter(v=>{const p=v.clone().project(cam);return p.z< -1||p.z>1||Math.abs(p.x)>.94||Math.abs(p.y)>.94;}).length;
        const visibilidad=visibilidadConsulta(cam.position);
        if(recortes||visibilidad.some(v=>v.muestras<3||v.fraccion<.6))throw Error('consulta recortada u oculta: '+JSON.stringify({s,recortes,visibilidad}));
        coberturaConsulta={esquinas_evaluadas:esquinas.length,esquinas_recortadas:recortes,visibilidad,limite:.6,limites:'Cinco rayos por raíz; lectura humana adicional obligatoria.'};
      }
      consultaGhost.forEach(({ghost})=>ghost.traverse(m=>{if(m.isMesh)m.geometry.dispose();}));
      const clearanceAntes=requireCameraClearance''')
sub("encuadre:k===0?'uso':'conjunto'", "encuadre:tipo==='trofeos'?(k===0?'frente_completo':'consulta_completa'):(k===0?'uso':'conjunto'),...(coberturaConsulta?{cobertura_consulta:coberturaConsulta}:{})")
if base:
    # Candidate's exact pose/target in baseline; baseline has the legacy seat/table.
    # Its image is a causal comparison, not a claim of the same furniture/coverage.
    original=photo.JS
    poses=json.loads((o/'comparativa_r8_completa/despues/casa_trofeos.json').read_text())
    photo.JS=original.replace("if(k===1&&tipo==='trofeos'&&consulta.length!==2)throw Error('consulta incompleta');",'')
    photo.JS=photo.JS.replace('const cx = foco?', 'let cx = foco?').replace('const alturaObjetivo=objetivos.length?', 'let alturaObjetivo=objetivos.length?')
    marker="      if(!Number.isFinite(mejor))throw Error('sin cámara libre: '+tipo+'/'+s);"
    hook=r'''
      const canonical=POSES.find(row=>row.seed===s)?.vistas[k];
      if(!canonical||canonical.fov!==fov||Math.abs(canonical.y-y-1.6)>1e-6)throw Error('pose común inválida');
      x=canonical.x;z=canonical.z;cx=canonical.objetivo[0];cz=canonical.objetivo[2];alturaObjetivo=canonical.objetivo[1]-y;
      clearanceElegido=requireCameraClearance(h,est,col,{x,z},'pose común consulta');
'''.replace('POSES',json.dumps(poses))
    sub(marker,marker+hook)
    # Baseline has no new consultation group. Do not claim its geometry coverage.
    photo.JS=photo.JS.replace("const consulta=k===1&&tipo==='trofeos'?",'const consulta=false?').replace("const frente=k===0&&tipo==='trofeos'?",'const frente=false?')
sys.argv=[str(f),'trofeos','3'];photo.main()
