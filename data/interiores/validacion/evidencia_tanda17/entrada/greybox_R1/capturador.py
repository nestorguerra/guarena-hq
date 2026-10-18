from pathlib import Path
import sys,json,hashlib,shutil
r=Path.cwd();sys.path.insert(0,str(r/'tools/interiores'));sys.path.insert(0,str(r/'tools/perf'))
from beta import PrivateTab
from integracion import LISTO
from fotos_casa import JS
out=r/'.cache/calidad/tanda17/entrada1594';out.mkdir(exist_ok=False)
prefix=JS[:JS.index('  const g = window.game, tipo')]
suffix=r'''
 const g=window.game,seed=1594,label=__LABEL__,d=g.interiors.doors.find(d=>d.seed===seed);
 if(!d)throw Error('sin puerta real1594');
 await g.interiors.enter(d,{mode:'visit',silent:true,seed});
 if(g.interiors.life){g.interiors.life.dispose();g.interiors.life=null;}
 const h=g.interior,rm=h.rooms.find(r=>r.type==='estudio'),e=h.estancias.find(e=>e.sala===rm.id),desk=e.colocados.find(p=>p.obj==='vb_escritorio'||p.obj==='t17_mesa_amplio');
 if(!desk)throw Error('sin puesto de trabajo');
 if(g.player.char?.object)g.player.char.object.visible=false;
 const renderer=g.renderer;renderer.setSize(1280,720,false);g.composer?.setSize(1280,720);
 for(let i=0;i<3;i++)g.frame(1/30);g.sky.hour=12;
 const cam=g.camera,col=h.levels?.[rm.lv]||h.collider,b=caja(desk.obj),lx=(b.x0+b.x1)/2,lz=(b.z0+b.z1)/2;
 const point=[e.origen.x+e.inicio.x,e.origen.y+1.6,e.origen.z+e.inicio.z],target=[e.origen.x+desk.x+lx*Math.cos(desk.ry)+lz*Math.sin(desk.ry),e.origen.y+.98,e.origen.z+desk.z-lx*Math.sin(desk.ry)+lz*Math.cos(desk.ry)];
 cam.aspect=16/9;cam.fov=75;cam.updateProjectionMatrix();cam.position.set(...point);cam.lookAt(...target);cam.updateMatrixWorld(true);h.group.updateMatrixWorld(true);
 const before=requireCameraClearance(h,e,col,cam.position,'entrada1594 antes'),pose=JSON.stringify({p:cam.position.toArray(),q:cam.quaternion.toArray(),fov:cam.fov});
 g.render();const after=requireCameraClearance(h,e,col,cam.position,'entrada1594 después');
 if(JSON.stringify({p:cam.position.toArray(),q:cam.quaternion.toArray(),fov:cam.fov})!==pose)throw Error('render cambia cámara');
 await fetch('/__snap?name=entrada_t17_'+label+'_1594',{method:'POST',body:renderer.domElement.toDataURL('image/jpeg',.86)});
 return JSON.stringify({seed,perfil:h.profile.id,calidad:g.qKey,dpr:renderer.getPixelRatio(),punto:point,objetivo:target,fov:75,inicio:e.inicio,camara:{before,after},puesto:desk.obj,marco:{W:e.W,D:e.D,H:e.H},limite:'Pose fija en inicio físico real, mirada al puesto real; no es cámara canónica ni evaluación formal.'});
})()'''
for label,port in [('base_T16',8920),('greybox',8922)]:
 with PrivateTab() as t:
  t.call('Emulation.setDeviceMetricsOverride',dict(width=1280,height=720,deviceScaleFactor=1,mobile=False));t.call('Page.addScriptToEvaluateOnNewDocument',{'source':"localStorage.setItem('guarena_hq_save',JSON.stringify({quality:'alta',qualityMode:'manual',dynRes:false,weatherLive:false,pick:'annie'}));"});t.call('Page.navigate',{'url':f'http://localhost:{port}/index.html?estilo=plastilina'});t.ev(LISTO,timeout=240)
  assert t.ev("game.qKey==='alta'&&!game.autoQuality&&game.renderer.getPixelRatio()===1")
  d=json.loads(t.ev(prefix+suffix.replace('__LABEL__',json.dumps(label)),timeout=300));(out/(label+'.json')).write_text(json.dumps(d,ensure_ascii=False,indent=1)+'\n')
 source=(r if port==8920 else r/'.cache/calidad/tanda17/preview_greybox')/'.snaps'/f'entrada_t17_{label}_1594.jpg';shutil.copy2(source,out/(label+'.jpg'));print(label,'capturada, guardas libres',flush=True)
a=json.loads((out/'base_T16.json').read_text());b=json.loads((out/'greybox.json').read_text());assert a['punto']==b['punto'];print('Mismo punto físico; objetivo sigue puesto real, sin cambiar fuente/cámaras canónicas.')
