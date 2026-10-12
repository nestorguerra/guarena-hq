// The inside of Santa María in high definition (docs/hiperrealismo.md, «El interior (fase 6)», the source of truth):
// its architecture modelled in Blender (tools/blender/interior.py → assets/hq/interior/) on church.js's own measures,
// in the Realista look. church.js still builds the whole church — doors and lobbies, colliders, pews, altars, images,
// people —; here the meshes of its architecture (h.archMats) are hidden and the model stands in their place.
// The model is not inside the page (the published page already weighs 27 MB): it is fetched once, in the background
// after the town has loaded or on the way in, and kept; until it comes, the church is the one it always was.
//
// Its light is baked, as Unreal or Unity bake what does not move (phase 6a): Cycles has worked out, over a second set of
// UVs, the sky's light through the windows (and its bounces), the sun's bounce at five hours of the game's day, and the
// lamps' light; here they are mixed by the hour, the sky's colour and strength and whether the lamps are on. The sun's
// own light comes in real time (its patches move with the hour, through the model's windows); the game's ambient light
// and its lamps' point lights do not touch the model (they are in the bake) — they still light the people and the
// furniture, set to the level of the baked light round them. Inside, the eye adapts: the light is scaled up as a
// camera's exposure would be.
import * as THREE from 'three';
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';
import { MeshoptDecoder } from 'three/addons/libs/meshopt_decoder.module.js';
import { STYLE } from './style.js';
import { loadAssetBytes, loadAssetImage } from './assets.js';
import { clamp, lerp } from './util.js';

let model = null;     // { scene, marks, U }
let loading = null;
const FURN = ['madera', 'terciopelo', 'dorado', 'talla', 'plata', 'azul', 'blanco', 'lino', 'piedra', 'marmol', 'hierro'];
const BAKED = ['cal', 'granito', 'tambor', 'fuste', 'caseton', 'caseton_fondo', 'sillar', 'suelo', 'oro', ...FURN];
// (the furniture in high definition, tools/blender/muebles.py: when the model brings a group of it — its interior.json says
// which — church.js's meshes of that group are hidden: h.furn)
const METAL = ['oro', 'dorado', 'talla', 'plata'];
// the paintings (6c): public-domain canvases (tools/blender/cuadros.py → assets/hq/interior/cuadros), laid on church.js's
// own canvases by their subject (userData.painting); the chapels' subjects with no canvas of their own take another's
const CUADROS = ['pedro', 'pablo', 'andres', 'santiago', 'juan', 'tomas', 'mateo', 'bartolome', 'felipe', 'menor', 'simon', 'tadeo',
  'crucifixion', 'jeronimo', 'ambrosio', 'gregorio', 'agustin', 'bautismo', 'isidro', 'ana', 'roque', 'isabel', 'francisco', 'antonio', 'lucia'];
const CUADRO_DE = { gregorioOst: 'francisco', barbara: 'isabel', blas: 'francisco' };

async function canvasTex(path) {
  // (a painting on church.js's own planes: their UVs run up, as an image's — flipY on)
  const img = await loadAssetImage(path).catch(() => null);
  if (!img) return null;
  const t = new THREE.Texture(img);
  t.colorSpace = THREE.SRGBColorSpace; t.anisotropy = 8; t.needsUpdate = true;
  return t;
}
async function tex(path, { srgb = true, repeat = true } = {}) {
  const img = await loadAssetImage(path).catch(() => null);
  if (!img) return null;
  const t = new THREE.Texture(img);
  t.colorSpace = srgb ? THREE.SRGBColorSpace : THREE.NoColorSpace;
  t.flipY = false; // (the glTF's UVs: v down)
  if (repeat) t.wrapS = t.wrapT = THREE.RepeatWrapping;
  t.anisotropy = 8;
  t.needsUpdate = true;
  return t;
}

// fetch and parse the model (once), its textures and lightmaps; resolves to it, or null (the old church stays)
export function loadInterior() {
  if (STYLE.plastilina) return Promise.resolve(null);
  if (model) return Promise.resolve(model);
  if (!loading) loading = (async () => {
    const bytes = await loadAssetBytes('hq/interior/interior.glb');
    if (!bytes) return null;
    const buf = bytes.buffer.slice(bytes.byteOffset, bytes.byteOffset + bytes.byteLength);
    const gltf = await new Promise((res, rej) => new GLTFLoader().setMeshoptDecoder(MeshoptDecoder).parse(buf, '', res, rej)); // (its meshes come compressed: EXT_meshopt_compression)
    const mb = await loadAssetBytes('hq/interior/interior.json').catch(() => null);
    const marks = mb ? JSON.parse(new TextDecoder().decode(mb)) : {};
    const L = marks.luz;
    const T = {};
    const names = ['cal_diff', 'cal_nor', 'cal_rough', 'granito_diff', 'granito_nor', 'granito_rough', 'suelo_diff', 'suelo_nor', 'suelo_rough', 'vidrio_diff'];
    let furn = false; gltf.scene.traverse((o) => { if (o.isMesh && o.material && FURN.includes(o.material.name)) furn = true; });
    if (furn) names.push('madera_diff', 'madera_nor', 'madera_rough', 'terciopelo_diff', 'terciopelo_nor', 'terciopelo_rough', 'dorado_diff', 'dorado_nor', 'dorado_rough', 'talla_diff', 'talla_nor', 'talla_rough', 'plata_diff', 'plata_rough', 'azul_diff', 'azul_rough', 'blanco_diff', 'lino_diff', 'lino_nor', 'lino_rough', 'marmol_diff', 'marmol_rough', 'hierro_diff', 'hierro_rough');
    await Promise.all(names.map(async (n) => { T[n] = await tex(`hq/interior/tex/${n}.jpg`, { srgb: /_diff$/.test(n) }); }));
    const LM = {};
    if (L) {
      const hh = (h) => String(Math.floor(h)).padStart(2, '0') + String(Math.round((h % 1) * 60)).padStart(2, '0');
      await Promise.all(['cielo', 'noche', ...L.horas.map((h) => 'sol_' + hh(h))].map(async (n) => { LM[n] = await tex(`hq/interior/luz/${n}.${L.formato || 'jpg'}`, { repeat: false }); }));
    }
    // the light's uniforms, shared by every baked material: the sky's, the two nearest hours' sun bounce, the lamps'
    const U = {
      uHqSky: { value: new THREE.Color(0, 0, 0) }, uHqSunA: { value: new THREE.Color(0, 0, 0) }, uHqSunB: { value: new THREE.Color(0, 0, 0) }, uHqNight: { value: new THREE.Color(0, 0, 0) },
      tHqSunA: { value: null }, tHqSunB: { value: null }, tHqNight: { value: LM.noche || null },
      uHqRef: { value: 1 }, // (the light where the reflections were photographed: each surface's reflection is scaled by its own light against it)
      uHqLampSpark: { value: 1 }, // (the lamps' real-time light on the metals: see look())
    };
    const mats = makeMaterials(T, LM, U, !!L);
    const pb = L && L.sondas ? await loadAssetBytes('hq/interior/luz/sondas.bin').catch(() => null) : null;
    const probes = pb ? makeProbes(pb, L.sondas) : null;
    gltf.scene.name = 'hiper:interior';
    gltf.scene.traverse((o) => {
      if (!o.isMesh) return;
      o.userData.shared = true; // (kept from one visit to the next: interiors.js does not dispose it)
      const role = o.material && o.material.name;
      if (mats[role]) o.material = mats[role];
      const glass = role === 'vidrio';
      o.castShadow = !glass; o.receiveShadow = !glass;
      // (the faces nobody inside sees — the walls' outer faces and tops, the roofs: they only cast the sun's shadows,
      // so the walls are thick to it and it does not creep in at the corners)
      if (role === 'sombra') { o.material = new THREE.MeshBasicMaterial({ name: 'sombra', colorWrite: false, depthWrite: false, side: THREE.DoubleSide }); o.receiveShadow = false; }
    });
    const cuadros = {};
    await Promise.all(CUADROS.map(async (k) => { cuadros[k] = await canvasTex(`hq/interior/cuadros/${k}.jpg`); }));
    // the images, carved (tools/blender/imagenes.py): one node a figure, by its name; each one's height kept
    let imagenes = null;
    const ib = await loadAssetBytes('hq/interior/imagenes.glb').catch(() => null);
    if (ib) {
      const ibuf = ib.buffer.slice(ib.byteOffset, ib.byteOffset + ib.byteLength);
      const ig = await new Promise((res, rej) => new GLTFLoader().setMeshoptDecoder(MeshoptDecoder).parse(ibuf, '', res, rej)).catch(() => null);
      if (ig) {
        imagenes = {};
        // (their glass eyes: the iris and pupil painted in their texture — tools/blender/texturas_interior.py, «ojo»)
        const eye = await tex('hq/interior/tex/ojo_diff.jpg', { srgb: true }).catch(() => null);
        const glass = (mt) => { if (eye && mt && mt.name === 'ojo') { mt.map = eye; mt.color.set(0xffffff); mt.roughness = 0.12; mt.needsUpdate = true; } };
        for (const o of ig.scene.children) {
          const bb = new THREE.Box3().setFromObject(o);
          o.traverse((q) => { if (q.isMesh) { q.castShadow = true; q.receiveShadow = true; q.userData.shared = true; q.userData.imagenMesh = true; [].concat(q.material).forEach(glass); } });
          imagenes[o.name] = { node: o, height: bb.max.y - bb.min.y, base: bb.min.y };
        }
      }
    }
    return (model = { scene: gltf.scene, marks, U, LM, L, probes, furn, cuadros, imagenes });
  })().catch((e) => { console.warn('[hiperinterior]', e); loading = null; return null; });
  return loading;
}

// the materials, by the model's material names; the baked ones get the lightmaps and the light's patch
function makeMaterials(T, LM, U, baked) {
  const n = (name) => { const t = T[name]; return t; };
  const M = {};
  const std = (name, o) => new THREE.MeshStandardMaterial({ name, ...o });
  M.cal = std('cal', { map: n('cal_diff'), normalMap: n('cal_nor'), roughnessMap: n('cal_rough'), roughness: 1, normalScale: new THREE.Vector2(0.8, -0.8) });
  M.caseton = std('caseton', { map: n('cal_diff'), normalMap: n('cal_nor'), roughnessMap: n('cal_rough'), roughness: 1, color: 0xeeeeee, normalScale: new THREE.Vector2(0.8, -0.8) });
  M.caseton_fondo = std('caseton_fondo', { map: n('cal_diff'), normalMap: n('cal_nor'), roughnessMap: n('cal_rough'), roughness: 1, color: 0xa9abb0, normalScale: new THREE.Vector2(0.8, -0.8) }); // (the coffers' panels: a greyer lime, the photo's darker centres)
  for (const k of ['granito', 'tambor', 'fuste', 'sillar']) M[k] = std(k, { map: n('granito_diff'), normalMap: n('granito_nor'), roughnessMap: n('granito_rough'), roughness: 1, normalScale: new THREE.Vector2(1, -1) });
  M.suelo = std('suelo', { map: n('suelo_diff'), normalMap: n('suelo_nor'), roughnessMap: n('suelo_rough'), roughness: 1, normalScale: new THREE.Vector2(1, -1) });
  M.oro = std('oro', { color: 0xd9ae55, metalness: 0.92, roughness: 0.32 });
  // the furniture: oak stained dark and varnished; the kneelers' garnet velvet, its sheen at a glance
  M.madera = std('madera', { map: n('madera_diff'), normalMap: n('madera_nor'), roughnessMap: n('madera_rough'), roughness: 1, normalScale: new THREE.Vector2(0.6, -0.6) });
  M.terciopelo = new THREE.MeshPhysicalMaterial({ name: 'terciopelo', map: n('terciopelo_diff'), normalMap: n('terciopelo_nor'), roughnessMap: n('terciopelo_rough'), roughness: 1, normalScale: new THREE.Vector2(0.5, -0.5), sheen: 1, sheenColor: new THREE.Color(0.5, 0.12, 0.15), sheenRoughness: 0.45 });
  // the retablos' gilding: gold leaf burnished, and over the carving duller, punched, the red bole where it is worn; the
  // exhibitor's silver; the niche's starred blue; white paint (the dove, the glory)
  M.dorado = std('dorado', { map: n('dorado_diff'), normalMap: n('dorado_nor'), roughnessMap: n('dorado_rough'), roughness: 1, metalness: 1, normalScale: new THREE.Vector2(1, -1) });
  M.talla = std('talla', { map: n('talla_diff'), normalMap: n('talla_nor'), roughnessMap: n('talla_rough'), roughness: 1, metalness: 1, normalScale: new THREE.Vector2(1, -1) });
  M.plata = std('plata', { map: n('plata_diff'), roughnessMap: n('plata_rough'), roughness: 1, metalness: 1 });
  M.azul = std('azul', { map: n('azul_diff'), roughnessMap: n('azul_rough'), roughness: 1 });
  M.blanco = std('blanco', { map: n('blanco_diff'), roughness: 0.55 });
  // the altars' cloths, linen; their stone, the architecture's granite
  M.lino = std('lino', { map: n('lino_diff'), normalMap: n('lino_nor'), roughnessMap: n('lino_rough'), roughness: 1, normalScale: new THREE.Vector2(0.6, -0.6) });
  M.piedra = std('piedra', { map: n('granito_diff'), normalMap: n('granito_nor'), roughnessMap: n('granito_rough'), roughness: 1, normalScale: new THREE.Vector2(1, -1) });
  // the presbytery's altar, white marble polished; the grilles, stairs and rails, wrought iron
  M.marmol = std('marmol', { map: n('marmol_diff'), roughnessMap: n('marmol_rough'), roughness: 1 });
  M.hierro = std('hierro', { map: n('hierro_diff'), roughnessMap: n('hierro_rough'), roughness: 1, metalness: 0.65 });
  M.vidrio = new THREE.MeshStandardMaterial({ name: 'vidrio', map: n('vidrio_diff'), color: 0xffffff, emissive: 0xfff0d0, emissiveMap: n('vidrio_diff'), emissiveIntensity: 1.3, roughness: 0.4, transparent: true, opacity: 0.9, depthWrite: false });
  if (baked) for (const k of BAKED) bakeLight(M[k], LM.cielo, U, k);
  for (const k of BAKED) { M[k].shadowSide = THREE.DoubleSide; }
  return M;
}

// the stones' joints, drawn over the granite by its UVs (metres over its 0,7 m tile): the drums of the shafts and the
// voussoirs of arches and ribs across their length (v), every 0,62 m; the ashlar of the plinth, pedestals, jambs and
// steps in courses of 0,40 m, its joints every 0,60 m, staggered (a block ≈ 60 × 40 cm, the table's). A line of greyer, dirtier mortar a few millimetres wide,
// softened by the pixel's own width (fwidth) so that far away it fades instead of shimmering
const JOINT = /* glsl */ `
  float hqJoint(float t, float w) { float d = min(fract(t), 1.0 - fract(t)); float fw = fwidth(t); return 1.0 - smoothstep(w, w + fw * 1.5, d); }`;
const JOINTS = {
  tambor: `{ float t = vMapUv.y * 0.7 / 0.62; float j = hqJoint(t, 0.006 / 0.62); diffuseColor.rgb *= 1.0 - 0.32 * j; }`,
  fuste: `{ float t = vMapUv.y * 0.7 / 0.62; float j = hqJoint(t, 0.006 / 0.62); diffuseColor.rgb *= 1.0 - 0.32 * j; }`,
  sillar: `{ float tv = vMapUv.y * 0.7 / 0.40; float row = floor(tv); float tu = vMapUv.x * 0.7 / 0.60 + 0.5 * mod(row, 2.0);
             float j = max(hqJoint(tv, 0.006 / 0.40), hqJoint(tu, 0.006 / 0.60)); diffuseColor.rgb *= 1.0 - 0.3 * j; }`,
};

// three's own chunk for the indirect light, its lightmap part ours (__HQ_LIGHTMAP__) and the reflections' map giving no
// diffuse light (the lightmap or the probes are that); and the reflections scaled by the light where each surface is,
// against the light where they were photographed (uHqRef): gold in a dark chapel does not shine like gold in the nave
const MAPS = THREE.ShaderChunk.lights_fragment_maps
  .replace(/#ifdef USE_LIGHTMAP[\s\S]*?#endif/, '__HQ_LIGHTMAP__')
  .replace('iblIrradiance += getIBLIrradiance( geometryNormal );', '');
// three's direct lights without the lamps' point and spot lights — their light is baked (the lightmaps, the probes);
// the sun's stays. (Made on the chunk itself: in onBeforeCompile the shader still holds its #includes, and a replace
// aimed inside one found nothing — the lamps were lighting everything a second time, warm, by day too)
const BEGIN_NO_LAMPS = THREE.ShaderChunk.lights_fragment_begin
  .replace('#if ( NUM_POINT_LIGHTS > 0 ) && defined( RE_Direct )', '#if 0')
  .replace('#if ( NUM_SPOT_LIGHTS > 0 ) && defined( RE_Direct )', '#if 0');
if (BEGIN_NO_LAMPS.split('#if 0').length !== 3) console.error('hiperinterior: three\'s lights_fragment_begin has changed');
// and for the metals: the lamps' light kept (their sparkle), scaled by uHqLampSpark — whole by day, dimmer at night (the
// eye adapted to the dark; and the night's bloom)
const BEGIN_METAL = THREE.ShaderChunk.lights_fragment_begin
  .replace('getPointLightInfo( pointLight, geometryPosition, directLight );', 'getPointLightInfo( pointLight, geometryPosition, directLight ); directLight.color *= uHqLampSpark;')
  .replace('getSpotLightInfo( spotLight, geometryPosition, directLight );', 'getSpotLightInfo( spotLight, geometryPosition, directLight ); directLight.color *= uHqLampSpark;');
if (BEGIN_METAL.split('uHqLampSpark').length !== 3) console.error('hiperinterior: three\'s lights_fragment_begin has changed (metals)');
const LOCAL_SPEC = `
  #if defined( USE_ENVMAP ) && defined( RE_IndirectSpecular )
    { float hqL = dot(irradiance, vec3(0.2126, 0.7152, 0.0722)); radiance *= clamp(hqL / max(uHqRef, 1e-4), 0.03, 2.0); }
  #endif`;

// the baked light: the sky's lightmap in three's own lightMap slot, the sun's two hours and the lamps' in uniforms of
// their own, all over the second UV set; the irradiance is theirs alone (no ambient, no light probe), and the lamps'
// point and spot lights are left out (their light is in the bake); the sun stays (its direct light is real-time)
function bakeLight(m, sky, U, key) {
  if (!m || !sky) return;
  m.lightMap = sky; sky.channel = 1;
  m.lightMapIntensity = 1;
  m.onBeforeCompile = (sh) => {
    Object.assign(sh.uniforms, U);
    sh.fragmentShader = sh.fragmentShader
      .replace('#include <lightmap_pars_fragment>', `#include <lightmap_pars_fragment>
        ${JOINT}
        uniform vec3 uHqSky; uniform vec3 uHqSunA; uniform vec3 uHqSunB; uniform vec3 uHqNight; uniform float uHqRef; uniform float uHqLampSpark;
        uniform sampler2D tHqSunA; uniform sampler2D tHqSunB; uniform sampler2D tHqNight;`)
      .replace('#include <lights_fragment_maps>', MAPS.replace('__HQ_LIGHTMAP__', `
          irradiance = texture2D( lightMap, vLightMapUv ).rgb * uHqSky
            + texture2D( tHqSunA, vLightMapUv ).rgb * uHqSunA + texture2D( tHqSunB, vLightMapUv ).rgb * uHqSunB
            + texture2D( tHqNight, vLightMapUv ).rgb * uHqNight; // (the lamps' warm colour is in uHqNight: the map is its luminance)
          ${key === 'fuste' ? `{ float k = fract(vMapUv.x * 0.7 / 0.175406 + 0.1333);
            float t = k / 0.82 * 2.0 - 1.0; irradiance *= k > 0.82 ? 1.0 : 1.0 - 0.4 * pow(max(0.0, 1.0 - t * t), 0.75); }` : ''}`) + LOCAL_SPEC)
      .replace('#include <lights_fragment_begin>', METAL.includes(key) ? BEGIN_METAL : BEGIN_NO_LAMPS); // (a metal has no diffuse light to count twice: the lamps' sparkle on the gilding stays)
    if (JOINTS[key]) sh.fragmentShader = sh.fragmentShader.replace('#include <map_fragment>', '#include <map_fragment>\n' + JOINTS[key]);
  };
  m.customProgramCacheKey = () => 'hq-interior-' + key;
  m.needsUpdate = true;
}

// put the model into a church just built (church.js's h): now if it is here, else as soon as it comes — if the player
// is still in that church
export function attachInterior(h, g) {
  if (STYLE.plastilina || !h || !h.church) return;
  const put = (m) => {
    if (!m || g.interior !== h || h.hiper) return;
    for (const o of h.group.children) if (o.isMesh && h.archMats && h.archMats.has(o.material)) o.visible = false;
    // (before the model goes in: only church.js's meshes are walked)
    const groups = [...((m.marks && m.marks.muebles) || []), ...(m.imagenes ? ['imagenes'] : [])];
    for (const gname of groups) {
      const G = h.furn && h.furn[gname]; if (!G) continue;
      h.group.traverse((o) => { if (o.isMesh && ((G.mats && G.mats.has(o.material)) || (G.tag && o.userData.hd === G.tag))) o.visible = false; });
    }
    const root = m.scene;
    root.position.set(h.origin.x, 0, h.origin.z);
    h.group.add(root);
    h.hiper = root;
    root.traverse((o) => { if (o.isMesh && o.material.name === 'vidrio') h.glass = o.material; });
    if (m.marks.ventanas) {
      for (const b of h.beams || []) { h.group.remove(b.m); b.m.geometry.dispose(); b.m.material.dispose(); }
      h.windows = m.marks.ventanas.map((w) => ({ ...w, x: w.x + h.origin.x, z: w.z + h.origin.z }));
      h.beams = makeBeams(h.group, h.windows); // (the sun's beams of dust, soft: below)
    }
    hangPaintings(h, m); // (before the probes dress church.js's materials: the canvases go into them)
    placeImages(h, m);   // (and the carved images, in church.js's images' places: the probes light them too)
    if (m.probes && TUNE.probes !== false) probeFurniture(h, m);
    if (m.L) {
      h.daylight = { sun: 1, hemi: 1 }; // (the outdoor light comes in whole: look() makes the inside of it)
      h.look = (gg) => look(gg, h, m);
      h.unlook = (gg) => unlook(gg, h);
    }
  };
  if (model) put(model);
  else loadInterior().then(put);
}

// each frame, after the sky (interiors.js dimSky): the baked light at this hour, the eye's adaptation, the sun inside
const _c = new THREE.Color();
// (the lamps' bake is in Blender's watts, the sky's per unit of sky: `lamps` puts them in the game's units — by day they
// add a little warm light to the daylight; at night the eye adapts to them)
// (by day the lamps give a third of their light — some lit, as in a church between masses: theirs is warm, and the
// daylight should read grey and cool)
// the lamps' colour, ≈3000 K — church.js's chandeliers (#ffdcaa) — at a luminance of 1 (the baked map is the luminance);
// for the lightmaps and the probes alike
const LAMP = [1.33, 0.95, 0.53];
export const TUNE = { exposure: 1.0, sun: 1.0, lamps: 0.0008, lampsDay: 0.3, target: 1.15, nightLevel: 0.45, sunCap: 30, moonCap: 1.5, wb: 0.7, sky: 1, sparkDay: 1.0, sparkNight: 0.3 };
const SKY = [0.974, 1.005, 1.026]; // (the sky through clear glass on grey stone: neutral, faintly cool — at a luminance of 1)
const lum = (c) => 0.2126 * c.r + 0.7152 * c.g + 0.0722 * c.b;
const _ill = new THREE.Color(), _wb = new THREE.Color(), _c2 = new THREE.Color();
// the sun's colour as the sky set it this frame (look() tints it after: if look() runs twice in a frame, the sky's, not
// ours left over)
function sunColour(s, h) {
  if (!h.hqSunSet || !s.sun.color.equals(h.hqSunSet)) (h.hqSunSky || (h.hqSunSky = new THREE.Color())).copy(s.sun.color);
  return h.hqSunSky;
}
function look(g, h, m) {
  const s = g.sky, L = m.L, U = m.U;
  const hour = s.hour;
  // the two baked hours either side of this one (before the first and after the last, the nearest alone)
  const H = L.horas;
  let i = H.findIndex((x) => x > hour); if (i < 0) i = H.length; const a = Math.max(0, i - 1), b = Math.min(H.length - 1, i);
  const t = a === b ? 0 : clamp((hour - H[a]) / (H[b] - H[a]), 0, 1);
  const hh = (x) => 'sol_' + String(Math.floor(x)).padStart(2, '0') + String(Math.round((x % 1) * 60)).padStart(2, '0');
  U.tHqSunA.value = m.LM[hh(H[a])]; U.tHqSunB.value = m.LM[hh(H[b])];
  const sun = s.sun.intensity, sky = s.hemi.intensity;           // (the outdoor light: h.daylight lets it in whole)
  const night = s.night || 0, day = s.lightDir ? clamp(s.lightDir.y * 4, 0, 1) * (1 - night) : 0;
  const night0 = s.night || 0, lamps = h.powered === false ? 0 : lerp(TUNE.lampsDay, 1, night0);
  // what the bake gives, in three's irradiance: sky — its map (L_d per unit of sky radiance) × the hemisphere's colour
  // and strength; sun — π × its map × the sun's; lamps — π × its map
  const kSky = L.cielo.escala, kA = L.sol[a].escala, kB = L.sol[b].escala, kN = L.noche.escala;
  // the eye: the median of what lights the inside, brought to a mid level
  const med = L.cielo.mediana * sky + Math.PI * lerp(L.sol[a].mediana, L.sol[b].mediana, t) * sun * day + Math.PI * L.noche.mediana * lamps * TUNE.lamps;
  // (at night the eye does not quite adapt: the lamps' pools of light, the vaults in half-light)
  const K = TUNE.exposure * TUNE.target * lerp(1, TUNE.nightLevel, night) / Math.max(1e-4, med);
  // and its colour: the light's own — sky, sun and lamps by their shares of that median — partly undone, as the eye (or a
  // camera's white balance) sees lime as white under a warm sun; at night much less (the lamps keep their warmth)
  const sunCol = sunColour(s, h), lumS = Math.max(1e-4, lum(sunCol));
  _ill.setRGB(...SKY).multiplyScalar(L.cielo.mediana * sky)
    .add(_c2.copy(sunCol).multiplyScalar(Math.PI * lerp(L.sol[a].mediana, L.sol[b].mediana, t) * sun * day / lumS))
    .add(_c2.setRGB(...LAMP).multiplyScalar(Math.PI * L.noche.mediana * lamps * TUNE.lamps));
  const il = lum(_ill), adapt = TUNE.wb * lerp(1, 0.3, night);
  if (il > 1e-6) { _wb.setRGB(lerp(1, il / Math.max(1e-6, _ill.r), adapt), lerp(1, il / Math.max(1e-6, _ill.g), adapt), lerp(1, il / Math.max(1e-6, _ill.b), adapt)); _wb.multiplyScalar(1 / lum(_wb)); }
  else _wb.setRGB(1, 1, 1);
  const lumH = lum(s.hemi.color);
  U.uHqSky.value.setRGB(...SKY).multiplyScalar(lumH * sky * kSky * K * TUNE.sky).multiply(_wb); // (TUNE.sky: 1; 0 to see the sun's bounce alone)
  _c.copy(sunCol).multiplyScalar(Math.PI * sun * day * K * TUNE.sun).multiply(_wb);
  U.uHqSunA.value.copy(_c).multiplyScalar(kA * (1 - t));
  U.uHqSunB.value.copy(_c).multiplyScalar(kB * t);
  U.uHqNight.value.setRGB(...LAMP).multiplyScalar(Math.PI * kN * lamps * TUNE.lamps * K).multiply(_wb);
  // the sun inside (its patches), adapted too — held below a ceiling, as a camera's highlights roll off
  s.sun.intensity = Math.min(sun * K * TUNE.sun, day > 0.05 ? TUNE.sunCap : TUNE.moonCap);
  s.sun.color.copy(sunCol).multiply(_wb); (h.hqSunSet || (h.hqSunSet = new THREE.Color())).copy(s.sun.color);
  // what is not baked (people, furniture): the hemisphere at the level of the baked light round it
  s.hemi.intensity = TUNE.target * 0.9 * lerp(1, TUNE.nightLevel, night); // (and at night as dim as the baked light round it)
  s.hemi.color.setRGB(1.0, 0.96, 0.9).multiply(_wb); s.hemi.groundColor.setRGB(0.55, 0.5, 0.45).multiply(_wb);
  U.uHqLampSpark.value = lerp(TUNE.sparkDay, TUNE.sparkNight, night);
  h.hqK = K;
  if (TUNE.beams === false) for (const bm of h.beams || []) bm.m.material.visible = false;
  if (m.probes) mixProbes(m.probes, U, a, b);
  // the reflections: a photograph in a cube of the inside, from the middle of the nave, taken once it is lit and again
  // every game hour (the light changes)
  if (!h.hqEnvAt || Math.abs(hour - h.hqEnvAt) > 1) envShot(g, h, m, hour);
}

let cubeRT = null, cubeCam = null, pmrem = null;
function envShot(g, h, m, hour) {
  const r = g.renderer;
  if (!cubeRT) { cubeRT = new THREE.WebGLCubeRenderTarget(256, { type: THREE.HalfFloatType }); cubeCam = new THREE.CubeCamera(0.3, 200, cubeRT); pmrem = new THREE.PMREMGenerator(r); }
  cubeCam.position.set(h.origin.x + 0, 7.5, h.origin.z);
  const vis = [];
  g.scene.traverse((o) => { if (o.isMesh && o.userData.noEnvShot) { vis.push([o, o.visible]); o.visible = false; } });
  cubeCam.update(r, g.scene);
  for (const [o, v] of vis) o.visible = v;
  if (h.hqEnv) h.hqEnv.dispose();
  h.hqEnv = pmrem.fromCubemap(cubeRT.texture).texture;
  if (m.probes) m.U.uHqRef.value = Math.max(1e-4, probeLum(m.probes, m.U, 0, 7.5, 0));
  m.scene.traverse((o) => { if (o.isMesh && o.material && o.material.name !== 'vidrio' && o.material.envMap !== h.hqEnv) { o.material.envMap = h.hqEnv; o.material.envMapIntensity = METAL.includes(o.material.name) ? 1.0 : 0.6; o.material.needsUpdate = true; } });
  // (and church.js's furniture, lit by the probes: what reflects — its gold, brass, silver — the inside too)
  for (const mt of h.hqProbeMats || []) if (mt.envMap && mt.envMap !== h.hqEnv) { mt.envMap = h.hqEnv; mt.envMapIntensity = Math.min(mt.envMapIntensity, 1.0); }
  h.hqEnvAt = hour;
}

function unlook(g, h) { h.hqK = 0; }

// the carved images in the places church.js's stood in, at their height (the Christ by his body: his cross stands taller)
function placeImages(h, m) {
  if (!m.imagenes || !h.imagenes) return;
  for (const q of h.imagenes) {
    const I = m.imagenes[q.kind]; if (!I) continue;
    const o = I.node.clone(true);
    const k = q.h / (q.kind === 'cristo' ? I.height * 0.62 : I.height);
    o.scale.setScalar(k); o.rotation.set(0, q.ry, 0);
    o.position.set(q.x, q.y - I.base * k, q.z);
    o.userData.imagen = q.kind;
    h.group.add(o);
  }
}

// the real canvases on church.js's: each by its subject, varnished (a soft sheen); the Crucifixion's plane narrowed to
// El Greco's canvas, taller than church.js's (its frame in the model is made to it)
function hangPaintings(h, m) {
  if (!m.cuadros) return;
  h.group.traverse((o) => {
    if (!o.isMesh || !o.userData.painting) return;
    const t = m.cuadros[CUADRO_DE[o.userData.painting] || o.userData.painting];
    if (!t) return;
    const mt = o.material.clone();
    mt.map = t; mt.color.set(0xffffff); mt.roughness = 0.38; mt.metalness = 0; mt.needsUpdate = true;
    o.material = mt;
    if (o.userData.painting === 'crucifixion' && !o.userData.fitted) {
      const g = o.geometry; g.computeBoundingBox(); const b = g.boundingBox, cz = (b.min.z + b.max.z) / 2, hh = b.max.y - b.min.y, ww = b.max.z - b.min.z;
      const k = (hh * (636 / 1024)) / ww; const p = g.attributes.position;
      for (let i = 0; i < p.count; i++) p.setZ(i, cz + (p.getZ(i) - cz) * k);
      p.needsUpdate = true; g.computeBoundingBox(); g.computeBoundingSphere(); o.userData.fitted = true;
    }
  });
}

// ---------------------------------------------------------------- the light probes (what is not baked)
// The furniture, the doors, the pictures — church.js's, not baked — take their light from the probes baked with the
// lightmaps (interior.py): a grid every 1,5 m through the church, at each point the light from its six sides (an «ambient
// cube», as Valve's engine has it). Mixed here, on the CPU, for the hour, the sky and the lamps (as the lightmaps are),
// into six 3D textures, one a side; their shader reads them at its own place and normal instead of the game's ambient
// light, and leaves out the lamps' point lights (their light is in the probes). Only the sun stays real-time.
function makeProbes(bytes, P) {
  const [nx, ny, nz] = P.n, N = nx * ny * nz;
  const lin = new Float32Array(256);
  for (let i = 0; i < 256; i++) { const v = i / 255; lin[i] = v <= 0.04045 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4); }
  const tex = [], data = [];
  for (let f = 0; f < 6; f++) {
    const d = new Uint16Array(N * 4);
    const t = new THREE.Data3DTexture(d, nx, ny, nz);
    t.format = THREE.RGBAFormat; t.type = THREE.HalfFloatType; t.minFilter = t.magFilter = THREE.LinearFilter;
    t.wrapS = t.wrapT = t.wrapR = THREE.ClampToEdgeWrapping; t.unpackAlignment = 1;
    tex.push(t); data.push(d);
  }
  const index = (name) => P.orden.indexOf(name);
  const uniforms = {
    tHqA0: { value: tex[0] }, tHqA1: { value: tex[1] }, tHqA2: { value: tex[2] }, tHqA3: { value: tex[3] }, tHqA4: { value: tex[4] }, tHqA5: { value: tex[5] },
    uHqGridO: { value: new THREE.Vector3() }, uHqGridStep: { value: P.paso }, uHqGridN: { value: new THREE.Vector3(nx, ny, nz) },
  };
  return { P, bytes, lin, tex, data, N, index, uniforms, last: '' };
}
const HOURNAME = (x) => 'sol_' + String(Math.floor(x)).padStart(2, '0') + String(Math.round((x % 1) * 60)).padStart(2, '0');
function mixProbes(pr, U, a, b) {
  // a new mix only when the light has changed by more than a few per cent, at most once a second; and spread over six
  // frames, one side a frame (about a millisecond and one small 3D texture each)
  const L = model.L, H = L.horas, now = performance.now();
  if (pr.job) return stepProbes(pr);
  const w = [[pr.index('cielo'), U.uHqSky.value], [pr.index(HOURNAME(H[a])), U.uHqSunA.value], [pr.index(HOURNAME(H[b])), U.uHqSunB.value], [pr.index('noche'), U.uHqNight.value]]
    .filter(([c]) => c >= 0).map(([c, col]) => [c, col.r, col.g, col.b]);
  if (pr.lastW && now - pr.lastT < 1000) return;
  if (pr.lastW && pr.lastW.length === w.length && pr.lastW.every((x, i) => x[0] === w[i][0] && [1, 2, 3].every((k) => Math.abs(x[k] - w[i][k]) <= 0.03 * Math.max(1e-6, Math.abs(x[k]), Math.abs(w[i][k]))))) return;
  pr.lastW = w; pr.lastT = now;
  pr.job = { w: w.filter((x) => x[1] || x[2] || x[3]), f: 0 };
  // (the first time, all six at once: the church must not show unlit for six frames)
  if (!pr.ready) { while (pr.job) stepProbes(pr); pr.ready = true; }
  else stepProbes(pr);
}
function stepProbes(pr) {
  const t0 = performance.now();
  const { bytes, lin, data, N } = pr, toHalf = THREE.DataUtils.toHalfFloat, { w, f } = pr.job, d = data[f];
  for (let n = 0; n < N; n++) {
    let r = 0, g = 0, bl = 0;
    for (let k = 0; k < w.length; k++) {
      const x = w[k], o = ((x[0] * N + n) * 6 + f) * 3;
      r += lin[bytes[o]] * x[1]; g += lin[bytes[o + 1]] * x[2]; bl += lin[bytes[o + 2]] * x[3];
    }
    const q = n * 4;
    d[q] = toHalf(r); d[q + 1] = toHalf(g); d[q + 2] = toHalf(bl); d[q + 3] = toHalf(1);
  }
  pr.tex[f].needsUpdate = true;
  pr.job.f++;
  if (pr.job.f >= 6) pr.job = null;
  STATS.mix++; STATS.mixMs += performance.now() - t0;
}
export const STATS = { mix: 0, mixMs: 0 };
// church.js's own materials in this church (not the model's): cloned (a material may be shared with the town) and made
// to take their ambient light from the probes; their lamps' glow by day toned down (it stood in for light they lacked)
function probeFurniture(h, m) {
  const pr = m.probes, P = pr.P;
  pr.uniforms.uHqRef = m.U.uHqRef;
  pr.uniforms.uHqGridO.value.set(h.origin.x + P.origen[0], P.origen[1], h.origin.z + P.origen[2]);
  const done = new Map();
  h.group.traverse((o) => {
    if (!o.isMesh || !o.visible || (o.userData.shared && !o.userData.imagenMesh)) return; // (the carved images: shared geometry, lit by the probes all the same)
    let p = o.parent; while (p && p !== h.group) { if (p === m.scene) return; p = p.parent; }
    const mats = [].concat(o.material);
    const out = mats.map((mt) => {
      if (!mt || !(mt.isMeshStandardMaterial || mt.isMeshPhysicalMaterial) || mt.transparent) return mt;
      if (!done.has(mt)) {
        const c = mt.clone();
        c.onBeforeCompile = (sh) => {
          Object.assign(sh.uniforms, pr.uniforms);
          sh.vertexShader = sh.vertexShader.replace('#include <common>', '#include <common>\nvarying vec3 vHqW;')
            .replace('#include <worldpos_vertex>', '#include <worldpos_vertex>\nvHqW = (modelMatrix * vec4(transformed, 1.0)).xyz;');
          sh.fragmentShader = sh.fragmentShader.replace('#include <common>', `#include <common>
            varying vec3 vHqW;
            uniform highp sampler3D tHqA0; uniform highp sampler3D tHqA1; uniform highp sampler3D tHqA2;
            uniform highp sampler3D tHqA3; uniform highp sampler3D tHqA4; uniform highp sampler3D tHqA5;
            uniform vec3 uHqGridO; uniform float uHqGridStep; uniform vec3 uHqGridN; uniform float uHqRef;
            vec3 hqProbe(vec3 p, vec3 n) {
              vec3 c = ((p - uHqGridO) / uHqGridStep + 0.5) / uHqGridN;
              vec3 n2 = n * n;
              return n2.x * (n.x >= 0.0 ? texture(tHqA0, c).rgb : texture(tHqA1, c).rgb)
                   + n2.y * (n.y >= 0.0 ? texture(tHqA2, c).rgb : texture(tHqA3, c).rgb)
                   + n2.z * (n.z >= 0.0 ? texture(tHqA4, c).rgb : texture(tHqA5, c).rgb);
            }`)
            .replace('#include <lights_fragment_begin>', BEGIN_NO_LAMPS + `
              #if defined( RE_IndirectDiffuse )
                irradiance = hqProbe(vHqW, inverseTransformDirection(normal, viewMatrix));
              #endif`)
            .replace('#include <lights_fragment_maps>', MAPS.replace('__HQ_LIGHTMAP__', '') + LOCAL_SPEC);
        };
        c.customProgramCacheKey = () => 'hq-sonda-' + mt.type;
        if (c.emissiveIntensity && !o.userData.lamp) c.emissiveIntensity *= 0.25;
        done.set(mt, c);
        (h.hqProbeMats = h.hqProbeMats || []).push(c);
      }
      return done.get(mt);
    });
    o.material = Array.isArray(o.material) ? out : out[0];
  });
}

// the light at a point of the church (its frame) from the probes as now mixed: the six sides' luminance, averaged
function probeLum(pr, U, x, y, z) {
  const P = pr.P, [nx, ny, nz] = P.n;
  const i = clamp(Math.round((x - P.origen[0]) / P.paso), 0, nx - 1), j = clamp(Math.round((y - P.origen[1]) / P.paso), 0, ny - 1), k = clamp(Math.round((z - P.origen[2]) / P.paso), 0, nz - 1);
  const n = (k * ny + j) * nx + i, H = model.L.horas;
  const w = [[pr.index('cielo'), U.uHqSky.value], [pr.index('noche'), U.uHqNight.value]];
  for (const name of pr.P.orden) if (name.startsWith('sol_')) {
    const x0 = pr.index(name), tex = model.LM[name];
    if (U.tHqSunA.value === tex) w.push([x0, U.uHqSunA.value]); else if (U.tHqSunB.value === tex) w.push([x0, U.uHqSunB.value]);
  }
  let sum = 0;
  for (let f = 0; f < 6; f++) for (const [c, col] of w) {
    if (c < 0) continue;
    const o = ((c * pr.N + n) * 6 + f) * 3;
    sum += 0.2126 * pr.lin[pr.bytes[o]] * col.r + 0.7152 * pr.lin[pr.bytes[o + 1]] * col.g + 0.0722 * pr.lin[pr.bytes[o + 2]] * col.b;
  }
  return sum / 6;
}

// ---------------------------------------------------------------- the sun's beams through the windows
// church.js drew them as boxes faded at their edges: seen from below they were flat sheets with hard borders, lines across
// the vaults (the reviewer). Here each beam is a soft shaft of light in the air: drawn on its box's far faces, the ray
// from the eye through it is followed across the beam (six steps), and at each the light of an ellipse soft to its rim,
// fading in at the window and out towards the floor, the dust drifting in it — summed over the length crossed. Its
// uniforms are church.js's (updateBeams keeps driving them: where the sun is, how strong)
const BEAM_VS = /* glsl */ `
uniform vec3 uBase; uniform vec3 uU; uniform vec3 uV; uniform vec3 uD; uniform float uLen;
varying vec3 vW;
void main() {
  vec3 p = uBase + uU * position.x + uV * position.y + uD * (position.z * uLen);
  vW = p;
  gl_Position = projectionMatrix * viewMatrix * vec4(p, 1.0);
}`;
const BEAM_FS = /* glsl */ `
uniform vec3 uBase; uniform vec3 uU; uniform vec3 uV; uniform vec3 uD; uniform float uLen;
uniform float uK; uniform float uTime; uniform vec3 uCol;
varying vec3 vW;
void main() {
  mat3 Mx = mat3(uU, uV, uD * uLen);
  mat3 Mi = inverse(Mx);
  vec3 ro = Mi * (cameraPosition - uBase), rd = Mi * (vW - cameraPosition);
  vec3 inv = 1.0 / rd, t0 = (vec3(-0.5, -0.5, 0.0) - ro) * inv, t1 = (vec3(0.5, 0.5, 1.0) - ro) * inv;
  vec3 tn = min(t0, t1), tf = max(t0, t1);
  float ta = max(max(tn.x, tn.y), max(tn.z, 0.0)), tb = min(min(tf.x, tf.y), min(tf.z, 1.0));
  if (tb <= ta) discard;
  float acc = 0.0;
  for (int i = 0; i < 6; i++) {
    vec3 q = ro + rd * mix(ta, tb, (float(i) + 0.5) / 6.0);
    float r = length(q.xy * 2.0);
    float prof = 1.0 - smoothstep(0.25, 1.0, r);
    float along = smoothstep(0.0, 0.12, q.z) * (1.0 - smoothstep(0.35, 1.0, q.z));
    float dust = 0.85 + 0.15 * sin(q.z * 41.0 + uTime * 0.45 + q.x * 7.0) * sin(q.y * 23.0 - uTime * 0.3);
    acc += prof * along * dust;
  }
  float len = length(Mx * rd) * (tb - ta);
  float a = clamp(acc / 6.0 * len * uK * 0.6, 0.0, 1.0);
  gl_FragColor = vec4(uCol, a);
}`;
function makeBeams(group, windows) {
  const out = [];
  for (const w of windows) {
    const g = new THREE.BoxGeometry(1, 1, 1); g.translate(0, 0, 0.5);
    const u = {
      uBase: { value: new THREE.Vector3() }, uU: { value: new THREE.Vector3() }, uV: { value: new THREE.Vector3() }, uD: { value: new THREE.Vector3() }, uLen: { value: 20 },
      uK: { value: 0 }, uTime: { value: 0 }, uCol: { value: new THREE.Color(1.0, 0.94, 0.8) },
    };
    const m = new THREE.Mesh(g, new THREE.ShaderMaterial({ uniforms: u, vertexShader: BEAM_VS, fragmentShader: BEAM_FS, transparent: true, depthWrite: false, blending: THREE.AdditiveBlending, side: THREE.BackSide }));
    m.frustumCulled = false; m.renderOrder = 5; m.userData.noInk = true; m.userData.noEnvShot = true;
    group.add(m);
    out.push({ w, m, u });
  }
  return out;
}
