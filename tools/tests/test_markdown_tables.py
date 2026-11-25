"""Generated tables must be in markdownlint's "compact" style (MD060): one space inside every
pipe, including the delimiter row. The repo lint config ignores the generated files, so this is
the only thing that checks them."""

import re

import pytest
from conftest import REPO_ROOT

from tasc_index.markdown import table

GENERATED = [
    "adr/README.md",
    "recommendations/README.md",
    "registries/README.md",
    "requirements/README.md",
]
DELIMITER = re.compile(r"^\|( :?-{3,}:? \|)+$")


def test_table_helper_writes_an_empty_cell_as_one_space():
    assert table(["A", "B"], [["", "2"]]).splitlines()[2] == "| | 2 |"


def test_table_helper_emits_a_compact_delimiter_row():
    assert table(["A", "B"], [["1", "2"]]).splitlines() == [
        "| A | B |",
        "| --- | --- |",
        "| 1 | 2 |",
    ]


def assert_compact(lines):
    assert lines
    for line in lines:
        cells = re.split(r"(?<!\\)\|", line)[1:-1]
        assert all(c.startswith(" ") and c.endswith(" ") for c in cells), line
        if set(line) <= set("|- :"):
            assert DELIMITER.match(line), line


def table_lines(text):
    return [line for line in text.splitlines() if line.startswith("|")]


@pytest.mark.parametrize("path", GENERATED)
def test_committed_generated_tables_are_compact(path):
    assert_compact(table_lines((REPO_ROOT / path).read_text(encoding="utf-8")))
