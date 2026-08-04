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
uv run pip-audit || true

echo "4. Executing Full 5-Tier Test Suite & SLAs (uv run pytest tests/)..."
uv run pytest tests/

echo "=========================================="
echo "✅ All local guardrails PASSED! Push allowed."
echo "=========================================="
