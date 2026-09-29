# Semiotics

An inspectable foundation for recording signs and their context dependent readings.
The repository started empty. This initial model is a proposal, not a claim that
the word “semiotics” uniquely specifies this product.

## What it does

The same form can support several meanings. Each interpretation names a sign,
its meaning, a source, and context tags that are required or excluded. The engine
returns every compatible reading and orders more specific matches first. It does
not infer meaning from text, assign probabilities, or convert source descriptions
into verified evidence. Example conventions are illustrative.

## Run

```sh
python -m pip install -e .
semiotics examples/registry.json red-light --tag studio
python -m unittest discover -s tests -v
```

The CLI emits JSON. For the included example, `--tag studio` yields “Recording
in progress”; `--tag road` yields “Stop at the signal”; no tag yields `[]`.

## Registry

`signs` contain `id`, `form`, and `modality`. `sources` contain `id`,
`description`, and optional `locator`. `interpretations` contain `id`,
`sign_id`, `meaning`, `source_id`, and optional `required_tags` and
`excluded_tags`. Tags are exact strings. A missing source reference or
duplicate interpretation ID fails explicitly. A compatible reading means only
that the registered context predicates matched. See [docs/CONTRACT.md](docs/CONTRACT.md)
for the exact behavioral contract and [schema/registry.schema.json](schema/registry.schema.json)
for the machine-readable registry shape.

## Scope and next decisions

This is a deterministic registry and query kernel. A research corpus would need
proper bibliographic citations, source criticism, dated claims, revision history,
and a policy for contradictory readings. A product using learned interpretation
would also need an evaluation set and uncertainty calibration. Those decisions
should be driven by the intended domain rather than silently baked into this model.

No runtime dependency or network service is required. See [docs/ROADMAP.md](docs/ROADMAP.md)
for deliberately non-binding future directions.

The repository is currently all-rights-reserved; see [LICENSE](LICENSE).
