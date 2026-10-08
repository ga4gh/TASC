"""Document types, status enums and the index entry model.

The status enums here are the single source of truth in code. They are
mirrored in ``index/*-index.schema.json`` and in the ADR/recommendation
templates; ``tools/tests/test_consistency.py`` fails if the three drift apart.
"""

from __future__ import annotations

import re
from dataclasses import asdict, dataclass
from enum import Enum


class DocType(str, Enum):
    ADR = "adr"
    RECOMMENDATION = "recommendation"
    GOVERNANCE = "governance"


class AdrStatus(str, Enum):
    DRAFT = "Draft"
    PROPOSED = "Proposed"
    ACCEPTED = "Accepted"
    DEPRECATED = "Deprecated"
    SUPERSEDED = "Superseded"


class RecommendationStatus(str, Enum):
    DRAFT = "Draft"
    APPROVED = "Approved"
    SUPERSEDED = "Superseded"


# Governance documents share the recommendation metadata header
# (see governance/TASC_Document_Standards.md), so they share its statuses.
STATUS_ENUMS: dict[DocType, type[Enum]] = {
    DocType.ADR: AdrStatus,
    DocType.RECOMMENDATION: RecommendationStatus,
    DocType.GOVERNANCE: RecommendationStatus,
}

# Identifier formats from the Numbering Convention in TASC_Document_Standards.md.
ID_PATTERNS: dict[DocType, re.Pattern[str]] = {
    DocType.ADR: re.compile(r"^TASC-ADR-\d{3,}$"),
    DocType.RECOMMENDATION: re.compile(r"^GA4GH-REC-\d{2,}$"),
    DocType.GOVERNANCE: re.compile(r"^TASC-GOV-\d{2,}$"),
}


@dataclass(frozen=True)
class Document:
    """One entry in the generated index."""

    id: str
    type: DocType
    name: str
    date: str  # ISO 8601, YYYY-MM-DD
    status: str
    description: str
    path: str  # repo-relative, POSIX separators
    url: str  # permanent link to the file on GitHub
    short_name: str | None = None  # ADRs only; see short_names.json

    def to_dict(self) -> dict[str, str]:
        data = asdict(self)
        data["type"] = self.type.value
        if self.short_name is None:
            del data["short_name"]
        return data
