# Guareña HQ — reglas para trabajar en este proyecto

Juego de mundo abierto del Guareña real en el navegador (three.js). Esta copia (HQ) es donde se prueba el
**hiperrealismo**, empezando por la zona de la iglesia de Santa María.

## Las fuentes de verdad (no adivinar nunca)
- `docs/hiperrealismo.md`: qué se construye y cómo — el mundo, la iglesia con sus medidas, los materiales, la luz, las
  fases y lo que hace falta para dar cada una por buena. Si algo no está ahí, se pregunta o se añade antes de hacerlo.
- `docs/hiperrealismo-registro.md`: cada comentario del usuario y cada arreglo, con su motivo. Se lee antes de empezar
  y se escribe al acabar: el siguiente paso empieza sabiendo lo que ya se aprendió.
- Los datos reales: el Catastro (`data/map.json`), las ortofotos del PNOA (solo para medir; las teselas no salen de
  `.cache/pnoa`), los textos publicados (BOE, estudios) y fotos libres de Wikimedia Commons, **solo como referencia**:
  en el juego no entra ni un píxel de ninguna foto. Nada de Google ni Street View.

## Cómo se trabaja
1. Se modela en **Blender** (5.2 LTS, `/Applications/Blender.app`), con scripts de Python en `tools/blender/`, sin
   abrir su ventana: `Blender --background --factory-startup --python tools/blender/iglesia.py -- …`. Cada pieza sale
   en glTF a `assets/hq/`. Nada se hace a mano: el script es el modelo.
2. Primero un **greybox** (los volúmenes a su medida, en gris), comparado con las referencias desde los mismos puntos de
   vista; luego el detalle, los materiales y la luz, capa por capa.
3. **El que construye nunca aprueba.** Cada paso lo revisa un agente revisor aparte, que solo mira (capturas del juego
   frente a las referencias y el documento de diseño) y dice «aprobado» o qué falta. Su veredicto va al registro.
4. El usuario da el visto bueno final; sus comentarios («demasiado oscuro al atardecer») se apuntan con su motivo.

## Reglas de siempre
- Las pruebas, **siempre sin sonido**: el Chrome sin ventana con `--mute-audio`, nunca `--autoplay-policy`.
- Texturas: solo CC0 (Poly Haven, ambientCG) o propias, con su crédito en `docs/hiperrealismo.md`. Las originales, en
  `.cache/` (fuera del repositorio); al juego van versiones optimizadas.
- Nada se publica (commit, GitHub Pages, artefactos) sin que el usuario lo pida.
- Mensajes de commit en español: un título y viñetas, terminados con la línea Co-Authored-By.
- La HQ guarda su propia partida y sus salas online: no tocar las claves de la Evolución ni de la fija.
