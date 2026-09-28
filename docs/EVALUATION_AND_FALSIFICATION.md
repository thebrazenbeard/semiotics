# Evaluation and Falsification

## Current executable contract

The v0.1 kernel is tested for contextual selection, competing readings, exclusion predicates, unknown source references, duplicate IDs, rejected claim state, bounded support values, and the rule that support metadata does not secretly determine ranking.

## Adversarial cases for the next corpus

- same vehicle, different contexts;
- same context, competing conventions;
- ambiguous language with multiple live readings;
- mixed iconic/indexical/conventional features;
- producer/receiver divergence;
- historical semantic drift;
- false-friend similarity;
- non-equivalence;
- post-hoc semantic naming;
- missing context where unresolved/empty is correct.

Any future learned interpreter should be compared with simpler baselines such as lookup, retrieval, rule systems, ordinary classifiers, and language-model prompting with equivalent context access.

Falsifiers include ambiguity collapse without discriminating evidence, confidence-driven ranking hidden behind neutral language, producer intent inferred from receiver success alone, provenance lost after transformation, missing registry entries treated as negative semantic evidence, or needless duplication of Semantic Atlas/SPM/UNVTRSLR.
