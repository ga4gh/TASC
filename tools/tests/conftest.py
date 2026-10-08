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
    status: str = "Accepted",
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
    for schema in (REPO_ROOT / "index").glob("*.schema.json"):
        shutil.copy(schema, tmp_path / "index" / schema.name)
    return tmp_path
