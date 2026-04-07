import json
import os
from glob import glob
from datetime import datetime

RUNS_DIR = "runs"
OUT_PATH = "experiments/results_table.md"

def load_metrics():
    paths = glob(os.path.join(RUNS_DIR, "**", "metrics.json"), recursive=True)
    rows = []
    for p in paths:
        run_name = os.path.basename(os.path.dirname(p))
        try:
            with open(p, "r", encoding="utf-8") as f:
                m = json.load(f)
            rows.append({
                "run": run_name,
                "mse": m.get("mse", ""),
                "note": m.get("note", ""),
            })
        except Exception as e:
            rows.append({"run": run_name, "mse": "", "note": f"failed to read: {e}"})
    return rows

def main():
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    rows = load_metrics()

    lines = []
    lines.append("# Results Table (Auto-generated)")
    lines.append("")
    lines.append(f"_Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}_")
    lines.append("")
    lines.append("> Note: `runs/` is not committed. This table is generated from local run outputs.")
    lines.append("")

    lines.append("| Run | MSE | Notes |")
    lines.append("|---|---:|---|")

    if not rows:
        lines.append("| (no local runs found) |  | Run `python src/train_baseline.py` and re-run this script. |")
    else:
        for r in sorted(rows, key=lambda x: x["run"]):
            mse = r["mse"]
            try:
                mse = f"{float(mse):.4f}"
            except Exception:
                mse = str(mse)
            note = str(r["note"]).replace("\n", " ").strip()
            lines.append(f"| {r['run']} | {mse} | {note} |")

    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

    print(f"Wrote {OUT_PATH}")

if __name__ == "__main__":
    main()