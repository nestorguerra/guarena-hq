// Painted pictures for the objects of the «comercio» family (data/objetos): signs, screens, labels, packaging — drawn on a
// canvas, never a photograph. Each one: tipo → { w, h, draw(ctx, w, h, tex, seed) } (tex: the part's own tex, its words…).
// Read by src/objetos.js (textura). Every textured part instance is a mesh of its own: a handful per room.
// No real brand anywhere: invented names and plain shapes.

const FUENTE = '"Helvetica Neue", Arial, sans-serif';
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
function cruz(x, cx, cy, r, c1, c2) {
  const a = r * 0.34;
  x.fillStyle = c1;
  x.fillRect(cx - a, cy - r, a * 2, r * 2); x.fillRect(cx - r, cy - a, r * 2, a * 2);
  if (c2) { x.fillStyle = c2; const b = a * 0.62; x.fillRect(cx - b, cy - r * 0.86, b * 2, r * 1.72); x.fillRect(cx - r * 0.86, cy - b, r * 1.72, b * 2); }
}

export const TEXTURAS = {
  // the shop's own sign: its name on a plate (the clothes shop's, over the counter)
  rotulo: {
    w: 512, h: 128,
    draw(x, w, h, t) {
      x.fillStyle = t.fondo || '#2d3f35'; x.fillRect(0, 0, w, h);
      x.strokeStyle = t.color || '#f2e8c8'; x.lineWidth = 3; x.strokeRect(8, 8, w - 16, h - 16);
      x.fillStyle = t.color || '#f2e8c8'; x.textAlign = 'center'; x.textBaseline = 'middle';
      ajustado(x, t.titulo || t.texto || 'Moda', w / 2, t.sub ? h * 0.42 : h / 2, w - 60, 58, 'bold', 'Georgia, serif');
      if (t.sub) ajustado(x, t.sub, w / 2, h * 0.76, w - 70, 22, 'normal', FUENTE);
    },
  },
  cartel_rebajas: {
    w: 256, h: 368,
    draw(x, w, h) {
      x.fillStyle = '#c0302a'; x.fillRect(0, 0, w, h);
      x.fillStyle = '#f6efe0'; x.fillRect(14, 14, w - 28, h - 28);
      x.fillStyle = '#c0302a'; x.textAlign = 'center'; x.textBaseline = 'middle';
      ajustado(x, 'REBAJAS', w / 2, 80, w - 50, 54, 'bold');
      x.font = `bold 110px ${FUENTE}`; x.fillText('-30%', w / 2, 190);
      x.fillStyle = '#2a2a2e'; ajustado(x, 'en toda la tienda', w / 2, 270, w - 50, 26, 'normal');
      ajustado(x, 'hasta fin de existencias', w / 2, 306, w - 50, 20, 'normal');
    },
  },
  // a fashion print: a stylised figure in flat colours (never a photograph)
  cartel_moda: {
    w: 256, h: 368,
    draw(x, w, h, t) {
      const e = t.estilo || 1, fondo = e === 1 ? '#e9d8c8' : '#cfdcd6', prenda = e === 1 ? '#b3342a' : '#2c5aa0', piel = '#d8b9a0';
      x.fillStyle = fondo; x.fillRect(0, 0, w, h);
      x.fillStyle = e === 1 ? '#f4ebe0' : '#e6efe9'; x.beginPath(); x.arc(w * 0.5, h * 0.4, w * 0.42, 0, 7); x.fill();
      x.fillStyle = piel; x.beginPath(); x.ellipse(w / 2, h * 0.2, 22, 28, 0, 0, 7); x.fill(); x.fillRect(w / 2 - 7, h * 0.24, 14, 22);
      x.fillStyle = prenda; x.beginPath(); x.moveTo(w / 2 - 38, h * 0.3); x.lineTo(w / 2 + 38, h * 0.3); x.lineTo(w / 2 + 70, h * 0.84); x.lineTo(w / 2 - 70, h * 0.84); x.closePath(); x.fill();
      x.fillStyle = piel; x.fillRect(w / 2 - 22, h * 0.84, 10, 46); x.fillRect(w / 2 + 12, h * 0.84, 10, 46);
      x.fillStyle = '#2a2a2e'; x.textAlign = 'center'; x.font = `bold 20px Georgia, serif`; x.fillText(e === 1 ? 'Otoño' : 'Verano', w / 2, h - 22);
    },
  },
  // the pharmacy's green cross, lit
  cruz_farmacia: {
    w: 256, h: 256,
    draw(x, w, h, t) {
      x.fillStyle = '#16201a'; x.fillRect(0, 0, w, h);
      cruz(x, w / 2, h * 0.42, 78, '#25b34a', '#7ff29a');
      x.fillStyle = '#d8f5de'; x.textAlign = 'center'; x.textBaseline = 'middle';
      ajustado(x, t.texto || 'FARMACIA', w / 2, h * 0.88, w - 40, 34, 'bold');
    },
  },
  // the ticket display: the turn being served, in red LED digits
  turno: {
    w: 256, h: 96,
    draw(x, w, h, t) {
      x.fillStyle = '#0c0c0e'; x.fillRect(0, 0, w, h);
      x.fillStyle = '#ff3b2a'; x.textAlign = 'left'; x.textBaseline = 'middle';
      x.font = `bold 22px ${FUENTE}`; x.fillText('TURNO', 14, 24);
      x.font = `bold 62px "Courier New", monospace`; x.fillText(t.numero || '042', 120, 52);
      x.fillStyle = '#ffb02a'; x.font = `bold 18px ${FUENTE}`; x.fillText('MOSTRADOR 1', 14, 78);
      x.fillStyle = '#ff3b2a'; x.beginPath(); x.moveTo(228, 40); x.lineTo(246, 52); x.lineTo(228, 64); x.closePath(); x.fill();
    },
  },
  pantalla_promo: {
    w: 256, h: 144,
    draw(x, w, h, t) {
      const g = x.createLinearGradient(0, 0, w, h); g.addColorStop(0, t.a || '#1f8a5a'); g.addColorStop(1, t.b || '#7fd6a8');
      x.fillStyle = g; x.fillRect(0, 0, w, h);
      x.fillStyle = 'rgba(255,255,255,0.18)'; x.beginPath(); x.arc(w * 0.82, h * 0.3, 46, 0, 7); x.fill();
      cruz(x, w * 0.82, h * 0.3, 24, '#ffffff');
      x.fillStyle = '#ffffff'; x.textAlign = 'left'; x.textBaseline = 'middle';
      ajustado(x, t.titulo || 'Cuida tu piel', 16, h * 0.34, w * 0.58, 30, 'bold');
      x.textAlign = 'left'; ajustado(x, t.sub || 'Protección solar todo el año', 16, h * 0.66, w * 0.7, 17, 'normal');
      x.fillStyle = 'rgba(0,0,0,0.25)'; x.fillRect(0, h - 22, w, 22); x.fillStyle = '#fff'; x.font = `13px ${FUENTE}`; x.fillText('Pregunte a su farmacéutico', 12, h - 11);
    },
  },
  // the blood-pressure machine's small screen
  tensiometro: {
    w: 128, h: 64,
    draw(x, w, h) {
      x.fillStyle = '#b8d4b0'; x.fillRect(0, 0, w, h);
      x.fillStyle = '#23402c'; x.textAlign = 'left'; x.textBaseline = 'middle';
      x.font = `bold 30px "Courier New", monospace`; x.fillText('124/78', 8, 24);
      x.font = `bold 14px ${FUENTE}`; x.fillText('mmHg', 92, 18); x.fillText('PULSO 68', 8, 52);
      x.fillStyle = '#c0302a'; x.beginPath(); x.arc(112, 50, 6, 0, 7); x.fill();
    },
  },
  horario: {
    w: 256, h: 320,
    draw(x, w, h) {
      x.fillStyle = '#f4f1e8'; x.fillRect(0, 0, w, h);
      x.fillStyle = '#1f7a40'; x.fillRect(0, 0, w, 62); cruz(x, 34, 31, 20, '#ffffff');
      x.fillStyle = '#ffffff'; x.textAlign = 'left'; x.textBaseline = 'middle'; ajustado(x, 'HORARIO', 66, 31, w - 80, 30, 'bold');
      x.fillStyle = '#23262a'; x.textAlign = 'center';
      const L = [['Lunes a viernes', '9:30 – 14:00', '17:00 – 20:30'], ['Sábados', '9:30 – 14:00', ''], ['Domingos', 'Cerrado', '']];
      L.forEach(([a, b, c], i) => { const y = 96 + i * 72; x.font = `bold 20px ${FUENTE}`; x.fillText(a, w / 2, y); x.font = `19px ${FUENTE}`; x.fillText(b, w / 2, y + 24); if (c) x.fillText(c, w / 2, y + 46); });
      x.fillStyle = '#1f7a40'; x.fillRect(20, h - 30, w - 40, 3);
    },
  },
  cartel_guardia: {
    w: 256, h: 360,
    draw(x, w, h) {
      x.fillStyle = '#e8f2ea'; x.fillRect(0, 0, w, h);
      x.fillStyle = '#1f7a40'; x.fillRect(0, 0, w, 14); x.fillRect(0, h - 14, w, 14);
      cruz(x, w / 2, 96, 52, '#25b34a', '#7ff29a');
      x.fillStyle = '#1f3a2a'; x.textAlign = 'center'; x.textBaseline = 'middle';
      ajustado(x, 'FARMACIA DE GUARDIA', w / 2, 188, w - 30, 28, 'bold'); ajustado(x, 'Consulte la farmacia', w / 2, 228, w - 40, 20, 'normal'); ajustado(x, 'de guardia más cercana', w / 2, 254, w - 40, 20, 'normal');
      x.fillStyle = '#1f7a40'; ajustado(x, 'Tablón del Colegio de Farmacéuticos', w / 2, 316, w - 40, 15, 'normal');
    },
  },
  // a hanging section sign of the supermarket
  seccion: {
    w: 512, h: 128,
    draw(x, w, h, t) {
      x.fillStyle = t.fondo || '#2f7a3a'; x.fillRect(0, 0, w, h);
      x.fillStyle = 'rgba(255,255,255,0.14)'; x.fillRect(0, h - 22, w, 22);
      x.fillStyle = t.color || '#ffffff'; x.textAlign = 'center'; x.textBaseline = 'middle';
      ajustado(x, t.texto || 'SECCIÓN', w / 2, h * 0.44, w - 50, 64, 'bold');
      if (t.sub) ajustado(x, t.sub, w / 2, h - 11, w - 60, 16, 'normal');
    },
  },
  caja_numero: {
    w: 128, h: 128,
    draw(x, w, h, t) {
      x.fillStyle = '#0c0c0e'; x.fillRect(0, 0, w, h);
      x.fillStyle = '#25b34a'; x.textAlign = 'center'; x.textBaseline = 'middle';
      x.font = `bold 22px ${FUENTE}`; x.fillText('CAJA', w / 2, 26);
      x.font = `bold 78px ${FUENTE}`; x.fillText(String(t.n || 1), w / 2, 82);
    },
  },
  cartel_oferta: {
    w: 256, h: 256,
    draw(x, w, h, t) {
      x.fillStyle = '#f2c21a'; x.fillRect(0, 0, w, h);
      x.fillStyle = '#c0302a'; x.fillRect(0, 0, w, 54);
      x.fillStyle = '#ffffff'; x.textAlign = 'center'; x.textBaseline = 'middle'; ajustado(x, 'OFERTA', w / 2, 28, w - 30, 38, 'bold');
      x.fillStyle = '#23262a'; x.font = `bold 96px ${FUENTE}`; x.fillText(t.texto || '2x1', w / 2, 138);
      ajustado(x, t.sub || 'en toda la gama', w / 2, 214, w - 30, 24, 'normal');
    },
  },
};
