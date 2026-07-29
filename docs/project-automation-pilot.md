# GitHub Projects automation pilot

## What this is

A dry-run routing evaluator for `norrisaftcc/the_algorithm`.

**This pilot does not write to any GitHub Project.** It evaluates which open issues and pull requests *would be* routed to a project and reports them without making any change. Scope is fixed to this repository only.

---

## Routing rules

An item is routed `would_add` when all of these are true:

1. State is `open`.
2. Item type is `issue` or `pull_request`.
3. Item has the label `project:track`.
4. Item does not have the label `project:ignore`.
5. Item repository exactly matches `norrisaftcc/the_algorithm`.
6. Item is not already in the project (`already_in_project` is false).

Otherwise the result is:

| Result | Condition |
|---|---|
| `would_add` | All routing criteria met. |
| `ignored` | Item is closed, missing a required label, or has an excluded label. |
| `already_present` | Item already exists in the project. |
| `error` | Item comes from the wrong repository, has an unsupported type, or is missing required fields. |

Exclusion is checked before required labels. An item with both `project:track` and `project:ignore` is always `ignored`.

Unsupported types (for example `discussion`) produce an `error` result and do not block the run, but the evaluator exits with status 2 when any errors are present.

---

## Configuration file

`.github/project-automation.yml`

| Field | Value | Notes |
|---|---|---|
| `schema_version` | `1` | Evaluated against a hardcoded constant. |
| `repository.name` | `norrisaftcc/the_algorithm` | Exact match required. |
| `project.owner` | `null` | Placeholder. No live Project lookup. |
| `project.number` | `null` | Placeholder. No live Project lookup. |
| `routing.required_labels` | `["project:track"]` | |
| `routing.excluded_labels` | `["project:ignore"]` | |
| `routing.item_types` | `["issue", "pull_request"]` | |
| `backfill.enabled` | `false` | |
| `backfill.maximum_items` | `25` | Hard cap on candidates. |
| `safety.dry_run` | `true` | Permanently true. |
| `safety.allow_project_writes` | `false` | |
| `safety.allow_delete` | `false` | |
| `safety.allow_archive` | `false` | |
| `safety.allow_cross_repository_items` | `false` | |

Setting any safety flag incorrectly causes the evaluator to fail closed with exit status 1.

---

## How to run locally

Requirements: Python 3.11 or later, `pyyaml`.

```bash
pip install pyyaml
```

Run with the built-in fixture candidates (no live API calls):

```bash
python scripts/project_router.py --fixture
```

Run with a local JSON candidates file:

```bash
python scripts/project_router.py --candidates /path/to/candidates.json
```

Write a JSON report to a file:

```bash
python scripts/project_router.py --fixture --output report.json
```

Candidates JSON format (array of objects):

```json
[
  {
    "number": 42,
    "type": "issue",
    "state": "open",
    "labels": ["project:track"],
    "repository": "norrisaftcc/the_algorithm",
    "already_in_project": false
  }
]
```

Run the automated tests:

```bash
python -m unittest tests.test_project_router -v
```

---

## How to manually trigger the workflow

1. Go to **Actions** → **project-automation-pilot**.
2. Click **Run workflow**.
3. Leave `dry_run_confirm` as `true` (any other value aborts the run).
4. Optionally set `candidate_limit` to a number from 1 to 25.
5. Click **Run workflow**.

The workflow produces a `dry-run-report` artifact (JSON) available for 7 days under the run's **Artifacts** section.

---

## Report fields

The JSON report contains:

| Field | Description |
|---|---|
| `repository` | Repository name from config. |
| `dry_run` | Always `true`. |
| `candidates_evaluated` | Number of items examined. |
| `items` | Array of per-item results. |
| `items[].number` | Issue or PR number. |
| `items[].type` | `issue` or `pull_request`. |
| `items[].result` | One of `would_add`, `ignored`, `already_present`, `error`. |
| `items[].reason` | Human-readable explanation. |
| `summary.would_add` | Count of items that would be added. |
| `summary.ignored` | Count of items skipped by routing rules. |
| `summary.already_present` | Count of items already in the project. |
| `summary.error` | Count of items with an error result. |

---

## Permissions

The workflow requests:

- `contents: read` — read repository files.
- `issues: read` — list open issues.
- `pull-requests: read` — list open pull requests.

No write permissions are requested or used. The `github.token` provided automatically has these permissions for public repositories.

---

## Known limitations

- **No live Project validation.** The pilot does not query the GitHub Projects API. `project.owner` and `project.number` in the config are placeholders.
- **No duplicate detection from live Projects.** The `already_in_project` field in candidates is always `false` when collected from the API. Callers may set it in a pre-processed candidates file.
- **No backfill.** `backfill.enabled` is `false`. Items are evaluated on demand only.
- **`gh` CLI state field.** The `gh` CLI returns states in uppercase (`OPEN`, `CLOSED`, `MERGED`). The collector normalizes these to lowercase before passing them to the evaluator.

---

## Future activation steps

These steps are **not implemented** and require separate human approval before any one of them is taken.

1. Supply a real `project.owner` and `project.number` in `.github/project-automation.yml`.
2. Create or reuse a GitHub Personal Access Token or GitHub App with `project` write scope.
3. Store the token as a repository secret (for example `PROJECTS_TOKEN`).
4. Implement a live Project membership check (query the Projects v2 GraphQL API).
5. Implement a write path to add items to the project.
6. Change `safety.allow_project_writes` to `true` after a separate review.
7. Optionally enable automatic event triggers (issues, pull_request) in the workflow.
8. Optionally enable backfill (`backfill.enabled: true`) for existing open items.

**None of these steps may be taken without explicit human review and approval.**

---

## Rollback

To disable this pilot:

1. Disable the workflow: **Actions** → **project-automation-pilot** → **⋯** → **Disable workflow**.
2. Or delete `.github/workflows/project-automation-pilot.yml` and revert this pull request.
3. No GitHub Project data is affected. The pilot creates no project items.
4. Remove any labels (`project:track`, `project:ignore`) from issues and PRs if desired.

---

## Files changed by this pilot

```
.github/project-automation.yml          — routing configuration
.github/workflows/project-automation-pilot.yml  — workflow (manual trigger only)
scripts/project_router.py               — routing evaluator (pure Python, no writes)
tests/__init__.py                        — test package marker
tests/test_project_router.py            — 33 automated tests
docs/project-automation-pilot.md        — this document
```
