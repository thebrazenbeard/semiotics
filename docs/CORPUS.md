# Scholarly seed corpus

corpus/foundations.json is the first source-backed corpus shipped with the
repository. It is intentionally small and theory-labeled rather than presented
as a universal ontology of semiotics.

The current seed records three frameworks:

- Peirce: triadic sign structure plus icon, index, and symbol classifications;
- Saussure: signifier/signified, arbitrariness, and differential value;
- Morris: syntactics, semantics, and pragmatics.

Each interpretation is a concise paraphrase tied to an explicit source record.
The source record is provenance, not a truth score. Framework tags are required
where terminology is theory-specific so that the query engine does not silently
collapse distinct traditions into one meaning.

The corpus should grow by adding stable bibliographic metadata and source-bound
paraphrases. New or corrected readings should be appended and linked with
supersedes_id rather than destructively rewriting historical records.
