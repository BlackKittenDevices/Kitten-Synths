# Kitten Synths manual

Firmware for the **M-VAVE FM-1** · version 2.8-kitten · Black Kitten Devices · [Leer en español](MANUAL.md)

Kitten Synths is built on **SLOOP 2.8**. Everything SLOOP does works the same here, with the same gestures. This manual covers the whole instrument and marks what Kitten Synths adds with **★ NEW**. For the fine detail of each SLOOP page, see the [original SLOOP guide](https://github.com/isod89/sloop-fm1/blob/ec9e53721cc576816a5750220391f2d0217c01cb/GUIDE.md).

## Contents

1. [What Kitten Synths adds](#1-what-kitten-synths-adds)
2. [Installing](#2-installing)
3. [The panel and the five tracks](#3-the-panel-and-the-five-tracks)
4. [Your first beat in 60 seconds](#4-your-first-beat-in-60-seconds)
5. [Playing live: the layers](#5-playing-live-the-layers)
6. [Drums](#6-drums)
7. [Recording and the sequencer](#7-recording-and-the-sequencer)
8. [Songs, saving and autosave](#8-songs-saving-and-autosave)
9. [Engines and sounds](#9-engines-and-sounds)
10. [MUUG, the Moog-style synth](#10-muug-the-moog-style-synth)
11. [The LITE part (fourth synth)](#11-the-lite-part-fourth-synth)
12. [Effects](#12-effects)
13. [HOME menu, colours and lights](#13-home-menu-colours-and-lights)
14. [MIDI and USB audio](#14-midi-and-usb-audio)
15. [The web editor](#15-the-web-editor)
16. [Your own samples](#16-your-own-samples)
17. [Troubleshooting](#17-troubleshooting)
18. [Known limits](#18-known-limits)

---

## 1. What Kitten Synths adds

Compared with SLOOP 2.8, Kitten Synths adds:

### ★ A new engine: MUUG

- A synth in the style of Moog's classic **three-oscillator** instruments, ported from [FMini-1](https://github.com/ruppert/fmini-1). It is engine number 13 (SLOOP has 12).
- **100 factory sounds** (basses, leads, pads, brass, plucks, keys, effects), ready in the preset list.
- A **24 dB per octave** ladder low pass filter with its own contour (attack, decay, sustain), resonance and keyboard tracking.
- **Full editing on the FM-1 itself**: new pages for the oscillators, the mixer, modulation and the filter envelope. You don't need the web editor to build a sound.
- **Your own patch ("OWN")**: start from any of the 100 sounds, change it, and it is kept as your patch on that track.
- Up to **8 voices**. Each preset chooses polyphonic or monophonic (legato) play.
- **Mod wheel (CC 1)** over MIDI: takes the modulation depth up to the maximum.

More in [chapter 10](#10-muug-the-moog-style-synth).

### ★ A fourth synth: the LITE part

An extra synth track, **grey**, placed before the drums. It uses only light engines (**DIGITAL, PHASE, LOFI, SAMPLE and VOICE**), so four synths and the drums can sound at once without choking the processor. It is saved with your projects and with autosave. More in [chapter 11](#11-the-lite-part-fourth-synth).

### ★ Five tracks everywhere

The order is always **1, 2, 3, LITE, drums** (drums last). You see it on the tracks screen (HOME), in the mixer (GLO), in the visualizers, in the web editor and in mute / solo.

### ★ Kittens and Halloween

- A boot logo with the **kitten** (2.5 seconds).
- **PUMPKIN factory palette**: a black background and orange text, with tracks in violet, acid green, yellow, bone grey and orange. The other palettes are SLIME (green), BONE (grey), WITCH (violet) and BLOOD (red).
- A new visualizer: **the kitten whose eyes open and close on the BPM**.
- The BOUNCE, SLOOP (little boat) and LCD visualizers were removed.
- The installer and the web editor use Kitten Synths' identity.

### ★ Filter and envelope graphs

- MUUG's **FLT ENV** page draws the filter contour (F.ATK, F.DEC, F.SUS) with the same graph as the main envelope.
- MUUG's first EDIT page (CUT, EMPH, CNTR, F.ATK) draws the ladder **filter curve**: the vertical line marks the cutoff and the peak the resonance, and they move as you turn the knobs.
- ANALOG's FILTER page draws the curve in low pass (LP), band pass (BP) or high pass (HP), following the type chosen.

### ★ Its own installer and web editor

- The **installer** opens with a single command (`servir.py`): plug in the FM-1 and press Install.
- The **web editor** asks for MIDI access when it opens, sees the five tracks, edits MUUG patches and listens to a **MIDI controller** connected to the computer.

### ★ More saved

The LITE part and MUUG's own patches are saved **with each section (A–D)** and with autosave, in a separate area of memory. SLOOP's project files don't change.

### ★ Fewer SLOOP sounds, to make room

The FM-1's program memory is almost full. To fit everything, seven SLOOP sounds were removed: DIGITAL **STEEL DRUM**, SAMPLE **UP BASS**, VOICE **HARMONICA**, WHEEL **REGGAE ORG** and PHYS **HAND DRUM**, **MEMB TOMS** and **TABLA**. The samples, the drum kits and the filter tables were left untouched.

### What does not change

- **MIDI identical to SLOOP**: the same channels, CCs, clock, program change, bank select.
- The 64-step sequencer, song mode, the 27 punch-in effects, your own samples and USB rescue work the same.

### ★ Multitrack recording over USB

USB audio has **8 channels**: the master on 1-2 (as always) and each track on its own, pre-master (the 4 synths and the drums). See [chapter 14](#usb-audio).

---

## 2. Installing

> Installing custom firmware is **at your own risk**. Make a backup first.

### What you need

- An M-VAVE FM-1.
- A computer with **Chrome or Edge** and **Python 3**.
- A USB **data** cable, connected directly (no hub).

### Step by step

1. **Back up.** With the web editor of the firmware you have now, save a full backup (songs, your presets, samples, settings).
2. **Get the package.** From *Releases*, download `Kitten-Synths-instalador-…zip` and unzip it. (Or on GitHub: **Actions** tab → **build** → **Run workflow**, then download the **kitten-synths** artifact.)
3. **Open the installer.** Run `servir.py` (on Windows: double click, or `python servir.py` from a terminal in that folder). It opens `http://localhost:8766/site/webapp/installer/`.
4. **Plug in the FM-1** over USB and press **Install**. Allow MIDI access when the browser asks.
5. **Wait** for the done message. The FM-1 restarts with the kitten logo.
6. **Unplug and plug in** the FM-1 once, so the computer finds the USB audio.

Your projects, presets, samples and settings are kept when you install.

### Try it without the FM-1

**In the browser:** https://blackkittendevices.github.io/Kitten-Synths/play/?fw=kittensynths&mhz=60&latency=playback runs the real firmware on an emulated FM-1 (its screen, buttons, keys and sound; thanks to [fm1-emu](https://github.com/joakimeriksson/fm1-emu) by Joakim Eriksson). The playable editor without an FM-1: https://blackkittendevices.github.io/Kitten-Synths/simulator/playable.html?mock=1 (or, with `servir.py` running, `http://localhost:8766/simulator/index.html?mock=1`). Neither replaces the real device.

### If something goes wrong

- **The install was interrupted:** the FM-1 stays in update mode. Press Install again and it finishes.
- **The FM-1 no longer starts Kitten Synths:** hold **OCT−** while you switch it on (*USB rescue*) and install again.
- **The device doesn't switch on at all:** you need a recovery tool such as [FM-1-transporter](https://github.com/kurogedelic/FM-1-transporter).

### Going back

The Kitten Synths installer does **not** offer a way back to the official V15 firmware (it is no longer distributed). You can install the `.fwsc` of another compatible firmware, for example SLOOP. Back up first: Kitten Synths projects keep SLOOP's format, but only Kitten Synths understands the LITE part and MUUG's own patches.

---

## 3. The panel and the five tracks

### Tracks and colours

| Track | What it is | Colour |
| --- | --- | --- |
| 1 | Synth | violet |
| 2 | Synth | acid green |
| 3 | Synth | yellow |
| 4 | ★ LITE synth | light grey |
| 5 | Drums | orange |

Pick the track with the **ALGORITHM** knob. The order on screen is 1, 2, 3, LITE, drums. The screen's colour theme is changed in the HOME menu and on the web editor's Theme page.

### Controls

| Control | What it does |
| --- | --- |
| **MASTER** | Volume (and the USB audio level, if USB AUDIO is set to MASTER). |
| **SELECT** | On HOME and inside a layer: tempo. On a page: the previous or next page of its group. In DRUMS: grid / kit. |
| **ALGORITHM** | Picks the track. |
| **PRESETS** | The sound of the chosen track, or the drum kit. |
| **KNOB 1–4** | The four knobs below; each has the colour the screen shows. |
| **OCT− / OCT+** | Octave (both together: back to 0). On drums, held: soft / loud hits. |
| **FX · SEL · ENV · LFO · EDIT · GLO** (top row) | Tap: opens their pages. Hold FX, SEL, EDIT or GLO: opens a layer. **SEL** is the second button of the row, between FX and ENV. |
| **HOME** | Tracks screen. Hold: menu. Tap it while holding a layer: keeps the layer open. |
| **SAVE** | On the tracks screen: the song screen. Elsewhere: the save pages. Hold: the song layer. |
| **ARP · SEQ** | Tap: their pages. Hold: note repeat · steps. |
| **PLAY** | Starts / stops every track. Its light blinks on every beat. |
| **REC** | Playing: record / stop. Stopped: arm. Hold: clear the track. |
| **EDIT + OCT− / OCT+** | Undo / redo. |

White is what you play; red is recording.

---

## 4. Your first beat in 60 seconds

1. With **ALGORITHM** choose the **drums** (orange). The white keys are 16 sounds; **PRESETS** chooses the kit (try *808* or *BOOMBAP*).
2. Press **REC** and play a free rhythm at your own tempo. Holding **OCT−** you play ghost notes; holding **OCT+**, loud hits.
3. **Press REC on the "1" after your last bar.** The loop closes, its length sets the tempo, the hits snap to the grid and it plays.
4. **REC** again while it plays: you record on top. Holding **ARP** and a hi-hat key, you play a roll.
5. Choose track **1**, **REC**, play a bass line. Try any **MUUG** preset. Holding **SEL** you play the key of your song.
6. Holding **FX**, play a key for a punch-in effect; still holding FX, **KNOB 2** is DUST and **KNOB 3** is DUCK.
7. A mistake? **EDIT + OCT−** undoes it.

---

## 5. Playing live: the layers

Each function button is a **layer**: hold it and the 16 white keys and the four knobs change job (the screen shows it). Tap it and its pages open. To keep a layer open, hold it and tap HOME.

| Hold | White keys | KNOB 1 · 2 · 3 · 4 |
| --- | --- | --- |
| **FX** (punch-in) | 27 punch-in effects over the whole mix: loops, stutter, reverse, tape stop, filters, bitcrush, echo... The black keys: bass / mid / treble cuts, rewind, octave, flanger, auto-pan, freeze, mono, fade out | FILTER · DUST · DUCK · track filter |
| **EDIT** (erase) | Erases a sound or note while the loop plays. A black key: mutes the drums live | SHIFT · LENGTH ×2 / ½ · TRANSPOSE |
| **ARP** (roll) | Note repeat on the grid | RATE (1/8 … 1/64) |
| **SEQ** (steps) | The 16 steps of the page. A step held: level, roll, nudge, parameter locks | SOUND / NOTE · DIV · SWING · LENGTH |
| **SEL** (key) | The song's key | CHORD · SCALE · KEYS · TRANSPOSE |
| **GLO** (mix) | 1–5 mute, 6–10 solo, fill, tap tempo | Track levels |
| **SAVE** (song) | 1–4 play sections A–D, 5–8 save the loop into them, 13 loop / song, 14 record song, 16 chain | — |

> With five tracks, in GLO the mutes go from 1 to 5 and the solos from 6 to 10, in the screen's order (LITE before the drums).

---

## 6. Drums

- **16 sounds** on the white keys; a black key doubles the white key on its left (two-finger rolls).
- **Ghost and loud hits**: hold **OCT−** / **OCT+** while you play. Each hit keeps its level and a roll (x1–x4).
- **37 kits**: one sampled acoustic kit in 5 treatments (CC0 studio recordings) and 32 synthesized ones (808, 909, 606, trap, drill, boom bap, lo-fi, house, techno, jungle, amapiano, jazz brushes...).
- **Your own kits**: USR1–USR4 and USR3+4 use samples you load in the web editor. **SYN1–SYN4** are synthesized kits you build on the editor's Drum synth page.
- The DRUMS screen has a grid (the keys are the steps of the chosen sound) and the kit.
- **TUNE** and **DECAY** per sound, on the SOUND page of the DRUMS screen.

---

## 7. Recording and the sequencer

### Recording

- While it plays, **REC** records at once and each pass is added on top (overdub). Notes land where you heard them: the keys' latency is compensated.
- **REC screen** (before the first note): *mode* free (the tempo follows you) or fixed tempo; *length* of 1, 2 or 4 bars; *start* on your first note or after a one-bar count-in; **QUANT off** keeps your feel as nudges.
- Hold **REC** about 2 seconds to clear the track; undo brings it back.

### Sequencer

- **64 steps per track**, each with its own length and division (1/32 up to two bars), so polyrhythms stay in phase.
- Chords of up to 4 notes per step, ties, slide, MPC-style **swing** from 0 to 100, and one precise clock (no drift at any tempo).
- **Parameter locks**: hold a step to give it its own value of any parameter.
- **Nudge** (micro timing) and **fill conditions** per step.
- A piano roll note editor for the synths (SEQ → NOTES). For a step's sheet, hold OCT+ on it: SLIDE, NUDGE, FILL, MOVE, COPY, DELETE.

---

## 8. Songs, saving and autosave

- **Sections A–D**: save the loop (SAVE + keys 5–8), play them live on the next bar (SAVE + keys 1–4) and **record the song** while you play it (SAVE + key 14). Hold SAVE and tap several sections for a **quick chain**. The SONG screen edits the order by hand.
- **Autosave**: leave the device still for 2.5 seconds and your work is saved; at power-on everything comes back as you left it.
- **32 user presets**, **27 FM6 patches**, undo / redo.
- **Full backup** from the web editor: one file with everything.

### ★ What Kitten Synths saves

With each section and with autosave, the **LITE part** (its sound and its sequence) and **MUUG's own patches** are saved too. This lives in a separate area of memory. Two things to keep in mind:

- If that area doesn't have room for a section's LITE part, the device says so (*SAVED, LITE NOT* or *LITE TOO BIG*) and saves the rest anyway.
- That area has a single copy: if the power goes off exactly while it is written, the LITE part and your own patches can be lost, but **not** the rest of your projects.

---

## 9. Engines and sounds

### The 13 engines

| Engine | What it is | In LITE |
| --- | --- | --- |
| ANALOG | Subtractive analog, LP / BP / HP filter | no |
| DIGITAL | 4-operator FM | **yes** |
| FM6 | 6-operator FM with DX7 patches | no |
| PHASE | Phase distortion | **yes** |
| TRIO | Three oscillators | no |
| WHEEL | Tonewheel organ (drawbars) | no |
| VOICE | Formant voice | **yes** |
| GRAIN | Granular | no |
| LOFI | Lo-fi chip | **yes** |
| SAMPLE | Sampler | **yes** |
| PHYS | Physical models (guitars, sitar, bells) | no |
| NOISE | Noise | no |
| ★ **MUUG** | Moog-style synth (100 sounds) | no |

### Sounds

**250 sounds** in all (150 from SLOOP and 100 from MUUG), browsable by type: basses, keys, organs, pads, leads, plucks, stabs and effects. All levelled with each other. There is room for **32 presets of your own**.

### Polyphony (voices)

There is a budget of **8 voices shared by all the synth tracks**; if you play more, the oldest voice leaves with a fade (never the bass or the lead). Each engine has its own cap when it plays alone:

| Engine | Voices |
| --- | --- |
| ANALOG, DIGITAL, PHASE, LOFI, SAMPLE, TRIO, WHEEL, NOISE | 8 |
| ★ MUUG | 8 (by preset: polyphonic or monophonic) |
| FM6 | 6 |
| VOICE | 4 |
| GRAIN | 3 |
| PHYS | 3 (SYMP model: 2) |

The drums have their own 6 voices. The MONO and LEGATO modes play one note at a time.

### Voice modes

POLY, MONO, LEGATO and UNISON, plus glide, detune, pan and note priority (VOICE and VOICE 2 pages).

---

## 10. MUUG, the Moog-style synth

MUUG is Kitten Synths' version of the FMini-1 engine: three oscillators, a mixer with noise, a 24 dB per octave ladder filter with its own contour, and modulation from the LFO or noise. It sounds like the original FMini-1.

### Choosing a sound

On a synth track, open **PRESETS** and choose any of the 100 MUUG sounds. Names that recall songs or artists are in Spanish or have a letter changed (for example MANDARINA, SIENTO ARP, FARFISAH, SOLINAH), on purpose.

The categories in the list: basses (11), leads and brass (32), pads and atmospheres (22), keys and organs (13), plucks and stabs (12) and effects (10). The full list is in [CARACTERISTICAS.md](CARACTERISTICAS.md#los-100-sonidos-muug-por-categoría).

### The eight EDIT knobs

The **EDIT 1** and **EDIT 2** pages show what you use most:

| Parameter | What it does |
| --- | --- |
| CUT | Filter cutoff |
| EMPH | Emphasis (resonance) |
| CNTR | Filter contour amount |
| F.ATK · F.DEC · F.SUS | Attack, decay and sustain of the filter contour |
| MOD | Modulation depth |
| SLOT | Which patch it uses: 1 to 100 (factory) or **OWN** (yours) |

### ★ Edit pages on the device

There are also pages only MUUG has:

| Where | Page | Parameters |
| --- | --- | --- |
| EDIT | **OSC RNG** | RNG 1, RNG 2, RNG 3 (each oscillator's range: LO, 32', 16', 8', 4', 2') and OSC ON (which ones sound) |
| EDIT | **OSC WAV** | WAVE 1, WAVE 2, WAVE 3 (TRI, SHARK, SAW, SQR, PLS W, PLS N) and TUNE |
| EDIT | **OSC FRQ** | FREQ 2, FREQ 3 (±7 semitones), KBD (keyboard tracking) and NOISE (off, white, pink) |
| EDIT | **MIXER** | Level of OSC 1, OSC 2, OSC 3 and noise |
| ENV | **FLT ENV** | The filter contour: F.ATK, F.DEC, F.SUS, CNTR |
| LFO | **MUUG MOD** | SRC (modulation source, from LFO to noise), >OSC (modulates the pitch), >FILT (modulates the filter) and SQR |

The volume envelope is the normal ENV (ATK, DEC, SUS, REL).

### Your own patch (OWN)

When you change anything on the oscillator, mixer or modulation pages (or send a patch from the web editor), the result is that track's **own** patch and SLOT goes to **OWN**. Turning SLOT to a number from 1 to 100 loads that factory sound, and your own patch is kept aside: going back to OWN brings it back. Your own patches are saved with the section and with autosave.

### Polyphony and each preset's mode

MUUG plays up to 8 voices. Each preset brings its mode: leads and basses come in **MONO** (legato) and pads, keys and organs in **POLY**. You can change it on the VOICE page.

### Mod wheel

**CC 1** from your MIDI controller takes the modulation depth (MOD) up to the maximum. You can also assign it with MIDI LEARN.

---

## 11. The LITE part (fourth synth)

The LITE part is one more synth track, grey, chosen with ALGORITHM between track 3 and the drums.

**What it plays:** DIGITAL, PHASE, LOFI, SAMPLE and VOICE, the engines with the lowest cost and state memory. With the LITE part chosen, the sound list only offers what it can play.

**What it is for:** layers, accompaniment, textures, a chip arpeggio next to a MUUG bass.

**How it differs from tracks 1–3:**

- It has no memory arena of its own and no **SLICER**.
- It has no MIDI channel of its own in GLO → MIDI (it stays OFF): you play it over MIDI on the channels that follow the chosen track (4–16), or from the keys.
- It is saved with the sections and autosave, in the separate area described in [chapter 8](#8-songs-saving-and-autosave).
- It shares the budget of 8 voices with the other synth tracks.

---

## 12. Effects

- **Punch-in effects (FX)**: 27, in time with the tempo.
- **Master**: **DUST** (old sampler and record: bits, rate, crackle), **DUCK** (the kick makes the synths pump), **FILT** (DJ filter) and an output limiter.
- **TEXTURE**: a background bed in a loop (vinyl, tape, rain, wind, radio, ambience or one of your samples).
- **Per track**: drive, **INSERT** (soft and hard clip, wavefolder, fuzz, bitcrush, phaser, flanger, chorus), slicer (not in LITE), and sends to stereo **chorus**, synced **delay** and stereo **reverb**.
- Filter resonance per track, and the FX filter works on the drums too.

---

## 13. HOME menu, colours and lights

Hold **HOME** to open the menu. SELECT moves between sections, KNOB 1–3 change the rows, PRESETS moves the cursor, OCT+ changes or opens, OCT− closes.

| Item | Options |
| --- | --- |
| **COLOR** | 5 palettes (★ PUMPKIN, the factory one, orange; SLIME, BONE, WITCH and BLOOD) and your own theme (made in the web editor) |
| **ZOOM** | A big read-out of the value you turn |
| **KNOB ACCEL** | The knobs speed up when you turn them fast |
| **LIGHTS** | Button brightness: OFF / LOW / MID / HIGH |
| **KEYS** | Keys that light up: C / whites / all |
| **NOTES** | The notes playing light their keys |
| **SPEAKER LOWCUT** | A bass cut for the small speaker |
| **USB AUDIO** | MASTER or FULL |
| **USB RATE** | ★ 8 CH 44.1 (fixed: the multitrack input runs at 44.1 kHz) |
| **HARDWARE CALIBRATION** | Panel calibration |
| **ABOUT** | Version and credits |

On HOME, the full-screen **visualizer** opens from the tracks screen; SELECT changes its style. ★ One of the styles is the **kitten** blinking on the tempo.

---

## 14. MIDI and USB audio

**Compatibility is identical to SLOOP.**

### MIDI in

Through the **3.5 mm TRS** jack (with a TRS to DIN adapter) and over **USB** (computer, phone or host box). A USB keyboard plugged straight into the FM-1 doesn't work (both are USB devices); Bluetooth MIDI doesn't either.

| MIDI channel | Plays |
| --- | --- |
| 1, 2, 3 | Synths 1, 2, 3 |
| 10 | The drums |
| The others (4–16) | The track chosen at the moment |

In GLO → MIDI you can set each track's channel; GLO → MIDI 2 sets IN, OTHER, OUT and BEND.

### MIDI out and clock

- What you play always goes out over USB MIDI; with **OUT = SEQ** what the sequencer and the arpeggiator play goes out too.
- **Clock in**: GLO → SYSTEM → SYNC = USB or TRS. It follows START, CONTINUE and STOP, without drift. **IN = CLOCK** follows the clock alone.

### CCs and MIDI LEARN

| CC | Controls |
| --- | --- |
| 1 | ★ MUUG modulation (mod wheel) |
| 5 | GLIDE |
| 7 | Level |
| 10 | Pan |
| 64 | Sustain pedal |
| 71 | Engine resonance |
| 72 · 73 · 75 | Release · attack · decay |
| 74 | Track filter |
| 91 · 93 · 94 | Reverb, chorus and delay sends |

Also: pitch bend (range in GLO → MIDI 2 → BEND), Program Change and **Bank Select (CC 0)**. **MIDI LEARN**: hold GLO and play F#3, move the FM-1's knob, move your controller's; repeat to finish.

### USB audio

The FM-1 is also an **8-channel USB sound card** ("Felucca"), 44.1 kHz, 16-bit, no drivers. ★ Each track comes out on its own channel, so you can record them separately in your DAW:

| Channels | What they carry |
| --- | --- |
| 1-2 | The stereo **master**, exactly what the headphones get (as in SLOOP) |
| 3 | Track 1 (synth) |
| 4 | Track 2 (synth) |
| 5 | Track 3 (synth) |
| 6 | Track 4, LITE |
| 7 | Drums |
| 8 | (silent) |

The tracks (3 to 7) are **mono and pre-master**: with their level, pan, mute, solo, DIST, INSERT and track filter, but **without** the shared chorus, delay and reverb and without the master effects (DUST, FILT, the MASTER knob). If you want effects on the separate tracks, add them in the DAW, or record the master too.

- Most programs record channels 1-2 by default: if you only want the mix, nothing changes.
- **Reaper, Ableton, Bitwig, Cubase, Studio One:** pick the "Felucca" input with its 8 channels and arm one track per channel (3, 4, 5, 6, 7 mono and 1-2 stereo).
- **Audacity:** Preferences → Devices → Recording → Channels: 8.
- **Windows:** if an app only sees 2 channels, use WASAPI exclusive mode (or ASIO4ALL) in your DAW.
- The master's level (1-2) is set by HOME → USB AUDIO (MASTER or FULL); the tracks' don't depend on the MASTER knob.
- After installing, **unplug and plug in** the FM-1 once: the computer has to see it as a new 8-channel device.

---

## 15. The web editor

**Online:** https://blackkittendevices.github.io/Kitten-Synths/site/webapp/editor/ — or from the installer (`http://localhost:8766/site/webapp/editor/`, with `servir.py` running), in Chrome or Edge. It asks for MIDI access when it opens. With the FM-1 connected, press **Connect**: the editor follows the device live.

Main pages: **Sound** (every parameter of the track and the engines; ★ includes MUUG's parameters), **Sequencer** (steps, piano roll, MIDI export and import), **Tracks** (the ★ five tracks), **Song**, **Library**, **Samples** (with CHOP), **Drum synth**, **Song & sections** (with backup) and **Settings**.

★ **MIDI controller**: the editor can listen to a controller connected to the computer and play the FM-1's tracks with it.

The protocol is documented in `web/EDITOR_PROTOCOL.md` in SLOOP's source code.

---

## 16. Your own samples

- **Four slots** (USR1–USR4) of about 7.4 seconds each; play them from a track with the SAMPLE engine or as a drum kit (USR3+4 makes a kit of about 15 s). Up to 16 WAV files per slot, one per key.
- **CHOP** in the web editor: open or drag in a recording of any length (WAV, MP3, AIFF...), mark hits by hand or automatically, keep the slices you want and send them to a slot.

---

## 17. Troubleshooting

**The installer or the editor doesn't find the FM-1.** Use Chrome or Edge, a data cable, no hub, and allow MIDI access. Close any other app or tab using MIDI and reload.

**The install was interrupted.** Press Install again. If the device doesn't start, hold **OCT−** at power-on (USB rescue) and install again.

**The black keys don't sound on a synth track.** That track is in chord or scale mode: hold SEL, set KNOB 1 CHORD to OFF and KNOB 3 KEYS to OFF.

**Nothing plays through the MIDI jack.** Try the other adapter type (A or B) and check your keyboard's channel.

**The USB audio input doesn't appear.** Unplug and plug in the FM-1. In Audacity: Transport → Rescan Audio Devices.

**The USB recording is quiet.** HOME → USB AUDIO to FULL, or turn MASTER up.

**Recorded notes move to the grid.** That is quantizing: set QUANT to off on the REC screen.

**Notes drop out in a dense part.** The processor reaches its limit and a voice leaves (never the bass or the lead). Use fewer held notes or a lighter engine.

**The LITE part or a MUUG patch of yours didn't come back when loading a section.** Look at the message when saving (*LITE NOT*, *LITE TOO BIG*) and save again; see [chapter 8](#8-songs-saving-and-autosave).

**A SLOOP sound you used is missing.** Seven were removed (see [chapter 1](#1-what-kitten-synths-adds)).

Something else? Open an *issue* on GitHub with what you did, what you expected, what happened and the version (HOME → ABOUT).

---

## 18. Known limits

- **Program memory almost full** (a few hundred bytes left). Any new feature means removing something.
- **No sixth track** (a second drum track with its own kit): left for later.
- **LITE** has no MIDI channel of its own, no SLICER, and is limited to five engines.
- **A single copy** of the LITE area and MUUG's own patches (see chapter 8).
- **Colours** of LITE and the drums can't be edited separately yet (they use the theme's).
- **MUUG** plays 8 voices, not the original FMini-1's 12 (the FM-1's budget is 8 in all).
- The installer doesn't offer a way back to the official V15 firmware.
