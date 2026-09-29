# Semiotics

An inspectable foundation for recording signs, source-bound interpretations,
context, and revision history.

## What it does

The same form can support several meanings. Each interpretation names a sign,
a meaning, a source, and exact context tags that are required or excluded. The
engine returns every compatible current reading and orders more specific matches
first. Historical readings remain available through explicit revision links.

The engine does not infer meaning from text, assign probabilities, or convert
source descriptions into verified evidence.

## Install and test

    python -m pip install -e ".[test]"
    python -m unittest discover -s tests -v

There are no runtime dependencies or network-service requirements. The test
extra installs jsonschema so CI can verify the published schema behavior.

## Query

Illustrative example:

    semiotics examples/registry.json red-light --tag studio

Scholarly seed corpus:

    semiotics corpus/foundations.json sign --tag framework:peirce
    semiotics corpus/foundations.json sign --tag framework:saussure

Use --include-superseded when historical interpretations should be included.

## Registry

signs contain id, form, and modality.

sources contain id and description, plus optional locator, citation, and
published_year bibliographic metadata.

interpretations contain id, sign_id, meaning, source_id, optional required_tags
and excluded_tags, and optional supersedes_id for append-only revision history.
A revision target must exist, belong to the same sign, and may not participate
in a revision cycle.

Tags are exact strings. Compatible means only that registered context predicates
matched. Specificity is deterministic ordering, not confidence or truth.

See docs/CONTRACT.md for the behavioral contract and
schema/registry.schema.json for the machine-readable shape.

## Corpus

corpus/foundations.json is the first source-backed seed corpus. It currently
keeps Peircean, Saussurean, and Morris-derived readings framework-labeled rather
than pretending they are interchangeable. See docs/CORPUS.md for corpus policy.

The older examples/registry.json remains deliberately illustrative and should
not be mistaken for scholarly evidence.

## Scope

This is still a deterministic registry and query kernel. Rich contradiction
modeling, source criticism, learned interpretation, uncertainty calibration,
and evaluation corpora remain separate work. See docs/ROADMAP.md.

The repository is currently all-rights-reserved; see LICENSE.
