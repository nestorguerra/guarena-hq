// Only the 3D scene needs multisampling and depth. Full-screen colour passes do not.
import * as THREE from 'three';
import { RenderPass } from 'three/addons/postprocessing/RenderPass.js';
import { ShaderPass } from 'three/addons/postprocessing/ShaderPass.js';
import { CopyShader } from 'three/addons/shaders/CopyShader.js';

export function scenePass(scene, camera, { samples = 4, depth = true } = {}) {
  const pass = new RenderPass(scene, camera);
  const target = new THREE.WebGLRenderTarget(1, 1, {
    type: THREE.HalfFloatType, samples,
    depthTexture: depth ? new THREE.DepthTexture(1, 1) : null,
  });
  const copy = new ShaderPass(CopyShader);
  copy.material.blending = THREE.NoBlending;
  copy.material.depthTest = copy.material.depthWrite = false;
  const draw = pass.render.bind(pass);
  pass.target = target;
  pass.canReadDirectly = null;
  pass.directOutput = false;
  pass.setSize = (w, h) => target.setSize(w, h);
  pass.render = (renderer, writeBuffer, readBuffer, dt, mask) => {
    const screen = pass.renderToScreen;
    try {
      pass.renderToScreen = false;
      draw(renderer, writeBuffer, target, dt, mask);
      // A following colour pass can consume this texture without a full-screen copy.
      // Debug/disabled-pass configurations keep the ordinary composer contract.
      pass.directOutput = !screen && !!pass.canReadDirectly?.();
      if (!pass.directOutput) {
        copy.renderToScreen = screen;
        copy.render(renderer, readBuffer, target, dt, mask);
      }
    } finally { pass.renderToScreen = screen; }
  };
  pass.dispose = () => { target.dispose(); copy.dispose(); };
  return pass;
}
