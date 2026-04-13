## 2. Related Work (Clean Draft)

### RNA structure prediction
RNA structure prediction has traditionally been approached through physics-inspired and thermodynamics-based methods, especially for secondary structure. More recently, deep learning methods have expanded the toolbox by learning structure-relevant representations directly from sequence and related features. Reviews of this area highlight both progress and persistent challenges, including dataset limitations and the difficulty of capturing higher-order (3D) constraints from sequence alone.

### Deep learning for RNA structural modeling
Modern neural approaches for RNA structure prediction span sequence models, graph-based methods, and geometry-aware architectures. Transformer-based sequence models are a natural baseline because they can represent long-range dependencies through self-attention, which is relevant for base-pairing and tertiary contacts that connect distant sequence positions. However, sequence-only approaches often lack explicit geometric inductive bias, motivating structure-aware modeling when the target is truly 3D.

### Geometry-aware / equivariant modeling (motivation)
A recurring theme across structural biology and molecular modeling is that respecting symmetries of 3D space (e.g., rotation/translation equivariance) can improve sample efficiency and robustness. This motivates future work that introduces geometry-aware inductive bias for RNA structure modeling, especially when predicting 3D coordinates or spatial relationships.

### CryoET structural localization (qualitative case study)
Cryo-electron tomography (CryoET) produces 3D reconstructions of cellular structures but often under substantial noise and imaging artifacts. Targets of interest may be small relative to the full volume, and performance can degrade under domain shift across specimens and reconstruction pipelines. The CryoET case study included in this project is intentionally qualitative and is used to highlight cross-domain realism: structural localization in noisy 3D volumes shares many practical challenges with sequence-to-structure learning (limited labels, ambiguity, and robustness constraints).

### Positioning of this work
This project emphasizes reproducible baselines, conservative claims, and error-analysis-driven iteration rather than leaderboard-style optimization. The related work provides context for (1) why sequence-only transformers are a reasonable baseline and (2) why geometry-aware modeling is a likely next step for stronger 3D structural fidelity.