Enhancing AI Music Generation with Multi-Module Neural Networks : A Novel Approach to Chord, Rhythm, and Pitch Synthesis

Overview:

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

Features:

Multi-module neural architecture for chords, rhythm, and pitch
High accuracy and harmonic coherence
Support for MIDI-based dataset training
Automatic evaluation (Accuracy, Precision, Recall, F1)

Project Structure:

MUSIC_GENERATION/
│
├── dataset/midi           # MIDI dataset
├── checkpoints/           # Model weights
├── music_dataset.py             # Dataset loader
├── model_components.py    # Model modules (TGDC, TCN, Transformer)
├── train.py               # Training script
├── evaluate.py            # Evaluation script
├── config.py              # Configurations
├── main.py                # Entry point
├── results.csv            # Evaluation metrics
└── README.md              # Project documentation

 Installation

# Clone repository
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
Usage
Train the model:
bash
Copy
Edit
python MUSIC_GENERATION/main.py
# Enter mode: train
Evaluate the model:
bash
Copy
Edit
python MUSIC_GENERATION/main.py
# Enter mode: eval
