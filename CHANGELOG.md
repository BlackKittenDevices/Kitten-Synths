# Historial de cambios

Versión **2.8-kitten** (sobre SLOOP 2.8). Cada parche (`fix-NN.patch`) se aplica después de `muug.patch`.

## fix-20 · Segunda pista de batería (versión de prueba)

- **Una sexta pista: la batería 2.** Tiene su propio kit (arranca en ACOUSTIC), patrón, nivel, paneo, mute, solo y filtro, para combinar por ejemplo una batería acústica o sampleada con la 808. Va después de la batería 1: el orden es 1, 2, 3, LITE, batería, batería 2.
- **Cómo se elige:** con la perilla de pista, como las demás. La pantalla DRUMS, sus teclas, el kit, el SOUND (TUNE / DECAY de cada sonido) y la grabación son los de la batería elegida.
- **MIDI:** la batería 2 escucha y envía por el **canal 11**; los demás canales quedan como en SLOOP. Si una pista de sinte está en el 11, el canal sigue siendo de esa pista.
- **Audio USB:** la batería 2 sale sola por el **canal 8**, que antes iba en silencio.
- **Pantallas:** la de pistas, el mezclador, la de REC y los vúmetros muestran seis pistas.
- **GLO (mezcla):** las teclas 1–6 son mute, 7–12 solo, 13 fill y 14 la próxima barra de fill. El tap tempo sigue en la última tecla.
- **Nivel:** la batería 1 sigue usando GLO > DRUMS (LVL, REV, DLY); la batería 2 usa su propio LEVEL, REV y DLY, como una pista de sinte.
- **Guardado:** se guarda junto a cada proyecto (A–D y el autoguardado), como la parte LITE. Ocupa el último sector de USR4, que pasa de 80 a **76 KiB** (unos 0,2 s menos de muestras en esa ranura). El editor web ya conoce el tamaño nuevo.
- El editor web todavía no muestra ni edita la batería 2 (la ves y la tocás en el FM-1).
- No cambia ningún sonido de las otras pistas. Memoria flash libre: unos 1.300 bytes.

## fix-19 · El gatito vuelve al arranque

- Al encender aparece otra vez el dibujo del gatito, en vez de "=^.^=" en texto. Es el mismo gatito del visualizador: aparece con los ojos abiertos y parpadea una vez antes de entrar. Ya no se guarda una imagen aparte para el arranque (la de la calabaza).
- Para hacerle lugar se quitaron cuatro visualizadores de SLOOP: SPECTRUM, TAPE, ORBIT y WIRES. Quedan seis: OSCILLOSCOPE, SPECTROGRAM, LISSAJOUS, VU METERS, CIRCLE y KITTEN. Un estilo guardado que ya no existe pasa a otro de los seis.
- No cambia ningún sonido.

## fix-18 · Arreglos de SLOOP 2.8.1 a 2.8.4 (secuenciador, audio, unísono)

Kitten Synths sigue sobre SLOOP 2.8 (la versión 2.8.4 entera no entra en la memoria del FM-1 junto con MUUG y la parte LITE). Se traen solo sus arreglos:

- **Secuenciador:** en una pista POLY, una nota sostenida mientras grabás otras encima ya no se corta ni se reinicia (en vivo, en la toma libre y en overdub). LEN de una nota sigue por debajo de las siguientes (SEQ > NOTES). En MONO / LEGATO avisa *MONO: SET VOICE POLY*. En REC READY cada perilla cambia solo su valor. La hoja del paso (OCT+) es una tira abajo y deja ver el roll.
- **Audio:** sin distorsión al final de las notas: la mezcla redondea en vez de truncar, en la salida de 3,5 mm y en USB. El UNISON ya no apila sus voces en fase en ningún motor. En MUUG, cada voz lee el ruido desde su propio lugar del bloque, una de cada dos invertida. Un sample tocado otra vez arranca desde el silencio con su ATK, sin click.
- **Estabilidad:** sin notas colgadas tras una ráfaga MIDI. En un ritmo cargado el bombo ya no se pierde. Un toque corto de un botón ya no hace parpadear su página.
- No se traen la protección del segundo núcleo, la afinación de PHYS, GRAIN ni que NZ ARCADE siga las teclas agudas (no entran en la memoria).
- Para hacer lugar, sin cambiar ningún sonido: la tabla de nivel de los presets va sin relleno y el visualizador se compila por tamaño.
- Pruebas nuevas de SLOOP: notas sostenidas, LEN, batería, samples, fundidos, perillas y unísono. Las huellas de sonido (`tests/golden.txt`) se regeneraron.

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
