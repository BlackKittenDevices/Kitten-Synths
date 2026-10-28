# Historial de cambios

Versión **2.8-kitten** (sobre SLOOP 2.8). Cada parche (`fix-NN.patch`) se aplica después de `muug.patch`.

## fix-11 · MUUG a 8 voces
- El tope de voces de MUUG sube de 4 a 8 (el presupuesto compartido del FM-1). Cada preset conserva su modo polifónico o monofónico. Sin costo de memoria de programa.

## fix-10 · Menos sonidos, nombres en español
- Se quitan siete sonidos de SLOOP para liberar memoria: DIGITAL STEEL DRUM, SAMPLE UP BASS, VOICE HARMONICA, WHEEL REGGAE ORG, PHYS HAND DRUM, MEMB TOMS y TABLA.
- Los sonidos MUUG que evocan canciones o artistas pasan al español; los que evocan apellidos o marcas llevan una letra cambiada.
- Las pruebas siguen a la parte LITE.

## Mejora del flujo de compilación
- `size.log` incluye cuántos bytes de memoria de programa quedan libres.

## fix-09 · Ahorro de memoria de programa
- Los parches de fábrica de MUUG se guardan en 18 bytes cada uno (−1,4 KB).
- El logo de inicio cae a texto si la memoria se llena.

## fix-08 · Guardado de LITE y de los parches propios de MUUG
- La parte LITE y los parches propios de MUUG se guardan con las secciones A–D y con el autoguardado, en un objeto aparte de la memoria flash.

## fix-07 · Páginas de MUUG en el panel
- EDIT: OSC RNG, OSC WAV, OSC FRQ y MIXER. ENV: FLT ENV. LFO: MUUG MOD.

## fix-01 … fix-06 y muug.patch
- El motor MUUG con sus 100 sonidos y el filtro de escalera.
- La cuarta parte sintetizadora LITE y las cinco pistas en pantalla, mezclador y secuenciador.
- La estética de gatitos: logo de bienvenida, visualizador del gatito, colores.
- Instalador y editor web de Kitten Synths con entrada MIDI de controlador y las cinco pistas.
- Rueda de modulación (CC 1) para MUUG.
- Pruebas nuevas para todo lo anterior.
