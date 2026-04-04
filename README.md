# AI Music Generation

# Enhancing AI Music Generation with Multi-Module Neural Networks A Novel Approach to Chord, Rhythm, and Pitch Synthesis

[![MIT License](https://github.com/user-attachments/assets/f0fc5011-9ca9-485f-bfb6-1661708a0be5)](https://raw.githubusercontent.com/Athira1979/multi-module-music-gen/refs/heads/main/LICENSE)

## Table of Contents

+ [Overview](#overview)
+ [Features](#features)
+ [Installation](#install)
+ [Usage](#use)
+ [License](#license)

## 📌 Overview <a name = "overview"></a>

- Automatic music generation plays a crucial role in generating creative compositions autonomously, facilitating applications in various fields, including entertainment and education.
- The current approaches often struggle to:
   - Capture temporal dependencies across sequences.
   - Maintain harmonic coherence.
   - Generate dynamic rhythmic patterns effectively.
- This project introduces a Multi-Module Neural Network `(MNN)` for automatic music composition, combining several specialized modules.
- The modules are:
   - 🎼 Temporal Graph Dilated Convolution `(TGDC)`: Captures chord progression dependencies.
   - 🥁 Rhythm Generator `(MobileNet-TCN)`: Creates expressive rhythmic patterns.
   - 🎹 Pitch Generator `(Sparse Transformer)`: Generates coherent pitch sequences aligned with rhythm.
   - 🎶 Fusion & Post-Processing: Merges rhythm and pitch while refining timing, velocity, and harmonic structure.
- The result is a highly expressive, scalable music generation system that outputs MIDI files or audio-ready compositions.

## 🚀 Features <a name = "features"></a>

- Multi-module neural architecture for chords, rhythm, and pitch.
- High accuracy and harmonic coherence.
- 98.98% Accuracy and 98.13% F1 Score in experimental results.
- Support for MIDI-based dataset training.
- Automatic evaluation (Accuracy, Precision, Recall, F1, BRA, CTR).

## 🔧 Installation <a name = "install"></a>

### Clone repository

```bash
https://github.com/Athira1979/multi-module-music-gen.git
cd multi-module-music-gen
```

### Create virtual environment

```bash
python -m venv .venv
python  .venv\Scripts\activate # activate in windows
```

### Install requirements

```bash
pip install -r requirements.txt
```

## Usage <a name = "use"></a>

### Train the model

```bash
python main.py --mode train
```

### Evaluate the model

```bash
python main.py --mode eval
```

## License <a name = "license"></a>

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
