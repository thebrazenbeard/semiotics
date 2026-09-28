> **License:** Source-visible, not open source. Original material is proprietary. Commercial use, redistribution, hosted-service use, and commercial derivative products require written permission. See [LICENSE](LICENSE) and [COMMERCIAL_LICENSE.md](COMMERCIAL_LICENSE.md).

# Semiotics

Semiotics is a research and reference-implementation repository for representing **sign processes**: sign vehicles, contextual conditions, competing interpretations, sources, and the evidence state attached to those interpretations.

The executable v0.1 kernel is deliberately small. It records signs and sourced interpretations, filters them by explicit context predicates, preserves multiple compatible readings, and refuses to treat a score or source label as truth. It does **not** infer meaning from raw input, adjudicate a universal ontology, or replace the portfolio's existing semantic systems.

## Portfolio role

- **Semantic Atlas** remains the provenance-aware semantic ledger and adjudication architecture.
- **SPM** remains the cognition-substrate research program for meaning in context.
- **UNVTRSLR** remains the semantic-grounding and mediation research program.
- **Discovery** remains the mechanism for deciding whether portfolio abstractions have earned reuse.
- **Semiotics** focuses on how something functions as a sign for an interpreter in a context.

See [docs/PORTFOLIO_BOUNDARIES.md](docs/PORTFOLIO_BOUNDARIES.md) for immutable source bindings and separation rules.

## Run

    python -m pip install -e .
    semiotics examples/registry.json red-light --tag studio
    python -m unittest discover -s tests -v

The CLI emits every compatible live reading, ordered by explicit contextual specificity and then stable interpretation ID. The optional `support` value is returned as metadata and is never used as hidden truth or ranking authority.

## Core invariants

- A sign form is not its meaning.
- Context constrains interpretation without granting truth or action authority.
- Multiple compatible interpretations remain multiple records until evidence or explicit adjudication resolves them.
- Source attribution and evidence class are provenance, not proof.
- Rejected interpretations remain representable as history but are excluded from live readings.
- Theory labels such as `peirce:index` are namespaced analytical tags, not universal ontology claims.
- An empty registry result is not evidence that a sign has no meaning.

## Repository map

- `src/semiotics/` — deterministic reference kernel and CLI.
- `tests/` — behavioral qualification for ambiguity, context, provenance references, and claim state.
- `schemas/` — machine-readable registry contract.
- `examples/` — explicitly illustrative registries, not verified scholarly datasets.
- `docs/` — architecture, claim controls, falsification plan, portfolio boundaries, and roadmap.
- `research/` — source bindings, references, and claims/evidence ledger.

## Status

`FOUNDATION_V0_1 / EXECUTABLE_REGISTRY_KERNEL / RESEARCH_ARCHITECTURE_ACTIVE / NO_LEARNED_SEMIOTIC_INFERENCE_CLAIM`
