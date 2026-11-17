"""Parse the bold-key metadata header used by TASC markdown documents.

Two header styles exist (see governance/TASC_Document_Standards.md)::

    **Date:** 2026-03-23 | **Status:** Proposed     (ADRs, several keys per line)
    **Status**: Approved                              (recommendations, one key per line)
"""

from __future__ import annotations

import re
from dataclasses import dataclass

# "**Key:** value" or "**Key**: value"; the value ends at " | **" or end of line.
_FIELD = re.compile(
    r"\*\*(?P<key>[^*:]+?)(?::\*\*|\*\*:)[ \t]*(?P<value>.*?)(?=[ \t]*\|[ \t]*\*\*|[ \t]*$)"
)
_H1 = re.compile(r"^# (?P<title>.+?)\s*$", re.MULTILINE)
_ADR_TITLE = re.compile(r"^(?P<id>TASC-ADR-\d+):\s*(?P<name>.+)$")


class ParseError(ValueError):
    """A document does not follow the expected TASC structure."""


def parse_metadata(text: str) -> dict[str, str]:
    """Return header fields keyed by lower-cased name.

    The header ends at the first ``## `` heading or ``---`` rule. When a key
    repeats, the first occurrence wins.
    """
    fields: dict[str, str] = {}
    for line in text.splitlines():
        if line.startswith("## ") or line.strip() == "---":
            break
        for match in _FIELD.finditer(line):
            fields.setdefault(match["key"].strip().lower(), match["value"].strip())
    return fields


def parse_h1(text: str) -> str:
    match = _H1.search(text)
    if not match:
        raise ParseError("no level-1 heading found")
    return match["title"]


@dataclass(frozen=True)
class AdrTitle:
    id: str
    name: str


def parse_adr_title(text: str) -> AdrTitle:
    """Split ``# TASC-ADR-001: Some title`` into identifier and name."""
    match = _ADR_TITLE.match(parse_h1(text))
    if not match:
        raise ParseError("H1 must look like '# TASC-ADR-NNN: Title'")
    return AdrTitle(id=match["id"], name=match["name"].strip())


def extract_section(text: str, heading: str) -> str:
    """Return the body of a ``## heading`` section, or '' if absent."""
    pattern = re.compile(
        rf"^## {re.escape(heading)}\s*$(?P<body>.*?)(?=^## |^---\s*$|\Z)",
        re.MULTILINE | re.DOTALL | re.IGNORECASE,
    )
    match = pattern.search(text)
    return match["body"].strip() if match else ""
