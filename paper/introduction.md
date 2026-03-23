## 1. Introduction
RNA structure often determines biological function, making structure prediction important for downstream biomedical and scientific applications. Unlike many standard prediction problems, RNA folding requires modeling long-range dependencies: nucleotides far apart in the sequence can form base-pairs or tertiary contacts and end up adjacent in three-dimensional space. Traditional physics-based approaches can be computationally expensive and difficult to scale, motivating interest in data-driven methods that learn structural representations from sequence.

Transformer architectures are effective at capturing long-range context in sequence data. This raises a practical research question: to what extent can sequence-only transformers learn structure-relevant dependencies, and what limitations emerge when geometric constraints are not explicitly encoded? In this work, I explore a transformer-based baseline and a simple experimental workflow focused on reproducibility and interpretability rather than maximal performance.

The primary case study focuses on RNA sequence-to-structure learning using publicly available benchmark tasks. I report a clear methodology, a minimal set of baselines, and an error-analysis mindset that highlights recurring failure modes. To strengthen the cross-disciplinary framing, I include a qualitative CryoET case study (flagellar motor localization) that demonstrates similar challenges in structural reasoning under noise and limited labels. Together, these case studies motivate future directions such as geometry-aware neural architectures and hybrid modeling approaches.

### Contributions (high level)
- A reproducible baseline framework for RNA sequence-to-structure exploration with transparent reporting.
- An error-analysis-oriented evaluation approach that surfaces recurring failure modes and limitations.
- A qualitative CryoET case study illustrating cross-domain challenges in structural localization and dataset realism.
- Practical future directions emphasizing geometric inductive bias and hybrid approaches.