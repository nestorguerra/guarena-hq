// The objects of the interiors as data (technical backlog, I-02 / X-01): each one is a handful of primitives —
// boxes, cylinders, spheres, cones and textured planes — written in data/objetos/*.json (tools/interiores), in its own
// frame: x across, y up from its foot, z out of its front. Here they become geometry: one batch of vertex-coloured
// meshes per material family (matte, metal, glass, lit), and a mesh of its own for each picture, slate or screen.
import * as THREE from 'three';
import { mergeGeometries } from 'three/addons/utils/BufferGeometryUtils.js';
import { OBJETOS } from './interiores_datos.js';
import { pictureTexture } from './housekit.js';
import { mulberry32 } from './util.js';
import { TEXTURAS as TEX_COMERCIO } from './texturas/comercio.js';
import { TEXTURAS as TEX_SERVICIOS } from './texturas/servicios.js';
import { TEXTURAS as TEX_TIENDAS_A } from './texturas/tiendas_a.js';
import { TEXTURAS as TEX_TIENDAS_B } from './texturas/tiendas_b.js';
import { TEXTURAS as TEX_VIVIENDA_A } from './texturas/vivienda_a.js';
import { TEXTURAS as TEX_VIVIENDA_B } from './texturas/vivienda_b.js';

const TEX_FAMILIAS = { ...TEX_COMERCIO, ...TEX_SERVICIOS, ...TEX_TIENDAS_A, ...TEX_TIENDAS_B, ...TEX_VIVIENDA_A, ...TEX_VIVIENDA_B };

const DEG = Math.PI / 180;
const FAMILIA = { metal: 'metal', cristal: 'cristal' };
const RECORTE = new Set(['diana']); // (pictures clear outside their shape)
// the extents of an object in its own frame, from its parts: { x0, x1, y0, y1, z0, z1 }
const BB = new Map();
export function caja(id) {
  if (BB.has(id)) return BB.get(id);
  const o = OBJETOS[id];
  const b = { x0: Infinity, x1: -Infinity, y0: Infinity, y1: -Infinity, z0: Infinity, z1: -Infinity };
  const v = new THREE.Vector3();
  for (const p of o.partes) {
    const g = parteGeo(p, true);
    g.computeBoundingBox();
    const bb = g.boundingBox;
    for (const x of [bb.min.x, bb.max.x]) for (const y of [bb.min.y, bb.max.y]) for (const z of [bb.min.z, bb.max.z]) {
      v.set(x, y, z);
      b.x0 = Math.min(b.x0, v.x); b.x1 = Math.max(b.x1, v.x); b.y0 = Math.min(b.y0, v.y); b.y1 = Math.max(b.y1, v.y); b.z0 = Math.min(b.z0, v.z); b.z1 = Math.max(b.z1, v.z);
    }
    g.dispose();
  }
  b.w = b.x1 - b.x0; b.h = b.y1 - b.y0; b.d = b.z1 - b.z0;
  BB.set(id, b);
  return b;
}

// one part as geometry in the object's frame
function parteGeo(p, bare = false) {
  let g;
  const d = p.d;
  if (p.f === 'caja') g = new THREE.BoxGeometry(d[0], d[1], d[2]);
  else if (p.f === 'cil') g = new THREE.CylinderGeometry(d[0], d[1], d[2], p.seg || 12);
  else if (p.f === 'esfera') g = new THREE.SphereGeometry(d[0], 12, 8);
  else if (p.f === 'cono') g = new THREE.ConeGeometry(d[0], d[1], p.seg || 14, 1, false);
  else g = new THREE.PlaneGeometry(d[0], d[1]);
  if (p.s) g.scale(p.s[0], p.s[1], p.s[2]);
  if (p.r) g.applyMatrix4(new THREE.Matrix4().makeRotationFromEuler(new THREE.Euler(p.r[0] * DEG, p.r[1] * DEG, p.r[2] * DEG)));
  g.translate(p.p[0], p.p[1], p.p[2]);
  if (bare) return g;
  return g.index ? g.toNonIndexed() : g;
}

// ---------------------------------------------------------------- the pictures, slates and screens
const TEX = new Map();
function canvasTex(key, w, h, draw) {
  if (TEX.has(key)) return TEX.get(key);
  const c = document.createElement('canvas'); c.width = w; c.height = h;
  draw(c.getContext('2d'), w, h);
  const t = new THREE.CanvasTexture(c); t.colorSpace = THREE.SRGBColorSpace; t.anisotropy = 4;
  TEX.set(key, t);
  return t;
}
function textura(tex, seed) {
  const k = tex.tipo;
  if (TEX_FAMILIAS[k]) { const T = TEX_FAMILIAS[k]; return canvasTex(k + ':' + JSON.stringify(tex), T.w || 256, T.h || 256, (x, w, h) => T.draw(x, w, h, tex, seed)); }
  if (k === 'paisaje' || k === 'foto' || k === 'calendario') {
    const key = k + ':' + (seed % 5);
    if (!TEX.has(key)) TEX.set(key, pictureTexture(k, seed % 5 + 1)); // (housekit's: already a texture)
    return TEX.get(key);
  }
  if (k === 'pizarra') return canvasTex('pizarra:' + (tex.lineas || []).join('|'), 512, 340, (x, w, h) => {
    x.fillStyle = '#20261f'; x.fillRect(0, 0, w, h);
    x.fillStyle = 'rgba(255,255,255,0.06)'; for (let i = 0; i < 40; i++) x.fillRect(Math.random() * w, Math.random() * h, 40, 2);
    x.fillStyle = '#f2efe4'; x.font = 'bold 34px "Comic Sans MS", "Marker Felt", cursive'; x.textBaseline = 'top';
    (tex.lineas || []).forEach((l, i) => { const [a, b] = l.split(/\s{2,}/); x.textAlign = 'left'; x.fillText(a, 26, 22 + i * 52); if (b) { x.textAlign = 'right'; x.fillStyle = '#f2d27a'; x.fillText(b + ' €', w - 24, 22 + i * 52); x.fillStyle = '#f2efe4'; } });
  });
  if (k === 'menu_dia') return canvasTex('menu', 256, 360, (x, w, h) => {
    x.fillStyle = '#23281f'; x.fillRect(0, 0, w, h); x.fillStyle = '#f2efe4'; x.textAlign = 'center';
    x.font = 'bold 30px "Marker Felt", cursive'; x.fillText('MENÚ DEL DÍA', w / 2, 46);
    x.font = '22px "Marker Felt", cursive'; ['Migas extremeñas', 'Caldereta', 'Ensalada', '— · —', 'Pan, vino y postre', '11 €'].forEach((t, i) => x.fillText(t, w / 2, 100 + i * 42));
  });
  if (k === 'pantalla') return canvasTex('pantalla', 256, 144, (x, w, h) => {
    x.fillStyle = '#2f7a34'; x.fillRect(0, 0, w, h); x.strokeStyle = '#e8f2e0'; x.lineWidth = 2;
    x.strokeRect(10, 10, w - 20, h - 20); x.beginPath(); x.moveTo(w / 2, 10); x.lineTo(w / 2, h - 10); x.stroke(); x.beginPath(); x.arc(w / 2, h / 2, 18, 0, 7); x.stroke();
    x.fillStyle = '#101010'; x.fillRect(8, 8, 90, 20); x.fillStyle = '#fff'; x.font = 'bold 13px Arial'; x.fillText('GUA 1 - 0 VVA', 12, 23);
  });
  if (k === 'reloj') return canvasTex('reloj', 128, 128, (x, w) => {
    x.fillStyle = '#f6f2e6'; x.fillRect(0, 0, w, w); x.strokeStyle = '#222'; x.lineWidth = 6; x.beginPath(); x.arc(64, 64, 58, 0, 7); x.stroke();
    for (let i = 0; i < 12; i++) { const a = (i / 12) * Math.PI * 2; x.fillStyle = '#222'; x.fillRect(64 + Math.sin(a) * 48 - 2, 64 - Math.cos(a) * 48 - 2, 4, 4); }
    x.lineWidth = 4; x.beginPath(); x.moveTo(64, 64); x.lineTo(64, 28); x.moveTo(64, 64); x.lineTo(90, 70); x.stroke();
  });
  if (k === 'cartel_fiesta') return canvasTex('cartel', 192, 288, (x, w, h) => {
    x.fillStyle = '#f2e2b0'; x.fillRect(0, 0, w, h); x.fillStyle = '#b8302a'; x.fillRect(0, 0, w, 60);
    x.fillStyle = '#f2e2b0'; x.font = 'bold 22px Georgia'; x.textAlign = 'center'; x.fillText('FERIA DE', w / 2, 26); x.fillText('SAN GREGORIO', w / 2, 52);
    x.fillStyle = '#3a2a1a'; x.beginPath(); x.ellipse(w / 2, 160, 60, 40, 0, 0, 7); x.fill();
    x.font = '16px Georgia'; x.fillText('Guareña · Mayo', w / 2, 260);
  });
  if (k === 'tragaperras') return canvasTex('tragaperras', 192, 192, (x, w) => {
    x.fillStyle = '#1a0a2a'; x.fillRect(0, 0, w, w); const col = ['#e8302a', '#f2c230', '#3ab04a'];
    for (let i = 0; i < 3; i++) { x.fillStyle = '#f6f2e6'; x.fillRect(16 + i * 58, 60, 50, 70); x.fillStyle = col[i]; x.beginPath(); x.arc(41 + i * 58, 95, 16, 0, 7); x.fill(); }
    x.fillStyle = '#f2c230'; x.font = 'bold 22px Arial'; x.textAlign = 'center'; x.fillText('¡BONUS!', w / 2, 36);
  });
  if (k === 'diana') return canvasTex('diana', 256, 256, (x, w) => { // (a dartboard: its twenty wedges, the doubles and trebles; clear outside)
    const c = w / 2;
    x.clearRect(0, 0, w, w);
    x.fillStyle = '#141414'; x.beginPath(); x.arc(c, c, c - 2, 0, 7); x.fill();
    for (let i = 0; i < 20; i++) {
      const a0 = ((i - 0.5) / 20) * Math.PI * 2 - Math.PI / 2, a1 = ((i + 0.5) / 20) * Math.PI * 2 - Math.PI / 2;
      for (const [r0, r1, col] of [[0, 0.78, i % 2 ? '#efe2c0' : '#1a1a1a'], [0.78, 0.84, i % 2 ? '#2a8a3a' : '#c8202a'], [0.46, 0.52, i % 2 ? '#2a8a3a' : '#c8202a']]) {
        x.fillStyle = col; x.beginPath(); x.arc(c, c, r1 * (c - 18), a0, a1); x.arc(c, c, r0 * (c - 18), a1, a0, true); x.closePath(); x.fill();
      }
    }
    x.fillStyle = '#2a8a3a'; x.beginPath(); x.arc(c, c, 12, 0, 7); x.fill(); x.fillStyle = '#c8202a'; x.beginPath(); x.arc(c, c, 5, 0, 7); x.fill();
  });
  if (k === 'futbolin') return canvasTex('futbolin', 256, 128, (x, w, h) => {
    x.fillStyle = '#2f8a3a'; x.fillRect(0, 0, w, h); x.strokeStyle = '#eef6e8'; x.lineWidth = 2;
    x.strokeRect(6, 6, w - 12, h - 12); x.beginPath(); x.moveTo(w / 2, 6); x.lineTo(w / 2, h - 6); x.stroke(); x.beginPath(); x.arc(w / 2, h / 2, 16, 0, 7); x.stroke();
    x.strokeRect(6, h / 2 - 24, 22, 48); x.strokeRect(w - 28, h / 2 - 24, 22, 48);
  });
  if (k === 'periodico') return canvasTex('periodico', 128, 170, (x, w, h) => {
    x.fillStyle = '#ece8dc'; x.fillRect(0, 0, w, h); x.fillStyle = '#222'; x.font = 'bold 16px Georgia'; x.fillText('HOY', 8, 20);
    for (let i = 0; i < 14; i++) x.fillRect(8, 32 + i * 9, i % 5 === 0 ? 70 : 110, 3);
  });
  return null;
}

// ---------------------------------------------------------------- a batch of placed objects → meshes
const MATS = {};
function mat(f) {
  if (MATS[f]) return MATS[f];
  return (MATS[f] = f === 'metal' ? new THREE.MeshStandardMaterial({ vertexColors: true, roughness: 0.38, metalness: 0.55 })
    : f === 'cristal' ? new THREE.MeshStandardMaterial({ vertexColors: true, roughness: 0.08, metalness: 0.1, transparent: true, opacity: 0.45, depthWrite: false })
      : f.startsWith('luz') ? new THREE.MeshStandardMaterial({ vertexColors: true, roughness: 0.4, emissive: new THREE.Color(f.slice(4) || '#ffffff'), emissiveIntensity: 0.9 }) // (it glows its own colour: a bulb white, a screen blue, a pilot red)
        : new THREE.MeshStandardMaterial({ vertexColors: true, roughness: 0.78, metalness: 0 }));
}
const _c = new THREE.Color();
// items: [{ obj, x, y, z, ry, seed, paleta? }] in world metres → THREE.Group. paleta (a house's style): { tela, madera }
// colour the parts marked tinte 'tela' (one of the fabrics, the same for all of a piece) or 'madera'. A part marked aparte
// is a mesh of its own (the telly's screen, switched on and off): group.userData.aparte = [{ i (the item), mesh }]
export function construir(items) {
  const bins = { mate: [], metal: [], cristal: [] }, extra = [], aparte = [];
  const M = new THREE.Matrix4(), Q = new THREE.Quaternion(), S = new THREE.Vector3(1, 1, 1), P = new THREE.Vector3(), Y = new THREE.Vector3(0, 1, 0);
  for (const [ii, it] of items.entries()) {
    const o = OBJETOS[it.obj];
    if (!o) continue;
    Q.setFromAxisAngle(Y, it.ry || 0); P.set(it.x, it.y || 0, it.z); M.compose(P, Q, S);
    for (const p of o.partes) {
      if (p.tex) {
        const t = textura(it.titulo && p.tex.rotulo_local ? { ...p.tex, titulo: it.titulo } : p.tex, it.seed || 1); // (a sign of the business: its own name)
        if (t) {
          const g = parteGeo(p); g.applyMatrix4(M);
          const m = new THREE.Mesh(g, new THREE.MeshStandardMaterial({ map: t, roughness: 0.7, alphaTest: RECORTE.has(p.tex.tipo) ? 0.5 : 0, emissive: p.luz ? 0xffffff : 0x000000, emissiveMap: p.luz ? t : null, emissiveIntensity: p.luz ? 0.5 : 0, side: p.f === 'plano' ? THREE.FrontSide : THREE.FrontSide }));
          m.castShadow = false; m.receiveShadow = true; extra.push(m);
          continue;
        }
      }
      const g = parteGeo(p); g.applyMatrix4(M);
      const pal = it.paleta, col0 = pal && p.tinte === 'tela' && pal.tela && pal.tela.length ? pal.tela[(it.seed || 0) % pal.tela.length] : pal && p.tinte === 'madera' && pal.madera ? pal.madera : p.c;
      if (p.aparte) { // (its own mesh and material: the screen)
        const m = new THREE.Mesh(g, new THREE.MeshStandardMaterial({ color: new THREE.Color(col0 || '#202020'), emissive: 0x6a8aa8, emissiveIntensity: 0, roughness: 0.3 }));
        extra.push(m); aparte.push({ i: ii, mesh: m });
        continue;
      }
      _c.set(col0 || '#888888').convertSRGBToLinear();
      const n = g.attributes.position.count, col = new Float32Array(n * 3);
      for (let i = 0; i < n; i++) { col[i * 3] = _c.r; col[i * 3 + 1] = _c.g; col[i * 3 + 2] = _c.b; }
      g.setAttribute('color', new THREE.BufferAttribute(col, 3));
      if (g.attributes.uv) g.deleteAttribute('uv');
      const f = p.luz ? 'luz:' + (p.c || '#ffffff').toLowerCase() : FAMILIA[p.m] || 'mate';
      (bins[f] = bins[f] || []).push(g);
    }
  }
  const group = new THREE.Group();
  for (const [f, list] of Object.entries(bins)) {
    if (!list.length) continue;
    const m = new THREE.Mesh(mergeGeometries(list, false), mat(f));
    m.castShadow = f !== 'cristal' && !f.startsWith('luz'); m.receiveShadow = true;
    group.add(m);
  }
  for (const m of extra) group.add(m);
  group.userData.aparte = aparte;
  return group;
}

// the colour of a light of so many kelvin (Tanner Helland's fit), for the lamps of an interior
export function kelvin(k) {
  const t = k / 100;
  let r, g, b;
  if (t <= 66) { r = 255; g = 99.4708025861 * Math.log(t) - 161.1195681661; b = t <= 19 ? 0 : 138.5177312231 * Math.log(t - 10) - 305.0447927307; }
  else { r = 329.698727446 * Math.pow(t - 60, -0.1332047592); g = 288.1221695283 * Math.pow(t - 60, -0.0755148492); b = 255; }
  const c = (v) => Math.max(0, Math.min(255, v)) / 255;
  return new THREE.Color(c(r), c(g), c(b));
}
