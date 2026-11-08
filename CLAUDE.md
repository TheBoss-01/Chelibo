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
- Publicada en https://claude.ai/artifact/89VM1wC61e3ty89qG1V5Uq.
  Para actualizarla: `python3 chelibo/build.py --fragmento <ruta>` y publicar ese archivo con esa URL.
- Logos (de los PDF originales): `chelibo/assets/chelibo-sello.svg` y `chelibo-firma.svg`.
  Iconos de WhatsApp, Facebook e Instagram: Simple Icons (CC0), en `chelibo/assets/iconos/`.
- Estilo: negro y dorado. Fuentes Anton (titulares) e Instrument Sans (texto).
- Pendiente de la dueña, en el objeto `CHELIBO` al principio del `<script>` de la plantilla:
  teléfono, enlace de WhatsApp, enlace de Facebook y las 6 fotos (van en `chelibo/fotos/`).
  Lo que está vacío se muestra como "Próximamente" o no se muestra.
  La carta (platos y precios) y los horarios de "Dónde estamos" siguen con texto de relleno.
- Rendimiento: el sello 3D se dibuja en un `<canvas>` (una sola capa) y solo se redibuja si cambia el giro;
  el flotado, la firma y las cintas son animaciones de GPU. El bucle JS se para cuando no hay nada que mover
  y los efectos de fondo se pausan tras 12 s sin interacción. Con "movimiento reducido" la página es estática.
