# Características de Kitten Synths

Ficha técnica de la versión **2.8-kitten** (basada en SLOOP 2.8). Lo marcado con ★ es nuevo respecto de SLOOP.

## En una mirada

- **Cuatro sintetizadores + batería**, tocados en vivo.
- **13 motores de síntesis** (★ MUUG).
- **250 sonidos** de fábrica (150 de SLOOP + ★ 100 de MUUG) y 32 presets propios.
- **37 kits de batería** y 4 ranuras para tus muestras.
- Secuenciador de **64 pasos** por pista, modo canción con 4 secciones.
- MIDI USB y TRS, clock, audio USB y editor web.
- **MIDI idéntico a SLOOP.**

## Pistas

| Pista | Tipo | Color |
| --- | --- | --- |
| 1, 2, 3 | Sintes completos (cualquier motor) | azul, verde, amarillo |
| ★ 4 | Sinte LITE: DIGITAL, PHASE, LOFI, SAMPLE, VOICE | gris claro |
| 5 | Batería (16 sonidos) | naranja |

## ★ MUUG

| | |
| --- | --- |
| Origen | Motor FMini-1 de Guilherme Ruppert (GPL-3.0), portado a la interfaz de motores de SLOOP |
| Osciladores | 3, con formas TRI, SHARK, SAW, SQR, pulso ancho y pulso angosto (con polyBLEP), rangos LO, 32', 16', 8', 4', 2' |
| Ruido | Blanco o rosa |
| Mezclador | Nivel de cada oscilador y del ruido, con saturación suave |
| Filtro | Pasabajos de escalera de 24 dB/oct al estilo Minimoog, resonancia (EMPH), contorno propio (ataque, decaimiento, sostenido) y seguimiento del teclado |
| Modulación | LFO o ruido hacia el tono (>OSC) y el filtro (>FILT); la rueda de modulación (CC 1) lleva la profundidad al máximo |
| Sonidos | 100 de fábrica, más parche propio (OWN) por pista |
| Voces | Hasta 8, polifónico o monofónico según el preset |
| Edición | Todo en el FM-1: EDIT 1 y 2 (CUT, EMPH, CNTR, F.ATK, F.DEC, F.SUS, MOD, SLOT), OSC RNG, OSC WAV, OSC FRQ, MIXER, FLT ENV y MUUG MOD |

### Los 100 sonidos MUUG por categoría

- **Leads y metales (32):** MINI LEAD, CS-80X BRASS, EMMERSON, NUMANN, HAMMER, FIFTHS, RAVE ARP, ACID LEAD, PULSE HERO, TITAN, FUZZ LEAD, GROWL, MOOGH FLUTE, G-FUNK, SINE SOLO, BANKSH, OBOE, SOLO VIOLIN, DREAMER, WHISTLE, MELLOW PULSE, SAX LEAD, MOOGH BRASS, SALTO BRASS, TRUMPET, FRENCH HORN, BRASS STAB, BRASS SWELL, HORN RIFF, TROMBONE, FLUGEL, FANFARE.
- **Bajos (11):** SIENTO ARP, MOOGH BASS, CAMALEON, SUB BASS, WOBBLE BASS, OCTAVE PUMP, SEQ BASS, REESE, RUBBER, FUZZ BASS, WONDERS BASS.
- **Pads y atmósferas (22):** LUSH STRINGS, SPACE DRONE, SOLINAH, WARM PAD, JUNOH PWM, CHOIR, SWEEP PAD, ANGELS, ECLIPSE, PULSE PAD, CELLOS, AIR PAD, DARK DRONE, STAR DUST, ALIEN CHOIR, GLASS HARP, OCEAN TIDE, PULSAR, IRON DRONE, GHOST SEQ, HORROR, SINGING BOWL.
- **Teclados y órganos (13):** ROTARY ORG, CRYSTAL BELL, E.PIANO, CLAVINETE, PIPE ORGAN, SYNTH PIANO, HARPSICHORD, VIBES, WURLEY, TUBULAR, MUSIC BOX, ACCORDION, FARFISAH.
- **Plucks y stabs (12):** DUB STAB, MANDARINA, PLUCK SAW, MARIMBA, KALIMBA, FUNK ARP, NYLON, STEELDRUM, 8-BIT ARP, PIZZICATO, POP PLUCK, HARP.
- **Efectos (10):** JET SWEEP, THUNDER, WIND, SIREN, TELEPHONE, POWER UP, LASER ZAP, HELICOPTER, ROBOT, UFO.

Los nombres que evocan canciones o artistas se pasaron al español (MANDARINA, SIENTO ARP, NUMANN...) o llevan una letra cambiada (FARFISAH, SOLINAH...).

## ★ Parte LITE

- Motores permitidos: **DIGITAL, PHASE, LOFI, SAMPLE y VOICE**.
- Sin arena de memoria propia, sin SLICER y sin canal MIDI dedicado.
- Se guarda con las secciones A–D y con el autoguardado.
- Comparte el presupuesto de 8 voces con las demás pistas sintetizadoras.

## Motores y voces

| Motor | Voces solo |
| --- | --- |
| ANALOG, DIGITAL, PHASE, LOFI, SAMPLE, TRIO, WHEEL, NOISE | 8 |
| ★ MUUG | 8 |
| FM6 | 6 |
| VOICE | 4 |
| GRAIN | 3 |
| PHYS | 3 (SYMP: 2) |

Presupuesto compartido de 8 voces entre las pistas sintetizadoras; la batería tiene 6 aparte.

## Batería

- 16 sonidos en las teclas blancas, golpes fantasma / suaves / normales / fuertes, redoble x1–x4.
- 37 kits: 5 muestreados (CC0) y 32 sintetizados; kits propios USR1–USR4, USR3+4 y SYN1–SYN4.

## Secuenciador y grabación

- 64 pasos por pista, largo y división propios (1/32 a dos compases), swing 0–100, bloqueos de parámetros (24 por pista), micro timing de ±½ paso, condiciones de fill.
- Acordes de hasta 4 notas por paso, ligaduras, slide, editor de notas tipo piano roll.
- Grabación en vivo con compensación de latencia, overdub, modo libre o tempo fijo, cuenta regresiva, 1, 2 o 4 compases.

## Canciones y memoria

- 4 secciones A–D, cadena rápida de hasta 8, grabación de canción en vivo.
- Autoguardado a los 2,5 segundos, deshacer / rehacer, 32 presets de usuario, 27 parches FM6.
- Copia de seguridad y restauración completas desde el editor web.
- ★ La parte LITE y los parches propios de MUUG se guardan junto a cada sección.

## Efectos

- 27 efectos de golpe sincronizados al tempo.
- Master: DUST, DUCK, filtro DJ y limitador.
- TEXTURE: cama de fondo en bucle.
- Por pista: drive, INSERT (7 tipos), slicer, resonancia del filtro, envíos a chorus, delay (con corcheas con puntillo) y reverb estéreo.

## MIDI y USB

- MIDI USB (clase estándar) de entrada y salida; entrada TRS de 3,5 mm; clock de entrada por USB o TRS.
- Canales 1–3 sintes, 10 batería, 4–16 la pista elegida (configurable en GLO → MIDI).
- CC de nivel, panorama, filtro, resonancia, envolvente, glide y envíos; ★ CC 1 para la modulación de MUUG; pedal de sustain, pitch bend, Program Change, Bank Select, MIDI LEARN.
- Audio USB: entrada de 8 canales de 16 bits a 44,1 kHz, sin drivers: master estéreo (1-2), pistas 1-4 (3-6) y batería (7), pre-master y en mono.

## Interfaz

- ★ Logo de bienvenida y visualizador del gatito que parpadea al tempo.
- Luces de botones y teclas, 5 paletas de color más tema propio.
- ★ Pantallas de pistas, mezclador y visualizadores con cinco pistas.

## Instalador y editor web

- ★ Instalación en un clic con `servir.py` (Chrome o Edge).
- ★ Editor web con las cinco pistas, parámetros de MUUG y entrada de controlador MIDI.
- Simulador en el navegador (sin hardware).
- Actualización segura: verificación SHA-256 y CRC, rescate USB (OCT− al encender).

## Lo que se sacó de SLOOP

Para liberar memoria de programa: DIGITAL STEEL DRUM, SAMPLE UP BASS, VOICE HARMONICA, WHEEL REGGAE ORG, PHYS HAND DRUM, MEMB TOMS y TABLA, y los visualizadores BOUNCE, SLOOP y LCD. No se tocaron las muestras ni las tablas del filtro.

## Límites

- La memoria de programa del FM-1 está casi llena (cientos de bytes libres).
- Sin segunda batería (sexta pista) por ahora.
