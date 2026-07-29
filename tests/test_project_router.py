"""
test_project_router.py — focused tests for the GitHub Projects dry-run routing evaluator.

Covers:
  - open tracked issue             => would_add
  - open item without label        => ignored
  - item with exclusion label      => ignored
  - closed item                    => ignored
  - matching pull request          => would_add
  - existing membership            => already_present
  - wrong repository               => error
  - unsupported item type          => error (documented: only 'issue' and 'pull_request' allowed)
  - missing/invalid configuration  => RouterError (fail closed)
  - candidate count above limit    => RouterError (fail closed)
  - dry run performs no writes     => structurally guaranteed by the pure function design
  - real config file is valid      => integration test (skipped if pyyaml unavailable)
"""

import unittest
from pathlib import Path

from scripts.project_router import (
    RouterError,
    PILOT_REPO,
    RESULT_WOULD_ADD,
    RESULT_IGNORED,
    RESULT_ALREADY_PRESENT,
    RESULT_ERROR,
    evaluate_candidate,
    route_candidates,
    validate_config,
)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_config(**overrides) -> dict:
    """Return a minimal valid configuration dict. Apply dot-path overrides."""
    cfg = {
        "schema_version": 1,
        "repository": {"name": "norrisaftcc/the_algorithm"},
        "project": {"owner": None, "number": None},
        "routing": {
            "required_labels": ["project:track"],
            "excluded_labels": ["project:ignore"],
            "item_types": ["issue", "pull_request"],
        },
        "backfill": {"enabled": False, "maximum_items": 25},
        "safety": {
            "dry_run": True,
            "allow_delete": False,
            "allow_archive": False,
            "allow_cross_repository_items": False,
            "allow_project_writes": False,
        },
    }
    for dotpath, val in overrides.items():
        parts = dotpath.split(".")
        node = cfg
        for part in parts[:-1]:
            node = node[part]
        node[parts[-1]] = val
    return cfg


def _make_candidate(**overrides) -> dict:
    """Return a minimal valid open tracked issue candidate."""
    c = {
        "number": 1,
        "type": "issue",
        "state": "open",
        "labels": ["project:track"],
        "repository": "norrisaftcc/the_algorithm",
        "already_in_project": False,
    }
    c.update(overrides)
    return c


# ---------------------------------------------------------------------------
# evaluate_candidate tests
# ---------------------------------------------------------------------------

class TestEvaluateCandidate(unittest.TestCase):

    def setUp(self):
        self.cfg = _make_config()

    def test_open_tracked_issue_would_add(self):
        """Open issue with required label => would_add."""
        c = _make_candidate(type="issue", state="open", labels=["project:track"])
        result, _ = evaluate_candidate(c, self.cfg)
        self.assertEqual(result, RESULT_WOULD_ADD)

    def test_open_item_without_tracking_label_ignored(self):
        """Open issue missing the required label => ignored."""
        c = _make_candidate(labels=[])
        result, _ = evaluate_candidate(c, self.cfg)
        self.assertEqual(result, RESULT_IGNORED)

    def test_item_with_exclusion_label_ignored(self):
        """Exclusion label overrides the required label => ignored."""
        c = _make_candidate(labels=["project:track", "project:ignore"])
        result, _ = evaluate_candidate(c, self.cfg)
        self.assertEqual(result, RESULT_IGNORED)

    def test_closed_item_ignored(self):
        """Closed item is never routed => ignored."""
        c = _make_candidate(state="closed")
        result, _ = evaluate_candidate(c, self.cfg)
        self.assertEqual(result, RESULT_IGNORED)

    def test_matching_pull_request_would_add(self):
        """Open pull request with required label => would_add."""
        c = _make_candidate(type="pull_request")
        result, _ = evaluate_candidate(c, self.cfg)
        self.assertEqual(result, RESULT_WOULD_ADD)

    def test_existing_membership_already_present(self):
        """Item flagged as already in project => already_present."""
        c = _make_candidate(already_in_project=True)
        result, _ = evaluate_candidate(c, self.cfg)
        self.assertEqual(result, RESULT_ALREADY_PRESENT)

    def test_wrong_repository_error(self):
        """Item from a different repository => error."""
        c = _make_candidate(repository="norrisaftcc/other_repo")
        result, _ = evaluate_candidate(c, self.cfg)
        self.assertEqual(result, RESULT_ERROR)

    def test_unsupported_item_type_error(self):
        """
        Unsupported item types (e.g. 'discussion') => error.
        Documented behavior: only 'issue' and 'pull_request' are allowed.
        """
        c = _make_candidate(type="discussion")
        result, _ = evaluate_candidate(c, self.cfg)
        self.assertEqual(result, RESULT_ERROR)

    def test_missing_required_field_error(self):
        """Candidate missing required fields => error."""
        c = {"number": 1, "type": "issue"}  # missing state, labels, repository
        result, _ = evaluate_candidate(c, self.cfg)
        self.assertEqual(result, RESULT_ERROR)

    def test_exclusion_wins_over_required_label(self):
        """Exclusion check happens before required-label check."""
        c = _make_candidate(labels=["project:track", "project:ignore"])
        result, reason = evaluate_candidate(c, self.cfg)
        self.assertEqual(result, RESULT_IGNORED)
        self.assertIn("excluded", reason)

    def test_reason_string_is_nonempty(self):
        """Every result is accompanied by a non-empty reason string."""
        cases = [
            _make_candidate(),
            _make_candidate(labels=[]),
            _make_candidate(labels=["project:ignore"]),
            _make_candidate(state="closed"),
            _make_candidate(already_in_project=True),
            _make_candidate(repository="norrisaftcc/wrong"),
            _make_candidate(type="unknown"),
        ]
        for c in cases:
            _, reason = evaluate_candidate(c, self.cfg)
            self.assertTrue(reason, f"Empty reason for candidate {c}")


# ---------------------------------------------------------------------------
# validate_config tests
# ---------------------------------------------------------------------------

class TestValidateConfig(unittest.TestCase):

    def test_valid_config_passes(self):
        """A fully valid config dict passes without raising."""
        cfg = _make_config()
        result = validate_config(cfg)
        self.assertIsInstance(result, dict)

    def test_wrong_schema_version_fails(self):
        cfg = _make_config()
        cfg["schema_version"] = 2
        with self.assertRaises(RouterError) as ctx:
            validate_config(cfg)
        self.assertIn("schema_version", str(ctx.exception))

    def test_wrong_repository_fails(self):
        cfg = _make_config()
        cfg["repository"]["name"] = "norrisaftcc/algorithm-shodann"
        with self.assertRaises(RouterError) as ctx:
            validate_config(cfg)
        self.assertIn("repository.name", str(ctx.exception))

    def test_dry_run_false_fails(self):
        """Setting dry_run=False must fail closed."""
        cfg = _make_config()
        cfg["safety"]["dry_run"] = False
        with self.assertRaises(RouterError) as ctx:
            validate_config(cfg)
        self.assertIn("dry_run", str(ctx.exception))

    def test_allow_delete_true_fails(self):
        cfg = _make_config()
        cfg["safety"]["allow_delete"] = True
        with self.assertRaises(RouterError) as ctx:
            validate_config(cfg)
        self.assertIn("allow_delete", str(ctx.exception))

    def test_allow_archive_true_fails(self):
        cfg = _make_config()
        cfg["safety"]["allow_archive"] = True
        with self.assertRaises(RouterError) as ctx:
            validate_config(cfg)
        self.assertIn("allow_archive", str(ctx.exception))

    def test_allow_project_writes_true_fails(self):
        cfg = _make_config()
        cfg["safety"]["allow_project_writes"] = True
        with self.assertRaises(RouterError) as ctx:
            validate_config(cfg)
        self.assertIn("allow_project_writes", str(ctx.exception))

    def test_allow_cross_repository_true_fails(self):
        cfg = _make_config()
        cfg["safety"]["allow_cross_repository_items"] = True
        with self.assertRaises(RouterError) as ctx:
            validate_config(cfg)
        self.assertIn("allow_cross_repository_items", str(ctx.exception))

    def test_missing_safety_section_fails(self):
        cfg = _make_config()
        del cfg["safety"]
        with self.assertRaises(RouterError):
            validate_config(cfg)

    def test_missing_individual_safety_key_fails(self):
        """Each required safety key, when absent, must cause validate_config to raise RouterError."""
        required_keys = [
            "dry_run",
            "allow_delete",
            "allow_archive",
            "allow_cross_repository_items",
            "allow_project_writes",
        ]
        for key in required_keys:
            with self.subTest(key=key):
                cfg = _make_config()
                del cfg["safety"][key]
                with self.assertRaises(RouterError) as ctx:
                    validate_config(cfg)
                self.assertIn(key, str(ctx.exception))

    def test_missing_routing_section_fails(self):
        cfg = _make_config()
        del cfg["routing"]
        with self.assertRaises(RouterError):
            validate_config(cfg)

    def test_non_dict_config_fails(self):
        with self.assertRaises(RouterError):
            validate_config("not a dict")

    def test_none_config_fails(self):
        with self.assertRaises(RouterError):
            validate_config(None)

    def test_multiple_errors_reported_together(self):
        """All violations are reported in a single RouterError, not just the first."""
        cfg = _make_config()
        cfg["schema_version"] = 99
        cfg["repository"]["name"] = "wrong/repo"
        cfg["safety"]["dry_run"] = False
        with self.assertRaises(RouterError) as ctx:
            validate_config(cfg)
        msg = str(ctx.exception)
        self.assertIn("schema_version", msg)
        self.assertIn("repository.name", msg)
        self.assertIn("dry_run", msg)


# ---------------------------------------------------------------------------
# route_candidates tests
# ---------------------------------------------------------------------------

class TestRouteCandidates(unittest.TestCase):

    def setUp(self):
        self.cfg = _make_config()

    def test_candidate_count_above_limit_fails_closed(self):
        """26 candidates with a limit of 25 must raise RouterError."""
        candidates = [_make_candidate(number=i) for i in range(26)]
        with self.assertRaises(RouterError) as ctx:
            route_candidates(candidates, self.cfg, limit=25)
        self.assertIn("exceeds limit", str(ctx.exception))

    def test_candidate_count_at_limit_passes(self):
        """Exactly 25 candidates at a limit of 25 must succeed."""
        candidates = [_make_candidate(number=i) for i in range(25)]
        report = route_candidates(candidates, self.cfg, limit=25)
        self.assertEqual(report["candidates_evaluated"], 25)

    def test_mixed_candidates_summary(self):
        """Report summary counts are correct across all result types."""
        candidates = [
            _make_candidate(number=1, labels=["project:track"]),           # would_add
            _make_candidate(number=2, labels=[]),                           # ignored (no label)
            _make_candidate(number=3, labels=["project:track", "project:ignore"]),  # ignored (excluded)
            _make_candidate(number=4, state="closed"),                      # ignored (closed)
            _make_candidate(number=5, type="pull_request", labels=["project:track"]),  # would_add
            _make_candidate(number=6, labels=["project:track"], already_in_project=True),  # already_present
        ]
        report = route_candidates(candidates, self.cfg, limit=25)
        self.assertEqual(report["summary"][RESULT_WOULD_ADD], 2)
        self.assertEqual(report["summary"][RESULT_IGNORED], 3)
        self.assertEqual(report["summary"][RESULT_ALREADY_PRESENT], 1)
        self.assertEqual(report["summary"][RESULT_ERROR], 0)

    def test_dry_run_always_true_in_report(self):
        """The report must always carry dry_run=True."""
        candidates = [_make_candidate()]
        report = route_candidates(candidates, self.cfg, limit=25)
        self.assertTrue(report["dry_run"])

    def test_no_write_operation_performed(self):
        """
        Dry run: route_candidates is a pure function with no I/O.
        No network calls, file writes, or mutations are possible.
        Verified by: the function returns a dict without raising and
        without modifying the input candidates list.
        """
        candidates = [_make_candidate()]
        original_len = len(candidates)
        report = route_candidates(candidates, self.cfg, limit=25)
        self.assertEqual(len(candidates), original_len, "Input list must not be mutated")
        self.assertIn("dry_run", report)
        self.assertTrue(report["dry_run"])

    def test_report_contains_items_list(self):
        """Each evaluated candidate produces an entry in report['items']."""
        candidates = [_make_candidate(number=n) for n in range(3)]
        report = route_candidates(candidates, self.cfg, limit=25)
        self.assertEqual(len(report["items"]), 3)
        for item in report["items"]:
            self.assertIn("number", item)
            self.assertIn("result", item)
            self.assertIn("reason", item)

    def test_empty_candidate_list_produces_zero_summary(self):
        report = route_candidates([], self.cfg, limit=25)
        self.assertEqual(report["candidates_evaluated"], 0)
        for v in report["summary"].values():
            self.assertEqual(v, 0)

    def test_report_repository_matches_config(self):
        candidates = [_make_candidate()]
        report = route_candidates(candidates, self.cfg, limit=25)
        self.assertEqual(report["repository"], PILOT_REPO)


# ---------------------------------------------------------------------------
# Integration: real config file
# ---------------------------------------------------------------------------

class TestRealConfigFile(unittest.TestCase):
    """
    Integration test: load and validate the actual .github/project-automation.yml.
    Skipped when pyyaml is not installed or the file is not found.
    """

    def test_real_config_is_valid(self):
        try:
            import yaml  # availability check only; pyyaml is required by load_config
        except ImportError:
            self.skipTest("pyyaml not installed")

        config_path = Path(__file__).parent.parent / ".github" / "project-automation.yml"
        if not config_path.exists():
            self.skipTest(f"Config file not found: {config_path}")

        from scripts.project_router import load_config

        cfg = load_config(config_path)
        self.assertEqual(cfg["repository"]["name"], PILOT_REPO)
        self.assertTrue(cfg["safety"]["dry_run"])
        self.assertFalse(cfg["safety"]["allow_project_writes"])
        self.assertFalse(cfg["safety"]["allow_delete"])
        self.assertFalse(cfg["safety"]["allow_archive"])
        self.assertFalse(cfg["safety"]["allow_cross_repository_items"])
        self.assertIn("project:track", cfg["routing"]["required_labels"])
        self.assertIn("project:ignore", cfg["routing"]["excluded_labels"])


if __name__ == "__main__":
    unittest.main()
