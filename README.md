# Kitten Synths

Firmware for the **M-VAVE FM-1**, based on [SLOOP](https://github.com/isod89/sloop-fm1) (Felucca), with the **MUUG** engine (the Minimoog of [FMini-1](https://github.com/ruppert/fmini-1)), a 4th "lite" synth part and a web editor with MIDI IN for a controller. Halloween and black cats.

> Private while it is tested on the hardware. GPL-3.0, like SLOOP, Felucca and FMini-1: it is published with its source when it is shared.

## Build (automatic)
`Actions` > `build` > `Run workflow`. When it ends, download the artifact **kitten-synths**:

1. Unzip it.
2. Run `servir.py` (Python 3; Chrome or Edge). The installer opens: plug the FM-1 in and press install.
3. The simulator (no FM-1 needed): `http://localhost:8766/simulator/index.html?mock=1`.

Before the first install: make a **full copy of the FM-1 memory** (MvaveFM1Unbricker) and keep the official V15 at hand (the installer has "return to official V15").

## What is in the repository
- `muug.patch`: what is added to SLOOP 2.8 (commit `ec9e537`): Muug, the lite part, the editor, tests.
- `.github/workflows/build.yml`: gets SLOOP, applies the patch, runs the tests and builds with JieLi's toolchain.
- `servir.py`: serves the artifact on your computer.
