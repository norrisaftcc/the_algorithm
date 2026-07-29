#!/usr/bin/env python3
"""
project_router.py — dry-run GitHub Projects routing evaluator.
Pilot scope: norrisaftcc/the_algorithm only.
No writes are performed. No live Project lookup is attempted.

Requires Python 3.9 or later (for built-in generic type hints).
"""

import sys

if sys.version_info < (3, 9):
    print(
        "ERROR: Python 3.9 or later is required.",
        file=sys.stderr,
    )
    sys.exit(1)

import json
import argparse
from pathlib import Path

try:
    import yaml
except ImportError:
    print(
        "ERROR: pyyaml is required. Install with: pip install pyyaml",
        file=sys.stderr,
    )
    sys.exit(1)

PILOT_REPO = "norrisaftcc/the_algorithm"
SCHEMA_VERSION = 1
DEFAULT_MAXIMUM_ITEMS = 25

# Valid routing results.
RESULT_WOULD_ADD = "would_add"
RESULT_IGNORED = "ignored"
RESULT_ALREADY_PRESENT = "already_present"
RESULT_ERROR = "error"


class RouterError(Exception):
    """Raised when configuration is invalid or a hard constraint is violated."""


def load_config(config_path: Path) -> dict:
    """Load YAML configuration from file. Fail closed on any error."""
    if not config_path.exists():
        raise RouterError(f"Configuration file not found: {config_path}")
    try:
        with open(config_path) as f:
            cfg = yaml.safe_load(f)
    except yaml.YAMLError as e:
        raise RouterError(f"Invalid YAML in config: {e}")
    return validate_config(cfg)


def validate_config(cfg: object) -> dict:
    """
    Validate a configuration mapping.
    Raises RouterError listing all violations if the config is invalid.
    Returns the validated config dict unchanged.
    """
    if not isinstance(cfg, dict):
        raise RouterError("Configuration must be a YAML/JSON mapping.")

    errors = []

    # Schema version.
    if cfg.get("schema_version") != SCHEMA_VERSION:
        errors.append(
            f"schema_version must be {SCHEMA_VERSION} "
            f"(got {cfg.get('schema_version')!r})"
        )

    # Exact repository name.
    repo = cfg.get("repository")
    if not isinstance(repo, dict) or repo.get("name") != PILOT_REPO:
        errors.append(
            f"repository.name must be exactly '{PILOT_REPO}' "
            f"(got {repo.get('name') if isinstance(repo, dict) else repo!r})"
        )

    # Routing section.
    routing = cfg.get("routing")
    if not isinstance(routing, dict):
        errors.append("routing section is required and must be a mapping.")

    # Safety section — all constraints must be present and set correctly.
    safety = cfg.get("safety")
    if not isinstance(safety, dict):
        errors.append("safety section is required and must be a mapping.")
    else:
        if not safety.get("dry_run", False):
            errors.append(
                "safety.dry_run must be true; "
                "live mode is not available in this pilot."
            )
        if safety.get("allow_delete", False):
            errors.append("safety.allow_delete must be false.")
        if safety.get("allow_archive", False):
            errors.append("safety.allow_archive must be false.")
        if safety.get("allow_cross_repository_items", False):
            errors.append("safety.allow_cross_repository_items must be false.")
        if safety.get("allow_project_writes", False):
            errors.append("safety.allow_project_writes must be false.")

    if errors:
        raise RouterError(
            "Configuration invalid:\n" + "\n".join(f"  - {e}" for e in errors)
        )

    return cfg


def evaluate_candidate(candidate: dict, cfg: dict) -> tuple:
    """
    Evaluate one candidate item against the routing configuration.

    Returns a (result, reason) tuple where result is one of:
      would_add       — item meets all routing criteria; would be added
      ignored         — item does not meet routing criteria; no action
      already_present — item already exists in the target project
      error           — item is invalid or violates a hard constraint

    Documented behavior for unsupported types:
      If candidate.type is not in routing.item_types, result is 'error'.
      The caller may filter or document these separately.
    """
    routing = cfg.get("routing", {})
    required_labels = set(routing.get("required_labels", []))
    excluded_labels = set(routing.get("excluded_labels", []))
    allowed_types = set(routing.get("item_types", []))
    repo_name = cfg["repository"]["name"]

    # Validate required candidate fields.
    for field in ("number", "type", "state", "labels", "repository"):
        if field not in candidate:
            return RESULT_ERROR, f"missing required field '{field}'"

    # Repository check — hard constraint.
    if candidate["repository"] != repo_name:
        return (
            RESULT_ERROR,
            f"repository '{candidate['repository']}' does not match '{repo_name}'",
        )

    # Type check — unsupported types are an error (documented).
    item_type = candidate["type"]
    if item_type not in allowed_types:
        return (
            RESULT_ERROR,
            f"item type '{item_type}' is not in allowed types {sorted(allowed_types)}",
        )

    # State check.
    if candidate["state"] != "open":
        return RESULT_IGNORED, f"state is '{candidate['state']}', not 'open'"

    # Exclusion label check (evaluated before required labels).
    item_labels = set(candidate["labels"])
    excluded_present = item_labels & excluded_labels
    if excluded_present:
        return RESULT_IGNORED, f"has excluded label(s): {sorted(excluded_present)}"

    # Required label check.
    missing_required = required_labels - item_labels
    if missing_required:
        return RESULT_IGNORED, f"missing required label(s): {sorted(missing_required)}"

    # Existing project membership.
    if candidate.get("already_in_project", False):
        return RESULT_ALREADY_PRESENT, "item is already in the project"

    return RESULT_WOULD_ADD, "meets all routing criteria"


def route_candidates(candidates: list, cfg: dict, limit: int) -> dict:
    """
    Route all candidates and return a structured report.

    Raises RouterError if the candidate count exceeds limit.
    The report always carries dry_run=True; no writes are performed.
    """
    if len(candidates) > limit:
        max_allowed = cfg.get("backfill", {}).get("maximum_items", DEFAULT_MAXIMUM_ITEMS)
        raise RouterError(
            f"Candidate count {len(candidates)} exceeds limit {limit} "
            f"(configured maximum: {max_allowed}). "
            f"Reduce scope or lower the candidate limit."
        )

    report = {
        "repository": cfg["repository"]["name"],
        "dry_run": True,
        "candidates_evaluated": len(candidates),
        "items": [],
        "summary": {
            RESULT_WOULD_ADD: 0,
            RESULT_IGNORED: 0,
            RESULT_ALREADY_PRESENT: 0,
            RESULT_ERROR: 0,
        },
    }

    for c in candidates:
        result, reason = evaluate_candidate(c, cfg)
        report["items"].append(
            {
                "number": c.get("number"),
                "type": c.get("type"),
                "result": result,
                "reason": reason,
            }
        )
        report["summary"][result] += 1

    return report


def get_fixture_candidates() -> list:
    """
    Return a small set of fixture candidates for local testing and dry runs
    when no live collection is available.
    """
    return [
        {
            "number": 101,
            "type": "issue",
            "state": "open",
            "labels": ["project:track"],
            "repository": PILOT_REPO,
            "already_in_project": False,
        },
        {
            "number": 102,
            "type": "issue",
            "state": "open",
            "labels": [],
            "repository": PILOT_REPO,
            "already_in_project": False,
        },
        {
            "number": 103,
            "type": "issue",
            "state": "open",
            "labels": ["project:track", "project:ignore"],
            "repository": PILOT_REPO,
            "already_in_project": False,
        },
        {
            "number": 104,
            "type": "pull_request",
            "state": "open",
            "labels": ["project:track"],
            "repository": PILOT_REPO,
            "already_in_project": True,
        },
    ]


def _print_summary(report: dict) -> None:
    s = report["summary"]
    print()
    print("--- DRY-RUN REPORT ---")
    print(f"Repository:      {report['repository']}")
    print(f"Mode:            DRY RUN — no writes performed")
    print(f"Evaluated:       {report['candidates_evaluated']} candidate(s)")
    print(f"would_add:       {s[RESULT_WOULD_ADD]}")
    print(f"ignored:         {s[RESULT_IGNORED]}")
    print(f"already_present: {s[RESULT_ALREADY_PRESENT]}")
    print(f"error:           {s[RESULT_ERROR]}")
    print("--- END REPORT ---")
    print()


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Dry-run GitHub Projects routing evaluator. "
            "Pilot: norrisaftcc/the_algorithm only. "
            "No writes are performed."
        )
    )
    parser.add_argument(
        "--config",
        default=".github/project-automation.yml",
        help="Path to configuration file (default: .github/project-automation.yml)",
    )
    parser.add_argument(
        "--candidates",
        help="Path to JSON file of candidate items (use '-' for stdin)",
    )
    parser.add_argument(
        "--fixture",
        action="store_true",
        help="Use built-in fixture candidates instead of --candidates",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Override candidate limit (must not exceed configured maximum)",
    )
    parser.add_argument(
        "--output",
        default=None,
        help="Path to write JSON report (printed to stdout if omitted)",
    )
    args = parser.parse_args()

    # Load and validate configuration.
    try:
        cfg = load_config(Path(args.config))
    except RouterError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)

    max_configured = cfg.get("backfill", {}).get("maximum_items", DEFAULT_MAXIMUM_ITEMS)
    effective_limit = max_configured
    if args.limit is not None:
        if args.limit > max_configured:
            print(
                f"ERROR: --limit {args.limit} exceeds configured maximum {max_configured}",
                file=sys.stderr,
            )
            sys.exit(1)
        effective_limit = args.limit

    # Load candidates.
    if args.fixture:
        candidates = get_fixture_candidates()
        print(f"Using fixture candidates ({len(candidates)} item(s)).")
    elif args.candidates:
        try:
            if args.candidates == "-":
                raw = sys.stdin.read()
            else:
                raw = Path(args.candidates).read_text()
            candidates = json.loads(raw)
        except (json.JSONDecodeError, OSError) as e:
            print(f"ERROR: Could not load candidates: {e}", file=sys.stderr)
            sys.exit(1)
        if not isinstance(candidates, list):
            print("ERROR: Candidates must be a JSON array.", file=sys.stderr)
            sys.exit(1)
    else:
        print(
            "ERROR: Provide --candidates <path> or --fixture.",
            file=sys.stderr,
        )
        sys.exit(1)

    # Route candidates.
    try:
        report = route_candidates(candidates, cfg, effective_limit)
    except RouterError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)

    # Output report.
    report_json = json.dumps(report, indent=2)

    if args.output:
        Path(args.output).write_text(report_json + "\n")
        print(f"JSON report written to: {args.output}")
    else:
        print(report_json)

    _print_summary(report)

    # Exit nonzero if any errors were found in candidates.
    if report["summary"][RESULT_ERROR] > 0:
        sys.exit(2)


if __name__ == "__main__":
    main()
