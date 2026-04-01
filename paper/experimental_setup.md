## 4. Experimental Setup (Baseline Exploration)

### 4.1 Data and access
Experiments in this repository are designed to be reproducible using publicly available benchmark tasks. This project does not redistribute restricted datasets. Where dataset access requires a host platform or portal, the repository provides only instructions, derived visualizations, and citation-compliant references.

### 4.2 Baselines
Two lightweight baselines are included to validate the workflow and establish reference points:
- **Baseline 0:** Mean/constant predictor (sanity check)
- **Baseline 1:** Simple MLP scaffold (workflow validation baseline)

These baselines are intentionally modest; their purpose is to ensure that logging, evaluation, and error analysis are reliable before introducing more complex models.

### 4.3 Reporting and reproducibility
Each experiment run writes a `metrics.json` file to a local `runs/` directory (ignored by git). A running summary of experiments is maintained in `experiments/results.md`, and recurring failure modes are tracked in `experiments/error_analysis.md`.