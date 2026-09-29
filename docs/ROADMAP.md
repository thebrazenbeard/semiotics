# Roadmap

The repository should grow by making evidence and semantics more explicit, not
by quietly turning deterministic matching into an AI guesser.

## v0.1 - deterministic kernel

Complete: explicit registry validation, exact context predicates, deterministic
query ordering, JSON CLI, examples, tests, CI, and a machine-readable schema.

## v0.2 - corpus discipline

In progress. Implemented:

- bibliographic source metadata through citation, locator, and published_year;
- append-only interpretation revision links through supersedes_id;
- current-versus-historical query behavior;
- CLI access to superseded history;
- executable JSON Schema validation in the test suite;
- a source-backed foundational corpus separated by theoretical framework.

Still open:

- explicit relations among signs, contexts, and interpretations;
- first-class competing-reading and contradiction representation;
- richer source criticism beyond bibliographic provenance;
- import/export tooling beyond loading validated JSON.

## Candidate v0.3 - evaluation layer

Before learned or probabilistic interpretation is admitted, establish a labeled
evaluation corpus, metrics, uncertainty representation, provenance for model
outputs, and a hard distinction between generated hypotheses and registered
source-backed readings.

Roadmap candidates are not authorization to introduce probabilistic inference
or external learned services into the deterministic kernel.
