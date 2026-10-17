"""Dos vistas por habitación de la casa real de Annie, sin alterar puertas ni mobiliario."""
import os,sys,json
ROOT=os.path.abspath(os.path.join(os.path.dirname(__file__),'..','..'))
sys.path.insert(0,os.path.join(ROOT,'tools','perf'))
from cdp import Tab
from PIL import Image,ImageDraw
from integracion import LISTO

def main():
    t=Tab(9333,'http://localhost:8920/index.html?estilo=plastilina',w=1280,h=720,dpr=1)
    try:
        t.ev(LISTO,timeout=240)
        t.ev("(async()=>{const t=performance.now();while(game.cam.cinematic&&performance.now()-t<60000)await new Promise(r=>setTimeout(r,100));if(game.cam.cinematic)throw Error('introducción todavía activa');})()",timeout=75)
        rows=json.loads(t.ev('''(async()=>{
          const g=game;g.sky.hour=12;const d=g.interiors.doors.find(d=>d.owner==='annie');const h=await g.interiors.enter(d,{silent:true});await new Promise(r=>setTimeout(r,500));g.frame=()=>{};
          const campos=[...h.rooms,{id:'patio',lv:0,x0:h.origin.x-3.2,x1:h.origin.x+3.2,z0:h.origin.z+10.5,z1:h.origin.z+13.5},{id:'recibidor',lv:0,x0:h.origin.x+.9,x1:h.origin.x+3.2,z0:h.origin.z+3.8,z1:h.origin.z+5}];
          if(g.player.char?.object)g.player.char.object.visible=false;
          g.renderer.setSize(1280,720,false);if(g.composer)g.composer.setSize(1280,720);g.camera.aspect=16/9;g.camera.fov=75;g.camera.updateProjectionMatrix();
          for(const rm of campos){for(const k of [0,1]){
            let x,z;const y=rm.lv*3.1,cx=(rm.x0+rm.x1)/2,cz=(rm.z0+rm.z1)/2,col=h.levels[rm.lv],f=k?.82:.18;
            for(const [fx,fz] of [[f,f],[1-f,f],[f,1-f],[f,.5],[.5,f]]){const p={x:rm.x0+(rm.x1-rm.x0)*fx,z:rm.z0+(rm.z1-rm.z0)*fz},q={...p};col.resolveCircle(q,.24);x=p.x;z=p.z;if(Math.hypot(q.x-p.x,q.z-p.z)<.05)break;}
            for(let i=0;i<3;i++)g.frame(1/30);g.camera.position.set(x,y+1.6,z);g.camera.lookAt(2*cx-x,y+.9,2*cz-z);g.camera.updateMatrixWorld(true);g.render();
            await fetch('/__snap?name=annie_'+rm.id+'_'+k,{method:'POST',body:g.renderer.domElement.toDataURL('image/jpeg',.88)});
          }}g.interiors.leave(true);return JSON.stringify(campos);
        })()''',timeout=240))
        sheet=Image.new('RGB',(1280,386*len(rows)))
        for j,rm in enumerate(rows):
            ImageDraw.Draw(sheet).text((8,j*386+5),'Annie / '+rm['id']+' / planta '+str(rm['lv']),fill='white')
            for k in [0,1]:sheet.paste(Image.open(os.path.join(ROOT,'.snaps','annie_'+rm['id']+'_'+str(k)+'.jpg')).resize((640,360)),(k*640,j*386+26))
        dest=os.path.join(ROOT,'data','interiores','fichas','casa_annie')
        sheet.save(dest+'.jpg',quality=86);json.dump(rows,open(dest+'.json','w'),ensure_ascii=False,indent=1)
        print(len(rows),'espacios de Annie capturados')
    finally:t.close()
if __name__=='__main__':main()
