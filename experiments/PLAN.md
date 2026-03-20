# Experiment Plan (RNA)

## Baselines (Week 1)
- Mean/constant predictor (sanity check)
- Simple MLP on averaged token embeddings (light baseline)

## Main Model (Week 2+)
- Transformer encoder + regression head (sequence-to-structure)

## Ablations (pick 1–2)
- With vs without positional encoding
- Truncation/length bucket strategy
- Loss variant (MSE vs robust loss)

## Reporting
- Save metrics to `runs/<name>/metrics.json`
- Maintain `experiments/results.md` as a small running log
- Add `experiments/error_analysis.md` for failure modes