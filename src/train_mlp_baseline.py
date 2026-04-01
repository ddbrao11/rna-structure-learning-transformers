import argparse
import json
import os
from dataclasses import dataclass
from typing import Dict, Any

import numpy as np


@dataclass
class Config:
    seed: int = 42
    seq_len: int = 128
    n_samples: int = 512
    hidden_dim: int = 128
    num_layers: int = 2
    epochs: int = 5
    lr: float = 1e-3
    out_dir: str = "runs/mlp_baseline"


def set_seed(seed: int):
    np.random.seed(seed)


def fake_load_data(n: int, seq_len: int):
    # Placeholder tokens (0..3) and placeholder targets (3 floats)
    X = np.random.randint(0, 4, size=(n, seq_len)).astype(np.float32)
    y = np.random.randn(n, 3).astype(np.float32)
    return X, y


def one_hot(x: np.ndarray, num_classes: int = 4) -> np.ndarray:
    # x: (n, seq_len) ints stored as float; cast to int
    xi = x.astype(np.int32)
    out = np.eye(num_classes, dtype=np.float32)[xi]  # (n, seq_len, 4)
    return out.reshape(out.shape[0], -1)  # flatten


def init_mlp(in_dim: int, hidden_dim: int, num_layers: int, out_dim: int = 3):
    weights = []
    biases = []

    dims = [in_dim] + [hidden_dim] * num_layers + [out_dim]
    for d_in, d_out in zip(dims[:-1], dims[1:]):
        w = np.random.randn(d_in, d_out).astype(np.float32) * (1.0 / np.sqrt(d_in))
        b = np.zeros((d_out,), dtype=np.float32)
        weights.append(w)
        biases.append(b)

    return weights, biases


def relu(x: np.ndarray) -> np.ndarray:
    return np.maximum(0.0, x)


def forward(x: np.ndarray, weights, biases) -> np.ndarray:
    h = x
    for i in range(len(weights)):
        h = h @ weights[i] + biases[i]
        if i < len(weights) - 1:
            h = relu(h)
    return h


def mse(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    return float(np.mean((y_true - y_pred) ** 2))


def train(cfg: Config) -> Dict[str, Any]:
    set_seed(cfg.seed)
    os.makedirs(cfg.out_dir, exist_ok=True)

    X, y = fake_load_data(cfg.n_samples, cfg.seq_len)
    Xf = one_hot(X, 4)

    weights, biases = init_mlp(
        in_dim=Xf.shape[1],
        hidden_dim=cfg.hidden_dim,
        num_layers=cfg.num_layers,
        out_dim=y.shape[1],
    )

    # Very simple SGD (numpy) – placeholder training loop
    for _ in range(cfg.epochs):
        y_pred = forward(Xf, weights, biases)
        # gradients (linear approx; simplistic, for scaffold only)
        # We keep this as a runnable placeholder, not an optimized trainer.
        loss = mse(y, y_pred)

        # Save last loss only (keep it simple)
        last_loss = loss

    metrics = {
        "mse": last_loss,
        "note": "MLP baseline scaffold (placeholder trainer for reproducible workflow)",
        "n_samples": cfg.n_samples,
        "seq_len": cfg.seq_len,
        "epochs": cfg.epochs,
    }

    with open(os.path.join(cfg.out_dir, "metrics.json"), "w", encoding="utf-8") as f:
        json.dump(metrics, f, indent=2)

    return metrics


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--out_dir", default="runs/mlp_baseline")
    p.add_argument("--epochs", type=int, default=5)
    args = p.parse_args()

    cfg = Config(out_dir=args.out_dir, epochs=args.epochs)
    m = train(cfg)
    print(m)