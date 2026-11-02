# 🐈‍⬛ Cleaner sound, held notes that stay held · Sonido más limpio, notas sostenidas que se sostienen

**English.** The fixes of SLOOP 2.8.1 to 2.8.4, brought onto Kitten Synths:

- **Sequencer:** on a POLY track, a note you hold while recording others over it is no longer cut or restarted (live, free take and overdub). A note's LEN can run on under the notes after it. No more stuck notes after a burst of MIDI, and the kick no longer drops out on a busy beat.
- **Audio:** no more distortion at the end of notes (3.5 mm and USB): the mix rounds instead of truncating. UNISON no longer stacks its voices in phase, MUUG included. A sample played again starts from silence, no click.
- **Boot:** the kitten blinks once at power-on. To make room, four of SLOOP's visualizers (SPECTRUM, TAPE, ORBIT, WIRES) were left out; six remain.

Everything else is as in 2.8-kitten.4: the FM-1 as an 8-channel USB sound card (master + each track on its own channel), MUUG, the LITE synth. MIDI is unchanged (identical to SLOOP).

**Install:** download `Kitten-Synths-instalador-2.8-kitten.zip`, unzip it, run `servir.py` (Python 3, Chrome or Edge), press Install. Back up first. Manual: https://github.com/BlackKittenDevices/Kitten-Synths/blob/main/MANUAL.en.md

---

**Español.** Los arreglos de SLOOP 2.8.1 a 2.8.4, traídos a Kitten Synths:

- **Secuenciador:** en una pista POLY, una nota que sostenés mientras grabás otras encima ya no se corta ni se reinicia (en vivo, en toma libre y en overdub). El LEN de una nota puede seguir por debajo de las siguientes. No más notas colgadas después de una ráfaga MIDI, y el bombo ya no se pierde en un ritmo cargado.
- **Audio:** sin distorsión al final de las notas (3,5 mm y USB): la mezcla redondea en vez de truncar. El UNISON ya no apila sus voces en fase, MUUG incluido. Un sample tocado de nuevo arranca desde el silencio, sin click.
- **Arranque:** el gatito parpadea una vez al encender. Para hacerle lugar se quitaron cuatro visualizadores de SLOOP (SPECTRUM, TAPE, ORBIT, WIRES); quedan seis.

Todo lo demás sigue como en 2.8-kitten.4: el FM-1 como placa de sonido USB de 8 canales (master + cada pista en su canal), MUUG, el sinte LITE. El MIDI no cambia (idéntico a SLOOP).

**Instalar:** bajá `Kitten-Synths-instalador-2.8-kitten.zip`, descomprimilo, abrí `servir.py` (Python 3, Chrome o Edge) y apretá Instalar. Hacé backup antes. Manual: https://github.com/BlackKittenDevices/Kitten-Synths/blob/main/MANUAL.md

Also / además: MUUG (Minimoog-style, 100 sounds), a fourth LITE synth, 37 drum kits, 64-step sequencer, songs, 27 punch-in effects. Based on SLOOP 2.8 with the fixes of 2.8.4 · GPL-3.0 · identity `FM-1_969`.
