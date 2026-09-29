from __future__ import annotations

import json
from dataclasses import asdict
from pathlib import Path
from typing import Any

from .model import Interpretation, Sign, Source


class RegistryError(ValueError):
    """Raised when registry data violates the explicit schema or references."""


class Registry:
    def __init__(
        self,
        signs: list[Sign],
        sources: list[Source],
        interpretations: list[Interpretation],
    ) -> None:
        self.signs = {item.id: item for item in signs}
        self.sources = {item.id: item for item in sources}
        self.interpretations = interpretations

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Registry":
        signs = [_parse_sign(item) for item in _list_field(data, "signs")]
        sources = [_parse_source(item) for item in _list_field(data, "sources")]
        interpretations = [
            _parse_interpretation(item) for item in _list_field(data, "interpretations")
        ]

        _require_unique([item.id for item in signs], "sign")
        _require_unique([item.id for item in sources], "source")
        _require_unique([item.id for item in interpretations], "interpretation")

        sign_ids = {item.id for item in signs}
        source_ids = {item.id for item in sources}
        for item in interpretations:
            if item.sign_id not in sign_ids:
                raise RegistryError(
                    f"interpretation {item.id!r} references unknown sign {item.sign_id!r}"
                )
            if item.source_id not in source_ids:
                raise RegistryError(
                    f"interpretation {item.id!r} references unknown source {item.source_id!r}"
                )
            overlap = item.required_tags & item.excluded_tags
            if overlap:
                raise RegistryError(
                    f"interpretation {item.id!r} requires and excludes the same tags: "
                    + ", ".join(sorted(overlap))
                )

        return cls(signs, sources, interpretations)

    def query(self, sign_id: str, tags: set[str] | None = None) -> list[dict[str, Any]]:
        tags = tags or set()
        if sign_id not in self.signs:
            raise RegistryError(f"unknown sign {sign_id!r}")

        matches = [
            item
            for item in self.interpretations
            if item.sign_id == sign_id and item.matches(tags)
        ]
        matches.sort(key=lambda item: (-item.specificity, item.id))

        return [
            {
                "interpretation": _interpretation_dict(item),
                "source": asdict(self.sources[item.source_id]),
            }
            for item in matches
        ]


def load_registry(path: str | Path) -> Registry:
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise RegistryError("registry root must be a JSON object")
    return Registry.from_dict(payload)


def _interpretation_dict(item: Interpretation) -> dict[str, Any]:
    return {
        "id": item.id,
        "sign_id": item.sign_id,
        "meaning": item.meaning,
        "source_id": item.source_id,
        "required_tags": sorted(item.required_tags),
        "excluded_tags": sorted(item.excluded_tags),
    }


def _list_field(data: dict[str, Any], name: str) -> list[dict[str, Any]]:
    value = data.get(name)
    if not isinstance(value, list):
        raise RegistryError(f"{name!r} must be a list")
    if not all(isinstance(item, dict) for item in value):
        raise RegistryError(f"every item in {name!r} must be an object")
    return value


def _require_unique(values: list[str], kind: str) -> None:
    seen: set[str] = set()
    for value in values:
        if value in seen:
            raise RegistryError(f"duplicate {kind} id {value!r}")
        seen.add(value)


def _required_text(item: dict[str, Any], name: str) -> str:
    value = item.get(name)
    if not isinstance(value, str) or not value.strip():
        raise RegistryError(f"{name!r} must be a non-empty string")
    return value


def _optional_text(item: dict[str, Any], name: str) -> str | None:
    value = item.get(name)
    if value is None:
        return None
    if not isinstance(value, str) or not value.strip():
        raise RegistryError(f"{name!r} must be a non-empty string when present")
    return value


def _tag_set(item: dict[str, Any], name: str) -> frozenset[str]:
    value = item.get(name, [])
    if not isinstance(value, list) or not all(
        isinstance(tag, str) and tag.strip() for tag in value
    ):
        raise RegistryError(f"{name!r} must be a list of non-empty strings")
    if len(value) != len(set(value)):
        raise RegistryError(f"{name!r} must not contain duplicate tags")
    return frozenset(value)


def _parse_sign(item: dict[str, Any]) -> Sign:
    return Sign(
        id=_required_text(item, "id"),
        form=_required_text(item, "form"),
        modality=_required_text(item, "modality"),
    )


def _parse_source(item: dict[str, Any]) -> Source:
    return Source(
        id=_required_text(item, "id"),
        description=_required_text(item, "description"),
        locator=_optional_text(item, "locator"),
    )


def _parse_interpretation(item: dict[str, Any]) -> Interpretation:
    return Interpretation(
        id=_required_text(item, "id"),
        sign_id=_required_text(item, "sign_id"),
        meaning=_required_text(item, "meaning"),
        source_id=_required_text(item, "source_id"),
        required_tags=_tag_set(item, "required_tags"),
        excluded_tags=_tag_set(item, "excluded_tags"),
    )
