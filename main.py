import os
import argparse
from train import train
from evaluate import run_eval
from config import MODEL_PATH, MIDI_PATH

def main():
    parser = argparse.ArgumentParser(description="Music Generation with Multi-Module Neural Networks")
    parser.add_argument("--mode", type=str, choices=["train", "eval"], required=True,
                        help="Mode to run: 'train' for training or 'eval' for evaluation")
    parser.add_argument("--dataset", type=str, default=MIDI_PATH,
                        help="Path to MIDI dataset (default: from config)")
    parser.add_argument("--model", type=str, default=MODEL_PATH,
                        help="Path to save/load the trained model (default: from config)")
    parser.add_argument("--csv", type=str, default="results.csv",
                        help="Path to save evaluation results (only for eval mode)")

    args = parser.parse_args()

    print("[DEBUG] Script started")
    print(f"[DEBUG] Selected mode: {args.mode}")
    print(f"[DEBUG] Scanning dataset directory: {args.dataset}")

    if not os.path.exists(args.dataset):
        print(f"[ERROR] Dataset path not found: {args.dataset}")
        return

    try:
        if args.mode == "train":
            print("[INFO] Starting training...")
            train(args.dataset)
            print("[INFO] Training completed successfully.")
        elif args.mode == "eval":
            print("[INFO] Starting evaluation...")
            run_eval(args.model, args.dataset, csv_path=args.csv)
            print("[INFO] Evaluation completed successfully.")
    except Exception as e:
        print(f"[ERROR] Something went wrong: {e}")

if __name__ == "__main__":
    main()
