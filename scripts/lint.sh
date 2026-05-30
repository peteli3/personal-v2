#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
VENV="$ROOT/.venv"

REALLY=0
while [[ $# -gt 0 ]]; do
    case "$1" in
        --really)
            REALLY=1
            shift
            ;;
        -h | --help)
            echo "Usage: $0 [--really]"
            echo "  (default)  check only; suitable for CI"
            echo "  --really   apply ruff fixes and format files in place"
            exit 0
            ;;
        *)
            echo "unknown option: $1" >&2
            echo "Usage: $0 [--really]" >&2
            exit 1
            ;;
    esac
done

if ((REALLY)); then
    echo "==> Mode: apply fixes"
else
    echo "==> Mode: check only"
fi

ensure_dev_env() {
    command -v python3 >/dev/null || {
        echo "missing: python3 (needed to create .venv)"
        exit 1
    }

    if [[ ! -d "$VENV" ]]; then
        echo "==> Creating .venv"
        python3 -m venv "$VENV"
    fi

    if [[ "${VIRTUAL_ENV:-}" != "$VENV" ]]; then
        # shellcheck disable=SC1091
        source "$VENV/bin/activate"
    fi

    echo "==> Syncing dependencies"
    python -m pip install -q -r "$ROOT/requirements.txt" -r "$ROOT/requirements-dev.txt"
}

ensure_dev_env

require() {
    command -v "$1" >/dev/null || {
        echo "missing: $1 (pip install -r requirements-dev.txt)"
        exit 1
    }
}
require ruff
# require mypy
# require djlint
# require deno

failed=0
run() {
    echo "==> $*"
    "$@" || failed=1
}

if ((REALLY)); then
    run ruff check --fix app tests
    run ruff format app tests
    # run mypy app
    # run djlint app/templates
    # run deno lint app/static
    # run deno fmt app/static
else
    run ruff check app tests
    run ruff format --check app tests
    # run mypy app
    # run djlint --check app/templates
    # run deno lint app/static
    # run deno fmt --check app/static
fi

exit "$failed"
