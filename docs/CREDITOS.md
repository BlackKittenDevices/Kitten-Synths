# Créditos

Kitten Synths es obra de **Black Kitten Devices** y existe gracias al trabajo abierto de muchas personas. Gracias a todas ellas.

## Base del proyecto

- **[SLOOP](https://github.com/isod89/sloop-fm1)** de **isod89** y su comunidad (versión 2.8): la groovebox sobre la que se construye todo. Kitten Synths lo toma de su repositorio en un commit fijo (`ec9e537`) y le aplica parches.
- **[Felucca](https://github.com/hugelton/Felucca)** de **Leo Kuroshita (@kurogedelic) / Hügelton Instruments**: el firmware base de SLOOP (motores, secuenciador, editor, instalador, audio USB, clock MIDI, motor FM6 y parches DX7, efectos INSERT, MIDI LEARN y mucho más).
- **[FMini-1](https://github.com/ruppert/fmini-1)** de **Guilherme Ruppert**: de ahí sale el motor del sintetizador tipo Moog, que Kitten Synths llama **MUUG**, con sus 100 parches de fábrica y su filtro de escalera.

## Colaboradores de SLOOP y Felucca

- **Wulgaren, etyrnal, benjaminguerrer, gospodindilly-ops, Armstrong1980, oMauNaProducer, lostfictions, planist79**: funciones pedidas y probadas en la comunidad de Felucca.
- **@renebohne**: luces de teclas, Program Change, CC 74.
- **ChanceTheMaker y keremimo**: entrada MIDI TRS y clock.
- **andrerezemini ([sloop-lab](https://github.com/andrerezemini/sloop-lab))**: sonido en el segundo núcleo y 38 KB de RAM recuperados, sobre el arranque de doble núcleo de **Charles Vestal ([X0X](https://github.com/charlesvestal/fm1-x0x))** y **keremimo ([Melodee](https://github.com/keremimo/melodee))**.
- **juanjiant-bit ([JIANT FM](https://github.com/juanjiant-bit/JIANT))**: aceleración de perillas y glide de nivel / panorama.
- **@ordenador (Mario Faúndez Vidal)**: vista previa de audio en el navegador (WebAssembly).
- Y todas las personas que instalaron SLOOP, lo probaron y reportaron errores.

## Material de terceros

| Qué | Licencia |
| --- | --- |
| Muestras de instrumentos y batería (Versilian Studios VSCO-2 CE, VCSL; Sonic Pi) | CC0 1.0 |
| Fuente Terminus (pantalla del FM-1 y editor web) | SIL OFL 1.1 |
| Fuente de íconos Fukiai (Hügelton Instruments), solo editor web | MIT |
| CrispyZebra de Leo Kuroshita: motor PHASE | GPL-3.0 |
| klattsch de Tony Gies: referencia de diseño del motor VOICE (sin código copiado) | MIT |
| msfa de Google Inc. y Pascal Gauthier (Dexed): motor FM6 | Apache-2.0 |
| DaisySP (Electrosmith, Emilie Gillet) y cuerdas simpáticas de Rings (Emilie Gillet): motor PHYS | MIT |
| SDK JieLi AC79: tres archivos que se leen al compilar y se incluyen en el paquete; no hay archivos del SDK en este repositorio | Apache-2.0 |

El detalle de cada licencia está en los archivos de SLOOP (`LICENSING.md`, `LICENSES/`), que el flujo de compilación descarga junto con el código.

## Kitten Synths

Diseño, parches, parte LITE, integración de MUUG, páginas de edición, guardado ampliado, estética de gatitos, instalador y editor adaptados: **Black Kitten Devices**, con desarrollo asistido por Claude (Anthropic).

## Marcas

M-VAVE y FM-1 son marcas de sus respectivos dueños. Kitten Synths es un firmware independiente: no está afiliado ni respaldado por M-VAVE, Hügelton Instruments, SLOOP ni los autores de FMini-1. Los nombres de los kits de batería describen estilos, no productos.
