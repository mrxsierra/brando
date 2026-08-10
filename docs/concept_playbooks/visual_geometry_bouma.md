# Bouma Silhouette Geometry & Visual Balance

The **Bouma shape** represents the visual outline created by lowercase ascenders (`b, d, f, h, k, l, t`) and descenders (`g, j, p, q, y`).

---

## Visual Silhouette Ratios

```text
  Ascender Height   ───►  [ b ]     [ l ]
  X-Height          ───►    [ a ] [ n ] [ d ]
  Descender Height  ───►                  [ g ]
```

- **Ascenders**: Characters extending above the x-height (`b, d, f, h, k, l, t`).

- **Descenders**: Characters extending below the baseline (`g, j, p, q, y`).

- **Neutral X-Height**: Characters contained within x-height (`a, c, e, m, n, o, r, s, u, v, w, x, z`).

---

## Bouma Score Computation

`brando` measures visual stability by calculating the symmetry between ascenders and descenders:

<div class="admonition info" style="font-family: var(--md-code-font); font-size: 0.95rem; text-align: center; padding: 14px; margin: 16px 0;">
  <strong>Visual Score</strong> = 100 − (15 × |N<sub>ascenders</sub> − N<sub>descenders</sub>| + 5 × P<sub>vowel</sub>)
</div>

---

## Python SDK Usage

```python
from brando.modules.visual import score_bouma_geometry

# Calculate visual geometry balance
score = score_bouma_geometry("Vanta")
print(f"Visual Score: {score:.2f}")
```
