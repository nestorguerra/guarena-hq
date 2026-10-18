// Painted pictures for the objects of the «tiendas_b» family (data/objetos): signs, screens, posters, paintings — drawn on a
// canvas, never a photograph. Each one: tipo → { w, h, draw(ctx, w, h, tex, seed) } (tex: the part's own tex, its words…;
// a sign marked rotulo_local gets tex.titulo, the name of the business it hangs in). Read by src/objetos.js (textura).
// Every textured part instance is a mesh of its own: a handful per room. No real brand anywhere: invented names, plain shapes.
// (the tex of a part with `rotulo_local` is `{ tipo, estilo, rotulo_local: true }`; the others carry their own `dibujo`/`estilo`)

const FUENTE = '"Helvetica Neue", Arial, sans-serif';
const SERIF = 'Georgia, "Times New Roman", serif';
function redondo(x, X, Y, w, h, r) {
  x.beginPath(); x.moveTo(X + r, Y); x.arcTo(X + w, Y, X + w, Y + h, r); x.arcTo(X + w, Y + h, X, Y + h, r); x.arcTo(X, Y + h, X, Y, r); x.arcTo(X, Y, X + w, Y, r); x.closePath();
}
// a text that shrinks to fit a width
function ajustado(x, texto, cx, cy, ancho, tam, peso = 'bold', fam = FUENTE) {
  let s = tam;
  x.font = `${peso} ${s}px ${fam}`;
  while (x.measureText(texto).width > ancho && s > 8) { s -= 2; x.font = `${peso} ${s}px ${fam}`; }
  x.fillText(texto, cx, cy);
}
function circulo(x, cx, cy, r, c) { x.fillStyle = c; x.beginPath(); x.arc(cx, cy, r, 0, 7); x.fill(); }
function elipse(x, cx, cy, rx, ry, c, rot = 0) { x.fillStyle = c; x.beginPath(); x.ellipse(cx, cy, rx, ry, rot, 0, 7); x.fill(); }
function poly(x, pts, c) { x.fillStyle = c; x.beginPath(); pts.forEach(([a, b], i) => (i ? x.lineTo(a, b) : x.moveTo(a, b))); x.closePath(); x.fill(); }
// a small deterministic random (the same picture for the same seed)
function azar(seed) { let s = (seed * 2654435761) >>> 0 || 1; return () => { s ^= s << 13; s >>>= 0; s ^= s >>> 17; s ^= s << 5; s >>>= 0; return s / 4294967296; }; }

// ---------------------------------------------------------------- the shop's own sign: its name on a plate
const ROTULOS = {
  muebles: { fondo: '#4a3626', color: '#f1e6cf', sub: 'Muebles · Decoración · Hogar', fam: SERIF, marco: '#c9a96a' },
  electro: { fondo: '#1f4e8c', color: '#ffffff', sub: 'Electrodomésticos · Imagen y sonido', fam: FUENTE, marco: '#f2c230' },
  informatica: { fondo: '#14243a', color: '#7fe0ff', sub: 'Informática · Móviles · Reparaciones', fam: FUENTE, marco: '#3a7aa8' },
  panaderia: { fondo: '#7a4a22', color: '#f6e3b8', sub: 'Pan y repostería artesana', fam: SERIF, marco: '#d9a85a' },
  fruteria: { fondo: '#2f7a3a', color: '#ffffff', sub: 'Frutas y verduras del día', fam: FUENTE, marco: '#d9e26a' },
  perfumeria: { fondo: '#1a1a1e', color: '#e8c97a', sub: 'Perfumería · Belleza · Cosmética', fam: SERIF, marco: '#e8c97a' },
  peluqueria: { fondo: '#2a2a2e', color: '#f4b6c8', sub: 'Peluquería y estética', fam: SERIF, marco: '#f4b6c8' },
  taller: { fondo: '#0f3d6e', color: '#ffd23a', sub: 'Mecánica · Electricidad · Neumáticos', fam: FUENTE, marco: '#ffd23a' },
};

// ---------------------------------------------------------------- posters: a flat drawing and a few words
const CARTELES = {
  peinado_a: { titulo: 'Melena y ondas', fondo: '#f1d9d2', dib(x, w, h) { // a head with long wavy hair, seen from the front
    poly(x, [[w * 0.28, h * 0.3], [w * 0.72, h * 0.3], [w * 0.8, h * 0.82], [w * 0.2, h * 0.82]], '#6a4426');
    for (let i = 0; i < 5; i++) { x.strokeStyle = '#8a5a34'; x.lineWidth = 5; x.beginPath(); x.moveTo(w * (0.26 + i * 0.12), h * 0.5); x.bezierCurveTo(w * (0.2 + i * 0.12), h * 0.62, w * (0.32 + i * 0.12), h * 0.72, w * (0.24 + i * 0.12), h * 0.82); x.stroke(); }
    elipse(x, w / 2, h * 0.36, w * 0.17, h * 0.15, '#e8c9b0'); elipse(x, w / 2, h * 0.27, w * 0.2, h * 0.1, '#6a4426');
    x.fillStyle = '#3a2a22'; x.fillRect(w * 0.42, h * 0.36, 8, 4); x.fillRect(w * 0.55, h * 0.36, 8, 4); x.strokeStyle = '#b86a6a'; x.lineWidth = 3; x.beginPath(); x.arc(w / 2, h * 0.43, 9, 0.2, 2.9); x.stroke(); } },
  peinado_b: { titulo: 'Recogidos de fiesta', fondo: '#d8d2e6', dib(x, w, h) { // an updo: a bun on top of a face
    circulo(x, w / 2, h * 0.19, w * 0.08, '#2e2a2a'); elipse(x, w / 2, h * 0.3, w * 0.2, h * 0.1, '#2e2a2a'); elipse(x, w / 2, h * 0.4, w * 0.16, h * 0.14, '#e8c9b0');
    elipse(x, w / 2, h * 0.31, w * 0.17, h * 0.07, '#2e2a2a'); x.fillStyle = '#3a2a22'; x.fillRect(w * 0.43, h * 0.39, 7, 4); x.fillRect(w * 0.54, h * 0.39, 7, 4);
    x.fillStyle = '#e8c9b0'; x.fillRect(w * 0.46, h * 0.53, w * 0.08, h * 0.06); poly(x, [[w * 0.22, h * 0.9], [w * 0.78, h * 0.9], [w * 0.66, h * 0.6], [w * 0.34, h * 0.6]], '#b3547a'); circulo(x, w * 0.6, h * 0.19, 5, '#e8c97a'); } },
  pan: { titulo: 'Pan de leña', fondo: '#f0dfc2', dib(x, w, h) {
    elipse(x, w * 0.35, h * 0.55, w * 0.22, h * 0.13, '#c8883a'); elipse(x, w * 0.66, h * 0.62, w * 0.2, h * 0.12, '#b8782e'); poly(x, [[w * 0.18, h * 0.8], [w * 0.82, h * 0.8], [w * 0.78, h * 0.86], [w * 0.22, h * 0.86]], '#8a5a2a');
    x.strokeStyle = '#e8c07a'; x.lineWidth = 4; for (let i = 0; i < 3; i++) { x.beginPath(); x.moveTo(w * (0.24 + i * 0.1), h * 0.48); x.lineTo(w * (0.28 + i * 0.1), h * 0.6); x.stroke(); } } },
  tarta: { titulo: 'Tartas por encargo', fondo: '#f4d6dc', dib(x, w, h) {
    x.fillStyle = '#e8c07a'; redondo(x, w * 0.22, h * 0.52, w * 0.56, h * 0.24, 8); x.fill(); x.fillStyle = '#fff4e8'; redondo(x, w * 0.22, h * 0.44, w * 0.56, h * 0.12, 8); x.fill();
    for (let i = 0; i < 4; i++) circulo(x, w * (0.3 + i * 0.13), h * 0.4, 9, '#c0302a'); for (let i = 0; i < 3; i++) { x.fillStyle = '#f2d060'; x.fillRect(w * (0.35 + i * 0.15), h * 0.3, 6, h * 0.1); circulo(x, w * (0.35 + i * 0.15) + 3, h * 0.28, 5, '#ff9a2a'); } } },
  fruta: { titulo: 'Fruta de temporada', fondo: '#e4efc8', dib(x, w, h) {
    circulo(x, w * 0.36, h * 0.52, w * 0.16, '#d8382a'); circulo(x, w * 0.64, h * 0.54, w * 0.16, '#f08a20'); circulo(x, w * 0.5, h * 0.4, w * 0.13, '#9ab83a');
    x.fillStyle = '#4a7a2a'; x.fillRect(w * 0.355, h * 0.32, 5, 14); elipse(x, w * 0.46, h * 0.28, 12, 6, '#4a7a2a', -0.4); } },
  perfume: { titulo: 'Fragancias de autor', fondo: '#e9e2f0', dib(x, w, h) {
    x.fillStyle = '#b3547a'; redondo(x, w * 0.3, h * 0.4, w * 0.4, h * 0.38, 12); x.fill(); x.fillStyle = '#f4d6e2'; redondo(x, w * 0.36, h * 0.46, w * 0.28, h * 0.12, 6); x.fill();
    x.fillStyle = '#e8c97a'; x.fillRect(w * 0.44, h * 0.3, w * 0.12, h * 0.1); x.fillStyle = '#2b2b2e'; x.fillRect(w * 0.41, h * 0.24, w * 0.18, h * 0.07); } },
  neumatico: { titulo: 'Neumáticos al mejor precio', fondo: '#dde6ee', dib(x, w, h) {
    circulo(x, w / 2, h * 0.5, w * 0.3, '#2e2e32'); circulo(x, w / 2, h * 0.5, w * 0.18, '#c3c7ca'); circulo(x, w / 2, h * 0.5, w * 0.06, '#5a5e62');
    x.strokeStyle = '#4a4a50'; x.lineWidth = 5; for (let i = 0; i < 16; i++) { const a = (i / 16) * Math.PI * 2; x.beginPath(); x.moveTo(w / 2 + Math.cos(a) * w * 0.26, h * 0.5 + Math.sin(a) * w * 0.26); x.lineTo(w / 2 + Math.cos(a) * w * 0.3, h * 0.5 + Math.sin(a) * w * 0.3); x.stroke(); } } },
  coche: { titulo: 'Revisión pre-ITV', fondo: '#e6eef2', dib(x, w, h) {
    poly(x, [[w * 0.15, h * 0.62], [w * 0.22, h * 0.48], [w * 0.38, h * 0.4], [w * 0.62, h * 0.4], [w * 0.8, h * 0.5], [w * 0.88, h * 0.62]], '#2c5aa0'); x.fillStyle = '#2c5aa0'; x.fillRect(w * 0.15, h * 0.6, w * 0.73, h * 0.08);
    poly(x, [[w * 0.28, h * 0.5], [w * 0.4, h * 0.43], [w * 0.5, h * 0.43], [w * 0.5, h * 0.5]], '#cfe3ea'); poly(x, [[w * 0.53, h * 0.43], [w * 0.62, h * 0.43], [w * 0.74, h * 0.5], [w * 0.53, h * 0.5]], '#cfe3ea');
    circulo(x, w * 0.3, h * 0.7, w * 0.07, '#2e2e32'); circulo(x, w * 0.74, h * 0.7, w * 0.07, '#2e2e32'); circulo(x, w * 0.3, h * 0.7, w * 0.03, '#c3c7ca'); circulo(x, w * 0.74, h * 0.7, w * 0.03, '#c3c7ca'); } },
  nevera: { titulo: 'Frío que dura', fondo: '#dcebf4', dib(x, w, h) {
    x.fillStyle = '#e9eef0'; redondo(x, w * 0.3, h * 0.2, w * 0.4, h * 0.62, 8); x.fill(); x.fillStyle = '#9aa7ad'; x.fillRect(w * 0.3, h * 0.44, w * 0.4, 4); x.fillRect(w * 0.62, h * 0.3, 5, h * 0.1); x.fillRect(w * 0.62, h * 0.52, 5, h * 0.18); } },
  lavadora: { titulo: 'Lavadoras de carga frontal', fondo: '#e2eaf4', dib(x, w, h) {
    x.fillStyle = '#f2f4f5'; redondo(x, w * 0.28, h * 0.2, w * 0.44, h * 0.6, 8); x.fill(); circulo(x, w / 2, h * 0.55, w * 0.15, '#9aa7ad'); circulo(x, w / 2, h * 0.55, w * 0.11, '#7aa0c8'); x.fillStyle = '#4a6a8a'; x.fillRect(w * 0.32, h * 0.25, w * 0.1, 8); circulo(x, w * 0.64, h * 0.27, 7, '#c0302a'); } },
  tv: { titulo: 'Tu tele, más grande', fondo: '#161a22', dib(x, w, h) {
    x.fillStyle = '#2b2f3a'; redondo(x, w * 0.14, h * 0.28, w * 0.72, h * 0.4, 6); x.fill(); const g = x.createLinearGradient(0, h * 0.3, w, h * 0.66); g.addColorStop(0, '#3a6ea5'); g.addColorStop(1, '#e0a84a'); x.fillStyle = g; x.fillRect(w * 0.17, h * 0.31, w * 0.66, h * 0.34); x.fillStyle = '#5a5f6a'; x.fillRect(w * 0.44, h * 0.68, w * 0.12, 10); x.fillRect(w * 0.36, h * 0.7, w * 0.28, 6); }, claro: true },
  movil: { titulo: 'Móviles libres', fondo: '#e0f0f4', dib(x, w, h) {
    x.fillStyle = '#2a2e38'; redondo(x, w * 0.34, h * 0.2, w * 0.32, h * 0.6, 12); x.fill(); const g = x.createLinearGradient(0, h * 0.24, 0, h * 0.74); g.addColorStop(0, '#5ab0e0'); g.addColorStop(1, '#2c5aa0'); x.fillStyle = g; x.fillRect(w * 0.37, h * 0.25, w * 0.26, h * 0.5); circulo(x, w / 2, h * 0.77, 5, '#5a5e68'); } },
  portatil: { titulo: 'Portátiles desde 299 €', fondo: '#e8edf5', dib(x, w, h) {
    x.fillStyle = '#2a2e38'; redondo(x, w * 0.24, h * 0.28, w * 0.52, h * 0.32, 5); x.fill(); x.fillStyle = '#7aa0d0'; x.fillRect(w * 0.26, h * 0.3, w * 0.48, h * 0.28); poly(x, [[w * 0.18, h * 0.66], [w * 0.82, h * 0.66], [w * 0.76, h * 0.62], [w * 0.24, h * 0.62]], '#9aa0aa'); } },
  sofa: { titulo: 'Sofás a medida', fondo: '#efe4d4', dib(x, w, h) {
    x.fillStyle = '#7a8a6a'; redondo(x, w * 0.18, h * 0.42, w * 0.64, h * 0.18, 10); x.fill(); redondo(x, w * 0.12, h * 0.5, w * 0.12, h * 0.22, 8); x.fill(); redondo(x, w * 0.76, h * 0.5, w * 0.12, h * 0.22, 8); x.fill();
    x.fillStyle = '#8c9c7c'; redondo(x, w * 0.22, h * 0.54, w * 0.56, h * 0.14, 8); x.fill(); x.fillStyle = '#5a3a22'; x.fillRect(w * 0.18, h * 0.72, 6, 12); x.fillRect(w * 0.78, h * 0.72, 6, 12); } },
  cama: { titulo: 'Descanso para toda la familia', fondo: '#e4e6f0', dib(x, w, h) {
    x.fillStyle = '#8a6a46'; x.fillRect(w * 0.16, h * 0.34, w * 0.1, h * 0.38); x.fillStyle = '#f2efe6'; redondo(x, w * 0.24, h * 0.5, w * 0.6, h * 0.16, 6); x.fill(); x.fillStyle = '#6a8ab0'; redondo(x, w * 0.4, h * 0.5, w * 0.44, h * 0.16, 6); x.fill();
    x.fillStyle = '#f8f6ee'; redondo(x, w * 0.27, h * 0.44, w * 0.18, h * 0.08, 6); x.fill(); x.fillStyle = '#5a3a22'; x.fillRect(w * 0.82, h * 0.58, 6, h * 0.14); } },
  oferta: { titulo: 'Ofertas de temporada', fondo: '#c0302a', dib(x, w, h) {
    x.fillStyle = '#f6efe0'; x.textAlign = 'center'; x.textBaseline = 'middle'; x.font = `bold ${Math.round(w * 0.3)}px ${FUENTE}`; x.fillText('-20%', w / 2, h * 0.5); }, claro: true },
};

// ---------------------------------------------------------------- screens (all invented: a landscape, a pitch, a news desk…)
const PANTALLAS = {
  paisaje(x, w, h) { const g = x.createLinearGradient(0, 0, 0, h); g.addColorStop(0, '#5ab0e8'); g.addColorStop(0.6, '#c9e6f2'); x.fillStyle = g; x.fillRect(0, 0, w, h); poly(x, [[0, h * 0.7], [w * 0.3, h * 0.4], [w * 0.55, h * 0.7]], '#6a8a6a'); poly(x, [[w * 0.35, h * 0.7], [w * 0.7, h * 0.32], [w, h * 0.7]], '#4a7a5a'); x.fillStyle = '#3a8a3a'; x.fillRect(0, h * 0.7, w, h * 0.3); circulo(x, w * 0.82, h * 0.2, h * 0.09, '#fff3a8'); },
  futbol(x, w, h) { x.fillStyle = '#2f7a34'; x.fillRect(0, 0, w, h); x.strokeStyle = '#e8f2e0'; x.lineWidth = 2; x.strokeRect(8, 8, w - 16, h - 16); x.beginPath(); x.moveTo(w / 2, 8); x.lineTo(w / 2, h - 8); x.stroke(); x.beginPath(); x.arc(w / 2, h / 2, h * 0.16, 0, 7); x.stroke(); x.strokeRect(8, h * 0.3, w * 0.12, h * 0.4); x.strokeRect(w - 8 - w * 0.12, h * 0.3, w * 0.12, h * 0.4); x.fillStyle = '#101010'; x.fillRect(8, 8, w * 0.34, h * 0.14); x.fillStyle = '#fff'; x.font = `bold ${Math.round(h * 0.1)}px ${FUENTE}`; x.textAlign = 'left'; x.fillText('GUA 1 - 0 VVA', 12, h * 0.17); },
  noticias(x, w, h) { x.fillStyle = '#1c2a44'; x.fillRect(0, 0, w, h); x.fillStyle = '#e8e0d0'; x.fillRect(w * 0.1, h * 0.55, w * 0.8, h * 0.1); circulo(x, w * 0.5, h * 0.32, h * 0.12, '#d8b49a'); x.fillStyle = '#2a3a5a'; redondo(x, w * 0.38, h * 0.42, w * 0.24, h * 0.16, 6); x.fill(); x.fillStyle = '#c0302a'; x.fillRect(0, h * 0.8, w, h * 0.12); x.fillStyle = '#fff'; x.font = `bold ${Math.round(h * 0.08)}px ${FUENTE}`; x.textAlign = 'left'; x.fillText('ÚLTIMA HORA · Vegas Altas', 10, h * 0.885); },
  cine(x, w, h) { const g = x.createLinearGradient(0, 0, w, h); g.addColorStop(0, '#3a1c4a'); g.addColorStop(1, '#e0743a'); x.fillStyle = g; x.fillRect(0, 0, w, h); poly(x, [[0, h * 0.8], [w * 0.4, h * 0.5], [w * 0.7, h * 0.8], [w, h * 0.6], [w, h], [0, h]], '#1a1024'); circulo(x, w * 0.7, h * 0.3, h * 0.12, '#ffd27a'); },
  escritorio(x, w, h) { const g = x.createLinearGradient(0, 0, w, h); g.addColorStop(0, '#2a5aa0'); g.addColorStop(1, '#7ac0e8'); x.fillStyle = g; x.fillRect(0, 0, w, h); x.fillStyle = '#e8eef4'; redondo(x, w * 0.12, h * 0.14, w * 0.4, h * 0.46, 6); x.fill(); x.fillStyle = '#5a7aa8'; x.fillRect(w * 0.12, h * 0.14, w * 0.4, h * 0.08); for (let i = 0; i < 4; i++) { x.fillStyle = '#9aa7b8'; x.fillRect(w * 0.16, h * (0.28 + i * 0.07), w * (0.3 - (i % 2) * 0.08), 4); } x.fillStyle = 'rgba(20,30,50,0.85)'; x.fillRect(0, h * 0.92, w, h * 0.08); for (let i = 0; i < 4; i++) { x.fillStyle = ['#e8a020', '#5aa0e0', '#e05a5a', '#7ac07a'][i]; x.fillRect(w * (0.03 + i * 0.05), h * 0.935, w * 0.03, h * 0.04); } },
  movil_a(x, w, h) { const g = x.createLinearGradient(0, 0, w, h); g.addColorStop(0, '#d04a8a'); g.addColorStop(1, '#4a3aa8'); x.fillStyle = g; x.fillRect(0, 0, w, h); for (let i = 0; i < 12; i++) { x.fillStyle = ['#ffd24a', '#5ae0a0', '#5ab0ff', '#ffffff'][i % 4]; redondo(x, w * (0.1 + (i % 4) * 0.22), h * (0.35 + Math.floor(i / 4) * 0.2), w * 0.16, w * 0.16, 6); x.fill(); } x.fillStyle = '#fff'; x.font = `bold ${Math.round(h * 0.12)}px ${FUENTE}`; x.textAlign = 'center'; x.fillText('12:30', w / 2, h * 0.2); },
  movil_b(x, w, h) { x.fillStyle = '#0c1c2c'; x.fillRect(0, 0, w, h); circulo(x, w / 2, h * 0.45, h * 0.3, '#1a4a6a'); circulo(x, w / 2, h * 0.45, h * 0.2, '#2c8ab0'); x.fillStyle = '#fff'; x.font = `bold ${Math.round(h * 0.14)}px ${FUENTE}`; x.textAlign = 'center'; x.fillText('08:15', w / 2, h * 0.9); },
  portatil(x, w, h) { x.fillStyle = '#ece8dd'; x.fillRect(0, 0, w, h); x.fillStyle = '#3a6ea5'; x.fillRect(0, 0, w, h * 0.12); for (let i = 0; i < 9; i++) { x.fillStyle = '#9aa0aa'; x.fillRect(w * 0.08, h * (0.2 + i * 0.08), w * (0.84 - (i % 3) * 0.2), 4); } },
  tablet(x, w, h) { const g = x.createLinearGradient(0, 0, 0, h); g.addColorStop(0, '#f2c85a'); g.addColorStop(1, '#e0743a'); x.fillStyle = g; x.fillRect(0, 0, w, h); for (let i = 0; i < 8; i++) { x.fillStyle = 'rgba(255,255,255,0.8)'; redondo(x, w * (0.08 + (i % 4) * 0.22), h * (0.2 + Math.floor(i / 4) * 0.32), w * 0.17, h * 0.22, 6); x.fill(); } },
  precios(x, w, h) { x.fillStyle = '#10141c'; x.fillRect(0, 0, w, h); x.fillStyle = '#f2c230'; x.font = `bold ${Math.round(h * 0.13)}px ${FUENTE}`; x.textAlign = 'left'; x.fillText('OFERTAS DEL MES', w * 0.05, h * 0.18); x.fillStyle = '#e8eef4'; x.font = `${Math.round(h * 0.1)}px ${FUENTE}`; ['Lavadora 8 kg   349', 'Frigorífico combi   429', 'Tele 43"   279', 'Horno   189', 'Microondas   69'].forEach((l, i) => { const [a, b] = l.split('   '); x.textAlign = 'left'; x.fillText(a, w * 0.05, h * (0.34 + i * 0.14)); x.textAlign = 'right'; x.fillStyle = '#f2c230'; x.fillText(b + ' €', w * 0.95, h * (0.34 + i * 0.14)); x.fillStyle = '#e8eef4'; }); },
  precios_inf(x, w, h) { x.fillStyle = '#0c1a2a'; x.fillRect(0, 0, w, h); x.fillStyle = '#7fe0ff'; x.font = `bold ${Math.round(h * 0.13)}px ${FUENTE}`; x.textAlign = 'left'; x.fillText('OFERTAS DE LA SEMANA', w * 0.05, h * 0.18); x.fillStyle = '#e8eef4'; x.font = `${Math.round(h * 0.1)}px ${FUENTE}`; ['Portátil 15"   449', 'Móvil libre   199', 'Monitor 24"   129', 'Impresora   69', 'Auriculares   25'].forEach((l, i) => { const [a, b] = l.split('   '); x.textAlign = 'left'; x.fillText(a, w * 0.05, h * (0.34 + i * 0.14)); x.textAlign = 'right'; x.fillStyle = '#ffd23a'; x.fillText(b + ' €', w * 0.95, h * (0.34 + i * 0.14)); x.fillStyle = '#e8eef4'; }); },
  radio(x, w, h) { x.fillStyle = '#1a2a1a'; x.fillRect(0, 0, w, h); x.fillStyle = '#7fe07f'; x.font = `bold ${Math.round(h * 0.4)}px "Courier New", monospace`; x.textAlign = 'center'; x.fillText('98.4', w / 2, h * 0.68); },
  apagada(x, w, h) { const g = x.createLinearGradient(0, 0, w, h); g.addColorStop(0, '#1a1c22'); g.addColorStop(0.5, '#2a2e38'); g.addColorStop(1, '#1a1c22'); x.fillStyle = g; x.fillRect(0, 0, w, h); },
};

export const TEXTURAS = {
  // the shop's own sign (its name, given when the room is built): hairdresser, bakery, workshop…
  rotulo_tb: {
    w: 512, h: 128,
    draw(x, w, h, t) {
      const e = ROTULOS[t.estilo] || ROTULOS.muebles;
      x.fillStyle = e.fondo; x.fillRect(0, 0, w, h);
      x.strokeStyle = e.marco; x.lineWidth = 3; x.strokeRect(8, 8, w - 16, h - 16);
      x.fillStyle = e.color; x.textAlign = 'center'; x.textBaseline = 'middle';
      ajustado(x, t.titulo || t.texto || 'Mi tienda', w / 2, e.sub ? h * 0.42 : h / 2, w - 60, 58, 'bold', e.fam);
      if (e.sub) { x.globalAlpha = 0.85; ajustado(x, e.sub, w / 2, h * 0.78, w - 70, 21, 'normal', FUENTE); x.globalAlpha = 1; }
    },
  },
  // a poster: a flat drawing and its title (dibujo: peinado_a, pan, tarta, fruta, perfume, neumatico, coche, nevera, lavadora, tv, movil, portatil, sofa, cama, oferta)
  cartel_tb: {
    w: 256, h: 368,
    draw(x, w, h, t) {
      const c = CARTELES[t.dibujo] || CARTELES.oferta;
      x.fillStyle = c.fondo; x.fillRect(0, 0, w, h);
      x.save(); x.translate(0, 18); x.scale(1, 0.84); c.dib(x, w, h); x.restore();
      x.fillStyle = c.claro ? '#f6efe0' : '#2a2a2e'; x.textAlign = 'center'; x.textBaseline = 'middle';
      ajustado(x, t.titulo || c.titulo, w / 2, h - 44, w - 36, 26, 'bold', SERIF);
      x.strokeStyle = c.claro ? '#f6efe0' : '#2a2a2e'; x.lineWidth = 3; x.strokeRect(8, 8, w - 16, h - 16);
    },
  },
  // a screen: estilo = paisaje, futbol, noticias, cine, escritorio, movil_a, movil_b, portatil, tablet, precios, radio, apagada
  pantalla_tb: {
    w: 256, h: 144,
    draw(x, w, h, t) { (PANTALLAS[t.estilo] || PANTALLAS.apagada)(x, w, h); },
  },
  // a painting for the furniture shop: abstract, a seascape, a still life (never a photograph)
  cuadro_tb: {
    w: 256, h: 192,
    draw(x, w, h, t, seed) {
      const r = azar((t.n || 1) * 977 + 5), e = t.estilo || 'abstracto';
      if (e === 'marina') {
        const g = x.createLinearGradient(0, 0, 0, h); g.addColorStop(0, '#f2d8a8'); g.addColorStop(0.5, '#a8cfe0'); g.addColorStop(0.5, '#3a6a8a'); g.addColorStop(1, '#1c3a56'); x.fillStyle = g; x.fillRect(0, 0, w, h);
        circulo(x, w * 0.7, h * 0.34, 18, '#fff3c8'); poly(x, [[w * 0.2, h * 0.7], [w * 0.5, h * 0.7], [w * 0.45, h * 0.78], [w * 0.25, h * 0.78]], '#8a4a2a'); poly(x, [[w * 0.34, h * 0.7], [w * 0.34, h * 0.4], [w * 0.5, h * 0.66]], '#f2efe6');
      } else if (e === 'bodegon') {
        x.fillStyle = '#4a3a2a'; x.fillRect(0, 0, w, h); x.fillStyle = '#6a4a32'; x.fillRect(0, h * 0.7, w, h * 0.3); circulo(x, w * 0.35, h * 0.62, 22, '#c0302a'); circulo(x, w * 0.5, h * 0.64, 20, '#e0a020'); circulo(x, w * 0.64, h * 0.62, 21, '#7aa03a'); poly(x, [[w * 0.78, h * 0.72], [w * 0.74, h * 0.4], [w * 0.84, h * 0.4], [w * 0.88, h * 0.72]], '#2c5a6a');
      } else if (e === 'flores') {
        x.fillStyle = '#dfe8dc'; x.fillRect(0, 0, w, h); x.fillStyle = '#4a7a4a'; for (let i = 0; i < 6; i++) { x.fillRect(w * (0.2 + i * 0.12), h * 0.45, 3, h * 0.45); } for (let i = 0; i < 6; i++) { const cx = w * (0.2 + i * 0.12) + 1, cy = h * (0.3 + r() * 0.15); for (let k = 0; k < 5; k++) { const a = (k / 5) * 6.28; circulo(x, cx + Math.cos(a) * 11, cy + Math.sin(a) * 11, 8, ['#e06a8a', '#f2c85a', '#c06ae0'][i % 3]); } circulo(x, cx, cy, 6, '#f6efe0'); }
      } else { // abstract: blocks of colour
        const paleta = [['#e8dcc4', '#c0583a', '#2c4a6a', '#e0b050'], ['#e0e6dc', '#4a7a6a', '#d8a050', '#2a3a4a'], ['#f0e0e0', '#8a4a6a', '#3a6a8a', '#e8c090'], ['#dde4ea', '#c08a3a', '#4a5a7a', '#a0b8a0']][(t.n || 1) % 4];
        x.fillStyle = paleta[0]; x.fillRect(0, 0, w, h);
        for (let i = 0; i < 5; i++) { x.fillStyle = paleta[1 + (i % 3)]; x.globalAlpha = 0.85; if (i % 2) circulo(x, w * (0.15 + r() * 0.7), h * (0.2 + r() * 0.6), 20 + r() * 34, paleta[1 + (i % 3)]); else x.fillRect(w * r() * 0.6, h * r() * 0.6, w * (0.2 + r() * 0.3), h * (0.15 + r() * 0.3)); x.globalAlpha = 1; }
      }
    },
  },
};
