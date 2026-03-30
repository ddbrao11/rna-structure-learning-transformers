# Error Analysis (Working Notes)

This file tracks recurring failure modes and hypotheses. The goal is to keep analysis honest and actionable.

## Observed / expected failure modes
- Long-range interactions that require global context
- Ambiguous patterns where multiple structural interpretations are plausible
- Generalization issues when sequence length distribution shifts

## Next checks
- Bucket by sequence length and compare baseline behavior
- Track cases where errors cluster around specific motif types (if available)