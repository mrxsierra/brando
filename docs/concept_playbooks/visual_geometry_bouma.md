# Bouma Silhouette Geometry & Visual Balance

The **Bouma shape** represents the visual outline created by lowercase ascenders (`b, d, f, h, k, l, t`) and descenders (`g, j, p, q, y`).

---

## 1. Visual Silhouette Ratios

```text
  Ascender Height   ───►  [ b ]     [ l ]
  X-Height          ───►    [ a ] [ n ] [ d ]
  Descender Height  ───►                  [ g ]
```

- **Ascenders**: Characters extending above the x-height (`b, d, f, h, k, l, t`).
- **Descenders**: Characters extending below the baseline (`g, j, p, q, y`).
- **Neutral X-Height**: Characters contained within x-height (`a, c, e, m, n, o, r, s, u, v, w, x, z`).

---

## 2. Bouma Score Computation

`brando` measures visual stability by calculating the symmetry between ascenders and descenders:

$$\text{Visual Score} = 100 - \left( 15 \cdot |N_{\text{ascenders}} - N_{\text{descenders}}| + 5 \cdot \text{Vowel Density Penalty} \right)$$
