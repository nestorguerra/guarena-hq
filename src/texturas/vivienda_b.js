// Painted pictures for the objects of the «vivienda_b» family (data/objetos): labels, tiles, calendars, screens — drawn on a
// canvas, never a photograph. Each one: tipo → { w, h, draw(ctx, w, h, tex, seed) }. Read by src/objetos.js (textura).
// (No «export { … }» anywhere: the game's packer, tools/build.py, only understands export const/function/class.)
export const TEXTURAS = {
  vivienda_lienzo_b: {w:256,h:192,draw(ctx,w,h,tex,seed){
    if(seed%3===1){ctx.fillStyle='#d9c4a2';ctx.fillRect(0,0,w,h);for(let i=0;i<7;i++){ctx.fillStyle=['#8f5d58','#718d82','#be9757'][i%3];ctx.fillRect(18+i*29,24+(i%3)*22,24,105-(i%3)*15);}return;}
    if(seed%3===2){ctx.fillStyle='#c1ced6';ctx.fillRect(0,0,w,h);ctx.fillStyle='#927962';ctx.fillRect(0,h*.68,w,h*.32);for(let i=0;i<4;i++){ctx.fillStyle=['#b17058','#d8bb75','#79948c','#667e99'][i];ctx.beginPath();ctx.ellipse(48+i*52,116-i*11,23,36,0,0,Math.PI*2);ctx.fill();}return;}
    ctx.fillStyle='#b9d6d4';ctx.fillRect(0,0,w,h);ctx.fillStyle='#b4a06b';ctx.fillRect(0,h*.58,w,h*.42);
    ctx.fillStyle='#dbd2b8';ctx.fillRect(135,75,55,47);ctx.fillStyle='#a5694e';ctx.beginPath();ctx.moveTo(127,76);ctx.lineTo(161,48);ctx.lineTo(198,76);ctx.fill();
    for(let i=0;i<13;i++){ctx.fillStyle=['#7d9163','#879e6c','#ab986b'][i%3];ctx.beginPath();ctx.ellipse((i*53+seed*7)%w,135+(i*11)%45,24,6,0,0,Math.PI*2);ctx.fill();}
  }},
};
