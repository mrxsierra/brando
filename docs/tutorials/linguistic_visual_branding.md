# Tutorial: Linguistic & Visual Branding API

This tutorial demonstrates how to import and use the Brando naming engine modules programmatically to filter and score brand names based on linguistic features, syllable counts, visual symmetry, midline ratios, and custom character heuristics.

## 1. Visual Aesthetics Analysis

Brando allows you to analyze visual properties of words, such as midline alignment ratios (percentage of characters without ascenders/descenders like `a`, `c`, `e`) and visual symmetry (checking if the number of ascenders matches descenders).

```python
from brando.generator import (
    calculate_midline_ratio,
    check_visual_symmetry,
    estimate_syllables,
)

name = "Vanta"

# Estimate syllable count
syllables = estimate_syllables(name)
print(f"Syllables: {syllables}")  # Output: 2

# Calculate midline ratio
midline = calculate_midline_ratio(name)
print(f"Midline Ratio: {midline}")  # Output: 0.8 (highly midline-balanced)

# Check vertical symmetry
symmetry = check_visual_symmetry(name)
print(f"Symmetrical: {symmetry}")  # Output: False (1 ascender 't', 0 descenders)
```

## 2. Character-Level Filtering Configuration

You can filter candidate names programmatically using custom character and vowel/consonant count limits inside `generate_candidates`.

```python
from brando.generator import generate_candidates

config = {
    "generation": {
        "max_candidates": 100,
        "min_letters": 4,
        "max_letters": 6,
        "max_syllables": 2,
        
        # Heuristics:
        "allowed_chars": "^[a-zA-Z]+$",  # Regex restricting allowed characters
        "disallowed_chars": ["x", "y"],  # Exclude specific characters
        "allow_numbers": False,          # Banish numbers
        "min_vowels": 2,                 # Force vowel count
        "max_vowels": 3,
    },
    "alignment": {
        "preferred_initials": ["A", "B", "V"],
    }
}

candidates = generate_candidates(config)
print(f"Generated {len(candidates)} names matching all visual & character filters.")
```
