## 5. Results (Early Baseline Summary)

This section summarizes early baseline checkpoints intended to validate the experimental workflow.

- Results are logged in: `experiments/results.md`
- Each run writes a local: `runs/<run_name>/metrics.json` (not committed)

### 5.1 What these results mean
At this stage, metrics are not used to claim strong predictive performance. Instead, they confirm that:
- the end-to-end run pipeline works,
- results can be reproduced consistently,
- the repo has a stable structure for future experiments and ablations.

### 5.2 Next experiment milestone
The next milestone is introducing a real trainable model baseline (e.g., a PyTorch implementation of an MLP or transformer encoder) while keeping the same logging and reporting conventions.