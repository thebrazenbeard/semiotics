"""Data model. Assertions are attached to sources; scores are ranking aids, not truth."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Source:
    id: str
    description: str
    locator: str = ""
    evidence_class: str = "source_attributed"

    def __post_init__(self):
        if not self.id or not self.description:
            raise ValueError("source id and description are required")


@dataclass(frozen=True)
class Sign:
    id: str
    form: str
    modality: str

    def __post_init__(self):
        if not all((self.id, self.form, self.modality)):
            raise ValueError("sign id, form, and modality are required")


@dataclass(frozen=True)
class Context:
    tags: frozenset[str] = frozenset()


@dataclass(frozen=True)
class Interpretation:
    id: str
    sign_id: str
    meaning: str
    source_id: str
    required_tags: frozenset[str] = frozenset()
    excluded_tags: frozenset[str] = frozenset()
    status: str = "candidate"
    theory_tags: frozenset[str] = frozenset()
    support: float | None = None
    scope: str = ""

    def __post_init__(self):
        if not all((self.id, self.sign_id, self.meaning, self.source_id)):
            raise ValueError("interpretation id, sign id, meaning, and source id are required")
        if self.required_tags & self.excluded_tags:
            raise ValueError("the same tag cannot be required and excluded")
        if self.status not in {"candidate", "supported", "unresolved", "rejected"}:
            raise ValueError(f"unsupported interpretation status: {self.status}")
        if self.support is not None and not 0.0 <= self.support <= 1.0:
            raise ValueError("support must be between 0 and 1")


@dataclass(frozen=True)
class Reading:
    interpretation: Interpretation
    source: Source
    matched_tags: frozenset[str]
