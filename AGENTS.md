# AGENTS.md

PyHAT demo app (FastAPI, Jinja2, HTMX, Tailwind/daisyUI). In-memory state only—no database.

**Stack:** FastAPI · Jinja2 · HTMX · Tailwind + daisyUI · nginx → app (Docker Compose)

## Layout

| Path | Role |
|------|------|
| `scripts/` | Helper scripts |
| `app/routers/` | Feature routers |
| `app/internal/` | Shared modules, singletons, constants, etc. |
| `app/templates/` | Jinja2 templates; extend `base.html` |
| `app/static/` | CSS, Javascript, and other assets |

## Architecture

- **Hypermedia UI:** server-rendered HTML is the application; HTMX swaps fragments instead of a separate SPA or client router.
- **Edge + app:** nginx terminates HTTP and proxies to a single FastAPI process; templates and static files are served from the app container.
- **Feature modules:** each area is a router plus Jinja templates; cross-cutting setup (templates, version metadata) lives in `app/internal/`.
- **No persistence layer:** demo state is in-process only—no database, migrations, or ORM unless explicitly added later.
- **Response model:** HTML is the default transport; JSON is reserved for small, intentional endpoints (e.g. health/version, simple counters).

## Patterns

- **New feature:** `app/routers/<name>.py` → register in `main.py` → `app/templates/<name>.html`.
- **HTMX mutations:** POST handlers return HTML; use Pydantic models with `hx-ext="json-enc"` where the table demo does.
- **Full pages:** include `request`, `version`, and `git_commit` in template context (see home/counter/table).
- **Imports in routers:** `from ..internal.common import ...`

## Frontend

- Prefer daisyUI/Tailwind classes in templates; avoid new global CSS.
- Do not hand-edit `output.css`; CSS comes from Dockerfile Tailwind stage (`app/static/input.css`, `tailwind.config.js`).
- After template/class changes affecting CSS: `./scripts/run.sh restart` (rebuild).

## Conventions

- **Lint:** `./scripts/lint.sh` (check, CI) · `./scripts/lint.sh --really` (ruff fix/format on `app/`).
- Match existing style: plain router functions, small classes in router files, minimal abstraction.
- `.env` is gitignored—never commit secrets.

## Verification

- Tests: `./scripts/test.sh` from repo root.
- After Python edits: `./scripts/lint.sh` and `./scripts/test.sh` from repo root.
- Runtime: `./scripts/run.sh up` or `./scripts/run.sh restart` from **git root**; app via nginx on port 80.
- Do not enable commented tools in `scripts/lint.sh` (mypy, djlint, deno) without request.

## Defaults for agents

- Small diffs; follow existing router/template/HTMX patterns.
- No commit/push or scope expansion (DB, auth, CI) unless asked.
- Do not touch `app/static/htmx*` except intentional HTMX upgrades.
