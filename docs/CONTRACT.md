# Registry contract

Semiotics v0.1 is an explicit registry, not an inference system.

## Entities

A **sign** records an identifier, a human-readable form, and a modality.

A **source** records where an interpretation came from. A source description is
provenance metadata; registering it does not establish that the source is true,
authoritative, independent, or correctly interpreted.

An **interpretation** links one sign to one meaning and one source. Its context is
expressed only through exact string predicates:

- every `required_tag` must be present in the query context;
- no `excluded_tag` may be present.

## Query semantics

A query names one registered sign and supplies zero or more context tags. Every
compatible interpretation is returned. Results are ordered by descending
specificity, defined as the number of required plus excluded predicates, then by
interpretation ID for deterministic tie-breaking.

Specificity is an ordering rule, not confidence, probability, evidentiary weight,
or truth.

## Failure semantics

Malformed registries fail closed. Duplicate IDs, dangling sign/source references,
and predicates that both require and exclude the same tag are rejected.

Unknown query sign IDs are errors. A known sign with no compatible interpretation
returns an empty list.

## Non-goals

v0.1 does not infer signs from text or images, normalize synonyms, learn meanings,
assign confidence, adjudicate contradictory sources, or claim that a registered
meaning is correct. Those require separate contracts and evidence.
