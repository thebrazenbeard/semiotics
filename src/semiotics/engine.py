"""Deterministic filtering of candidate meanings; no claim of semantic certainty."""

from collections.abc import Iterable

from .model import Context, Interpretation, Reading, Sign, Source


def interpret(
    sign: Sign,
    context: Context,
    interpretations: Iterable[Interpretation],
    sources: Iterable[Source],
) -> list[Reading]:
    """Return all compatible, sourced readings, most specific first.

    An empty result means no registered reading fits; it is not evidence that
    the sign has no meaning. Ties are ordered by stable interpretation ID.
    """
    source_map = {source.id: source for source in sources}
    readings = []
    seen = set()
    for item in interpretations:
        if item.id in seen:
            raise ValueError(f"duplicate interpretation id: {item.id}")
        seen.add(item.id)
        if item.sign_id != sign.id:
            continue
        if item.status == "rejected":
            continue
        if item.source_id not in source_map:
            raise ValueError(f"unknown source: {item.source_id}")
        if item.required_tags <= context.tags and not item.excluded_tags & context.tags:
            readings.append(Reading(item, source_map[item.source_id], item.required_tags))
    return sorted(readings, key=lambda reading: (-len(reading.matched_tags), reading.interpretation.id))
