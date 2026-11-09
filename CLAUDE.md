# Notas del repositorio

## Proyectos
- `chelibo/`: web del foodtruck Chelibo. Instagram: https://www.instagram.com/chelibo_
- Demo de efecto liquid glass hecha con CSS y filtros SVG, sin librerías. Estaba en `index.html` (raíz);
  se quitó del repositorio a petición del usuario. Sigue publicada en https://claude.ai/artifact/U8yybTZ72LtNHv6WZLiuXz
  y su código está en el historial de git (commit e512da7).
- La librería "websiteglass" no existe en npm y websiteglass.com no es accesible desde las sesiones en la nube.

## Chelibo
- Plantilla: `chelibo/src/pagina.html`. No edites `chelibo/index.html` a mano: se genera.
- Generar: `python3 chelibo/build.py` (escribe `chelibo/index.html` y `chelibo/assets/favicon.svg`).
- Tres versiones de la web, con `version` en `CHELIBO` (o `#moderna` / `#sello` / `#navidad` al final del enlace):
  - 'moderna': la primera, con la entrada de la moneda dorada y sin decoración de temporada.
  - 'sello': la entrada del tampón de madera y el fuego, sin decoración.
  - 'navidad': la del tampón con el tema navideño. Es la que tiene puesta la plantilla (y `index.html`).
  Cada versión es una entrada (`intro`) y un tema (`tema`), en `VERSIONES` al principio del script.
- Publicadas en claude.ai (una por versión):
  - Navidad (la principal, compartida con enlace): https://claude.ai/artifact/89VM1wC61e3ty89qG1V5Uq
  - Moderna: https://claude.ai/artifact/75C588UGjDSmZJ2vLDuWjt
  - Sello: https://claude.ai/artifact/WpA2sCPAfytmnNSv7zURTc
  Las dos últimas se crearon privadas: el usuario las comparte desde el menú Compartir.
  Para actualizarlas: `python3 chelibo/build.py --fragmento <ruta> [--version moderna|sello|navidad]` y publicar ese
  archivo con su URL (`--version` cambia solo el fragmento y añade la versión al título; `index.html` no cambia).
- Logos (de los PDF originales): `chelibo/assets/chelibo-sello.svg` y `chelibo-firma.svg`.
  Iconos de WhatsApp, Facebook e Instagram: Simple Icons (CC0), en `chelibo/assets/iconos/`.
- Estilo: negro y dorado. Fuentes Anton (titulares) e Instrument Sans (texto).
- Pendiente de la dueña, en el objeto `CHELIBO` al principio del `<script>` de la plantilla:
  teléfono, enlace de WhatsApp, enlace de Facebook y las 6 fotos (van en `chelibo/fotos/`).
  Lo que está vacío se muestra como "Próximamente" o no se muestra.
  La carta (platos y precios) y los horarios de "Dónde estamos" siguen con texto de relleno.
- Google Maps ("Dónde estamos"): tarjeta con un mapa dibujado (negro y oro, pin con el sello) y "Ver en Google Maps",
  que abre `googleMaps` (enlace compartido de la ficha de empresa "Chelibo" en Google: share.google redirige a una
  búsqueda con kgmid=/g/11zy2_gvhd). Falta `direccion`: con ella sale el texto, "Cómo llegar" y, fuera de las vistas
  de claude.ai (que no dejan incrustar Google), el mapa real en un iframe. Las páginas de Google no se pueden leer desde
  la nube (piden un navegador), así que la dirección y los horarios hay que pedírselos al usuario.
- Rendimiento: el sello 3D se dibuja en un `<canvas>` (una sola capa) y solo se redibuja si cambia el giro;
  el flotado, la firma y las cintas son animaciones de GPU. El bucle JS se para cuando no hay nada que mover
  y los efectos de fondo se pausan tras 12 s sin interacción. Con "movimiento reducido" la página es estática.
- Intros (sección 6 del script), las elige la versión; para probarlas sueltas, `#intro-sello` / `#intro-moneda`:
  - 'sello': un tampón de madera de cerezo barnizada (sin mano) llega en arco, estampa el logo en tinta roja sobre
    papel negro, se balancea, se despega rodando por un canto y se va; la cámara pasa de tres cuartos a cenital; un
    frente de fuego con llamas y chispas convierte la tinta en oro y el sello dorado vuela a la portada, donde lo
    sustituye el sello interactivo (`skipSpin`/`heroShown`, sin giro de entrada).
    Referencia del usuario: un vídeo "Animación Sello" (@FTANIMATIONPLAY) que subió como grabación de pantalla: tampón de
    madera clara y barnizada, base gruesa, cuello torneado y pomo esférico. Antes hubo mano con guante y parrilla; se
    quitaron a petición suya.
    El tampón, el papel, la tinta y las sombras se renderizan en 3D en tiempo real (WebGL, trazado de rayos por campos de
    distancia: `GLSL_S`, `glScene()`, `camAt()`, `stamp3At()`). En `fire0` la huella se copia del lienzo 3D (`handoff`) y
    el fuego sigue en canvas 2D (`composeSeal`), sin salto visible. Al preparar se mide la GPU: si va lenta baja la
    resolución, y si ni así llega (o no hay WebGL por hardware, o es `lite`) se usa el tampón 2D de reserva (`makeStamp`).
    Pruebas en el navegador de la nube (SwiftShader): `?gl=1` fuerza el 3D, `?gls=0.5` fija la resolución del 3D y
    `?t=1200` congela la intro en ese milisegundo.
  - 'moneda': la moneda dorada gira y la cámara entra en ella (la intro original).
  Para añadir otra versión: una función `introXxx()` que llame a `finish()` (o `finish('handoff')`) y su nombre en la regex de `hashIntro`.
- Temas de temporada (sección 10): los elige la versión ('navidad' o 'normal'); para probarlos, `#tema-navidad` / `#tema-normal`.
  Navidad: nieve continua (dos láminas pintadas una vez que caen con animación CSS, sin coste de procesador en reposo),
  guirnaldas en canvas (`data-guirnalda`, luces en dos capas que titilan), nieve que se acumula sobre las tarjetas de la
  galería (`.cap`, 42 s), gorro en el logo de la cabecera, acebo en los titulares, estrellas y textos de fiesta.
  El sello interactivo de la portada lleva el mismo gorro, en 3D a petición del usuario (`heroHat`/`hatStep()`,
  `GLSL_H`, `hatGL()`, geometría en `HG` sacada del dibujo del SVG de la cabecera: tres conos de terciopelo que se
  doblan, ribete toroidal y borla de pelo con ruido). Se renderiza con WebGL en el espacio del sello (pose en `hero.m`)
  solo cuando cambia algo; el sello tapa lo que queda detrás (cilindro en el shader) y la sombra del gorro cae sobre el
  oro. Cae sobre el sello al aparecer y se bambolea como un muelle (la punta se dobla) al girarlo, lanzarlo y al caer.
  El lienzo va dentro de `.chat3w`, que lo recorta 10 px antes del borde derecho (`M.hatRoom`): a 900-1100 px de ancho
  el sello está cerca del borde y si no la página se desplazaría de lado. Si la primera pintura tarda mucho baja la
  resolución, y el regulador `QL` también se la baja. Sin WebGL por hardware (o si ni así llega) se usa el gorro SVG
  plano (`.chat`), que sigue la cara del sello con una matriz CSS.
  Evitar capas animadas grandes (p. ej. lienzos del tamaño de la portada con opacidad animada): encarecen mucho la composición.
- En móvil la portada va centrada (sello, textos y botones).
- Sello interactivo (sección 9 del script): al terminar la entrada se puede arrastrar (inercia y se asienta de cara
  con un muelle), tocar/clic = lanzamiento como una moneda, teclado (Enter y flechas). En móvil, deslizar en vertical
  sigue haciendo scroll (`touch-action: pan-y`). La calidad baja sola (tabla `QL`) si hay más de un 15 % de fotogramas lentos.
