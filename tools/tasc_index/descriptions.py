"""Fallback one-line descriptions for documents that lack a ``Description`` field.

The description normally comes from the document's own metadata header. When it
is missing we derive one from the first sentence of the Abstract (or, for ADRs,
the Decision section) so that the index is never blank.
"""

from __future__ import annotations

import re

from tasc_index.models import DocType
from tasc_index.parsing import extract_section

MAX_LENGTH = 300

_SENTENCE_END = re.compile(r"(?<=[.!?])\s+")
_MARKDOWN_LINK = re.compile(r"\[([^\]]+)\]\([^)]*\)")


def derive_description(doc_type: DocType, text: str) -> str:
    """Best-effort one-liner from the document body; '' if nothing usable."""
    section = "Decision" if doc_type is DocType.ADR else "Abstract"
    paragraph = extract_section(text, section).split("\n\n", 1)[0]
    paragraph = _MARKDOWN_LINK.sub(r"\1", " ".join(paragraph.split())).replace("`", "")
    sentence = _SENTENCE_END.split(paragraph, maxsplit=1)[0]
    if len(sentence) > MAX_LENGTH:
        sentence = sentence[: MAX_LENGTH - 1].rstrip() + "…"
    return sentence
