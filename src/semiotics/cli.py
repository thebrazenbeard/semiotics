"""Run a contextual reading against a JSON registry."""

import argparse
import json
from pathlib import Path

from .engine import interpret
from .model import Context, Interpretation, Sign, Source


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("registry", type=Path)
    parser.add_argument("sign_id")
    parser.add_argument("--tag", action="append", default=[], help="Context tag; repeat as needed")
    args = parser.parse_args(argv)
    data = json.loads(args.registry.read_text(encoding="utf-8"))
    signs = {sign.id: sign for sign in (Sign(**row) for row in data["signs"])}
    if args.sign_id not in signs:
        parser.error(f"unknown sign id: {args.sign_id}")
    sources = [Source(**row) for row in data["sources"]]
    items = [
        Interpretation(
            **{**row,
               "required_tags": frozenset(row.get("required_tags", [])),
               "excluded_tags": frozenset(row.get("excluded_tags", [])),
               "theory_tags": frozenset(row.get("theory_tags", []))}
        )
        for row in data["interpretations"]
    ]
    readings = interpret(signs[args.sign_id], Context(frozenset(args.tag)), items, sources)
    print(json.dumps([
        {"id": r.interpretation.id, "meaning": r.interpretation.meaning,
         "source": r.source.id, "locator": r.source.locator,
         "matched_tags": sorted(r.matched_tags),
         "status": r.interpretation.status, "support": r.interpretation.support,
         "theory_tags": sorted(r.interpretation.theory_tags),
         "evidence_class": r.source.evidence_class}
        for r in readings
    ], indent=2))


if __name__ == "__main__":
    main()
