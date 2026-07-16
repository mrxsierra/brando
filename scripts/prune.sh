#!/bin/bash
# Prune generated outputs and configurations for fresh development runs.

# Determine project root directory (directory where the script is located, parent)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

# Source the .env file if it exists to get custom file paths
if [ -f "$PROJECT_ROOT/.env" ]; then
    echo "Sourcing environment configuration from .env..."
    # Export vars, ignoring comments/empty lines
    export $(grep -v '^#' "$PROJECT_ROOT/.env" | xargs)
fi

# Fallback defaults if envvars are empty
CONFIG_FILE="${BRAND_CONFIG_PATH:-config.yaml}"
DB_FILE="${BRAND_DB_PATH:-brand_candidates.csv}"
SHORTLIST_FILE="${BRAND_SHORTLIST_PATH:-shortlist.csv}"

# Make paths absolute relative to the project root
CONFIG_PATH="$PROJECT_ROOT/$CONFIG_FILE"
DB_PATH="$PROJECT_ROOT/$DB_FILE"
SHORTLIST_PATH="$PROJECT_ROOT/$SHORTLIST_FILE"

echo "Pruning workspace files..."

prune_file() {
    local filepath="$1"
    if [ -f "$filepath" ]; then
        echo "Removing: $filepath"
        rm "$filepath"
    else
        echo "Not found (skipping): $filepath"
    fi
}

prune_file "$CONFIG_PATH"
prune_file "$DB_PATH"
prune_file "$SHORTLIST_PATH"

echo "Pruning complete. Ready for a clean iteration!"
