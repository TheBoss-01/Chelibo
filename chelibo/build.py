#!/usr/bin/env python3
"""Genera la web de Chelibo a partir de la plantilla y los logos.

    python3 chelibo/build.py                      -> chelibo/index.html (web completa)
    python3 chelibo/build.py --fragmento RUTA     -> además, la versión para publicar en claude.ai

La plantilla es chelibo/src/pagina.html. Los datos de contacto y las fotos
se rellenan en el objeto CHELIBO, al principio de su <script>.
"""
import base64
import pathlib
import re
import sys

AQUI = pathlib.Path(__file__).resolve().parent
ASSETS = AQUI / 'assets'


def interior_svg(nombre):
    """Contenido de un SVG sin la etiqueta <svg> y sin colores fijos (heredan currentColor)."""
    t = (ASSETS / nombre).read_text(encoding='utf-8')
    t = t[t.index('>', t.index('<svg')) + 1:t.rindex('</svg>')]
    return re.sub(r'\s(fill|stroke)="rgb\([^)]*\)"', '', t).strip()


def construir():
    pagina = (AQUI / 'src' / 'pagina.html').read_text(encoding='utf-8')
    sello, firma = interior_svg('chelibo-sello.svg'), interior_svg('chelibo-firma.svg')
    mascara = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2546.81 1018.72"><g fill="#000">'
               + firma + '</g></svg>')
    pagina = pagina.replace('{{SELLO}}', sello)
    pagina = pagina.replace('{{FIRMA_B64}}', base64.b64encode(mascara.encode('utf-8')).decode('ascii'))
    pagina = re.sub(r'\{\{ICON:(\w+)\}\}', lambda m: interior_svg('iconos/%s.svg' % m.group(1)), pagina)
    faltan = re.findall(r'\{\{[^}]+\}\}', pagina)
    if faltan:
        sys.exit('Marcadores sin sustituir: %s' % ', '.join(sorted(set(faltan))))

    # Favicon dorado a partir del sello
    (ASSETS / 'favicon.svg').write_text(
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 1000">'
        '<g fill="#d9b25a" stroke="#d9b25a">' + sello + '</g></svg>\n', encoding='utf-8')

    cabecera = (
        '<!doctype html>\n<html lang="es">\n<head>\n'
        '<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
        '<meta name="theme-color" content="#0a0907">\n'
        '<meta property="og:title" content="Chelibo Foodtruck">\n'
        '<meta property="og:description" content="Carta, fotos, dónde estamos y contacto.">\n'
        '<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">\n'
    )
    (AQUI / 'index.html').write_text(cabecera + pagina + '\n</html>\n', encoding='utf-8')

    if '--fragmento' in sys.argv:
        destino = pathlib.Path(sys.argv[sys.argv.index('--fragmento') + 1])
        destino.write_text(pagina, encoding='utf-8')
    print('index.html: %d bytes' % len(cabecera + pagina))


if __name__ == '__main__':
    construir()
