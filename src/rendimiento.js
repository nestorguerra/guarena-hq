// Local capability hints, never a claim about the exact CPU or physical RAM.
const finitePositive = (v) => Number.isFinite(v) && v > 0 ? v : null;
export function machineHints(nav = {}, gl = null, coarse = false) {
  const hints = {
    logicalCores: finitePositive(nav.hardwareConcurrency),
    memoryGiBApprox: finitePositive(nav.deviceMemory),
    platform: nav.userAgentData?.platform || nav.platform || null,
    coarse: !!coarse, gpu: null, maxTextureSize: null, maxSamples: null,
  };
  if (gl) {
    try {
      const ext = gl.getExtension('WEBGL_debug_renderer_info');
      if (ext) hints.gpu = gl.getParameter(ext.UNMASKED_RENDERER_WEBGL) || null;
      hints.maxTextureSize = finitePositive(gl.getParameter(gl.MAX_TEXTURE_SIZE));
      hints.maxSamples = finitePositive(gl.getParameter(gl.MAX_SAMPLES));
    } catch (_) { /* privacy settings may hide capabilities; measurements still work */ }
  }
  return hints;
}

export function initialProfile(hints) {
  const cores = hints.logicalCores, memory = hints.memoryGiBApprox;
  const software = /swiftshader|llvmpipe|software rasterizer/i.test(hints.gpu || '');
  const weak = software || (memory !== null && memory <= 4) || (cores !== null && cores <= 2) ||
    (hints.maxTextureSize !== null && hints.maxTextureSize < 4096);
  const strong = !weak && !hints.coarse && cores >= 8 && memory >= 8;
  return {
    quality: weak ? 'baja' : strong ? 'alta' : 'media',
    // A pixel budget avoids starting a 4K/Retina screen at its native density.
    maxPixels: weak ? 900000 : strong && cores >= 12 && memory >= 16 ? 3200000 : 1800000,
    maxDpr: weak ? 0.8 : strong ? 1.5 : 1,
    exploreDpr: weak ? 0.8 : 1.5,
  };
}

export function automaticQuality(save = {}) {
  // An explicit old quality choice remains manual; fresh games default to automatic.
  return save.qualityMode === 'auto' || (save.qualityMode !== 'manual' && !save.quality);
}

export function pixelBudget(width, height, dpr, profile) {
  const native = finitePositive(dpr) || 1;
  const pixels = Math.max(1, width * height);
  return Math.min(native, profile.maxDpr, Math.sqrt(profile.maxPixels / pixels));
}

// Hysteresis in seconds, using raw presentation intervals rather than the physics timestep.
// An isolated hitch or a background tab must not teach the controller that the machine is slow.
export class QualityController {
  constructor(base, { effects = true, ceiling = base } = {}) {
    this.base = this.pr = base;
    this.ceiling = Math.max(base, ceiling);
    this.floor = Math.min(base, Math.max(0.6, base * 0.6));
    this.level = 0;
    this.effects = effects;
    this.grace = 3;
    this.lock = this.slow = this.fast = this.t = 0;
    this.avg = 1 / 60;
    this.work = 0;
    this.samples = 0;
    this.probe = null;
    this.pixelHold = 0;
    this.promotionHold = this.longFrames = 0;
  }
  suspend(seconds = 3) {
    const oldPr = this.pr;
    if (this.probe) {
      this.pr = this.probe.pr;
      if (this.probe.grow) this.promotionHold = 60;
    }
    this.grace = Math.max(this.grace, seconds);
    this.slow = this.fast = this.t = this.samples = 0;
    this.avg = 1 / 60;
    this.probe = null;
    this.longFrames = 0;
    return oldPr !== this.pr ? { pr: this.pr, level: this.level } : null;
  }
  resize(base, ceiling = base) {
    this.suspend(); // cancel an unvalidated trial before preserving its resolution ratio
    const ratio = this.base > 0 ? this.pr / this.base : 1;
    this.base = base;
    this.ceiling = Math.max(base, ceiling);
    this.floor = Math.min(base, Math.max(0.6, base * 0.6));
    this.pr = Math.max(this.floor, Math.min(this.ceiling, base * ratio));
    this.pixelHold = 0;
    return { pr: this.pr, level: this.level };
  }
  observe(dt, workMs = 0, active = true) {
    if (!active || !Number.isFinite(dt) || dt <= 0) return this.suspend();
    if (dt > 1) {
      const count = this.longFrames + 1;
      if (count < 3) { const cancelled = this.suspend(); this.longFrames = count; return cancelled; }
      this.longFrames = count;
    } else if (dt < 1 / 48) this.longFrames = 0;
    if (this.grace > 0) { this.grace -= dt; return null; }
    this.lock = Math.max(0, this.lock - dt);
    this.pixelHold = Math.max(0, this.pixelHold - dt);
    this.promotionHold = Math.max(0, this.promotionHold - dt);
    if (this.probe) this.probe.time += dt;
    const weight = 1 - Math.exp(-dt / 0.7);
    this.avg += (dt - this.avg) * weight;
    this.work += (Math.max(0, workMs) / 1000 - this.work) * weight;
    this.t += dt; this.samples++;
    if (this.t < 1 || this.samples < 4) return null;
    const elapsed = this.t; this.t = 0; this.samples = 0;
    if (this.probe?.time >= 4) {
      const probe = this.probe; this.probe = null;
      if (probe.grow ? this.avg > 1 / 55 : this.avg > probe.interval * 0.95) {
        // A CPU bottleneck, a capped display, or no measurable gain: keep the sharper image.
        this.pr = probe.pr; this.lock = 4;
        if (probe.grow) this.promotionHold = 60;
        else this.pixelHold = 20;
        this.slow = this.fast = 0;
        return { pr: this.pr, level: this.level };
      }
    }
    this.slow = this.avg > 1 / 48 ? this.slow + elapsed : 0;
    this.fast = this.avg < 1 / 57 ? this.fast + elapsed : 0;
    if (this.lock > 0) return null;
    const oldPr = this.pr, oldLevel = this.level;
    if (this.slow >= 2 && this.pixelHold <= 0) {
      // Try pixels first, then verify benefit; workMs alone cannot distinguish CPU from GL waits.
      if (this.pr > this.floor + 0.01) {
        this.probe = { pr: this.pr, interval: this.avg, time: 0 };
        this.pr = Math.max(this.floor, this.pr - 0.1);
      }
      else if (this.effects && this.level < 2) this.level++;
      this.slow = this.fast = 0; this.lock = 4;
    } else if (this.fast >= 12) {
      // Restore the contact/optical effects before increasing the pixel count.
      if (this.level > 0) this.level--;
      else if (this.pr < this.base) this.pr = Math.min(this.base, this.pr + 0.05);
      else if (this.effects && this.promotionHold <= 0 && this.pr < this.ceiling) {
        this.probe = { pr: this.pr, grow: true, time: 0 };
        this.pr = Math.min(this.ceiling, this.pr + 0.05);
      }
      this.fast = 0; this.lock = 8;
    }
    return this.pr !== oldPr || this.level !== oldLevel ? { pr: this.pr, level: this.level } : null;
  }
}
