## 2. Related Work (working notes)

### RNA structure prediction
- Classical and physics-inspired approaches model folding via thermodynamics/energy minimization.
- Deep learning approaches learn structure-relevant representations from sequence and/or pairwise features, with growing interest in geometry-aware modeling.

### Sequence modeling for structure
- Transformer architectures provide a natural baseline for long-range dependency modeling in biological sequences.
- A recurring limitation is the lack of explicit geometric inductive bias, motivating equivariant and structure-aware architectures.

### CryoET structure detection (qualitative case study)
- Cryo-electron tomography enables 3D reconstruction of cellular structures, but the data is noisy and targets can be small relative to the volume.
- Automated detection/localization is often framed as 3D segmentation or object localization, where preprocessing and domain shift can strongly affect reliability.

### Positioning of this work
- This project focuses on reproducible baselines + error analysis rather than maximal benchmark performance.
- The CryoET component is intentionally qualitative, used to highlight cross-domain structural challenges and dataset realism.