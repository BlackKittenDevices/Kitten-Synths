# 🥁 Two drum tracks, 8 channels into your DAW · Dos baterías y 8 canales a tu DAW

**English.** Kitten Synths now plays **six tracks at once: four synths and two drum kits**.

- **Drums 2 (track 6):** a whole second drum track with its own kit, pattern, level, pan, mute, solo, filter and SOUND page (tune / decay per sound). Pair an acoustic or sampled kit with an 808. Pick it with the track knob; it listens and sends on **MIDI channel 11** (every other channel is as in SLOOP).
- **8-channel USB audio:** the stereo master on 1-2 and each of the six tracks on its own channel (3-6 the synths, 7 drums, 8 drums 2), no drivers.
- **Screens and web editor** show the six tracks; GLO's keys: 1-6 mute, 7-12 solo, 13 fill, 14 fill next bar.
- Saved with each project. The USR4 sample slot holds 76 KiB now (its last 4 KiB keep drums 2).
- **New FM-1 units (flash chip UC25HQ80) work now:** the app, USB rescue and the updater know both flash chips, so projects save and the installer accepts the new units too. Untested on a new unit: please tell us how it goes.
- **Web editor:** drum pattern templates (12 styles x 2 variations: drum & bass, jungle, industrial, acid house, techno house, psy trance, hard techno, rock, heavy metal, doom metal, blues, jazz).
- Two drum tracks playing together no longer glitch in dense fills (issue #5): the second drum track now renders on the other core when both sound, instead of both one after the other on core 1.
- USB audio under load (issue #5): the copy into each 1 ms USB packet is cheaper, and the serial console `status` now reports `audio_max_total_us`, `audio_late`, `usb_poll_max_us` and the `uac_*` counters, to pin down a crackle while recording.
- Also: the fixes of SLOOP 2.8.1-2.8.4 (held notes while recording, clean note ends, UNISON spread) and the blinking kitten at power-on.

**Install:** download `Kitten-Synths-instalador-2.8-kitten.zip`, unzip it, run `servir.py` (Python 3, Chrome or Edge), press Install. Back up first. Manual: https://github.com/BlackKittenDevices/Kitten-Synths/blob/main/MANUAL.en.md

---

**Español.** Kitten Synths ahora toca **seis pistas a la vez: cuatro sintes y dos baterías**.

- **Batería 2 (pista 6):** otra batería completa con su kit, patrón, nivel, paneo, mute, solo, filtro y página SOUND (afinación y decay de cada sonido). Combiná una batería acústica o sampleada con una 808. Se elige con la perilla de pista; escucha y envía por el **canal MIDI 11** (los demás canales, como en SLOOP).
- **Audio USB de 8 canales:** el master estéreo en 1-2 y cada una de las seis pistas en su canal (3-6 los sintes, 7 la batería, 8 la batería 2), sin drivers.
- **Pantallas y editor web** con las seis pistas; teclas de GLO: 1-6 mute, 7-12 solo, 13 fill, 14 fill en la próxima barra.
- Se guarda con cada proyecto. La ranura USR4 queda en 76 KiB (sus últimos 4 KiB guardan la batería 2).
- **Los FM-1 nuevos (chip de flash UC25HQ80) funcionan:** la aplicación, el rescate USB y el actualizador conocen los dos chips; se guardan los proyectos y el instalador acepta las unidades nuevas. Sin probar en una unidad nueva: contanos cómo te va.
- **Editor web:** plantillas de patrones de batería (12 estilos x 2 variaciones: drum & bass, jungle, industrial, acid house, techno house, psy trance, hard techno, rock, heavy metal, doom metal, blues, jazz).
- **Pantallas nuevas (Noche de Brujas):** gatito en la cabecera, pistas en tarjetas de colores, filtro y envolvente con marco y área rellena, presets con caja. El editor web usa los mismos colores de pista.
- **Editor web, pestaña VISUAL (para ver mejor):** la pantalla del FM-1 en grande y con alto contraste (pistas, pasos y sonido), en tiempo real. Sin cambios en el firmware.
- Dos pistas de batería sonando juntas ya no glitchean en fills densos (issue #5): la segunda batería se renderiza en el otro núcleo cuando suenan las dos, en vez de las dos una detrás de otra en el núcleo 1.
- Audio USB bajo carga (issue #5): la copia de cada paquete USB de 1 ms es más barata, y `status` de la consola serie ahora informa `audio_max_total_us`, `audio_late`, `usb_poll_max_us` y los contadores `uac_*`, para ubicar un entrecortado al grabar.
- Además: los arreglos de SLOOP 2.8.1-2.8.4 (notas sostenidas al grabar, finales de nota limpios, UNISON abierto) y el gatito que parpadea al encender.

**Instalar:** bajá `Kitten-Synths-instalador-2.8-kitten.zip`, descomprimilo, abrí `servir.py` (Python 3, Chrome o Edge) y apretá Instalar. Hacé backup antes. Manual: https://github.com/BlackKittenDevices/Kitten-Synths/blob/main/MANUAL.md

Also / además: MUUG (Minimoog-style, 100 sounds), a fourth LITE synth, 37 drum kits, 64-step sequencer, songs, 27 punch-in effects. Based on SLOOP 2.8 with the fixes of 2.8.4 · GPL-3.0 · identity `FM-1_969`.
