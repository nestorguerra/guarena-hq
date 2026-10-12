// The hyperreal zone of Guareña HQ (docs/hiperrealismo.md, the source of truth): the church of Santa María modelled in
// Blender (tools/blender/iglesia.py → assets/hq/iglesia.glb) on the church's own frame as landmarks.js works it out
// (poi.churchFrame), in the Realista look. The old procedural church's masses are hidden; its portals stay, with the
// doors that open as you come and lead inside (churchdoors.js, church.js). The Plastilina keeps its clay church.
// Beside the model, assets/hq/iglesia.json marks what the game must know of it: the buttresses (they stand out of the
// Catastro's outline: they get colliders) and the bells (they swing when they ring).
import * as THREE from 'three';
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';
import { STYLE } from './style.js';
import { loadAssetBytes } from './assets.js';

// A wall's texture repeats every few metres; a whole church front shows the pattern. The stone materials are stained
// in world space — a little darker or warmer here and there, as weather and repairs leave a wall — so no two stretches
// of wall are alike. (Mixing a second, turned reading of the texture was tried: where the two met, ghosts of stones
// showed through each other.)
const MACRO = /* glsl */ `
float hqHash(vec2 p) { return fract(sin(dot(p, vec2(127.1, 311.7))) * 43758.5453); }
float hqNoise(vec2 p) {
  vec2 i = floor(p), f = fract(p); f = f * f * (3.0 - 2.0 * f);
  return mix(mix(hqHash(i), hqHash(i + vec2(1.0, 0.0)), f.x), mix(hqHash(i + vec2(0.0, 1.0)), hqHash(i + vec2(1.0, 1.0)), f.x), f.y);
}
float hqMacro(vec3 p) { vec2 q = vec2(p.x + p.z * 0.7, p.y * 1.3 + p.z * 0.4); return 0.65 * hqNoise(q * 0.13) + 0.35 * hqNoise(q * 0.41 + 7.3); }
`;

// The weathering layer (phase 5a, docs/hiperrealismo.md), worked out in the church's own frame — the GLB's object space
// — from the building's shape, as the Commons photo shows it on the real one:
//  - runoff stains: from the cornice here and there, each its own length; under each gargoyle; from both ends of every
//    window's sill; and the long, greenish one of the north wall, hanging from the first gargoyle down to the foot
//  - the foot: damp and splashed dirt over the plinth and the first metre and a half, ragged, worse on the north
//  - flaked patches on the rubble walls, paler, the west front most
//  - lichen on what looks up (cornices, sills, copings) and on the old tiles
//  - the walls not quite flat: a few centimetres of undulation over a metre or two, in the light
// Where the gargoyles and windows are comes from the model's marks (assets/hq/iglesia.json, «desgaste»).
const WEATHER = /* glsl */ `
varying vec3 vHqFrame;
varying vec3 vHqFrameN;
uniform float uHqKind;   // 0 rubble, 1 the west front's rubble, 2 ashlar, 3 the plinth, 4 tiles
uniform vec4 uHqGarg;    // the gargoyles: the first's x, their spacing, how many a side, their height
uniform vec4 uHqWinX;    // the windows' x
uniform vec4 uHqWinY;    // their sills
uniform vec4 uHqWall;    // the cornice's underside, a window's width, the long stain's x, the north wall's z
float hqH1(float n) { return fract(sin(n * 91.345) * 43758.5453); }
float hqN3(vec3 p) {
  vec3 i = floor(p), f = fract(p); f = f * f * (3.0 - 2.0 * f);
  float n = dot(i, vec3(1.0, 57.0, 113.0));
  return mix(mix(mix(hqH1(n), hqH1(n + 1.0), f.x), mix(hqH1(n + 57.0), hqH1(n + 58.0), f.x), f.y),
             mix(mix(hqH1(n + 113.0), hqH1(n + 114.0), f.x), mix(hqH1(n + 170.0), hqH1(n + 171.0), f.x), f.y), f.z);
}
float hqFbm3(vec3 p) { float s = 0.0, a = 0.5; for (int i = 0; i < 4; i++) { s += a * hqN3(p); p = p * 2.03 + 11.7; a *= 0.5; } return s; }
// a runoff stain hanging from (u0, top): w wide, fading over len below it, its edges wandering and fraying
float hqStreak(float u, float y, float u0, float top, float w, float len, float seed) {
  float d = top - y;
  if (d < 0.0) return 0.0;
  float wob = (hqNoise(vec2(seed * 7.13, y * 0.8)) - 0.5) * w * 0.8;
  float ww = w * (0.6 + 0.6 * hqNoise(vec2(seed * 3.7 + 5.0, y * 0.3)));
  float x = (u - u0 - wob) / ww;
  float fib = 0.7 + 0.3 * hqNoise(vec2(u * 7.0 + seed, y * 0.45));
  return exp(-x * x * 3.0) * exp(-d / len) * smoothstep(0.0, 0.25, d) * fib;
}
vec3 hqWeather(vec3 c, vec3 P, vec3 N) {
  float lum = dot(c, vec3(0.299, 0.587, 0.114));
  float y = P.y;
  bool wall = abs(N.y) < 0.45;
  bool north = N.z < -0.6, south = N.z > 0.6, west = N.x < -0.6;
  float u = (north || south) ? P.x : P.z;              // along the wall
  float side = north ? 1.0 : south ? 2.0 : west ? 3.0 : 4.0;
  float s = 0.0;
  if (wall && uHqKind < 3.5) {
    // from the cornice: four lanes in ten of 1,1 m drip, each its own length
    float lane = floor(u / 1.1);
    for (int k = -1; k <= 1; k++) {
      float id = lane + float(k);
      if (hqH1(id * 1.71 + side * 31.3) < 0.4) {
        float u0 = (id + 0.2 + 0.6 * hqH1(id * 3.1 + side)) * 1.1;
        float len = 1.2 + 9.0 * pow(hqH1(id * 7.7 + side * 2.0), 2.0);
        s += (0.5 + 0.6 * hqH1(id * 9.1 + side)) * hqStreak(u, y, u0, uHqWall.x - 0.05, 0.12 + 0.3 * hqH1(id * 5.3), len, id + side * 10.0);
      }
    }
    if (north || south) {
      for (int k = 0; k < 8; k++) { // under each gargoyle
        if (float(k) >= uHqGarg.z) break;
        float gx = uHqGarg.x + float(k) * uHqGarg.y;
        s += 1.0 * hqStreak(u, y, gx, uHqGarg.w - 0.15, 0.3, 2.5 + 3.0 * hqH1(float(k) + side * 10.0), float(k) + side * 5.0);
      }
      for (int k = 0; k < 4; k++) { // from both ends of each window's sill
        float hw = uHqWall.y * 0.5 + 0.18, top = uHqWinY[k] - 0.18;
        s += 0.75 * hqStreak(u, y, uHqWinX[k] - hw, top, 0.14, 1.6 + 2.0 * hqH1(float(k) * 3.3 + side), float(k) * 2.0 + side);
        s += 0.75 * hqStreak(u, y, uHqWinX[k] + hw, top, 0.14, 1.6 + 2.0 * hqH1(float(k) * 5.1 + side), float(k) * 2.0 + side + 0.5);
      }
    }
    if (north) s += 1.6 * hqStreak(u, y, uHqWall.z, uHqGarg.w - 0.1, 0.45, 40.0, 77.0); // the long one (the photo)
  }
  s = clamp(s, 0.0, 1.0);
  c = mix(c, c * (north ? vec3(0.36, 0.41, 0.33) : vec3(0.47, 0.46, 0.43)), s); // darker, greener where the sun never dries it
  float edge = (hqFbm3(vec3(u * 0.7, y * 0.6, side)) - 0.5) * 0.9;
  float foot = wall ? smoothstep(1.9, 0.2, y + edge) * (north ? 1.0 : 0.7) : 0.0;
  c = mix(c, mix(vec3(lum), c, 0.45) * vec3(0.6, 0.6, 0.57), foot * 0.9);
  if (uHqKind < 1.5 && wall) { // flaked patches on the rubble
    float fl = smoothstep(0.63, 0.655, hqFbm3(P * vec3(0.8, 1.2, 0.8) + 3.7)) * (uHqKind > 0.5 ? 1.0 : 0.55) * (1.0 - foot) * (1.0 - s);
    c = mix(c, vec3(lum) * vec3(1.32, 1.22, 1.05) + 0.03, fl * 0.7);
  }
  float li = smoothstep(0.56, 0.7, hqFbm3(P * 2.3 + 9.1)) * (uHqKind > 3.5 ? 1.0 : smoothstep(0.45, 0.85, N.y)); // lichen
  vec3 lic = mix(vec3(0.62, 0.58, 0.40), vec3(0.66, 0.42, 0.20), hqN3(P * 0.7 + 4.0));
  return mix(c, lic * (0.75 + 0.5 * lum), li * 0.6);
}
`;
const KIND = { mamposteria: 0, mamposteria_pies: 1, silleria: 2, zocalo: 3, teja: 4 };
function stone(m, kind, U) {
  if (!m.map || m.userData.hqMacro) return;
  m.userData.hqMacro = true;
  const amp = [0.05, 0.05, 0.02, 0.02, 0.03][kind]; // (how far the wall undulates: rubble most)
  m.onBeforeCompile = (sh) => {
    Object.assign(sh.uniforms, U, { uHqKind: { value: kind } });
    sh.vertexShader = sh.vertexShader.replace('#include <common>', '#include <common>\nvarying vec3 vHqWorld;\nvarying vec3 vHqFrame;\nvarying vec3 vHqFrameN;')
      .replace('#include <begin_vertex>', '#include <begin_vertex>\nvHqFrame = position; vHqFrameN = normal;')
      .replace('#include <worldpos_vertex>', '#include <worldpos_vertex>\nvHqWorld = (modelMatrix * vec4(transformed, 1.0)).xyz;');
    sh.fragmentShader = sh.fragmentShader.replace('#include <common>', '#include <common>\nvarying vec3 vHqWorld;\n' + MACRO + WEATHER)
      .replace('#include <map_fragment>', `
        vec4 sampledDiffuseColor = texture2D(map, vMapUv);
        float hqM = hqMacro(vHqWorld);
        sampledDiffuseColor.rgb *= mix(vec3(0.8, 0.78, 0.76), vec3(1.08, 1.05, 0.98), hqM);
        diffuseColor *= sampledDiffuseColor;
        diffuseColor.rgb = hqWeather(diffuseColor.rgb, vHqFrame, normalize(vHqFrameN));`)
      .replace('#include <normal_fragment_maps>', `#include <normal_fragment_maps>
        { // the wall not quite flat: a height of a few centimetres, its slope taken in world units (unnormalised sigmas)
          float fade = smoothstep(70.0, 25.0, length(vViewPosition));
          float hb = (hqFbm3(vHqFrame * 0.7) - 0.5) * ${amp.toFixed(3)} + (hqN3(vHqFrame * 2.5) - 0.5) * ${(amp * 0.25).toFixed(4)} * fade;
          vec3 sx = dFdx(-vViewPosition), sy = dFdy(-vViewPosition);
          vec3 R1 = cross(sy, normal), R2 = cross(normal, sx);
          float det = dot(sx, R1);
          normal = normalize(abs(det) * normal - sign(det) * (dFdx(hb) * R1 + dFdy(hb) * R2));
        }`);
  };
  m.customProgramCacheKey = () => 'hq-desgaste-' + kind;
  m.needsUpdate = true;
}

// The windows' glass gives back the sky, as glass does (Unity's picture showed it, 2026-10-11). Through the town's own
// reflections (scene.environment at 0,4–0,55, which suit stone and plaster) it stayed a black hole; it takes the same
// sky map by its own hand, whole. The map is the sky's one render target, redrawn in place (sky.js): taken once, it
// follows the hour.
function glass(mesh, m) {
  m.roughness = 0.06;
  m.envMapIntensity = 1;
  mesh.onBeforeRender = (renderer, scene) => {
    if (scene.environment && m.envMap !== scene.environment) { m.envMap = scene.environment; m.needsUpdate = true; }
  };
}

export async function hiperIglesia(landmarks, { aniso = 1 } = {}) {
  if (STYLE.plastilina) return null;
  const f = landmarks && landmarks.poi.churchFrame;
  if (!f) return null;
  const bytes = await loadAssetBytes('hq/iglesia.glb');
  if (!bytes) return null; // (no model: the old church stays as it was)
  const buf = bytes.buffer.slice(bytes.byteOffset, bytes.byteOffset + bytes.byteLength);
  const gltf = await new Promise((res, rej) => new GLTFLoader().parse(buf, '', res, rej));
  const root = gltf.scene;
  root.name = 'hiper:iglesia';
  // the weathering layer's places (defaults: the model's own table, overwritten from its marks below)
  const WU = {
    uHqGarg: { value: new THREE.Vector4(-19.1, 4.8, 8, 19.45) },
    uHqWinX: { value: new THREE.Vector4(-16.3, -6.9, 1.6, 10.5) },
    uHqWinY: { value: new THREE.Vector4(15.1, 14.6, 14.6, 14.6) },
    uHqWall: { value: new THREE.Vector4(21.3, 1.4, -19.3, -13.536) },
  };
  root.traverse((o) => {
    if (!o.isMesh) return;
    o.castShadow = true; o.receiveShadow = true;
    for (const m of [].concat(o.material)) {
      for (const k of ['map', 'normalMap', 'roughnessMap', 'metalnessMap']) if (m[k]) { m[k].anisotropy = aniso; m[k].needsUpdate = true; }
      if (m.name in KIND) stone(m, KIND[m.name], WU);
      if (m.name === 'vidrio') glass(o, m);
    }
  });
  const keep = new Set((f.portals || []).filter(Boolean));
  for (const c of f.group.children) if (!keep.has(c)) c.visible = false;
  // the portals stay the old ones for now (fase 2 remodels them): their granite, warmed to the church's golden stone
  const S = landmarks.mat && landmarks.mat.sillar;
  if (S) {
    const warm = S.clone(); warm.color.multiply(new THREE.Color(1.0, 0.8, 0.56));
    for (const p of keep) p.traverse((o) => { if (o.isMesh && o.material === S) o.material = warm; });
  }
  f.group.add(root);
  f.group.updateMatrixWorld(true);
  const mb = await loadAssetBytes('hq/iglesia.json').catch(() => null);
  const marks = mb ? JSON.parse(new TextDecoder().decode(mb)) : null;
  const D = marks && marks.desgaste;
  if (D) {
    WU.uHqGarg.value.set(D.gargolas.x0, D.gargolas.paso, D.gargolas.n, D.gargolas.y);
    const v = D.ventanas.concat([[0, -99], [0, -99], [0, -99], [0, -99]]).slice(0, 4);
    WU.uHqWinX.value.set(v[0][0], v[1][0], v[2][0], v[3][0]); WU.uHqWinY.value.set(v[0][1], v[1][1], v[2][1], v[3][1]);
    WU.uHqWall.value.set(D.cornisa, D.anchoVentana, D.churreteNorte, D.muroNorte);
  }
  if (marks) {
    const W = (x, z) => new THREE.Vector3(x, 0, z).applyMatrix4(f.group.matrixWorld);
    // the buttresses: a ring collider each, as the landmarks' own (addColliders runs after this)
    for (const c of marks.contrafuertes || []) {
      const ring = [];
      for (const [x, z] of [[c.x[0], c.z[0]], [c.x[1], c.z[0]], [c.x[1], c.z[1]], [c.x[0], c.z[1]]]) { const p = W(x, z); ring.push(p.x, p.z); }
      landmarks.colliders.push({ ring, h: c.y[1] });
    }
    // the west portal (the old one, churchdoors.js) at the photo's size: its pediment ≈7 m up, under the great oculus —
    // the model's door pocket is cut to match; its pedestals' colliders and its door's width follow
    const k = marks.portadaOeste && marks.portadaOeste.escala, wg = f.portals && f.portals[0], wp = f.westPosts;
    if (k && wg) {
      wg.scale.setScalar(k); wg.updateMatrixWorld(true);
      if (wp) for (let i = wp.from; i < wp.from + wp.n; i++) {
        const c = landmarks.circleColliders[i];
        c[0] = wp.origin.x + (c[0] - wp.origin.x) * k; c[1] = wp.origin.z + (c[1] - wp.origin.z) * k; c[2] *= k;
      }
      if (landmarks.poi.churchWest) landmarks.poi.churchWest.half *= k;
    }
    // the bells hang from their crowns: each into a pivot there, to swing as the old ones did (landmarks.animated)
    let phase = 0;
    for (const b of marks.campanas || []) {
      const mesh = root.getObjectByName(b.name);
      if (!mesh) continue;
      const pivot = new THREE.Group(); pivot.name = 'pivote:' + b.name;
      pivot.position.set(b.top[0], b.top[1], b.top[2]);
      root.add(pivot); pivot.updateMatrixWorld(true);
      pivot.attach(mesh);
      landmarks.animated.push({ kind: 'bell', mesh: pivot, phase: (phase += 1.7) });
    }
  }
  return root;
}
