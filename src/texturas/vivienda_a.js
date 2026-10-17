// Painted pictures for the objects of the «vivienda_a» family (data/objetos): labels, tiles, calendars, screens — drawn on a
// canvas, never a photograph. Each one: tipo → { w, h, draw(ctx, w, h, tex, seed) }. Read by src/objetos.js (textura).
// (No «export { … }» anywhere: the game's packer, tools/build.py, only understands export const/function/class.)
export const TEXTURAS = {
  vivienda_etiqueta_a: { w: 128, h: 128, draw(ctx, w, h, tex) {
    ctx.fillStyle = '#e7e0cf'; ctx.fillRect(0,0,w,h);
    ctx.fillStyle = '#667a70'; ctx.fillRect(0,0,w,16);
    ctx.fillStyle = '#454c49'; ctx.font = 'bold 14px sans-serif'; ctx.textAlign = 'center';
    const palabras = (tex.titulo || 'Hogar').split(' ');
    palabras.slice(0,4).forEach((p,i)=>ctx.fillText(p,w/2,39+i*20,w-10));
  } },
};
