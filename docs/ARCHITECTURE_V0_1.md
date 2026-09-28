# Architecture v0.1

Status: `FOUNDATION CANDIDATE`

## Executable object model

`Sign` identifies a registered sign vehicle by stable ID, form, and modality. `Context` is currently an exact set of tags. `Source` identifies the provenance description behind an interpretation and carries an `evidence_class`. `Interpretation` links one sign to one proposed meaning with required/excluded context tags, claim state, optional support metadata, scope, and namespaced theory tags. `Reading` is a query result joining an interpretation to its source.

The engine performs deterministic compatibility filtering only. It does not infer contexts, estimate calibrated probabilities, adjudicate truth, or normalize different theories into one ontology.

## Claim state

States are `candidate`, `supported`, `unresolved`, and `rejected`. Rejected records are retained but excluded from live query results. A supplied `support` value must be within [0,1], but query ordering ignores it and uses only explicit context specificity plus stable ID.

## Evidence and theory

`Source.evidence_class` is intentionally open in v0.1 so records can distinguish observation, primary text, secondary source, user-supplied material, portfolio contract, inference, or illustrative material. A future canonical evidence layer should separate exact source custody from summaries/projections.

`theory_tags` are a set, not a mutually exclusive enum. Namespaces such as `peirce:index`, `peirce:symbol`, `saussure:linguistic-sign`, or `pragmatics:speech-act` identify analytical framing; they do not establish universal theory truth.

## Next layer: sign events

The current `Sign` is registry-level identity. A later version should add a separate occurrence record with event time or interval, producer/observer/interpreter roles, channel, exact evidence references, contextual state, and links to candidate interpretations. Stable type identity and event history should not be collapsed.
