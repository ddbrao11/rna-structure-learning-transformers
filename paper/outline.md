# Preprint #1 Outline (AI + Bio)

## Working Title
Cross-Domain Structural Learning: RNA Sequence-to-Structure Modeling with a CryoET Case Study

## 1. Introduction
- Why structural learning matters in biology (RNA structure, scientific discovery)
- Why long-range dependencies make sequence-only modeling hard
- What this work explores (research framing, reproducibility)

## 2. Related Work (bullets for now)
- RNA structure prediction: sequence models, structure-aware models
- Geometry-aware learning (equivariant models)
- CryoET detection/localization (high-level)

## 3. Methodology (shared spine)
- Inputs and representations
- Modeling approach (transformer baseline + structured evaluation)
- Evaluation philosophy: benchmarks + error analysis
- See paper/methods.md for the baseline framework and evaluation philosophy

## 4. Case Study A (Primary): RNA
- Task framing + dataset access language (public benchmark tasks)
- Baselines + model variants
- Metrics + error analysis plan
- Experimental setup notes: paper/experimental_setup.md
- Results summary notes: paper/results_summary.md

## 5. Case Study B (Qualitative): CryoET / Flagellar motors
- Dataset provenance (CryoET Data Portal) + citation note
- Slice/MIP visualization + why localization is hard
- Conceptual detection pipeline + limitations

## 6. Limitations and Ethics
- Geometry bias, dataset limits, generalization risks
- Responsible reporting (no overclaims)

## 7. Future Work
- Geometry-aware models
- Hybrid constraints
- Agentic analysis / error-driven iteration