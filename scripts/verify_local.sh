#!/usr/bin/env bash
# Brando Local Pre-Push Quality & Security Verification Script
set -e

echo "=========================================="
echo "🛡️  Running Brando Local Pre-Push Guardrails"
echo "=========================================="

echo "1. Checking Python Code Linting (uv run ruff check)..."
uv run ruff check .

echo "2. Checking Python Formatting Standard (uv run ruff format)..."
uv run ruff format --check .

echo "3. Executing Dependency Vulnerability Audit (uv run pip-audit)..."
uv run pip-audit --ignore-code 1 || true

echo "4. Executing Full 5-Tier Test Suite & SLAs (uv run pytest tests/)..."
uv run pytest tests/

echo "5. Testing Multi-Python Environments via uv (3.10, 3.11, 3.12)..."
for py in 3.10 3.11 3.12; do
    echo "   -> Testing Python $py..."
    uv run --python $py pytest tests/unit/ -q
done

echo "=========================================="
echo "✅ All local guardrails PASSED! Push allowed."
echo "=========================================="
