import argparse
import json
import os
from dataclasses import dataclass
from typing import Dict, Any

import numpy as np


@dataclass
class TrainConfig:
    seed: int = 42
    out_dir: str = "runs/baseline"


def set_seed(seed: int):
    np.random.seed(seed)


def fake_load_data(n: int = 256, seq_len: int = 128):
    """
    Placeholder loader.
    Replace later with a real dataset loader.
    """
    X = np.random.randint(0, 4, size=(n, seq_len))  # RNA tokens 0..3
    y = np.random.randn(n, 3)  # placeholder "structure target"
    return X, y


def train(cfg: TrainConfig) -> Dict[str, Any]:
    set_seed(cfg.seed)
    os.makedirs(cfg.out_dir, exist_ok=True)

    _, y = fake_load_data()
    # Baseline: predict mean target vector
    y_hat = np.mean(y, axis=0, keepdims=True).repeat(y.shape[0], axis=0)
    mse = float(np.mean((y - y_hat) ** 2))

    metrics = {
        "mse": mse,
        "note": "mean-predictor baseline (placeholder to validate pipeline)",
    }

    with open(os.path.join(cfg.out_dir, "metrics.json"), "w", encoding="utf-8") as f:
        json.dump(metrics, f, indent=2)

    return metrics


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--out_dir", default="runs/baseline")
    p.add_argument("--seed", type=int, default=42)
    args = p.parse_args()

    cfg = TrainConfig(seed=args.seed, out_dir=args.out_dir)
    m = train(cfg)
    print(m)