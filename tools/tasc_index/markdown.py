"""Markdown helpers shared by the generators."""

from __future__ import annotations


def cell(text: str) -> str:
    """Escape text for use inside a table cell."""
    return text.replace("|", "\\|").replace("\n", " ")


def table(header: list[str], rows: list[list[str]]) -> str:
    """A table in markdownlint's compact style: a space inside every pipe, delimiter included."""
    delimiter = ["---"] * len(header)
    return "\n".join(_row(r) for r in [header, delimiter, *rows])


def _row(cells: list[str]) -> str:
    # An empty cell is "| |", not "|  |": compact style allows exactly one space.
    return "|" + "|".join(f" {c} " if c else " " for c in cells) + "|"
