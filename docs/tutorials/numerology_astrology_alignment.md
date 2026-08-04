# Tutorial: Numerology & Astrology Alignment API

This tutorial demonstrates how to compute esoteric alignments programmatically using Pythagorean and Chaldean numerology reductions and Vedic starting sound checks.

## 1. Numerology Destiny Reductions

Brando supports two main mapping systems: Pythagorean (sequential Western mapping 1-9) and Chaldean (ancient vibrational mapping 1-8). Both compute a sum and reduce it to a single-digit root number.

```python
from brando.esoteric import calculate_chaldean, calculate_pythagorean

name = "Vanta"

# Chaldean: V=6, a=1, n=5, t=4, a=1. Sum = 17. Reduced = 1+7 = 8.
c_sum, c_red = calculate_chaldean(name)
print(f"Chaldean Sum: {c_sum}, Reduced: {c_red}")

# Pythagorean: V=4, a=1, n=5, t=2, a=1. Sum = 13. Reduced = 1+3 = 4.
p_sum, p_red = calculate_pythagorean(name)
print(f"Pythagorean Sum: {p_sum}, Reduced: {p_red}")
```

## 2. Vedic Starting Sounds

You can cross-reference the name prefix against auspicious sounds determined by Vedic astrology.

```python
from brando.esoteric import check_vedic_astrology

# List of auspicious starting sounds matching candidate initials
auspicious_sounds = ["va", "vi", "ve", "vo"]

# Check if Vanta matches
matches = check_vedic_astrology("Vanta", auspicious_sounds)
print(f"Is Vanta auspicious? {matches}")  # Output: True
```
