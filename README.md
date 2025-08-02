🎶 Enhancing AI Music Generation with Multi-Module Neural Networks
A Novel Approach to Chord, Rhythm, and Pitch Synthesis



📌 Overview

Automatic music generation is a rapidly evolving area in artificial intelligence, but current approaches often struggle to:

Capture temporal dependencies across sequences

Maintain harmonic coherence

Generate dynamic rhythmic patterns effectively

This project introduces a Multi-Module Neural Network (MNN) for automatic music composition, combining several specialized modules:

🎼 Temporal Graph Dilated Convolution (TGDC): Captures chord progression dependencies.

🥁 Rhythm Generator (MobileNet-TCN): Creates expressive rhythmic patterns.

🎹 Pitch Generator (Sparse Transformer): Generates coherent pitch sequences aligned with rhythm.

🎶 Fusion & Post-Processing: Merges rhythm and pitch while refining timing, velocity, and harmonic structure.

The result is a highly expressive, scalable music generation system that outputs MIDI files or audio-ready compositions.

🚀 Features
Multi-module neural architecture for chords, rhythm, and pitch

High accuracy and harmonic coherence

98.98% Accuracy and 98.13% F1 Score in experimental results

Support for MIDI-based dataset training

Automatic evaluation (Accuracy, Precision, Recall, F1, BRA, CTR)

🔧 Installation


# Clone repository
https://github.com/Athira1979/multi-module-music-gen.git


cd multi-module-music-gen

# Create virtual environment

python -m venv .venv

source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

🎹 Usage


Train the model:


python main.py --mode train


Evaluate the model:


python main.py --mode eval


📜 License
This project is licensed under the MIT License.

📖 Citation
If you use this work in your research, please cite:

bibtex
Copy
Edit
@article{musicgen2025,
  title={Enhancing AI Music Generation with Multi-Module Neural Networks: A Novel Approach to Chord, Rhythm, and Pitch Synthesis},
  author={Your Name},
  year={2025}
}

