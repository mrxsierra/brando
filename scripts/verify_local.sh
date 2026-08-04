#!/usr/bin/env bash
# Brando Local Pre-Push Quality Verification Script
set -e

echo "=========================================="
echo "🛡️  Running Brando Local Pre-Push Guardrails"
echo "=========================================="

echo "1. Checking Python Code Linting (ruff check)..."
.venv/bin/ruff check .

echo "2. Checking Python Formatting Standard (ruff format)..."
.venv/bin/ruff format --check .

echo "3. Executing Full 5-Tier Test Suite & SLAs (pytest tests/)..."
.venv/bin/pytest tests/

echo "=========================================="
echo "✅ All local guardrails PASSED! Push allowed."
echo "=========================================="
