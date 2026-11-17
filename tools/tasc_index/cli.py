"""Command line entry point: ``python -m tasc_index``."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator

from tasc_index.builder import (
    DEFAULT_BRANCH,
    DEFAULT_REPO_URL,
    INDEXES,
    IndexBuildError,
    build_index,
    documents_for,
    render_index,
)

REPO_ROOT = Path(__file__).resolve().parents[2]


def validate_against_schema(rendered: str, schema_path: Path) -> list[str]:
    """Return human-readable schema violations (empty when valid)."""
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema)
    instance = json.loads(rendered)
    return [
        f"{'/'.join(str(p) for p in e.absolute_path) or '<root>'}: {e.message}"
        for e in sorted(validator.iter_errors(instance), key=lambda e: list(e.absolute_path))
    ]


def parse_args(argv: list[str] | None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="tasc_index", description="Generate the TASC ADR and recommendation index JSON files."
    )
    parser.add_argument("--root", type=Path, default=REPO_ROOT, help="repository root")
    parser.add_argument(
        "--index-dir",
        type=Path,
        help="directory holding the schemas and receiving the indexes (default: <root>/index)",
    )
    parser.add_argument("--repo-url", default=DEFAULT_REPO_URL)
    parser.add_argument("--branch", default=DEFAULT_BRANCH, help="branch used in generated links")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="fail if a document has no Description field or an ADR has no short name",
    )
    args = parser.parse_args(argv)
    args.index_dir = args.index_dir or args.root / "index"
    return args


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        result = build_index(
            args.root,
            strict=args.strict,
            repo_url=args.repo_url,
            branch=args.branch,
        )
    except IndexBuildError as exc:
        print("Index generation failed:", file=sys.stderr)
        for error in exc.errors:
            print(f"  - {error}", file=sys.stderr)
        return 1
    except (ValueError, OSError) as exc:
        print(f"Index generation failed: {exc}", file=sys.stderr)
        return 1

    for warning in result.warnings:
        print(f"warning: {warning}", file=sys.stderr)

    # Render and validate everything before writing anything.
    outputs: list[tuple[Path, str, int]] = []
    failed = False
    for spec in INDEXES:
        documents = documents_for(result.documents, spec.types)
        # Relative reference: valid while the schema sits beside the index.
        rendered = render_index(documents, spec.schema_filename)
        violations = validate_against_schema(rendered, args.index_dir / spec.schema_filename)
        for violation in violations:
            print(f"{spec.filename} does not satisfy its schema: {violation}", file=sys.stderr)
        failed = failed or bool(violations)
        outputs.append((args.index_dir / spec.filename, rendered, len(documents)))
    if failed:
        return 1

    for path, rendered, count in outputs:
        path.write_text(rendered, encoding="utf-8")
        print(f"Wrote {count} documents to {path}")
    return 0
