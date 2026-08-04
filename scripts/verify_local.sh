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

echo "3. Executing Unit Test Suite (pytest)..."
.venv/bin/pytest tests/unit/

echo "=========================================="
echo "✅ All local guardrails PASSED! Push allowed."
echo "=========================================="
