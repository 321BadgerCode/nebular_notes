<h1>Nebular Notes</h1>
<p>Microtonal MIDI Generator Based on Astrology Charts.</p>

---

## 🌌 Description

**Nebular Notes** is a Python-based generative music system that fuses astrology and algorithmic composition. It converts **birth chart data** — date, time, and location — into **microtonal MIDI melodies**, using planetary positions to algorithmically drive musical parameters.

Whether you're an experimental composer, astrologer, or creative technologist, this tool transforms cosmic alignments into deeply expressive sound.

---

## 🔧 Usage

```bash
# Install dependencies
pip install skyfield mido

# Run the program
git clone https://github.com/321BadgerCode/nebular_notes.git
cd ./nebular_notes/
python ./main.py
```

Then edit the birth chart values inside the script:

```python
date = "1995-06-15"
time = "12:00:00"
lat = 51.5074
lon = -0.1278
```

Output:  
🎵 A MIDI file like `astro_microtonal_output.mid` in the current directory.

---

## 🧠 Background

The inspiration comes from a blend of:

- **Microtonal theory** — Just Intonation, quarter-tones, harmonic ratios
- **Astrology** — Classical 7-planet model and angular relationships
- **Algorithmic composition** — Mapping data structures to musical parameters
- **Procedural aesthetics** — Generating melodies from hidden order

Instead of deterministic note patterns, the **planetary positions** become **musical DNA**:  
*Mars gives rhythm. Moon brings expression. Mercury alters phrasing.*

---

## ⚙️ How It Works

### 1. 🪐 Astronomy via Skyfield

AstroMicrotone uses the [Skyfield](https://rhodesmill.org/skyfield/) library to calculate ephemerides for celestial bodies:

- Mars, Moon, Mercury longitudes
- Angular distance between Mars and Moon

These are all extracted in **ecliptic degrees** and wrapped to [0°, 360°].

---

### 2. 🎼 Mapping Astrology to Music

| Celestial Body | Controls            | Mapping Logic                                                   |
|----------------|---------------------|------------------------------------------------------------------|
| Mars           | **Tempo**           | Mars longitude → BPM (60–240)                                   |
| Moon           | **Velocity**        | Moon longitude → MIDI velocity (40–127)                         |
| Mercury        | **Duration**        | Mercury longitude → duration (240–720 ticks)                    |
| Mars–Moon Angle| **Pitch Bend**      | Angle mapped to −100 to +100 cents, converted to pitch wheel    |

The MIDI output uses:
- 8 notes from a fixed C-major scale
- Pitch bend for microtonality
- Per-note dynamics and rhythm from astro inputs

---

### 3. 🎹 MIDI Output via Mido

The `mido` library sends the generated melody to a `.mid` file.

Pitch bending is encoded via MIDI pitch wheel messages:
```python
pitchwheel = cents_to_pitchbend(cents) # clamped in −8192..8191
```

---

## 🧪 Example Outputs

| Chart Date        | Location        | Output Filename                       | Unique Aspects                      |
|-------------------|-----------------|---------------------------------------|-------------------------------------|
| June 15, 1995     | London, UK      | `astro_microtonal_output_london.mid`  | Fast tempo, warm velocity           |
| May 8, 1945       | Germany, Earth  | `astro_microtonal_output_germany.mid` | Slow tempo, medium velocity         |
| December 31, 2020 | Toyko, Japan    | `astro_microtonal_output_tokyo.mid`   | Medium tempo, warm velocity         |

---

## ✨ Future Features

- 🎵 Harmony from Jupiter and Venus
- 🌗 Chord density from Moon phases
- 🎼 Export to **Scala tunings** or **MTS SysEx**
- 🖥 GUI with date pickers and real-time sound
- 🌐 Web version with WASM + WebMIDI

---

<div class="center">
Made with ☉ Sunlight, ☾ Moonlight, and 🎶 Music Theory
</div>