# Sound Symbolism & Industry Perception Matrix

Sound symbolism (phonesthemes) explores the subconscious perceptual associations linked to acoustic phonemes in brand names.

---

## Phonestheme Phoneme Mappings

| Phoneme Group | Acoustic Example | Perceptual Association | Ideal Industries |
| :--- | :--- | :--- | :--- |
| **Front Vowels** | `/i/`, `/e/` (e.g. *Zix*, *Vel*) | Small, fast, precise, light | FinTech, SaaS, Microchips |
| **Back Vowels** | `/o/`, `/u/` (e.g. *Kuro*, *Omni*) | Large, powerful, deep, premium | Automotive, Enterprise, AI |
| **Plosive Consonants** | `/p/`, `/t/`, `/k/` (e.g. *Kona*, *Trek*) | Sharp, reliable, energetic | Consumer Tech, Sports, Energy |
| **Fricative Consonants**| `/f/`, `/v/`, `/s/` (e.g. *Verve*, *Silk*) | Smooth, elegant, innovative | Luxury, Beauty, Security |
| **Nasal Consonants** | `/m/`, `/n/` (e.g. *Mono*, *Nox*) | Calm, trustworthy, natural | Healthcare, Pharma, Wellness |

---

## Programmatic Euphony Scoring Formula

`brando` evaluates phonetic euphony using weighted harmonic resonance across vowel harmony, plosive balance, and syllable rhythm:

<div class="admonition info" style="font-family: var(--md-code-font); font-size: 0.95rem; text-align: center; padding: 14px; margin: 16px 0;">
  <strong>Euphony Score</strong> = 0.40 × S<sub>vowel-harmony</sub> + 0.35 × S<sub>plosive-balance</sub> + 0.25 × S<sub>syllable-rhythm</sub>
</div>

---

## Python SDK Usage

```python
from brando.modules.phonetic import score_euphony

# Evaluate phonetic euphony for brand candidate
score = score_euphony("Vanta")
print(f"Euphony Score: {score:.2f}")
```
