import pytest
from conftest import adr_text, rec_text

from tasc_index.descriptions import derive_description
from tasc_index.models import DocType
from tasc_index.parsing import (
    ParseError,
    extract_section,
    parse_adr_title,
    parse_h1,
    parse_metadata,
)


def test_parses_multiple_fields_on_one_line():
    meta = parse_metadata(adr_text(date="2026-03-23", status="Proposed"))
    assert meta["date"] == "2026-03-23"
    assert meta["status"] == "Proposed"


def test_parses_one_field_per_line_with_colon_outside_bold():
    meta = parse_metadata(rec_text(doc_id="GA4GH-REC-07"))
    assert meta["recommendation"] == "GA4GH-REC-07"
    assert meta["status"] == "Approved"


def test_parses_colon_inside_bold():
    assert parse_metadata("**Date:** 2026-01-01  \n")["date"] == "2026-01-01"


def test_value_may_contain_markdown_links_and_commas():
    meta = parse_metadata("**Related GitHub issues**: [#1](https://x/1), [#2](https://x/2)  \n")
    assert meta["related github issues"] == "[#1](https://x/1), [#2](https://x/2)"


def test_header_stops_at_first_section():
    text = "# T\n\n**Status:** Draft\n\n## Body\n\n**Status:** Approved\n"
    assert parse_metadata(text)["status"] == "Draft"


def test_header_stops_at_rule():
    text = "# T\n\n**Status:** Draft\n---\n**Status:** Approved\n"
    assert parse_metadata(text)["status"] == "Draft"


def test_missing_fields_are_absent():
    assert parse_metadata("# Title\n\nNothing here\n") == {}


def test_parse_h1_requires_a_heading():
    with pytest.raises(ParseError):
        parse_h1("no heading\n")


def test_parse_adr_title_splits_id_and_name():
    title = parse_adr_title(adr_text(number="012", title="Role: of TASC"))
    assert (title.id, title.name) == ("TASC-ADR-012", "Role: of TASC")


@pytest.mark.parametrize(
    "h1", ["# Use Widgets", "# ADR-001: Use Widgets", "# TASC-ADR-001 Use Widgets"]
)
def test_parse_adr_title_rejects_malformed_titles(h1):
    with pytest.raises(ParseError):
        parse_adr_title(h1 + "\n")


def test_extract_section_returns_body_until_next_heading():
    text = "## Decision\n\nDo it.\n\n## Consequences\n\nLater.\n"
    assert extract_section(text, "Decision") == "Do it."


def test_extract_section_missing_is_empty():
    assert extract_section("## Context\n\nx\n", "Decision") == ""


def test_derive_description_uses_first_sentence_of_decision_for_adrs():
    assert derive_description(DocType.ADR, adr_text()) == "We will use widgets."


def test_derive_description_uses_abstract_for_recommendations():
    assert (
        derive_description(DocType.RECOMMENDATION, rec_text())
        == "This recommendation explains widgets."
    )


def test_derive_description_strips_links_and_code_and_truncates():
    text = "## Abstract\n\nSee [the guide](http://x) for `code`. " + "word " * 100 + "\n"
    assert derive_description(DocType.RECOMMENDATION, text) == "See the guide for code."
    long = "## Abstract\n\n" + "word " * 100 + "\n"
    derived = derive_description(DocType.RECOMMENDATION, long)
    assert len(derived) == 300 and derived.endswith("…")


def test_derive_description_empty_without_section():
    assert derive_description(DocType.ADR, "# T\n") == ""
