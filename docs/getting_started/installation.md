---
tags:
  - Installation
  - Setup
  - Package Managers
---

# Installation Guide

Install **`brando.`** using your preferred package manager.

---

## Quick Installation

=== "uv (Recommended)"

    ```bash
    # Ultra-fast isolated installation
    uv add brando
    ```

=== "pip"

    ```bash
    # Standard PyPI installation
    pip install brando
    ```

=== "Source Development"

    ```bash
    # Clone and install in editable development mode
    git clone https://github.com/mrxsierra/brando.git
    cd brando
    uv venv
    source .venv/bin/activate
    uv pip install -e .[dev]
    ```

=== "Docker"

    ```bash
    # Run containerized CLI wizard
    docker run -it ghcr.io/mrxsierra/brando:latest brando init
    ```

---

## Verify Installation

```bash
brando --version
```
