# Cómo se compila Kitten Synths

Este repositorio **no contiene el código de SLOOP**: contiene los parches que lo convierten en Kitten Synths y un flujo automático que arma todo en GitHub. No necesitás instalar nada en tu computadora para obtener el firmware.

## Compilación automática (recomendada)

1. En GitHub: pestaña **Actions** → **build** → **Run workflow**. (También se dispara solo cuando se sube un cambio a los parches, a las imágenes o al flujo.)
2. El flujo hace, en orden:
   1. Descarga SLOOP de [isod89/sloop-fm1](https://github.com/isod89/sloop-fm1) en el commit fijo `ec9e537`.
   2. Aplica `muug.patch` y después `fix-01.patch` … `fix-12.patch`, en ese orden.
   3. Instala las herramientas: Python, Node, Pillow, clang, la cadena de JieLi y tres archivos del SDK AC79.
   4. Revisa que el código principal compile.
   5. Compila el firmware (`build.sh --release 2.8-kitten`).
   6. Escribe `size.log` con los tamaños, incluida la línea `FLASH: image N B of 581564 B, free M B`.
   7. Corre las pruebas (no frena la compilación si alguna falla; mirá `tests.log`).
   8. Arma el sitio (instalador, editor web) y el simulador.
3. Descargá el artefacto **kitten-synths**: trae `servir.py`, el paquete `felucca-2.8-kitten.fwsc`, la carpeta `site/` (instalador y editor), `simulator/` y los registros `build.log`, `size.log` y `tests.log`.

### Memoria de programa

El FM-1 tiene un espacio fijo de **581 564 bytes** para el programa. Si el firmware no entra, el enlazado falla con el mensaje *overflow*. Mirá la línea `FLASH:` de `size.log` para saber cuánto queda libre. Con las funciones actuales quedan **372 bytes**, es decir que cualquier función nueva exige sacar algo antes (por ejemplo sonidos).

Si la memoria se llena, `build.py` reintenta solo con el logo de inicio en texto (`=^.^=`) en lugar de la imagen del gatito.

## Compilar a mano

Hace falta un Linux x86-64 (o WSL en Windows) con:

- Python 3 con `pillow` y `fonttools`, Node 20, `clang` y `lld`.
- La cadena de herramientas de JieLi (`sh tools/get_toolchain.sh` dentro del árbol de SLOOP).
- Los archivos `uboot.boot`, `cfg_tool.bin` y `eq_cfg_hw.bin` del SDK `fw-AC79_AIoT_SDK` (versión `AC79NN_SDK_V1.2.1_2023-12-13`).

Pasos:

```bash
git clone https://github.com/isod89/sloop-fm1.git sloop
cd sloop && git checkout ec9e53721cc576816a5750220391f2d0217c01cb
for p in ../muug.patch ../fix-*.patch; do git apply --index "$p"; done
sh tools/get_toolchain.sh
KITTEN_ART="../splashes y logos" bash ./build.sh --release 2.8-kitten
```

El resultado queda en `build/felucca-2.8-kitten.fwsc`. Para armar el instalador: `python3 web/make_site.py build/felucca-2.8-kitten.fwsc 2.8-kitten ../kitten-synths/site`. Las instrucciones detalladas del árbol de SLOOP están en su archivo `BUILDING.md`.

## Pruebas

`sh tests/run_tests.sh` corre las pruebas del código en la computadora, sin hardware: audio contra valores de referencia, presupuesto de CPU, tiempos del secuenciador, páginas de la interfaz, almacenamiento en memoria flash, MIDI y audio USB, y las páginas web. Kitten Synths agrega, entre otras, pruebas del guardado de la parte LITE y de los parches propios de MUUG, y de las páginas de edición de MUUG.

Algunas pruebas necesitan el SDK y el paquete compilado; fuera de la compilación automática pueden fallar por falta de esos archivos, sin que haya un problema en el código.

## Agregar un cambio

Los cambios se escriben como un parche nuevo (`fix-13.patch`, etc.) que se aplica después de los anteriores. Así el historial de lo que hace Kitten Synths queda separado del código de SLOOP. Antes de subirlo, comprobá que aplica sobre la cadena completa y mirá la línea `FLASH:` del registro.
