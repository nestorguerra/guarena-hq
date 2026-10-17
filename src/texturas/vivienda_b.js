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
  // Dibujos originales a lápiz de cera: casa, barco y cohete, sin iconos ni imágenes externas.
  vivienda_dibujo_ninos_b:{w:192,h:256,draw(ctx,w,h,tex,seed){
    const c=['#b66351','#d29d48','#4f7a91','#789a79'];
    ctx.fillStyle='#e9dfc9';ctx.fillRect(0,0,w,h);ctx.lineCap='round';ctx.lineJoin='round';ctx.lineWidth=5;
    const trazo=(color,pts,cerrar=false)=>{ctx.strokeStyle=color;ctx.beginPath();pts.forEach((p,i)=>i?ctx.lineTo(p[0],p[1]):ctx.moveTo(p[0],p[1]));if(cerrar)ctx.closePath();ctx.stroke();};
    const sol=()=>{ctx.fillStyle=c[1];ctx.beginPath();ctx.arc(151,43,18,0,Math.PI*2);ctx.fill();for(let i=0;i<8;i++){const a=i*Math.PI/4;trazo(c[1],[[151+Math.cos(a)*23,43+Math.sin(a)*23],[151+Math.cos(a)*31,43+Math.sin(a)*31]]);}};
    const tema=(tex.lamina||0)%3;
    if(tema===0){
      sol();ctx.fillStyle='#ceb888';ctx.fillRect(46,124,80,85);ctx.fillStyle=c[0];ctx.beginPath();ctx.moveTo(33,126);ctx.lineTo(86,72);ctx.lineTo(139,128);ctx.closePath();ctx.fill();
      trazo('#676354',[[45,208],[44,126],[85,74],[138,127],[124,127],[126,208],[45,208]]);
      ctx.fillStyle=c[2];ctx.fillRect(59,144,18,22);ctx.fillRect(99,144,16,22);ctx.fillStyle=c[0];ctx.fillRect(81,176,18,32);
      trazo(c[3],[[19,220],[169,218]]);for(const x of [22,154,170]){trazo(c[3],[[x,218],[x-2,184]]);ctx.fillStyle=c[(seed+x)%2];ctx.beginPath();ctx.arc(x,182,7,0,Math.PI*2);ctx.fill();}
    }else if(tema===1){
      sol();ctx.fillStyle=c[2];ctx.beginPath();ctx.moveTo(30,160);ctx.lineTo(161,161);ctx.lineTo(136,193);ctx.lineTo(53,194);ctx.closePath();ctx.fill();
      trazo('#646655',[[96,64],[96,161]]);ctx.fillStyle=c[0];ctx.beginPath();ctx.moveTo(89,75);ctx.lineTo(39,149);ctx.lineTo(89,149);ctx.closePath();ctx.fill();
      ctx.fillStyle=c[1];ctx.beginPath();ctx.moveTo(103,95);ctx.lineTo(146,150);ctx.lineTo(103,149);ctx.closePath();ctx.fill();
      for(const y of [211,229])trazo(c[2],[[12,y],[36,y-5],[60,y+2],[84,y-4],[111,y+1],[139,y-4],[177,y]]);
      trazo('#676354',[[22,74],[33,66],[43,73],[53,65],[64,72]]);
    }else{
      ctx.fillStyle=c[2];ctx.beginPath();ctx.moveTo(68,163);ctx.lineTo(70,93);ctx.lineTo(96,53);ctx.lineTo(123,95);ctx.lineTo(124,164);ctx.closePath();ctx.fill();
      ctx.fillStyle=c[0];ctx.beginPath();ctx.moveTo(68,135);ctx.lineTo(45,177);ctx.lineTo(70,165);ctx.moveTo(122,135);ctx.lineTo(148,177);ctx.lineTo(122,164);ctx.fill();
      ctx.fillStyle='#e3d5ac';ctx.beginPath();ctx.arc(96,109,14,0,Math.PI*2);ctx.fill();trazo(c[1],[[78,176],[83,213],[95,182],[108,221],[117,178]]);
      for(const [x,y] of [[29,40],[153,86],[36,132],[146,218]]){trazo(c[1],[[x-7,y],[x+7,y]]);trazo(c[1],[[x,y-8],[x,y+8]]);}
      ctx.strokeStyle=c[3];ctx.lineWidth=4;ctx.beginPath();ctx.ellipse(150,38,23,12,-.3,0,Math.PI*2);ctx.stroke();ctx.beginPath();ctx.arc(150,38,13,0,Math.PI*2);ctx.stroke();
    }
    // Pequeña marca de autor de ficción: un garabato, sin nombre ni dato personal.
    trazo('#6e7970',[[18,244],[25,237],[31,245],[39,239],[48,244]]);
  }},
  vivienda_juego_ninos_b:{w:384,h:256,draw(ctx,w,h,tex,seed){
    const p=[['#b7b78e','#526d79','#b76752'],['#a7bbac','#526b7a','#ce984d'],['#c4b290','#5d7676','#6c7d9b']][seed%3];
    ctx.fillStyle=p[0];ctx.fillRect(0,0,w,h);ctx.strokeStyle='#d7c9a6';ctx.lineWidth=12;ctx.strokeRect(8,8,w-16,h-16);
    const circuito=()=>{ctx.beginPath();ctx.moveTo(104,54);ctx.lineTo(282,54);ctx.quadraticCurveTo(333,54,333,104);ctx.lineTo(333,154);ctx.quadraticCurveTo(333,205,282,205);ctx.lineTo(104,205);ctx.quadraticCurveTo(53,205,53,154);ctx.lineTo(53,104);ctx.quadraticCurveTo(53,54,104,54);ctx.closePath();};
    ctx.lineJoin='round';ctx.lineCap='round';ctx.strokeStyle=p[1];ctx.lineWidth=40;circuito();ctx.stroke();
    ctx.strokeStyle='#e3d8b9';ctx.lineWidth=3;ctx.setLineDash([12,12]);circuito();ctx.stroke();ctx.setLineDash([]);
    // Un parque y un aparcamiento dentro del circuito dan una lectura de juego.
    ctx.fillStyle='#819c76';ctx.fillRect(110,91,78,73);for(const [x,y] of [[126,109],[166,111],[144,146]]){ctx.fillStyle='#647f64';ctx.beginPath();ctx.arc(x,y,11,0,Math.PI*2);ctx.fill();}
    ctx.strokeStyle='#e3d8b9';ctx.lineWidth=3;ctx.strokeRect(219,93,53,69);ctx.beginPath();ctx.moveTo(219,116);ctx.lineTo(272,116);ctx.moveTo(219,139);ctx.lineTo(272,139);ctx.stroke();
    ctx.fillStyle=p[2];ctx.fillRect(236,99,24,12);ctx.fillRect(128,43,30,20);ctx.fillStyle='#d5d9cc';ctx.fillRect(139,46,12,14);
    ctx.fillStyle='#60675f';for(const x of [131,150]){ctx.fillRect(x,40,5,5);ctx.fillRect(x,62,5,5);}
  }},
};
