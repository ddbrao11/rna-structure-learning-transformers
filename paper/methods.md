## 3. Methodology (Baseline Framework)

This work is structured as a reproducible baseline exploration rather than a leaderboard-optimized submission. The goal is to understand what sequence-only models capture for RNA structure-related prediction, where they fail, and what directions appear promising for improvement.

### 3.1 Problem framing (sequence → structure)
Given an RNA sequence, the objective is to learn a mapping from nucleotide tokens to a structure-related target representation. The exact target may vary by benchmark (e.g., coordinate-like representations, structural attributes, or derived supervision). In this project, the emphasis is on building a clear workflow that supports iteration, logging, and error analysis.

### 3.2 Input representation
RNA sequences are represented as token sequences over the alphabet {A, U, C, G}. Tokens are encoded numerically and combined with positional information to preserve ordering. This is a deliberately simple representation intended to test how far sequence-only modeling can go before explicit geometric constraints are required.

### 3.3 Model baseline (Transformer encoder)
As a baseline, a transformer encoder is used to model long-range dependencies within the RNA sequence. Self-attention provides a natural mechanism to relate distant positions, which is relevant for structural interactions where nucleotides far apart in sequence may become proximal in folded conformations.

In the baseline workflow, the transformer produces contextual token embeddings, which are pooled or aggregated and passed to a prediction head. The head outputs a structure-related prediction. This design is intentionally minimal so that later improvements (geometry-aware bias, pairwise features, equivariance) can be evaluated against a transparent starting point.

### 3.4 Baselines and sanity checks
Before investing in heavier models, the workflow includes basic sanity checks to validate the pipeline:
- Mean/constant predictor baseline to confirm logging and metrics plumbing
- A simple MLP baseline (planned) to separate “model capacity” from “representation quality”

These baselines are not intended to be strong; they exist to prevent misleading progress and to make failures interpretable.

### 3.5 Evaluation and error analysis mindset
Evaluation is designed to be transparent and iterative:
- Log metrics for each run in a consistent format (local `runs/` directory)
- Maintain a running results log in `experiments/results.md`
- Track recurring failure modes in `experiments/error_analysis.md` (e.g., long sequences, ambiguous motifs, systematic errors)

The key output of this work is not only metrics, but a defensible analysis of limitations and next steps.

### 3.6 Cross-domain case study (CryoET, qualitative)
To strengthen cross-disciplinary structural reasoning, a qualitative CryoET case study is included (flagellar motor localization). This component is intentionally qualitative: it highlights how structural localization in noisy 3D volumes faces challenges analogous to sequence-only RNA modeling (limited labels, noise/artifacts, domain shift). It serves as motivation for geometry-aware and robustness-focused modeling directions.