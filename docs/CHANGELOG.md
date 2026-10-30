# Historial de cambios

Versión **2.8-kitten** (sobre SLOOP 2.8). Cada parche (`fix-NN.patch`) se aplica después de `muug.patch`.

## fix-17 · Grabación multipista por USB (8 canales)

- La entrada de audio USB pasa de 2 a **8 canales** (16 bits, 44,1 kHz, sin drivers): 1-2 el master estéreo (como antes), 3-6 los cuatro sintes (3 = pista 1, 4 = pista 2, 5 = pista 3, 6 = LITE), 7 la batería, 8 en silencio.
- Cada pista va en mono y pre-master: con su nivel, paneo (sumado a mono), mute, solo, DIST, INSERT y filtro de pista; sin el chorus, el delay ni la reverb compartidos, sin DUST, FILT ni la perilla MASTER. El master (1-2) lleva todo.
- 44,1 kHz solamente: el menú USB RATE muestra "8 CH 44.1" (el remuestreo a 48 kHz no alcanza para 8 canales). Se libera su tabla en la memoria de programa.
- La computadora lo ve como un dispositivo nuevo (bcdDevice propio): al instalar, desenchufá y enchufá el FM-1.
- Pruebas nuevas: `tests/uac8_test.c` (descriptores, anillo y paquetes de 8 canales) y `tests/stems_test.c` (cada pista sola, todas, la suma igual a la mezcla seca, la división entre los dos núcleos).

## fix-16 · Identidad propia para el Firmware Hub

- El paquete ya no usa la identidad `FM-1_928` (la tiene otro firmware en el Hub). Kitten Synths se identifica ahora como **`FM-1_969`**, tanto en el paquete como por USB (MIDI).
- Se define en el workflow (`FM1_IDENTITY`) y `tools/build.py` la toma al compilar una versión.
- Se agrega `fmhub.json` con el texto de la tarjeta.

## fix-15 · Nombre del instalador y favicon
- El enlace del editor web dice "Kitty installer" (antes "SLOOP installer").
- El gato es el único ícono de pestaña de las páginas (se quita el ícono por archivo que podía elegirse en su lugar).

## fix-14 · Gráficos de filtro, paleta Halloween, ícono del navegador
- MUUG: la página FLT ENV dibuja el contorno del filtro como la envolvente principal, y EDIT 1 dibuja la curva del filtro con el corte y la resonancia.
- ANALOG: la página FILTER dibuja la curva en LP, BP o HP.
- Paleta de fábrica PUMPKIN (naranja sobre negro); pistas en violeta, verde ácido, amarillo, hueso y naranja. Paletas SLIME, BONE, WITCH y BLOOD. Editor e instalador con los mismos colores.
- Ícono de la pestaña del navegador con el gato (embebido, también en el editor guardado como archivo).
- El instalador dice 250 sonidos (decía 253).
- La compilación deja la memoria libre como anotación de la ejecución.

## fix-13 · Logo de inicio más largo
- El logo del gatito se muestra 2,5 segundos (antes 0,9) para poder leerlo completo.

## fix-12 · Pantalla ABOUT de Kitten Synths
- HOME → ABOUT muestra KITTEN SYNTHS y Black Kitten Devices, con los créditos de SLOOP, Felucca, FMini-1 (MUUG) y las muestras.

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
