# Registry contract

Semiotics v0.2 is an explicit, source-bound registry and deterministic query
system. It is not an inference system.

## Entities

A sign records an identifier, a human-readable form, and a modality.

A source records where an interpretation came from. description is required.
locator, citation, and published_year are optional bibliographic metadata.
Registering a source does not establish that the source is true, authoritative,
independent, or correctly interpreted.

An interpretation links one sign to one meaning and one source. Its context is
expressed only through exact string predicates:

- every required_tags value must be present in the query context;
- no excluded_tags value may be present.

An interpretation may also name supersedes_id. The referenced interpretation
must exist and belong to the same sign. Revision links may not form cycles.

## Query semantics

A query names one registered sign and supplies zero or more context tags. Every
compatible current interpretation is returned. An interpretation is historical
rather than current when another registered interpretation supersedes it.

Results are ordered by descending specificity, defined as the number of
required plus excluded predicates, then by interpretation ID for deterministic
tie-breaking. Specificity is an ordering rule, not confidence, probability,
evidentiary weight, or truth.

Library callers may set include_superseded to true to include revision history.
The CLI exposes the same behavior with --include-superseded.

## Failure semantics

Malformed JSON registries fail closed. Unknown fields, duplicate IDs, duplicate
tags, whitespace-only strings, dangling sign/source/revision references,
cross-sign revision links, revision cycles, and predicates that both require and
exclude the same tag are rejected. Runtime acceptance is intended to match the
published JSON Schema plus referential and cross-field checks that JSON Schema
alone does not express.

Unknown query sign IDs are errors. Query context tags must be non-empty strings.
A known sign with no compatible current interpretation returns an empty list.

## Provenance and corpus policy

Source records are provenance. They are not truth scores. A corpus may contain
competing framework-specific readings when each is explicitly source-bound and
its context is represented rather than silently reconciled.

Corrections should normally append a new interpretation and link it through
supersedes_id instead of destructively rewriting a historical record.

## Non-goals

v0.2 does not infer signs from text or images, normalize synonyms, learn
meanings, assign confidence, adjudicate contradictory sources, or claim that a
registered meaning is correct. Those require separate contracts and evidence.
