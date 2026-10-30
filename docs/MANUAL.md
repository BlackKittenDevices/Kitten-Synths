# Manual de Kitten Synths

Firmware para el **M-VAVE FM-1** · versión 2.8-kitten · Black Kitten Devices · [Read in English](MANUAL.en.md)

Kitten Synths está construido sobre **SLOOP 2.8**. Todo lo que hace SLOOP lo hace igual acá (y con los mismos gestos). Este manual explica el instrumento completo en español y marca con **★ NUEVO** lo que agrega Kitten Synths. Para el detalle fino de cada página de SLOOP existe la [guía original en inglés](https://github.com/isod89/sloop-fm1/blob/ec9e53721cc576816a5750220391f2d0217c01cb/GUIDE.md).

## Contenido

1. [Novedades de Kitten Synths](#1-novedades-de-kitten-synths)
2. [Instalación](#2-instalación)
3. [El panel y las cinco pistas](#3-el-panel-y-las-cinco-pistas)
4. [Tu primer ritmo en 60 segundos](#4-tu-primer-ritmo-en-60-segundos)
5. [Tocar en vivo: las capas](#5-tocar-en-vivo-las-capas)
6. [La batería](#6-la-batería)
7. [Grabar y el secuenciador](#7-grabar-y-el-secuenciador)
8. [Canciones, guardado y autoguardado](#8-canciones-guardado-y-autoguardado)
9. [Motores y sonidos](#9-motores-y-sonidos)
10. [MUUG, el sinte tipo Moog](#10-muug-el-sinte-tipo-moog)
11. [La parte LITE (cuarto sinte)](#11-la-parte-lite-cuarto-sinte)
12. [Efectos](#12-efectos)
13. [Menú HOME, colores y luces](#13-menú-home-colores-y-luces)
14. [MIDI y audio USB](#14-midi-y-audio-usb)
15. [El editor web](#15-el-editor-web)
16. [Tus propias muestras](#16-tus-propias-muestras)
17. [Solución de problemas](#17-solución-de-problemas)
18. [Límites conocidos](#18-límites-conocidos)

---

## 1. Novedades de Kitten Synths

Respecto de SLOOP 2.8, Kitten Synths agrega:

### ★ Un motor nuevo: MUUG

- Sinte al estilo de los clásicos de **tres osciladores de Moog**, portado de [FMini-1](https://github.com/ruppert/fmini-1). Es el motor número 13 (SLOOP trae 12).
- **100 sonidos de fábrica** (bajos, leads, pads, vientos, plucks, teclados, efectos) listos en la lista de presets.
- Filtro pasabajos de escalera de **24 dB por octava** con su propio contorno (ataque, decaimiento, sostenido), resonancia y seguimiento del teclado.
- **Edición completa en el propio FM-1**: páginas nuevas para osciladores, mezclador, modulación y envolvente de filtro. No hace falta el editor web para armar un sonido.
- **Parche propio ("OWN")**: partís de cualquiera de los 100 sonidos, lo cambiás y queda guardado como tu parche en esa pista.
- Hasta **8 voces**. Cada preset elige si toca en modo polifónico o monofónico (legato).
- **Rueda de modulación (CC 1)** por MIDI: lleva la profundidad de modulación hasta el máximo.

Más en el [capítulo 10](#10-muug-el-sinte-tipo-moog).

### ★ Cuarto sinte: la parte LITE

Una pista sintetizadora extra, **gris**, ubicada antes de la batería. Usa solo motores livianos (**DIGITAL, PHASE, LOFI, SAMPLE y VOICE**) para que puedas tener cuatro sintes y una batería sonando a la vez sin que el procesador se ahogue. Se guarda con tus proyectos y con el autoguardado. Más en el [capítulo 11](#11-la-parte-lite-cuarto-sinte).

### ★ Cinco pistas en todos lados

El orden es siempre **1, 2, 3, LITE, batería** (la batería, última). Lo ves en la pantalla de pistas (HOME), en el mezclador (GLO), en los visualizadores, en el editor web y en el mute/solo.

### ★ Estética de gatitos y Halloween

- Logo de bienvenida con el **gatito** (dura 2,5 segundos).
- **Paleta de fábrica PUMPKIN**: fondo negro y textos en naranja, con pistas en violeta, verde ácido, amarillo, gris hueso y naranja. Las otras paletas son SLIME (verde), BONE (gris), WITCH (violeta) y BLOOD (rojo).
- Un visualizador nuevo: **el gatito con los ojos que se abren y cierran al ritmo del BPM**.
- Se quitaron los visualizadores BOUNCE, SLOOP (barquito) y LCD.
- El instalador y el editor web usan la identidad de Kitten Synths.

### ★ Gráficos de filtro y de envolvente

- La página **FLT ENV** de MUUG dibuja el contorno del filtro (F.ATK, F.DEC, F.SUS) con el mismo gráfico que la envolvente principal.
- La primera página de EDIT de MUUG (CUT, EMPH, CNTR, F.ATK) dibuja la **curva del filtro** de escalera: la línea vertical marca la frecuencia de corte y el pico, la resonancia, y se mueven mientras girás las perillas.
- La página FILTER de ANALOG dibuja la curva en pasabajos (LP), pasabanda (BP) o pasaaltos (HP) según el tipo elegido.

### ★ Instalador y editor web propios

- El **instalador** se abre con un solo comando (`servir.py`): enchufás el FM-1 y apretás Instalar.
- El **editor web** pide acceso MIDI al abrirlo, ve las cinco pistas, edita los parches de MUUG y escucha un **controlador MIDI** conectado a la computadora.

### ★ Guardado ampliado

La parte LITE y los parches propios de MUUG se guardan **junto a cada sección (A–D)** y con el autoguardado, en un espacio aparte de la memoria. Los archivos de proyecto de SLOOP no cambian.

### ★ Menos sonidos de SLOOP, para hacer lugar

El FM-1 tiene la memoria de programa casi llena. Para que entre todo, se sacaron siete sonidos de SLOOP: DIGITAL **STEEL DRUM**, SAMPLE **UP BASS**, VOICE **HARMONICA**, WHEEL **REGGAE ORG** y PHYS **HAND DRUM**, **MEMB TOMS** y **TABLA**. Las muestras, los kits de batería y las tablas del filtro no se tocaron.

### Lo que no cambia

- **MIDI idéntico a SLOOP**: mismos canales, CC, clock, program change, bank select.
- El secuenciador de 64 pasos, el modo canción, los 27 efectos de golpe, las muestras propias y el rescate USB funcionan igual.

### ★ Grabación multipista por USB

El audio USB tiene **8 canales**: el master en 1-2 (como siempre) y cada pista por separado, pre-master (los 4 sintes y la batería). Ver el [capítulo 14](#audio-usb).

---

## 2. Instalación

> Instalar firmware propio es **bajo tu propio riesgo**. Hacé antes una copia de seguridad.

### Qué necesitás

- Un M-VAVE FM-1.
- Una computadora con **Chrome o Edge** y **Python 3**.
- Un cable USB **de datos**, conectado directo (sin hub).

### Paso a paso

1. **Copia de seguridad.** Con el editor web de tu firmware actual, guardá un respaldo completo (canciones, presets propios, muestras, ajustes).
2. **Conseguí el paquete.** En GitHub: pestaña **Actions** → **build** → **Run workflow**. Al terminar, descargá el artefacto **kitten-synths** y descomprimilo. (Si el proyecto publica una versión en *Releases*, podés bajarla directamente.)
3. **Abrí el instalador.** Ejecutá `servir.py` (en Windows: doble clic, o `python servir.py` desde una terminal en esa carpeta). Se abre `http://localhost:8766/site/webapp/installer/`.
4. **Conectá el FM-1** por USB y apretá **Instalar**. Permití el acceso MIDI cuando el navegador lo pida.
5. **Esperá** el aviso de listo. El FM-1 se reinicia con el logo del gatito.
6. **Desenchufá y enchufá** el FM-1 una vez, para que la computadora detecte el audio USB.

Tus proyectos, presets propios, muestras y ajustes se conservan al instalar.

### Probar sin el FM-1

**En el navegador:** https://blackkittendevices.github.io/Kitten-Synths/play/?fw=kittensynths&mhz=60&latency=0.25 corre el firmware real en un FM-1 emulado (pantalla, botones, teclas y sonido; gracias a [fm1-emu](https://github.com/joakimeriksson/fm1-emu) de Joakim Eriksson). El editor jugable sin FM-1: https://blackkittendevices.github.io/Kitten-Synths/simulator/playable.html?mock=1 (o, con `servir.py` en marcha, `http://localhost:8766/simulator/index.html?mock=1`). Ninguno reemplaza al equipo real.

### Si algo sale mal

- **Se cortó la instalación:** el FM-1 queda en modo actualización. Apretá Instalar de nuevo y termina.
- **El FM-1 ya no arranca Kitten Synths:** mantené **OCT−** apretado mientras lo encendés (*rescate USB*) y volvé a instalar.
- **El equipo no enciende para nada:** hace falta una herramienta de recuperación, como [FM-1-transporter](https://github.com/kurogedelic/FM-1-transporter).

### Volver atrás

El instalador de Kitten Synths **no** trae la opción de volver al firmware oficial V15 (ya no se distribuye). Podés instalar el `.fwsc` de otro firmware compatible, por ejemplo SLOOP. Guardá antes un respaldo: los proyectos de Kitten Synths conservan el formato de SLOOP, pero la parte LITE y los parches propios de MUUG solo los entiende Kitten Synths.

---

## 3. El panel y las cinco pistas

### Pistas y colores

| Pista | Qué es | Color |
| --- | --- | --- |
| 1 | Sinte | violeta |
| 2 | Sinte | verde ácido |
| 3 | Sinte | amarillo |
| 4 | ★ Sinte LITE | gris claro |
| 5 | Batería | naranja |

Elegís la pista con la perilla **ALGORITHM**. El orden en pantalla es 1, 2, 3, LITE, batería. El tema de colores de la pantalla se cambia desde el menú HOME y la página Theme del editor web.

### Controles

| Control | Qué hace |
| --- | --- |
| **MASTER** | Volumen (y nivel del audio USB, si USB AUDIO está en MASTER). |
| **SELECT** | En HOME y dentro de una capa: tempo. En una página: pasa a la anterior o siguiente de su grupo. En DRUMS: grilla / kit. |
| **ALGORITHM** | Elige la pista. |
| **PRESETS** | El sonido de la pista elegida, o el kit de la batería. |
| **KNOB 1–4** | Las cuatro perillas de abajo; cada una con el color que muestra la pantalla. |
| **OCT− / OCT+** | Octava (las dos juntas: vuelve a 0). En batería, mantenidas: golpes suaves / fuertes. |
| **FX · SEL · ENV · LFO · EDIT · GLO** (fila de arriba) | Tocar: abre sus páginas. Mantener FX, SEL, EDIT o GLO: abre una capa. **SEL** es el segundo botón de la fila, entre FX y ENV. |
| **HOME** | Pantalla de pistas. Mantener: menú. Tocarlo con una capa apretada: la fija. |
| **SAVE** | En pistas: pantalla de canción. En otra parte: páginas de guardado. Mantener: capa de canción. |
| **ARP · SEQ** | Tocar: sus páginas. Mantener: repetición de nota · pasos. |
| **PLAY** | Arranca / detiene todas las pistas. Su luz parpadea en cada tiempo. |
| **REC** | Tocando: grabar / parar. Detenido: armar. Mantener: borrar la pista. |
| **EDIT + OCT− / OCT+** | Deshacer / rehacer. |

El blanco es lo que tocás; el rojo es grabando.

---

## 4. Tu primer ritmo en 60 segundos

1. Con **ALGORITHM** elegí la **batería** (naranja). Las teclas blancas son 16 sonidos; **PRESETS** elige el kit (probá *808* o *BOOMBAP*).
2. Apretá **REC** y tocá un ritmo libre, a tu tempo. Con **OCT−** apretado tocás golpes fantasma; con **OCT+**, golpes fuertes.
3. **Apretá REC en el "1" después de tu último compás.** El bucle se cierra, su largo fija el tempo, los golpes se acomodan a la grilla y suena.
4. **REC** de nuevo mientras suena: grabás encima. Con **ARP** apretado y una tecla de hi-hat, hacés un redoble.
5. Elegí la pista **1**, **REC**, tocá una línea de bajo. Probá el preset **MUUG** que quieras. Con **SEL** apretado tocás la tecla de la tonalidad de tu canción.
6. Con **FX** apretado, tocá una tecla para un efecto de golpe; sin soltar FX, **KNOB 2** es DUST y **KNOB 3** es DUCK.
7. ¿Un error? **EDIT + OCT−** deshace.

---

## 5. Tocar en vivo: las capas

Cada botón de función es una **capa**: mantenelo apretado y las 16 teclas blancas y las cuatro perillas cambian de trabajo (la pantalla lo muestra). Tocalo y se abren sus páginas. Para dejar una capa abierta, mantenela y tocá HOME.

| Mantener | Teclas blancas | KNOB 1 · 2 · 3 · 4 |
| --- | --- | --- |
| **FX** (golpe) | 27 efectos de golpe sobre toda la mezcla: bucles, stutter, reversa, freno de cinta, filtros, bitcrush, eco... Las negras: cortes de graves / medios / agudos, rebobinar, octava, flanger, auto-pan, freeze, mono, fade out | FILTER · DUST · DUCK · filtro de la pista |
| **EDIT** (borrar) | Borra un sonido o nota mientras suena el bucle. Una negra: mutea batería en vivo | SHIFT · LENGTH ×2 / ½ · TRANSPOSE |
| **ARP** (redoble) | Repetición de nota sobre la grilla | RATE (1/8 … 1/64) |
| **SEQ** (pasos) | Los 16 pasos de la página. Un paso mantenido: nivel, redoble, desplazamiento, bloqueos de parámetros | SOUND / NOTE · DIV · SWING · LENGTH |
| **SEL** (tonalidad) | Tonalidad de la canción | CHORD · SCALE · KEYS · TRANSPOSE |
| **GLO** (mezcla) | 1–5 mute, 6–10 solo, fill, tap tempo | Niveles de las pistas |
| **SAVE** (canción) | 1–4 tocan las secciones A–D, 5–8 guardan el bucle en ellas, 13 bucle / canción, 14 grabar canción, 16 cadena | — |

> Con cinco pistas, en GLO los mutes van del 1 al 5 y los solos del 6 al 10, siguiendo el orden de la pantalla (LITE antes de la batería).

---

## 6. La batería

- **16 sonidos** en las teclas blancas; una negra duplica la blanca de su izquierda (redobles con dos dedos).
- **Golpes fantasma y fuertes**: **OCT−** / **OCT+** mantenidos mientras tocás. Cada golpe guarda su nivel y un redoble (x1–x4).
- **37 kits**: uno de batería acústica muestreada en 5 tratamientos (grabaciones de estudio CC0) y 32 sintetizados (808, 909, 606, trap, drill, boom bap, lo-fi, house, techno, jungle, amapiano, jazz brushes...).
- **Tus propios kits**: USR1–USR4 y USR3+4 usan muestras que cargás en el editor web. **SYN1–SYN4** son kits sintetizados que armás en la página Drum synth del editor.
- La pantalla DRUMS tiene grilla (las teclas son los pasos del sonido elegido) y kit.
- **TUNE** y **DECAY** por sonido, desde la página SOUND de la pantalla DRUMS.

---

## 7. Grabar y el secuenciador

### Grabar

- Mientras suena, **REC** graba al instante y cada vuelta se suma encima (overdub). Las notas caen donde las oíste: se compensa la latencia de las teclas.
- **Pantalla REC** (antes de la primera nota): *modo* libre (el tempo te sigue) o tempo fijo; *largo* de 1, 2 o 4 compases; *inicio* en tu primera nota o con cuenta regresiva de un compás; **QUANT off** conserva tu manera de tocar como desplazamientos.
- Mantené **REC** unos 2 segundos para borrar la pista; deshacer la recupera.

### Secuenciador

- **64 pasos por pista**, cada una con su propio largo y su división (1/32 hasta dos compases), así los polirritmos se mantienen en fase.
- Acordes de hasta 4 notas por paso, ligaduras, slide, **swing** de 0 a 100 estilo MPC y un único reloj preciso (sin deriva a ningún tempo).
- **Bloqueos de parámetros**: mantené un paso para darle su propio valor de cualquier parámetro.
- **Desplazamiento** (micro timing) y **condiciones de fill** por paso.
- Editor de notas tipo piano roll para los sintes (SEQ → NOTES). Para la hoja de un paso, mantené OCT+ sobre él: SLIDE, NUDGE, FILL, MOVE, COPY, DELETE.

---

## 8. Canciones, guardado y autoguardado

- **Secciones A–D**: guardá el bucle (SAVE + teclas 5–8), tocalas en vivo en el próximo compás (SAVE + teclas 1–4) y **grabá la canción** mientras la tocás (SAVE + tecla 14). Mantené SAVE y tocá varias secciones para una **cadena rápida**. La pantalla SONG edita el orden a mano.
- **Autoguardado**: dejá el equipo 2,5 segundos quieto y tu trabajo queda guardado; al encender vuelve todo como lo dejaste.
- **32 presets de usuario**, **27 parches FM6**, deshacer / rehacer.
- **Copia de seguridad completa** desde el editor web: un archivo con todo.

### ★ Qué se guarda de Kitten Synths

Con cada sección y con el autoguardado se guardan además la **parte LITE** (su sonido y su secuencia) y los **parches propios de MUUG**. Esto vive en un espacio aparte de la memoria. Dos cosas a tener en cuenta:

- Si ese espacio no alcanza para la parte LITE de una sección, el equipo avisa (*SAVED, LITE NOT* o *LITE TOO BIG*) y guarda el resto igual.
- Ese espacio tiene una sola copia: si se corta la luz justo mientras se escribe, se puede perder lo de LITE y los parches propios, pero **no** el resto de tus proyectos.

---

## 9. Motores y sonidos

### Los 13 motores

| Motor | Qué es | En LITE |
| --- | --- | --- |
| ANALOG | Analógico sustractivo, filtro LP / BP / HP | no |
| DIGITAL | FM de 4 operadores | **sí** |
| FM6 | FM de 6 operadores con parches DX7 | no |
| PHASE | Distorsión de fase | **sí** |
| TRIO | Tres osciladores | no |
| WHEEL | Órgano de ruedas (drawbar) | no |
| VOICE | Voz con formantes | **sí** |
| GRAIN | Granular | no |
| LOFI | Chip lo-fi | **sí** |
| SAMPLE | Sampler | **sí** |
| PHYS | Modelos físicos (guitarras, sitar, campanas) | no |
| NOISE | Ruido | no |
| ★ **MUUG** | Sinte tipo Moog (100 sonidos) | no |

### Sonidos

**250 sonidos** en total (150 de SLOOP y 100 de MUUG), navegables por tipo: bajos, teclados, órganos, pads, leads, plucks, stabs y efectos. Todos nivelados entre sí. Hay lugar para **32 presets propios**.

### Polifonía (voces)

Hay un presupuesto de **8 voces compartido entre todas las pistas sintetizadoras**; si tocás más, se retira la voz más vieja con un fade (nunca el bajo ni el lead). Cada motor tiene su tope cuando suena solo:

| Motor | Voces |
| --- | --- |
| ANALOG, DIGITAL, PHASE, LOFI, SAMPLE, TRIO, WHEEL, NOISE | 8 |
| ★ MUUG | 8 (según el preset: polifónico o monofónico) |
| FM6 | 6 |
| VOICE | 4 |
| GRAIN | 3 |
| PHYS | 3 (modelo SYMP: 2) |

La batería tiene aparte sus propias 6 voces. Los modos MONO y LEGATO tocan una nota por vez.

### Modos de voz

POLY, MONO, LEGATO y UNISON, además de glide, desafinación, panorama y prioridad de nota (páginas VOICE y VOICE 2).

---

## 10. MUUG, el sinte tipo Moog

MUUG es la versión de Kitten Synths del motor de FMini-1: tres osciladores, un mezclador con ruido, un filtro de escalera de 24 dB por octava con su propio contorno, y modulación por LFO o ruido. El sonido es el del FMini-1 original.

### Elegir un sonido

En una pista de sinte, abrí **PRESETS** y elegí cualquiera de los 100 sonidos MUUG. Los nombres que evocan canciones o artistas están en español o con una letra cambiada (por ejemplo MANDARINA, SIENTO ARP, FARFISAH, SOLINAH), a propósito.

Las categorías en la lista: bajos (11), leads y metales (32), pads y atmósferas (22), teclados y órganos (13), plucks y stabs (12) y efectos (10). La lista completa está en [CARACTERISTICAS.md](CARACTERISTICAS.md#los-100-sonidos-muug-por-categoría).

### Las ocho perillas de EDIT

Las páginas **EDIT 1** y **EDIT 2** muestran lo más usado:

| Parámetro | Qué hace |
| --- | --- |
| CUT | Frecuencia de corte del filtro |
| EMPH | Énfasis (resonancia) |
| CNTR | Cantidad del contorno del filtro |
| F.ATK · F.DEC · F.SUS | Ataque, decaimiento y sostenido del contorno del filtro |
| MOD | Profundidad de la modulación |
| SLOT | Qué parche usa: 1 a 100 (de fábrica) u **OWN** (el tuyo) |

### ★ Páginas de edición en el equipo

Además hay páginas exclusivas de MUUG:

| Dónde | Página | Parámetros |
| --- | --- | --- |
| EDIT | **OSC RNG** | RNG 1, RNG 2, RNG 3 (rango de cada oscilador: LO, 32', 16', 8', 4', 2') y OSC ON (cuáles suenan) |
| EDIT | **OSC WAV** | WAVE 1, WAVE 2, WAVE 3 (TRI, SHARK, SAW, SQR, PLS W, PLS N) y TUNE |
| EDIT | **OSC FRQ** | FREQ 2, FREQ 3 (±7 semitonos), KBD (seguimiento del teclado) y NOISE (apagado, blanco, rosa) |
| EDIT | **MIXER** | Nivel de OSC 1, OSC 2, OSC 3 y ruido |
| ENV | **FLT ENV** | El contorno del filtro: F.ATK, F.DEC, F.SUS, CNTR |
| LFO | **MUUG MOD** | SRC (fuente de modulación, del LFO al ruido), >OSC (modula el tono), >FILT (modula el filtro) y SQR |

La envolvente de volumen es la ENV normal (ATK, DEC, SUS, REL).

### Parche propio (OWN)

Cuando cambiás algo de las páginas de osciladores, mezclador o modulación (o mandás un parche desde el editor web), el resultado es tu parche **propio** de esa pista y SLOT pasa a **OWN**. Si girás SLOT a un número de 1 a 100 se carga ese sonido de fábrica, y tu parche propio queda guardado aparte: al volver a OWN lo recuperás. Los parches propios se guardan con la sección y con el autoguardado.

### Polifonía y modo de cada preset

MUUG toca hasta 8 voces. Cada preset trae su modo: los leads y bajos vienen en **MONO** (legato) y los pads, teclados y órganos en **POLY**. Podés cambiarlo en la página VOICE.

### Rueda de modulación

El **CC 1** de tu controlador MIDI lleva la profundidad de modulación (MOD) hasta el máximo. También podés asignarla con MIDI LEARN.

---

## 11. La parte LITE (cuarto sinte)

La parte LITE es una pista sintetizadora más, gris, que se elige con ALGORITHM entre la pista 3 y la batería.

**Qué toca:** DIGITAL, PHASE, LOFI, SAMPLE y VOICE. Son los motores de menor costo y memoria de estado. Al elegir la parte LITE, la lista de sonidos solo ofrece lo que puede tocar.

**Para qué sirve:** capas, acompañamientos, texturas, un arpegio chip junto a un bajo MUUG.

**Cómo es distinta de las pistas 1–3:**

- No tiene arena de memoria propia ni **SLICER**.
- No tiene canal MIDI propio en GLO → MIDI (queda en OFF): se toca por MIDI desde los canales que siguen a la pista elegida (4–16), o desde las teclas.
- Se guarda con las secciones y el autoguardado en el espacio aparte descrito en el [capítulo 8](#8-canciones-guardado-y-autoguardado).
- Comparte el presupuesto de 8 voces con las demás pistas sintetizadoras.

---

## 12. Efectos

- **Efectos de golpe (FX)**: 27, sincronizados al tempo.
- **Master**: **DUST** (sampler viejo y disco: bits, tasa, crujido), **DUCK** (el bombo hace "bombear" los sintes), **FILT** (filtro DJ) y un limitador de salida.
- **TEXTURE**: una cama de fondo en bucle (vinilo, cinta, lluvia, viento, radio, ambiente o una de tus muestras).
- **Por pista**: drive, **INSERT** (clip suave y duro, plegador de onda, fuzz, bitcrush, phaser, flanger, chorus), slicer (menos en LITE), y envíos a **chorus** estéreo, **delay** sincronizado y **reverb** estéreo.
- Resonancia del filtro por pista, y el filtro FX también funciona en la batería.

---

## 13. Menú HOME, colores y luces

Mantené **HOME** para abrir el menú. SELECT pasa de sección, KNOB 1–3 cambian las filas, PRESETS mueve el cursor, OCT+ cambia o abre, OCT− cierra.

| Ítem | Opciones |
| --- | --- |
| **COLOR** | 5 paletas (★ PUMPKIN, la de fábrica, naranja; SLIME, BONE, WITCH y BLOOD) y tu tema propio (hecho en el editor web) |
| **ZOOM** | Lectura grande del valor que girás |
| **KNOB ACCEL** | Las perillas aceleran si las girás rápido |
| **LIGHTS** | Brillo de los botones: OFF / LOW / MID / HIGH |
| **KEYS** | Teclas que se iluminan: C / blancas / todas |
| **NOTES** | Las notas que suenan iluminan sus teclas |
| **SPEAKER LOWCUT** | Corte de graves para el parlante chico |
| **USB AUDIO** | MASTER o FULL |
| **USB RATE** | ★ 8 CH 44.1 (fijo: la entrada multipista va a 44,1 kHz) |
| **HARDWARE CALIBRATION** | Calibración del panel |
| **ABOUT** | Versión y créditos |

En HOME, el **visualizador** a pantalla completa se abre desde la pantalla de pistas; SELECT cambia de estilo. ★ Uno de los estilos es el **gatito** que parpadea al ritmo del tempo.

---

## 14. MIDI y audio USB

**La compatibilidad es idéntica a SLOOP.**

### Entrada MIDI

Por el jack **TRS de 3,5 mm** (con un adaptador TRS a DIN) y por **USB** (computadora, celular o caja host). Un teclado USB enchufado directo al FM-1 no funciona (ambos son dispositivos USB); Bluetooth MIDI tampoco.

| Canal MIDI | Toca |
| --- | --- |
| 1, 2, 3 | Sintes 1, 2, 3 |
| 10 | La batería |
| Los demás (4–16) | La pista elegida en ese momento |

En GLO → MIDI podés fijar el canal de cada pista; GLO → MIDI 2 define IN, OTHER, OUT y BEND.

### Salida MIDI y clock

- Lo que tocás sale siempre por USB MIDI; con **OUT = SEQ** sale también lo que tocan el secuenciador y el arpegiador.
- **Clock de entrada**: GLO → SYSTEM → SYNC = USB o TRS. Sigue START, CONTINUE y STOP, sin deriva. **IN = CLOCK** sigue solo el reloj.

### CC y MIDI LEARN

| CC | Controla |
| --- | --- |
| 1 | ★ Modulación de MUUG (rueda de modulación) |
| 5 | GLIDE |
| 7 | Nivel |
| 10 | Panorama |
| 64 | Pedal de sustain |
| 71 | Resonancia del motor |
| 72 · 73 · 75 | Release · attack · decay |
| 74 | Filtro de la pista |
| 91 · 93 · 94 | Envíos de reverb, chorus y delay |

Además: pitch bend (rango en GLO → MIDI 2 → BEND), Program Change y **Bank Select (CC 0)**. **MIDI LEARN**: mantené GLO y tocá F#3, mové la perilla del FM-1, mové la de tu controlador; repetí para terminar.

### Audio USB

El FM-1 también es una **placa de sonido USB de 8 canales** ("Felucca"), de 44,1 kHz y 16 bits, sin drivers. ★ Cada pista sale por su propio canal, así podés grabarlas por separado en tu DAW:

| Canales | Qué llevan |
| --- | --- |
| 1-2 | El **master** estéreo, exactamente lo que sale por los auriculares (como en SLOOP) |
| 3 | Pista 1 (sinte) |
| 4 | Pista 2 (sinte) |
| 5 | Pista 3 (sinte) |
| 6 | Pista 4, LITE |
| 7 | Batería |
| 8 | (en silencio) |

Las pistas (3 a 7) van **en mono y pre-master**: con su nivel, paneo, mute, solo, DIST, INSERT y filtro de pista, pero **sin** el chorus, el delay ni la reverb compartidos y sin los efectos del master (DUST, FILT, perilla MASTER). Si querés los efectos en las pistas separadas, ponelos en el DAW; o grabá también el master.

- Casi todos los programas graban los canales 1-2 por defecto: si solo querés la mezcla, no hace falta cambiar nada.
- **Reaper, Ableton, Bitwig, Cubase, Studio One:** elegí la entrada "Felucca" con sus 8 canales y armá una pista por canal (3, 4, 5, 6, 7 en mono y 1-2 en estéreo).
- **Audacity:** Preferencias → Dispositivos → Grabación → Canales: 8.
- **Windows:** si una app ve solo 2 canales, usá en el DAW el modo WASAPI exclusivo (o ASIO4ALL).
- El nivel del master (1-2) lo define HOME → USB AUDIO (MASTER o FULL); el de las pistas no depende de la perilla MASTER.
- Después de instalar, **desenchufá y enchufá** el FM-1 una vez: la computadora tiene que verlo como dispositivo nuevo de 8 canales.

---

## 15. El editor web

Se abre desde el instalador (`http://localhost:8766/site/webapp/editor/`, con `servir.py` en marcha) en Chrome o Edge. Pide acceso MIDI al abrirse. Con el FM-1 conectado, apretá **Connect**: el editor sigue el equipo en vivo.

Páginas principales: **Sound** (todos los parámetros de la pista y los motores; ★ incluye los parámetros de MUUG), **Sequencer** (pasos, piano roll, exportar e importar MIDI), **Tracks** (las ★ cinco pistas), **Song**, **Library**, **Samples** (con CHOP), **Drum synth**, **Song & sections** (con copia de seguridad) y **Settings**.

★ **Controlador MIDI**: el editor puede escuchar un controlador conectado a la computadora y tocar con él las pistas del FM-1.

El protocolo está documentado en `web/EDITOR_PROTOCOL.md` del código fuente de SLOOP.

---

## 16. Tus propias muestras

- **Cuatro ranuras** (USR1–USR4) de unos 7,4 segundos cada una; se tocan desde una pista con motor SAMPLE o como kit de batería (USR3+4 forma un kit de unos 15 s). Hasta 16 archivos WAV por ranura, uno por tecla.
- **CHOP** en el editor web: abrí o arrastrá una grabación de cualquier largo (WAV, MP3, AIFF...), marcá golpes a mano o automáticamente, quedate con los cortes que quieras y mandalos a una ranura.

---

## 17. Solución de problemas

**El instalador o el editor no encuentra el FM-1.** Usá Chrome o Edge, un cable de datos, sin hub, y permití el acceso MIDI. Cerrá cualquier otra aplicación o pestaña que use MIDI y recargá.

**La instalación se cortó.** Apretá Instalar otra vez. Si el equipo no arranca, **OCT−** apretado al encender (rescate USB) y reinstalá.

**Las teclas negras no suenan en una pista de sinte.** Esa pista está en modo acordes o escala: mantené SEL, poné KNOB 1 CHORD en OFF y KNOB 3 KEYS en OFF.

**No suena nada por el jack MIDI.** Probá el otro tipo de adaptador (A o B) y revisá el canal de tu teclado.

**No aparece la entrada de audio USB.** Desenchufá y enchufá el FM-1. En Audacity: Transport → Rescan Audio Devices.

**La grabación USB suena baja.** HOME → USB AUDIO en FULL, o subí MASTER.

**Las notas grabadas se mueven a la grilla.** Es la cuantización: poné QUANT en off en la pantalla REC.

**Se apagan notas en una parte densa.** El procesador llega a su límite y se retira una voz (nunca el bajo ni el lead). Usá menos notas sostenidas o un motor más liviano.

**La parte LITE o un parche propio de MUUG no volvió al cargar una sección.** Mirá el aviso al guardar (*LITE NOT*, *LITE TOO BIG*) y guardá de nuevo; ver [capítulo 8](#8-canciones-guardado-y-autoguardado).

**Un sonido de SLOOP que usabas no está.** Se quitaron siete (ver el [capítulo 1](#1-novedades-de-kitten-synths)).

¿Otra cosa? Abrí un *issue* en GitHub contando qué hiciste, qué esperabas, qué pasó y la versión (HOME → ABOUT).

---

## 18. Límites conocidos

- **Memoria de programa casi llena** (quedan unos cientos de bytes). Cualquier función nueva exige sacar algo.
- **Sin sexta pista** (una segunda batería con su propio kit): queda para más adelante.
- **LITE** sin canal MIDI propio, sin SLICER, y limitada a cinco motores.
- **Un solo respaldo** del espacio de LITE y los parches propios de MUUG (ver capítulo 8).
- **Colores** de LITE y de la batería: todavía no se pueden editar por separado (usan los del tema).
- **MUUG** toca 8 voces, no las 12 del FMini-1 original (el presupuesto del FM-1 es de 8 en total).
- El instalador no ofrece volver al firmware oficial V15.
