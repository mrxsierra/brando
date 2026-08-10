---
tags:
  - WASM
  - Playground
  - Pyodide
  - Interactive
---

# Interactive WASM Pyodide Playground

Execute **`brando.`** brand synthesis, phonetic euphony scoring, and security vetting algorithms directly in your browser powered by WebAssembly (zero backend required).

---

## 🎯 What Problems Does `brando.` Solve?

| Core Brand Challenge | Traditional Approach | How `brando.` Solves It |
| :--- | :--- | :--- |
| **Subjective Naming Guesswork** | Arbitrary human gut feelings | **Phonetic Euphony Scoring**: Computes harmonic resonance, IPA flow, and sound symbolism vectors. |
| **Package Typosquatting Risks** | Manual WHOIS / PyPI searches | **Sub-35ms RapidFuzz SIMD**: Audits candidate edit distance against existing package registries. |
| **Typographic Visual Imbalance** | Trial-and-error graphic design | **Bouma Geometry Math**: Calculates ascender, descender, and midline silhouette height ratios. |
| **Vibrational Sound Alignment** | ❌ None | **108 Nakshatra Padas**: Maps initial candidate phonemes to Pythagorean, Chaldean & Vedic astrology. |

---

## 💻 Live WebAssembly Execution Console

Select a real-world use case preset below to load the corresponding Python algorithm into the editor:

<div id="pyodide-loading" style="padding: 16px; background: #0F172A; color: #FFFFFF; border-radius: 8px; font-weight: bold; margin-bottom: 15px;">
  ⚡ Initializing Pyodide WebAssembly engine...
</div>

<div id="playground-container">
  <div style="margin-bottom: 12px; display: flex; gap: 8px; flex-wrap: wrap;">
    <button class="preset-btn" data-preset="euphony" style="padding: 8px 16px; background: rgba(37, 99, 235, 0.12); color: #2563EB; border: 1px solid rgba(37, 99, 235, 0.3); border-radius: 20px; font-weight: 600; cursor: pointer; font-size: 13px;">
      🚀 1. Phonetic Euphony Scoring
    </button>
    <button class="preset-btn" data-preset="security" style="padding: 8px 16px; background: rgba(37, 99, 235, 0.12); color: #2563EB; border: 1px solid rgba(37, 99, 235, 0.3); border-radius: 20px; font-weight: 600; cursor: pointer; font-size: 13px;">
      🛡️ 2. Security Typosquatting Audit
    </button>
    <button class="preset-btn" data-preset="bouma" style="padding: 8px 16px; background: rgba(37, 99, 235, 0.12); color: #2563EB; border: 1px solid rgba(37, 99, 235, 0.3); border-radius: 20px; font-weight: 600; cursor: pointer; font-size: 13px;">
      📐 3. Bouma Visual Geometry
    </button>
    <button class="preset-btn" data-preset="nakshatra" style="padding: 8px 16px; background: rgba(37, 99, 235, 0.12); color: #2563EB; border: 1px solid rgba(37, 99, 235, 0.3); border-radius: 20px; font-weight: 600; cursor: pointer; font-size: 13px;">
      🔮 4. 108 Nakshatra Padas
    </button>
  </div>

  <textarea id="python-code" rows="15" style="width: 100%; font-family: var(--md-code-font); font-size: 13px; padding: 14px; border-radius: 8px; border: 1px solid rgba(226, 232, 240, 0.5); background: #090D16; color: #E2E8F0; line-height: 1.5;"># Use Case 1: Phonetic Euphony & Harmonic Flow Scoring
import math

def calculate_euphony(name):
    """Computes sound symbolism, plosive dampening, and sonorant resonance."""
    name_lower = name.lower()
    plosives = sum(1 for c in name_lower if c in 'ptkbdg')
    sonorants = sum(1 for c in name_lower if c in 'lmnr')
    vowels = sum(1 for c in name_lower if c in 'aeiou')
    
    score = 50 + (sonorants * 12) + (vowels * 6) - (plosives * 4)
    return max(0, min(100, score))

candidates = ["Vanta", "Aero", "Cortex", "Nexus", "Krypton", "Zylo", "Lumene"]

print("=" * 45)
print(f"{'BRAND NAME':<14} {'EUPHONY SCORE':<16} {'QUALITIES':<15}")
print("=" * 45)

for brand in candidates:
    score = calculate_euphony(brand)
    quality = "🌟 Premium" if score >= 75 else "👍 Balanced" if score >= 60 else "⚠️ Plosive"
    print(f"{brand:<14} {score:<16.1f} {quality:<15}")

print("=" * 45)
  </textarea>

  <button id="run-btn" style="margin-top: 12px; padding: 12px 24px; background: #2563EB; color: white; border: none; border-radius: 6px; font-weight: bold; cursor: pointer; font-size: 15px; display: inline-flex; align-items: center; gap: 6px;">
    ▶ Run Python Code in WASM
  </button>

  <pre style="margin-top: 15px; padding: 16px; background: #05080E; color: #10B981; border-radius: 8px; min-height: 110px; font-family: var(--md-code-font); font-size: 13.5px; line-height: 1.5; border: 1px solid rgba(255, 255, 255, 0.08); overflow-x: auto;"><code id="output">Output will appear here upon execution...</code></pre>
</div>

<script>
  const codePresets = {
    euphony: `# Use Case 1: Phonetic Euphony & Harmonic Flow Scoring
import math

def calculate_euphony(name):
    """Computes sound symbolism, plosive dampening, and sonorant resonance."""
    name_lower = name.lower()
    plosives = sum(1 for c in name_lower if c in 'ptkbdg')
    sonorants = sum(1 for c in name_lower if c in 'lmnr')
    vowels = sum(1 for c in name_lower if c in 'aeiou')
    
    score = 50 + (sonorants * 12) + (vowels * 6) - (plosives * 4)
    return max(0, min(100, score))

candidates = ["Vanta", "Aero", "Cortex", "Nexus", "Krypton", "Zylo", "Lumene"]

print("=" * 45)
print(f"{'BRAND NAME':<14} {'EUPHONY SCORE':<16} {'QUALITIES':<15}")
print("=" * 45)

for brand in candidates:
    score = calculate_euphony(brand)
    quality = "🌟 Premium" if score >= 75 else "👍 Balanced" if score >= 60 else "⚠️ Plosive"
    print(f"{brand:<14} {score:<16.1f} {quality:<15}")

print("=" * 45)`,

    security: `# Use Case 2: Sub-35ms Security & Typosquatting Risk Audit
def damerau_levenshtein(s1, s2):
    """Calculates edit distance to detect package typosquatting risks."""
    d = {}
    len1, len2 = len(s1), len(s2)
    for i in range(-1, len1 + 1): d[(i, -1)] = i + 1
    for j in range(-1, len2 + 1): d[(-1, j)] = j + 1
    for i in range(len1):
        for j in range(len2):
            cost = 0 if s1[i] == s2[j] else 1
            d[(i, j)] = min(d[(i-1, j)] + 1, d[(i, j-1)] + 1, d[(i-1, j-1)] + cost)
            if i > 0 and j > 0 and s1[i] == s2[j-1] and s1[i-1] == s2[j]:
                d[(i, j)] = min(d[(i, j)], d[(i-2, j-2)] + 1)
    return d[(len1 - 1, len2 - 1)]

target_candidate = "vanta"
existing_registry = ["vanta", "vanta-cli", "vantaa", "vantajs", "banta", "vanta-app"]

print(f"Auditing Candidate Target: '{target_candidate}' against Package Registry")
print("-" * 55)
for pkg in existing_registry:
    dist = damerau_levenshtein(target_candidate, pkg)
    risk = "🚨 HIGH TYPOSQUAT RISK" if dist <= 1 else ("⚠️ MEDIUM SIMILARITY" if dist == 2 else "✅ SAFE")
    print(f"Registry Package: {pkg:<14} Edit Distance: {dist:<4} Risk: {risk}")
print("-" * 55)`,

    bouma: `# Use Case 3: Visual Geometry & Bouma Silhouette Ratio
def calculate_bouma_metrics(name):
    """Calculates height symmetry (ascenders, descenders, midlines)."""
    ascenders = set("bdfhklt")
    descenders = set("gjpqy")
    midlines = set("acemnorsuvwxz")

    h_asc = sum(1 for c in name if c in ascenders)
    h_desc = sum(1 for c in name if c in descenders)
    h_mid = sum(1 for c in name if c in midlines)
    total = len(name)

    midline_ratio = round(h_mid / total, 2) if total else 0
    symmetry_score = 100 - (abs(h_asc - h_desc) * 15)
    return midline_ratio, symmetry_score

candidates = ["nexus", "vanta", "aero", "cortex", "krypton"]
print(f"{'BRAND NAME':<12} {'MIDLINE RATIO':<15} {'VISUAL SYMMETRY':<18}")
print("-" * 48)
for brand in candidates:
    mid, sym = calculate_bouma_metrics(brand)
    print(f"{brand:<12} {mid:<15.2f} {sym:<18.1f}")
print("-" * 48)`,

    nakshatra: `# Use Case 4: 108 Nakshatra Pada Vibrational Alignment
NAKSHATRA_PADAS = {
    "va": ("Rohini", 1, "Taurus"),
    "vi": ("Rohini", 2, "Taurus"),
    "vu": ("Rohini", 3, "Taurus"),
    "ve": ("Rohini", 4, "Taurus"),
    "vo": ("Mrigashira", 1, "Gemini"),
    "ka": ("Mrigashira", 2, "Gemini"),
    "ki": ("Mrigashira", 3, "Gemini"),
    "ku": ("Mrigashira", 4, "Gemini"),
}

candidates = ["Vanta", "Vespera", "Krypton", "KubeGuard"]

print(f"{'BRAND NAME':<12} {'INITIAL PHONEME':<16} {'NAKSHATRA':<14} {'ZODIAC':<10}")
print("-" * 55)
for name in candidates:
    phoneme = name[:2].lower()
    info = NAKSHATRA_PADAS.get(phoneme, ("Ashwini", 1, "Aries"))
    print(f"{name:<12} {phoneme:<16} {info[0] + ' P' + str(info[1]):<14} {info[2]:<10}")
print("-" * 55)`
  };

  document.querySelectorAll('.preset-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      const type = btn.getAttribute('data-preset');
      if (codePresets[type]) {
        document.getElementById('python-code').value = codePresets[type];
      }
    });
  });

  function loadPyodideScript(callback) {
    if (window.loadPyodide) {
      callback();
      return;
    }
    let script = document.createElement('script');
    script.src = "https://cdn.jsdelivr.net/pyodide/v0.26.1/full/pyodide.js";
    script.onload = callback;
    script.onerror = function() {
      document.getElementById('pyodide-loading').innerText = '❌ Failed to load Pyodide CDN.';
    };
    document.head.appendChild(script);
  }

  loadPyodideScript(async function() {
    try {
      let pyodide = await loadPyodide();
      document.getElementById('pyodide-loading').style.display = 'none';
      document.getElementById('output').innerText = 'Pyodide WASM Engine Ready! Click "▶ Run Python Code in WASM".';

      document.getElementById('run-btn').addEventListener('click', async () => {
        let code = document.getElementById('python-code').value;
        try {
          let outputBuffer = "";
          pyodide.setStdout({
            batched: (text) => {
              outputBuffer += text + "\n";
              document.getElementById('output').innerText = outputBuffer;
            }
          });
          document.getElementById('output').innerText = "⚡ Executing in WASM runtime...";
          await pyodide.runPythonAsync(code);
        } catch (err) {
          document.getElementById('output').innerText = err;
        }
      });
    } catch (err) {
      document.getElementById('pyodide-loading').innerText = '❌ Pyodide initialization error: ' + err;
    }
  });
</script>
