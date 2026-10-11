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
function breakTiling(m) {
  if (!m.map || m.userData.hqMacro) return;
  m.userData.hqMacro = true;
  m.onBeforeCompile = (sh) => {
    sh.vertexShader = sh.vertexShader.replace('#include <common>', '#include <common>\nvarying vec3 vHqWorld;')
      .replace('#include <worldpos_vertex>', '#include <worldpos_vertex>\nvHqWorld = (modelMatrix * vec4(transformed, 1.0)).xyz;');
    sh.fragmentShader = sh.fragmentShader.replace('#include <common>', '#include <common>\nvarying vec3 vHqWorld;\n' + MACRO)
      .replace('#include <map_fragment>', `
        vec4 sampledDiffuseColor = texture2D(map, vMapUv);
        float hqM = hqMacro(vHqWorld);
        sampledDiffuseColor.rgb *= mix(vec3(0.8, 0.78, 0.76), vec3(1.08, 1.05, 0.98), hqM);
        diffuseColor *= sampledDiffuseColor;`);
  };
  m.customProgramCacheKey = () => 'hq-macro';
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
  root.traverse((o) => {
    if (!o.isMesh) return;
    o.castShadow = true; o.receiveShadow = true;
    for (const m of [].concat(o.material)) {
      for (const k of ['map', 'normalMap', 'roughnessMap', 'metalnessMap']) if (m[k]) { m[k].anisotropy = aniso; m[k].needsUpdate = true; }
      if (['mamposteria', 'mamposteria_pies', 'silleria', 'zocalo'].includes(m.name)) breakTiling(m);
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
