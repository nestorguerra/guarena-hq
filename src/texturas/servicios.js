// Painted pictures for the objects of the «servicios» family (data/objetos): signs, screens, labels, packaging — drawn on a
// canvas, never a photograph. Each one: tipo → { w, h, draw(ctx, w, h, tex, seed) } (tex: the part's own tex, its words…).
// Read by src/objetos.js (textura). Only invented names (Banco del Valle, Seguros Encina): no real brands; a sign marked rotulo_local reads the name of the business it hangs in.
const SANS = '"Helvetica Neue", Arial, sans-serif';
const SERIF = 'Georgia, "Times New Roman", serif';
const centro = (x, t, cx, y, font, col) => { x.font = font; x.fillStyle = col; x.textAlign = 'center'; x.textBaseline = 'alphabetic'; x.fillText(t, cx, y); };
const izq = (x, t, px, y, font, col) => { x.font = font; x.fillStyle = col; x.textAlign = 'left'; x.textBaseline = 'alphabetic'; x.fillText(t, px, y); };
const der = (x, t, px, y, font, col) => { x.font = font; x.fillStyle = col; x.textAlign = 'right'; x.textBaseline = 'alphabetic'; x.fillText(t, px, y); };
const rect = (x, col, a, b, c, d) => { x.fillStyle = col; x.fillRect(a, b, c, d); };
const marco = (x, col, a, b, c, d, lw = 2) => { x.strokeStyle = col; x.lineWidth = lw; x.strokeRect(a, b, c, d); };
const TEAL = '#0f5c6e', GOLD = '#d9a441';
// the bank's mark: a gold ring with a leaf (a little valley)
function marca(x, cx, cy, r) {
  x.fillStyle = GOLD; x.beginPath(); x.arc(cx, cy, r, 0, 7); x.fill();
  x.fillStyle = TEAL; x.beginPath(); x.arc(cx, cy, r * 0.72, 0, 7); x.fill();
  x.fillStyle = GOLD; x.beginPath(); x.moveTo(cx - r * 0.5, cy + r * 0.3); x.quadraticCurveTo(cx, cy - r * 0.8, cx + r * 0.5, cy + r * 0.3); x.quadraticCurveTo(cx, cy + r * 0.05, cx - r * 0.5, cy + r * 0.3); x.fill();
}

export const TEXTURAS = {
  // the ATM's screen
  cajero_pantalla: { w: 256, h: 192, draw(x, w, h, tex) {
    const g = x.createLinearGradient(0, 0, 0, h); g.addColorStop(0, '#0f5c6e'); g.addColorStop(1, '#0a3a47'); x.fillStyle = g; x.fillRect(0, 0, w, h);
    rect(x, '#0b4553', 0, 0, w, 34); marca(x, 22, 17, 12); izq(x, tex.titulo || 'Banco del Valle', 42, 23, `bold 17px ${SANS}`, '#fff');
    centro(x, 'Bienvenido', w / 2, 82, `bold 26px ${SANS}`, '#fff');
    centro(x, 'Introduzca su tarjeta', w / 2, 112, `18px ${SANS}`, '#cfe8ee');
    rect(x, '#e8ecee', w / 2 - 34, 128, 68, 42); rect(x, '#d9a441', w / 2 - 24, 138, 20, 15); rect(x, '#8a9096', w / 2 - 34, 160, 68, 4);
    for (let i = 0; i < 3; i++) { rect(x, '#d9a441', 10, 50 + i * 40, 28, 7); rect(x, '#d9a441', w - 38, 50 + i * 40, 28, 7); }
  } },
  // the queue's display: the number being called and the window
  turnos_pantalla: { w: 512, h: 144, draw(x, w, h, tex, seed) {
    rect(x, '#06121a', 0, 0, w, h);
    const n = 10 + (seed * 7) % 80;
    izq(x, 'TURNO', 18, 34, `bold 24px ${SANS}`, '#8fd0dc'); centro(x, 'B ' + String(n).padStart(3, '0'), 130, 100, `bold 70px ${SANS}`, '#ffd24a');
    rect(x, '#27414c', 262, 14, 3, h - 28);
    izq(x, 'VENTANILLA', 290, 34, `bold 22px ${SANS}`, '#8fd0dc'); centro(x, String(1 + seed % 3), 396, 106, `bold 76px ${SANS}`, '#ffffff');
    der(x, 'B ' + String(n - 1).padStart(3, '0'), 496, 56, `22px ${SANS}`, '#587684'); der(x, 'B ' + String(n - 2).padStart(3, '0'), 496, 84, `22px ${SANS}`, '#47616d');
  } },
  // the bank's sign over the counter
  rotulo_banco: { w: 1024, h: 188, draw(x, w, h, tex) {
    rect(x, TEAL, 0, 0, w, h); marco(x, GOLD, 10, 10, w - 20, h - 20, 4); marca(x, 120, h / 2, 56);
    izq(x, (tex.titulo || 'Banco del Valle').toUpperCase(), 210, 112, `bold 82px ${SANS}`, '#ffffff'); izq(x, 'Oficina de Guareña', 214, 152, `30px ${SANS}`, '#bfe0e8');
  } },
  // posters of the bank
  cartel_banco: { w: 224, h: 336, draw(x, w, h, tex) {
    const hip = tex.lema === 'hipoteca';
    rect(x, hip ? '#f2efe6' : '#f6ecd0', 0, 0, w, h); rect(x, hip ? TEAL : '#7a5a1c', 0, 0, w, 74); marca(x, 34, 37, 22);
    centro(x, hip ? 'HIPOTECA' : 'PLAN DE', 136, 36, `bold 26px ${SANS}`, '#fff'); centro(x, hip ? 'HOGAR' : 'AHORRO', 136, 62, `bold 26px ${SANS}`, GOLD);
    if (hip) { // (a little house and its price)
      rect(x, '#c8b890', 54, 150, 116, 76); x.fillStyle = '#b5342c'; x.beginPath(); x.moveTo(44, 150); x.lineTo(112, 100); x.lineTo(180, 150); x.fill(); rect(x, '#5a3a24', 100, 182, 24, 44); rect(x, '#9ac4e0', 66, 168, 22, 22); rect(x, '#9ac4e0', 136, 168, 22, 22);
      centro(x, 'desde el 2,4 %', 112, 262, `bold 24px ${SANS}`, TEAL); centro(x, 'TIN a 30 años', 112, 288, `18px ${SANS}`, '#333');
    } else { // (a piggy bank)
      x.fillStyle = '#e8a0a0'; x.beginPath(); x.ellipse(110, 170, 62, 48, 0, 0, 7); x.fill(); x.beginPath(); x.moveTo(158, 150); x.lineTo(176, 128); x.lineTo(176, 160); x.fill();
      rect(x, '#e8a0a0', 70, 205, 14, 24); rect(x, '#e8a0a0', 130, 205, 14, 24); rect(x, '#7a5a1c', 96, 130, 30, 5); x.fillStyle = '#333'; x.beginPath(); x.arc(150, 160, 4, 0, 7); x.fill();
      x.fillStyle = GOLD; x.beginPath(); x.arc(110, 104, 14, 0, 7); x.fill(); centro(x, '€', 110, 111, `bold 18px ${SANS}`, '#7a5a1c');
      centro(x, 'hasta un 3 %', 112, 262, `bold 24px ${SANS}`, '#7a5a1c'); centro(x, 'TAE el primer año', 112, 288, `18px ${SANS}`, '#333');
    }
    centro(x, 'Pregunte en ventanilla', 112, 322, `italic 16px ${SERIF}`, '#555');
  } },
  // a notice with its title and its lines (opening hours)
  cartel_horario: { w: 240, h: 336, draw(x, w, h, tex) {
    rect(x, '#f6f4ee', 0, 0, w, h); rect(x, '#b5342c', 0, 0, w, 52); centro(x, tex.titulo || 'HORARIO', w / 2, 34, `bold 20px ${SANS}`, '#fff');
    (tex.lineas || []).forEach((l, i) => centro(x, l, w / 2, 96 + i * 42, i % 2 ? `bold 24px ${SANS}` : `19px ${SANS}`, i % 2 ? '#222' : '#555'));
  } },
  // a framed certificate (no name on it)
  diploma: { w: 304, h: 224, draw(x, w, h) {
    rect(x, '#f2e8cc', 0, 0, w, h); marco(x, '#8a6a2c', 8, 8, w - 16, h - 16, 4); marco(x, '#b89a54', 16, 16, w - 32, h - 32, 1.5);
    centro(x, 'DIPLOMA', w / 2, 58, `bold 34px ${SERIF}`, '#5a3a1c'); centro(x, 'de Gestión Administrativa', w / 2, 86, `italic 19px ${SERIF}`, '#5a3a1c');
    for (let i = 0; i < 4; i++) rect(x, '#9a8a6a', 52, 108 + i * 15, i === 3 ? 120 : 200, 2.5);
    x.fillStyle = '#b5342c'; x.beginPath(); x.arc(w - 58, h - 52, 20, 0, 7); x.fill(); rect(x, '#b5342c', w - 68, h - 36, 8, 22); rect(x, '#b5342c', w - 52, h - 36, 8, 22);
    rect(x, '#5a4a3a', 56, h - 48, 80, 2); centro(x, 'Guareña', 96, h - 30, `italic 14px ${SERIF}`, '#5a4a3a');
  } },
  // the insurer's poster (an invented one)
  cartel_seguros: { w: 240, h: 340, draw(x, w, h) {
    const g = x.createLinearGradient(0, 0, 0, h); g.addColorStop(0, '#1a3a5a'); g.addColorStop(1, '#2a5a7a'); x.fillStyle = g; x.fillRect(0, 0, w, h);
    centro(x, 'SEGUROS', w / 2, 52, `bold 32px ${SANS}`, '#fff'); centro(x, 'ENCINA', w / 2, 90, `bold 40px ${SERIF}`, '#e8c860');
    x.fillStyle = '#e8c860'; x.beginPath(); x.moveTo(40, 205); x.quadraticCurveTo(120, 90, 200, 205); x.lineTo(40, 205); x.fill(); rect(x, '#e8c860', 116, 205, 8, 60);
    x.fillStyle = '#4c8a42'; x.beginPath(); x.arc(120, 150, 42, Math.PI, 0); x.fill(); rect(x, '#6a4a2a', 116, 150, 8, 70);
    ['Hogar', 'Coche', 'Vida', 'Comercio'].forEach((t, i) => centro(x, t, w / 4 + (i % 2) * (w / 2), 262 + Math.floor(i / 2) * 28, `20px ${SANS}`, '#fff'));
    centro(x, 'Tu tranquilidad, a un paso', w / 2, 316, `italic 16px ${SERIF}`, '#cfe0ee');
  } },
  // the gym's poster of prices
  cartel_tarifas: { w: 224, h: 336, draw(x, w, h) {
    rect(x, '#25262a', 0, 0, w, h); rect(x, '#d8641c', 0, 0, w, 66); centro(x, 'TARIFAS', w / 2, 46, `bold 38px ${SANS}`, '#fff');
    [['Mensual', '29 €'], ['Trimestral', '75 €'], ['Anual', '260 €'], ['Estudiantes', '22 €'], ['Mayores', '20 €']].forEach(([a, b], i) => {
      izq(x, a, 18, 112 + i * 42, `22px ${SANS}`, '#f1efe9'); der(x, b, w - 18, 112 + i * 42, `bold 26px ${SANS}`, '#ffb070'); rect(x, '#3a3c40', 18, 122 + i * 42, w - 36, 1.5);
    });
    centro(x, 'Matrícula gratis', w / 2, 326, `bold 18px ${SANS}`, '#ffb070');
  } },
  // the week's directed classes
  cartel_clases: { w: 384, h: 288, draw(x, w, h) {
    rect(x, '#25262a', 0, 0, w, h); centro(x, 'CLASES DIRIGIDAS', w / 2, 40, `bold 28px ${SANS}`, '#ffb070');
    const dias = ['L', 'M', 'X', 'J', 'V'], filas = [['9:30', 'Pilates', '', 'Pilates', '', 'Yoga'], ['19:00', 'Ciclo', 'Baile', 'Ciclo', 'Baile', 'Ciclo'], ['20:15', 'Cross', 'Pilates', 'Cross', 'Yoga', 'Cross']];
    dias.forEach((d, i) => centro(x, d, 112 + i * 56, 80, `bold 20px ${SANS}`, '#d8641c'));
    filas.forEach((f, r) => {
      izq(x, f[0], 14, 128 + r * 56, `bold 19px ${SANS}`, '#f1efe9');
      f.slice(1).forEach((c, i) => { if (c) { rect(x, '#3a3c40', 112 + i * 56 - 26, 100 + r * 56, 52, 40); centro(x, c, 112 + i * 56, 125 + r * 56, `12px ${SANS}`, '#f1efe9'); } });
    });
  } },
  // a poster of an exercise: a stick figure and its name
  cartel_ejercicio: { w: 224, h: 316, draw(x, w, h, tex) {
    rect(x, '#25262a', 0, 0, w, h); rect(x, '#d8641c', 0, h - 56, w, 56);
    const press = tex.ejercicio === 'press';
    centro(x, press ? 'PRESS DE BANCA' : 'SENTADILLA', w / 2, h - 22, `bold 22px ${SANS}`, '#fff');
    x.strokeStyle = '#f1efe9'; x.lineWidth = 8; x.lineCap = 'round'; x.fillStyle = '#f1efe9';
    if (press) {
      rect(x, '#6a6e72', 30, 168, 164, 14); x.beginPath(); x.moveTo(60, 160); x.lineTo(160, 160); x.stroke(); // (the figure lying on the bench)
      x.beginPath(); x.arc(56, 140, 14, 0, 7); x.fill(); x.beginPath(); x.moveTo(72, 160); x.lineTo(150, 160); x.stroke(); x.beginPath(); x.moveTo(150, 160); x.lineTo(170, 200); x.moveTo(150, 160); x.lineTo(184, 190); x.stroke();
      x.beginPath(); x.moveTo(96, 160); x.lineTo(106, 100); x.stroke(); x.lineWidth = 6; x.beginPath(); x.moveTo(60, 100); x.lineTo(152, 100); x.stroke(); rect(x, '#d8641c', 50, 84, 12, 32); rect(x, '#d8641c', 150, 84, 12, 32);
    } else {
      x.beginPath(); x.arc(112, 80, 15, 0, 7); x.fill(); x.beginPath(); x.moveTo(112, 98); x.lineTo(106, 168); x.stroke(); x.beginPath(); x.moveTo(106, 168); x.lineTo(150, 188); x.lineTo(138, 244); x.stroke();
      x.lineWidth = 6; x.beginPath(); x.moveTo(60, 112); x.lineTo(166, 112); x.stroke(); rect(x, '#d8641c', 52, 96, 12, 32); rect(x, '#d8641c', 160, 96, 12, 32);
      x.lineWidth = 8; x.beginPath(); x.moveTo(110, 120); x.lineTo(130, 150); x.stroke(); rect(x, '#6a6e72', 80, 248, 100, 6);
    }
  } },
  // the gym's rules
  cartel_normas: { w: 240, h: 330, draw(x, w, h) {
    rect(x, '#f6f4ee', 0, 0, w, h); rect(x, '#b5342c', 0, 0, w, 50); centro(x, 'NORMAS', w / 2, 36, `bold 30px ${SANS}`, '#fff');
    ['Toalla siempre', 'Calzado deportivo', 'Recoge las pesas', 'Limpia el aparato', 'Prohibido gritar', 'Respeta los turnos'].forEach((t, i) => {
      x.fillStyle = '#b5342c'; x.beginPath(); x.arc(28, 90 + i * 40, 7, 0, 7); x.fill(); izq(x, t, 46, 97 + i * 40, `19px ${SANS}`, '#222');
    });
  } },
  // the chalkboard of the day's menu
  pizarra_menu: { w: 312, h: 392, draw(x, w, h, tex) {
    rect(x, '#20261f', 0, 0, w, h); x.fillStyle = 'rgba(255,255,255,0.05)'; for (let i = 0; i < 30; i++) x.fillRect((i * 83) % w, (i * 47) % h, 50, 2);
    const F = '"Marker Felt", "Comic Sans MS", cursive';
    centro(x, 'MENÚ DEL DÍA', w / 2, 46, `bold 36px ${F}`, '#f2d27a'); rect(x, '#f2efe4', 30, 58, w - 60, 2);
    const L = tex.lineas || [['PRIMEROS', ''], ['Migas extremeñas', ''], ['Ensalada de tomate', ''], ['SEGUNDOS', ''], ['Caldereta de cordero', ''], ['Bacalao dorado', ''], ['POSTRE CASERO', ''], ['Pan, bebida y café', '']];
    L.forEach(([t], i) => { const cab = t === t.toUpperCase(); centro(x, t, w / 2, 98 + i * 33 + (cab && i ? 6 : 0), cab ? `bold 22px ${F}` : `22px ${F}`, cab ? '#f2d27a' : '#f2efe4'); });
    centro(x, tex.precio || '12 €', w / 2, h - 28, `bold 40px ${F}`, '#f2d27a');
  } },
  // the sign of the «casa de comidas»
  rotulo_restaurante: { w: 810, h: 170, draw(x, w, h, tex) {
    rect(x, '#3a2418', 0, 0, w, h); marco(x, GOLD, 8, 8, w - 16, h - 16, 3);
    centro(x, (tex.titulo || 'Casa de comidas').toUpperCase(), w / 2, 92, `bold ${(tex.titulo || '').length > 14 ? 64 : 84}px ${SERIF}`, '#f2d27a'); centro(x, 'Comidas caseras · Menú del día', w / 2, 140, `italic 30px ${SERIF}`, '#e8d9b0');
  } },
};
