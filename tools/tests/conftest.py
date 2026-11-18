"""Shared helpers for building a throwaway TASC repository on disk."""

from __future__ import annotations

import shutil
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[2]


def adr_text(
    number: str = "001",
    title: str = "Use Widgets",
    date: str = "2026-01-02",
    status: str = "Approved",
) -> str:
    return f"""# TASC-ADR-{number}: {title}

**Date:** {date} | **Status:** {status}

**Description:** An ADR about widgets.
**Deciders:** TASC
**Keywords:** widgets

---

## Context

Some context.

## Decision

We will use widgets. They are great.

**Key Points:**

- One

---

## Consequences

None.
"""


def rec_text(
    doc_id: str = "GA4GH-REC-01",
    title: str = "Widget guide",
    date: str = "2025-03-04",
    status: str = "Approved",
    id_field: str = "Recommendation",
) -> str:
    return f"""# Widget guide recommendation

**Source**: TASC
**{id_field}**: {doc_id}
**Title**: {title}
**Description**: A recommendation about widgets.
**Authors**: Jane Doe
**Date:** {date}
**Status:** {status}
**Keywords**: widgets

## Abstract

This recommendation explains widgets. It has a second sentence.

## Recommendation

Use widgets.
"""


def registry_entry(slug: str = "widgets", **overrides) -> dict:
    """A registry README: H1 name plus header fields. A None value omits the line."""
    entry = {
        "slug": slug,
        "name": "Widget Registry",
        "description": "Lists the widget identifiers used by GA4GH products.",
        "defined_by": "GA4GH-REC-01",
        "data_file": "widgets.yaml",
        "external_location": None,
    }
    return {**entry, **overrides}


HEADER_FIELDS = {
    "description": "Description",
    "defined_by": "Defined by",
    "data_file": "Data file",
    "external_location": "External location",
}


def registry_readme(entry: dict) -> str:
    lines = [f"# {entry['name']}", ""]
    lines += [
        f"**{label}**: {entry[key]}  "
        for key, label in HEADER_FIELDS.items()
        if entry[key] is not None
    ]
    return "\n".join(lines) + "\n\n## Background\n\nText.\n"


def write_registry(root: Path, entries: list[dict]) -> None:
    """Replace the registries with one directory per entry (README, plus data file if named)."""
    for old in (root / "registries").glob("*/"):
        shutil.rmtree(old)
    for entry in entries:
        write(root, f"registries/{entry['slug']}/README.md", registry_readme(entry))
        if entry["data_file"] and "/" not in entry["data_file"]:
            write(root, f"registries/{entry['slug']}/{entry['data_file']}", "items: []\n")


def write(root: Path, rel: str, content: str) -> Path:
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


@pytest.fixture
def repo(tmp_path: Path) -> Path:
    """A minimal valid repository with one document of each type."""
    (tmp_path / "index").mkdir()
    write(tmp_path, "adr/TASC-ADR-001 Widgets.md", adr_text())
    write(tmp_path, "recommendations/Widget guide.md", rec_text())
    write(
        tmp_path,
        "governance/Charter.md",
        rec_text("TASC-GOV-01", "Charter", id_field="Document ID"),
    )
    write_registry(tmp_path, [registry_entry()])
    for schema in (REPO_ROOT / "index").glob("*.schema.json"):
        shutil.copy(schema, tmp_path / "index" / schema.name)
    return tmp_path
