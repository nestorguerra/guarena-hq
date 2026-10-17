// Painted pictures for the objects of the «tiendas_a» family (data/objetos): signs, screens, labels, packaging — drawn on a
// canvas, never a photograph. Each one: tipo → { w, h, draw(ctx, w, h, tex, seed) } (tex: the part's own tex, its words…;
// a sign marked rotulo_local gets tex.titulo, the name of the business it hangs in). Read by src/objetos.js (textura).
// Every textured part instance is a mesh of its own: a handful per room. No real brand anywhere: invented names and plain shapes.

const FUENTE = '"Helvetica Neue", Arial, sans-serif';
const SERIF = 'Georgia, "Times New Roman", serif';
// a text that shrinks to fit a width
function ajustado(x, texto, cx, cy, ancho, tam, peso = 'bold', fam = FUENTE) {
  let s = tam;
  x.font = `${peso} ${s}px ${fam}`;
  while (x.measureText(texto).width > ancho && s > 8) { s -= 2; x.font = `${peso} ${s}px ${fam}`; }
  x.fillText(texto, cx, cy);
}
function ajustadoContorno(x, texto, cx, cy, ancho, tam, relleno, contorno, grosor = 6, peso = 'bold', fam = FUENTE) {
  let s = tam;
  x.font = `${peso} ${s}px ${fam}`;
  while (x.measureText(texto).width > ancho && s > 8) { s -= 2; x.font = `${peso} ${s}px ${fam}`; }
  x.lineJoin = 'round'; x.lineWidth = grosor; x.strokeStyle = contorno; x.strokeText(texto, cx, cy);
  x.fillStyle = relleno; x.fillText(texto, cx, cy);
}
function redondo(x, X, Y, w, h, r) {
  x.beginPath(); x.moveTo(X + r, Y); x.arcTo(X + w, Y, X + w, Y + h, r); x.arcTo(X + w, Y + h, X, Y + h, r); x.arcTo(X, Y + h, X, Y, r); x.arcTo(X, Y, X + w, Y, r); x.closePath();
}
function estrella(x, cx, cy, R, r, n, giro = 0) {
  x.beginPath();
  for (let i = 0; i < n * 2; i++) { const a = giro + (Math.PI * i) / n - Math.PI / 2, rr = i % 2 ? r : R; x[i ? 'lineTo' : 'moveTo'](cx + Math.cos(a) * rr, cy + Math.sin(a) * rr); }
  x.closePath();
}

export const TEXTURAS = {
  // ---------------------------------------------------------------- the variety store
  ta_rotulo_bazar: {
    w: 512, h: 128,
    draw(x, w, h, t) {
      x.fillStyle = '#f0c030'; x.fillRect(0, 0, w, h);
      x.fillStyle = '#c0302a'; x.fillRect(0, h - 26, w, 26); x.fillRect(0, 0, w, 10);
      x.fillStyle = '#f6efe0'; for (let i = 0; i < 16; i++) x.fillRect(i * 32 + 6, h - 20, 16, 14);
      x.textAlign = 'center'; x.textBaseline = 'middle';
      ajustadoContorno(x, t.titulo || t.texto || 'Bazar', w / 2, h * 0.4, w - 70, 72, '#c0302a', '#f6efe0', 9, 'bold');
      x.fillStyle = '#2a2a2e'; ajustado(x, 'HOGAR · JUGUETES · PAPELERÍA · REGALOS', w / 2, h - 52, w - 70, 17, 'bold');
    },
  },
  ta_cartel_euro: {
    w: 256, h: 176,
    draw(x, w, h) {
      x.fillStyle = '#f0d030'; x.fillRect(0, 0, w, h);
      x.fillStyle = '#c0302a'; estrella(x, w / 2, h * 0.46, 118, 96, 14, 0.1); x.fill();
      x.fillStyle = '#f6efe0'; estrella(x, w / 2, h * 0.46, 104, 84, 14, 0.1); x.fill();
      x.fillStyle = '#c0302a'; x.textAlign = 'center'; x.textBaseline = 'middle';
      ajustado(x, 'TODO A', w / 2, h * 0.3, 130, 40, 'bold'); ajustado(x, '1 €', w / 2, h * 0.62, 150, 74, 'bold');
      x.fillStyle = '#2a2a2e'; ajustado(x, 'en esta sección', w / 2, h * 0.9, 150, 16, 'normal');
    },
  },
  ta_cartel_ofertas: {
    w: 256, h: 368,
    draw(x, w, h) {
      x.fillStyle = '#c0302a'; x.fillRect(0, 0, w, h);
      x.fillStyle = '#f6efe0'; x.fillRect(14, 14, w - 28, h - 28);
      x.fillStyle = '#c0302a'; x.textAlign = 'center'; x.textBaseline = 'middle';
      ajustado(x, 'OFERTAS', w / 2, 70, w - 60, 52, 'bold');
      x.fillStyle = '#f0c030'; x.beginPath(); x.arc(w / 2, 180, 80, 0, 7); x.fill();
      x.fillStyle = '#c0302a'; x.font = `bold 78px ${FUENTE}`; x.fillText('3x2', w / 2, 176);
      x.fillStyle = '#2a2a2e'; ajustado(x, 'en menaje y plásticos', w / 2, 286, w - 50, 24, 'normal'); ajustado(x, 'hasta fin de existencias', w / 2, 320, w - 50, 18, 'normal');
    },
  },
  // ---------------------------------------------------------------- the hardware shop
  ta_rotulo_ferreteria: {
    w: 512, h: 128,
    draw(x, w, h, t) {
      x.fillStyle = '#2f3a2c'; x.fillRect(0, 0, w, h);
      x.strokeStyle = '#d8c48a'; x.lineWidth = 4; x.strokeRect(8, 8, w - 16, h - 16);
      // a spanner and a hammer crossed at each end
      x.save(); x.translate(56, h / 2); x.rotate(-0.7); x.fillStyle = '#d8c48a'; x.fillRect(-4, -30, 8, 60); x.beginPath(); x.arc(0, -32, 11, 0.3, 5.9); x.lineWidth = 7; x.strokeStyle = '#d8c48a'; x.stroke(); x.restore();
      x.save(); x.translate(56, h / 2); x.rotate(0.7); x.fillStyle = '#d8c48a'; x.fillRect(-4, -26, 8, 56); x.fillRect(-16, -32, 32, 12); x.restore();
      x.save(); x.translate(w - 56, h / 2); x.rotate(0.7); x.fillStyle = '#d8c48a'; x.fillRect(-4, -30, 8, 60); x.beginPath(); x.arc(0, -32, 11, 0.3, 5.9); x.lineWidth = 7; x.strokeStyle = '#d8c48a'; x.stroke(); x.restore();
      x.save(); x.translate(w - 56, h / 2); x.rotate(-0.7); x.fillStyle = '#d8c48a'; x.fillRect(-4, -26, 8, 56); x.fillRect(-16, -32, 32, 12); x.restore();
      x.fillStyle = '#f2e8c8'; x.textAlign = 'center'; x.textBaseline = 'middle';
      ajustado(x, t.titulo || t.texto || 'Ferretería', w / 2, h * 0.42, w - 200, 56, 'bold', SERIF);
      x.fillStyle = '#d8c48a'; ajustado(x, 'FERRETERÍA · PINTURAS · MENAJE', w / 2, h * 0.78, w - 200, 17, 'normal');
    },
  },
  ta_cartel_llaves: {
    w: 256, h: 128,
    draw(x, w, h) {
      x.fillStyle = '#f0c030'; x.fillRect(0, 0, w, h);
      x.strokeStyle = '#2a2a2e'; x.lineWidth = 4; x.strokeRect(6, 6, w - 12, h - 12);
      // a key
      x.fillStyle = '#2a2a2e'; x.beginPath(); x.arc(44, 64, 20, 0, 7); x.fill(); x.fillStyle = '#f0c030'; x.beginPath(); x.arc(44, 64, 8, 0, 7); x.fill();
      x.fillStyle = '#2a2a2e'; x.fillRect(60, 59, 56, 10); x.fillRect(96, 69, 8, 14); x.fillRect(108, 69, 8, 10);
      x.textAlign = 'left'; x.textBaseline = 'middle'; ajustado(x, 'COPIA DE', 126, 48, 118, 30, 'bold'); ajustado(x, 'LLAVES', 126, 80, 118, 34, 'bold');
      x.textAlign = 'center'; ajustado(x, 'al momento · todo tipo', w / 2, 110, w - 30, 14, 'normal');
    },
  },
  ta_cartel_pinturas: {
    w: 256, h: 176,
    draw(x, w, h) {
      x.fillStyle = '#eeeae0'; x.fillRect(0, 0, w, h);
      const cols = ['#d23a2c', '#ee8a2a', '#f0c030', '#3f9a4a', '#2aa6a6', '#2f64b4', '#7a4aa0', '#e76a9a'];
      cols.forEach((c, i) => { x.fillStyle = c; x.fillRect(i * (w / 8), 0, w / 8, 44); });
      x.fillStyle = '#2a2a2e'; x.textAlign = 'center'; x.textBaseline = 'middle';
      ajustado(x, 'PINTURAS Y BARNICES', w / 2, 80, w - 24, 26, 'bold'); ajustado(x, 'Te preparamos el color', w / 2, 112, w - 30, 20, 'normal'); ajustado(x, 'que quieras', w / 2, 136, w - 30, 20, 'normal');
      cols.forEach((c, i) => { x.fillStyle = c; x.fillRect(i * (w / 8), h - 16, w / 8, 16); });
    },
  },
  // ---------------------------------------------------------------- the bookshop
  ta_rotulo_libreria: {
    w: 512, h: 128,
    draw(x, w, h, t) {
      x.fillStyle = '#3a2616'; x.fillRect(0, 0, w, h);
      x.strokeStyle = '#c8a040'; x.lineWidth = 3; x.strokeRect(8, 8, w - 16, h - 16); x.lineWidth = 1; x.strokeRect(14, 14, w - 28, h - 28);
      // an open book at each end
      for (const cx of [58, w - 58]) {
        x.fillStyle = '#c8a040'; x.beginPath(); x.moveTo(cx, h / 2 - 14); x.lineTo(cx - 34, h / 2 - 22); x.lineTo(cx - 34, h / 2 + 18); x.lineTo(cx, h / 2 + 26); x.lineTo(cx + 34, h / 2 + 18); x.lineTo(cx + 34, h / 2 - 22); x.closePath(); x.fill();
        x.strokeStyle = '#3a2616'; x.lineWidth = 2; x.beginPath(); x.moveTo(cx, h / 2 - 14); x.lineTo(cx, h / 2 + 26); x.stroke();
      }
      x.fillStyle = '#f0dfa8'; x.textAlign = 'center'; x.textBaseline = 'middle';
      ajustado(x, t.titulo || t.texto || 'Librería', w / 2, h * 0.43, w - 220, 54, 'italic bold', SERIF);
      x.fillStyle = '#c8a040'; ajustado(x, 'LIBROS · PAPELERÍA · PRENSA', w / 2, h * 0.8, w - 220, 16, 'normal', SERIF);
    },
  },
  ta_cartel_novedades: {
    w: 256, h: 88,
    draw(x, w, h) {
      x.fillStyle = '#2f5a3a'; x.fillRect(0, 0, w, h);
      x.strokeStyle = '#e0c070'; x.lineWidth = 2; x.strokeRect(5, 5, w - 10, h - 10);
      x.fillStyle = '#f0dfa8'; x.textAlign = 'center'; x.textBaseline = 'middle';
      ajustado(x, 'NOVEDADES', w / 2, h * 0.5, w - 40, 40, 'bold', SERIF);
      x.fillStyle = '#e0c070'; for (const px of [24, w - 24]) { estrella(x, px, h / 2, 9, 4, 5); x.fill(); }
    },
  },
  ta_cartel_texto: {
    w: 256, h: 88,
    draw(x, w, h) {
      x.fillStyle = '#27406e'; x.fillRect(0, 0, w, h);
      x.fillStyle = '#f0c030'; x.fillRect(0, h - 10, w, 10);
      x.fillStyle = '#f6efe0'; x.textAlign = 'center'; x.textBaseline = 'middle';
      ajustado(x, 'LIBROS DE TEXTO', w / 2, h * 0.32, w - 30, 28, 'bold'); ajustado(x, 'Material escolar · Papelería', w / 2, h * 0.64, w - 30, 18, 'normal');
    },
  },
  // ---------------------------------------------------------------- the toyshop
  ta_rotulo_jugueteria: {
    w: 512, h: 128,
    draw(x, w, h, t) {
      x.fillStyle = '#2f64b4'; x.fillRect(0, 0, w, h);
      x.fillStyle = '#f0c030'; x.fillRect(0, 0, w, 12); x.fillRect(0, h - 12, w, 12);
      const cols = ['#d23a2c', '#f0c030', '#3f9a4a', '#e76a9a', '#ee8a2a', '#2aa6a6'];
      for (let i = 0; i < 12; i++) { x.fillStyle = cols[i % 6]; estrella(x, 22 + i * 42, h - 28, 9, 4, 5, i * 0.3); x.fill(); }
      x.textAlign = 'center'; x.textBaseline = 'middle';
      ajustadoContorno(x, t.titulo || t.texto || 'Juguetería', w / 2, h * 0.42, w - 70, 66, '#f6efe0', '#c0302a', 8, 'bold');
      x.fillStyle = '#f6efe0'; ajustado(x, 'JUGUETES · JUEGOS · BICICLETAS', w / 2, h * 0.73, w - 100, 16, 'bold');
    },
  },
  ta_cartel_juguetes: {
    w: 256, h: 352,
    draw(x, w, h) {
      x.fillStyle = '#e76a9a'; x.fillRect(0, 0, w, h);
      x.fillStyle = '#f6efe0'; redondo(x, 14, 14, w - 28, h - 28, 18); x.fill();
      x.fillStyle = '#2f64b4'; x.textAlign = 'center'; x.textBaseline = 'middle';
      ajustado(x, 'GRAN', w / 2, 64, w - 50, 34, 'bold'); ajustado(x, 'CAMPAÑA', w / 2, 108, w - 50, 46, 'bold'); ajustado(x, 'DE JUGUETES', w / 2, 152, w - 50, 32, 'bold');
      const cols = ['#d23a2c', '#f0c030', '#3f9a4a', '#2aa6a6', '#7a4aa0'];
      cols.forEach((c, i) => { x.fillStyle = c; x.beginPath(); x.arc(46 + i * 41, 220, 17, 0, 7); x.fill(); });
      x.fillStyle = '#c0302a'; ajustado(x, 'hasta -30 %', w / 2, 284, w - 50, 32, 'bold'); x.fillStyle = '#2a2a2e'; ajustado(x, 'en juegos y muñecas', w / 2, 316, w - 50, 16, 'normal');
    },
  },
  ta_cartel_reyes: {
    w: 128, h: 96,
    draw(x, w, h) {
      x.fillStyle = '#f6efe0'; x.fillRect(0, 0, w, h);
      x.fillStyle = '#e0b030'; x.beginPath(); x.moveTo(24, 40); x.lineTo(24, 18); x.lineTo(46, 30); x.lineTo(64, 12); x.lineTo(82, 30); x.lineTo(104, 18); x.lineTo(104, 40); x.closePath(); x.fill();
      x.fillStyle = '#c0302a'; x.fillRect(24, 40, 80, 8);
      x.fillStyle = '#2a2a2e'; x.textAlign = 'center'; x.textBaseline = 'middle'; ajustado(x, 'CARTAS A LOS', w / 2, 62, w - 12, 12, 'bold'); ajustado(x, 'REYES MAGOS', w / 2, 80, w - 12, 14, 'bold');
    },
  },
  // ---------------------------------------------------------------- the florist
  ta_rotulo_floristeria: {
    w: 512, h: 128,
    draw(x, w, h, t) {
      x.fillStyle = '#3f5a3a'; x.fillRect(0, 0, w, h);
      x.strokeStyle = '#d8e8c8'; x.lineWidth = 3; x.strokeRect(8, 8, w - 16, h - 16);
      // a flower at each end: petals round a yellow heart
      for (const [cx, col] of [[56, '#e76a9a'], [w - 56, '#f0c030']]) {
        x.fillStyle = '#6f9a5a'; x.fillRect(cx - 2, h / 2 + 8, 4, 34); x.beginPath(); x.ellipse(cx + 12, h / 2 + 30, 12, 5, -0.5, 0, 7); x.fill();
        x.fillStyle = col; for (let i = 0; i < 6; i++) { const a = (i / 6) * Math.PI * 2; x.beginPath(); x.ellipse(cx + Math.cos(a) * 15, h / 2 - 8 + Math.sin(a) * 15, 11, 7, a, 0, 7); x.fill(); }
        x.fillStyle = '#f6efe0'; x.beginPath(); x.arc(cx, h / 2 - 8, 8, 0, 7); x.fill();
      }
      x.fillStyle = '#f2f6e8'; x.textAlign = 'center'; x.textBaseline = 'middle';
      ajustado(x, t.titulo || t.texto || 'Floristería', w / 2, h * 0.42, w - 220, 56, 'italic', SERIF);
      x.fillStyle = '#c8dcb0'; ajustado(x, 'FLORES · PLANTAS · RAMOS · CENTROS', w / 2, h * 0.8, w - 220, 15, 'normal');
    },
  },
  ta_pizarra_flores: {
    w: 256, h: 352,
    draw(x, w, h) {
      x.fillStyle = '#24302a'; x.fillRect(0, 0, w, h);
      x.strokeStyle = 'rgba(255,255,255,0.12)'; x.lineWidth = 6; for (let i = 0; i < 6; i++) { x.beginPath(); x.moveTo(20, 40 + i * 58); x.lineTo(w - 20, 44 + i * 58); x.stroke(); }
      x.fillStyle = '#f2efe4'; x.textAlign = 'center'; x.textBaseline = 'middle';
      x.font = 'bold 26px "Marker Felt", "Comic Sans MS", cursive'; x.fillText('Hoy en la tienda', w / 2, 34);
      const L = [['Rosas', '2,50 €'], ['Claveles', '1,50 €'], ['Girasoles', '3 €'], ['Ramo del día', '12 €'], ['Centro de mesa', '25 €'], ['Planta de interior', '9 €']];
      L.forEach(([a, b], i) => { x.textAlign = 'left'; x.font = '21px "Marker Felt", "Comic Sans MS", cursive'; x.fillText(a, 22, 82 + i * 42); x.textAlign = 'right'; x.fillStyle = '#f2d27a'; x.fillText(b, w - 22, 82 + i * 42); x.fillStyle = '#f2efe4'; });
      x.textAlign = 'center'; x.font = '16px "Marker Felt", "Comic Sans MS", cursive'; x.fillText('Encargos para el día de la Madre', w / 2, 336);
    },
  },
  ta_cartel_ramos: {
    w: 256, h: 176,
    draw(x, w, h) {
      x.fillStyle = '#f2f0e4'; x.fillRect(0, 0, w, h);
      x.fillStyle = '#6f9a5a'; x.fillRect(0, 0, w, 36);
      x.fillStyle = '#f6f6ea'; x.textAlign = 'center'; x.textBaseline = 'middle'; ajustado(x, 'SERVICIO A DOMICILIO', w / 2, 19, w - 20, 21, 'bold');
      x.fillStyle = '#2f3a2c'; ajustado(x, 'Ramos · Centros', w / 2, 72, w - 24, 30, 'bold'); ajustado(x, 'Plantas · Coronas', w / 2, 108, w - 24, 26, 'normal'); ajustado(x, 'Bodas y celebraciones', w / 2, 142, w - 24, 20, 'italic', SERIF);
    },
  },
  // ---------------------------------------------------------------- the estanco (tobacco, lottery and press): plain words, no logo, no brand
  ta_rotulo_estanco: {
    w: 512, h: 128,
    draw(x, w, h, t) {
      x.fillStyle = '#3a1f1a'; x.fillRect(0, 0, w, h);
      x.strokeStyle = '#d8b040'; x.lineWidth = 3; x.strokeRect(8, 8, w - 16, h - 16);
      x.fillStyle = '#d8b040'; for (const cx of [44, w - 44]) { x.beginPath(); x.moveTo(cx, h / 2 - 22); x.lineTo(cx + 16, h / 2); x.lineTo(cx, h / 2 + 22); x.lineTo(cx - 16, h / 2); x.closePath(); x.fill(); }
      x.fillStyle = '#f2e2b0'; x.textAlign = 'center'; x.textBaseline = 'middle';
      ajustado(x, t.titulo || t.texto || 'Estanco', w / 2, h * 0.42, w - 150, 58, 'bold', SERIF);
      x.fillStyle = '#d8b040'; ajustado(x, 'TABACOS · PRENSA · LOTERÍA', w / 2, h * 0.78, w - 150, 17, 'normal');
    },
  },
  ta_cartel_recargas: {
    w: 256, h: 176,
    draw(x, w, h) {
      x.fillStyle = '#2a2a2e'; x.fillRect(0, 0, w, h);
      x.fillStyle = '#f0c030'; redondo(x, 10, 10, w - 20, h - 20, 12); x.fill();
      x.fillStyle = '#2a2a2e'; x.textAlign = 'center'; x.textBaseline = 'middle';
      ajustado(x, 'RECARGAS', w / 2 - 14, 50, w - 90, 44, 'bold'); ajustado(x, 'DE MÓVIL', w / 2 - 14, 92, w - 90, 36, 'bold'); ajustado(x, 'Tarjetas prepago y más', w / 2, 132, w - 40, 18, 'normal');
      x.fillRect(w - 48, 24, 20, 34); x.fillStyle = '#f0c030'; x.fillRect(w - 45, 29, 14, 20);
    },
  },
  ta_cartel_loteria: {
    w: 256, h: 100,
    draw(x, w, h) {
      x.fillStyle = '#2f5a3a'; x.fillRect(0, 0, w, h);
      x.strokeStyle = '#e0c070'; x.lineWidth = 2; x.strokeRect(5, 5, w - 10, h - 10);
      x.fillStyle = '#e0c070'; x.beginPath(); for (let i = 0; i < 4; i++) { const a = (i / 4) * Math.PI * 2; x.moveTo(34 + Math.cos(a) * 3, h / 2 + Math.sin(a) * 3); x.arc(34 + Math.cos(a) * 11, h / 2 + Math.sin(a) * 11, 10, 0, 7); } x.fill();
      x.fillStyle = '#f6efe0'; x.textAlign = 'center'; x.textBaseline = 'middle';
      ajustado(x, 'LOTERÍA', w / 2 + 14, h * 0.34, w - 90, 38, 'bold', SERIF); x.fillStyle = '#e0c070'; ajustado(x, 'DÉCIMOS · APUESTAS · BOLETOS', w / 2 + 14, h * 0.7, w - 90, 15, 'normal');
    },
  },
  ta_cartel_sellos: {
    w: 256, h: 150,
    draw(x, w, h) {
      x.fillStyle = '#27406e'; x.fillRect(0, 0, w, h);
      x.fillStyle = '#f6efe0'; x.textAlign = 'center'; x.textBaseline = 'middle';
      ajustado(x, 'SELLOS', w / 2, 44, w - 40, 44, 'bold'); ajustado(x, 'Franqueo y envíos', w / 2, 88, w - 40, 24, 'normal');
      for (let i = 0; i < 6; i++) { x.fillStyle = ['#d23a2c', '#f0c030', '#3f9a4a', '#e76a9a', '#2aa6a6', '#ee8a2a'][i]; x.fillRect(24 + i * 36, 112, 28, 26); x.strokeStyle = '#f6efe0'; x.setLineDash([3, 3]); x.strokeRect(22 + i * 36, 110, 32, 30); }
    },
  },
  ta_cartel_menores: {
    w: 192, h: 128,
    draw(x, w, h) {
      x.fillStyle = '#f6f4ec'; x.fillRect(0, 0, w, h);
      x.strokeStyle = '#c0302a'; x.lineWidth = 7; x.beginPath(); x.arc(34, h / 2, 24, 0, 7); x.stroke(); x.beginPath(); x.moveTo(18, h / 2 + 16); x.lineTo(50, h / 2 - 16); x.stroke();
      x.fillStyle = '#2a2a2e'; x.textAlign = 'left'; x.textBaseline = 'middle';
      ajustado(x, 'PROHIBIDA LA VENTA', 66, 36, w - 74, 16, 'bold'); ajustado(x, 'DE TABACO A', 66, 60, w - 74, 16, 'bold'); ajustado(x, 'MENORES DE 18 AÑOS', 66, 84, w - 74, 14, 'bold');
    },
  },
  // ---------------------------------------------------------------- the jeweller-watchmaker / optician
  ta_rotulo_joyeria: {
    w: 512, h: 128,
    draw(x, w, h, t) {
      x.fillStyle = '#17120f'; x.fillRect(0, 0, w, h);
      const g = x.createLinearGradient(0, 0, w, 0); g.addColorStop(0, '#a8842a'); g.addColorStop(0.5, '#f0d680'); g.addColorStop(1, '#a8842a');
      x.strokeStyle = g; x.lineWidth = 3; x.strokeRect(8, 8, w - 16, h - 16); x.lineWidth = 1; x.strokeRect(14, 14, w - 28, h - 28);
      // a diamond at each end
      for (const cx of [50, w - 50]) { x.fillStyle = g; x.beginPath(); x.moveTo(cx - 20, h / 2 - 8); x.lineTo(cx - 10, h / 2 - 22); x.lineTo(cx + 10, h / 2 - 22); x.lineTo(cx + 20, h / 2 - 8); x.lineTo(cx, h / 2 + 22); x.closePath(); x.fill(); x.strokeStyle = '#17120f'; x.lineWidth = 1.5; x.beginPath(); x.moveTo(cx - 20, h / 2 - 8); x.lineTo(cx + 20, h / 2 - 8); x.moveTo(cx - 10, h / 2 - 22); x.lineTo(cx, h / 2 - 8); x.lineTo(cx + 10, h / 2 - 22); x.stroke(); }
      x.textAlign = 'center'; x.textBaseline = 'middle'; x.fillStyle = g;
      ajustado(x, t.titulo || t.texto || 'Joyería', w / 2, h * 0.42, w - 190, 56, 'italic', SERIF); x.fillStyle = '#d8c080'; ajustado(x, 'JOYERÍA · RELOJERÍA · ÓPTICA', w / 2, h * 0.78, w - 190, 15, 'normal', SERIF);
    },
  },
  ta_cartel_optica: {
    w: 256, h: 176,
    draw(x, w, h) {
      x.fillStyle = '#1f2a4a'; x.fillRect(0, 0, w, h);
      x.strokeStyle = '#f6efe0'; x.lineWidth = 6; x.beginPath(); x.arc(78, 48, 26, 0, 7); x.stroke(); x.beginPath(); x.arc(178, 48, 26, 0, 7); x.stroke(); x.beginPath(); x.moveTo(104, 44); x.lineTo(152, 44); x.stroke();
      x.fillStyle = '#f6efe0'; x.textAlign = 'center'; x.textBaseline = 'middle';
      ajustado(x, 'ÓPTICA', w / 2, 102, w - 30, 34, 'bold'); ajustado(x, 'Graduamos su vista', w / 2, 132, w - 30, 20, 'normal'); ajustado(x, 'Gafas y lentillas', w / 2, 156, w - 30, 18, 'normal');
    },
  },
  ta_cartel_arreglos: {
    w: 192, h: 128,
    draw(x, w, h) {
      x.fillStyle = '#2a2a2e'; x.fillRect(0, 0, w, h);
      const g = x.createLinearGradient(0, 0, w, 0); g.addColorStop(0, '#a8842a'); g.addColorStop(0.5, '#f0d680'); g.addColorStop(1, '#a8842a');
      x.strokeStyle = g; x.lineWidth = 2; x.strokeRect(6, 6, w - 12, h - 12); x.fillStyle = g; x.textAlign = 'center'; x.textBaseline = 'middle';
      ajustado(x, 'ARREGLOS', w / 2, 40, w - 30, 30, 'bold', SERIF); ajustado(x, 'Pilas de reloj', w / 2, 74, w - 30, 18, 'normal', SERIF); ajustado(x, 'Grabados · Correas', w / 2, 98, w - 30, 18, 'normal', SERIF);
    },
  },
};
