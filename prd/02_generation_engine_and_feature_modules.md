## **4. Generation Engine Architecture**

Brando's name generation is structured as three independent layers. **Layer 1 (Core Phoneme Synthesis) always runs** — it requires no external vocabulary and produces pronounceable, constraint-compliant candidates from structural phoneme templates. **Layer 2 (Vocabulary Enrichment)** is opt-in and supplements the core pool with semantically flavored candidates. **Layer 3 (Filtration + Scoring)** refines any pool regardless of how it was generated.

### **Why Phoneme Synthesis as Core?**

Pure random character generation (`a-z + 0-9`) at length 5 produces 60 million combinations, of which less than 0.03% are usable brand names — a 99.97% waste rate that makes storage, scoring, and filtering impractical. Phoneme synthesis inverts this: it generates only structurally pronounceable names, achieving ~90% signal quality before any filtering is applied.

| Approach | Pool Size (len=5) | Pronounceable | Signal Quality |
| :--- | :--- | :--- | :--- |
| Pure random (a-z+0-9) | 60,466,176 | ~3,000,000 | **~0.03%** |
| Phoneme synthesis (CVCV) | ~10,000 | ~9,500 | **~90%** |

```
┌──────────────────────────────────────────────────────────────────────┐
│           LAYER 1: Core Phoneme Synthesis Engine (always runs)       │
│  Constrained CVC / CVCV / VCVC / CVCVC pattern synthesis             │
│  Inputs: naming_context + registry + industry_context                │
│          + generation_alignment + length & syllable limits           │
│  Zero additional config needed — works out of the box                │
└───────────────────────────────┬──────────────────────────────────────┘
                                │ raw candidate pool
           ┌──────────────┤├──────────────┐
           │              │              │
     neoclassical   portmanteau    metaphorical   ← LAYER 2: Vocabulary Enrichment
     (root seeds)   (word blend)   (word bank)      (opt-in strategies)
           │              │              │
           └──────────────┤├──────────────┘
                                │ enriched pool
┌───────────────────────────────▼──────────────────────────────────────┐
│         LAYER 3: Filtration + Scoring + Verification                 │
│  Visual / Phonetic / Industry Fit / Esoteric / DNS / Trademark       │
└───────────────────────────────┬──────────────────────────────────────┘
                                │
                         shortlist.csv → verify
```

---

### **Layer 1: Core Phoneme Synthesis Engine** ✅ Always Active

The core engine generates candidate names by filling structural templates (`C` = consonant, `V` = vowel) from configurable phoneme pools. It fires on every `brando build` run, with or without any enrichment strategies enabled.

#### **Default Selection Rationale & Brand Evidence**

**Generation is maximally permissive. Quality judgment belongs entirely to the filter layer.**

All previous rationale for excluding consonants at the generation stage has been invalidated through iteration against real brand evidence. Every consonant appears in globally iconic brands:

```
Generation Layer:  produce ALL possible candidates from ALL consonants
                   ↓ store every candidate with full individual metric columns
Filter Layer:      user queries individual metrics to find names that match
                   their specific use case, aesthetic, and audience
```

| Previously Excluded | Wrong Reason | Brands That Disprove It |
| :--- | :--- | :--- |
| `b, d, g` | "Voiced plosives sound aggressive" | **Boat**, **Beats**, **Google**, **GitHub**, **Duracell** |
| `p` | "Aspirated, varies across languages" | **Pantaloons**, **Pinterest**, **Puma**, **PayPal**, **Pixar** |
| `k, f` | "Extended pool only" | **Kodak**, **Kindle**, **Fitbit**, **FedEx**, **Flipkart** |
| `h` | "Silent in French/Spanish" | **Honda**, **Heineken**, **Hershey's**, **H&M**, **Hyundai** |
| `j` | "Sounds different per language" | **JBL**, **Jockey**, **Jaguar**, **Jeep**, **Jabra** |
| `w` | "Inconsistent across languages" | **Walmart**, **WhatsApp**, **Wikipedia** |
| `y` | "Vowel-consonant hybrid" | **Yamaha**, **Yeti**, **YouTube**, **Yahoo** |
| `c` | "Hard/soft ambiguous" | **Coca-Cola**, **Canon**, **Chanel**, **Casio** |
| `q` | "Always needs u after it" | **Quiksilver**, **Quaker**, **Quiznos**, **Qualcomm** |
| `x` | "Position-dependent sound" | **Xerox**, **Xfinity**, **Xbox**, **XOXO** |

**Default pool: all 21 consonants** (`b c d f g h j k l m n p q r s t v w x y z`)

**Configurable `q` $\rightarrow$ `qu` Bigram Toggle (`auto_qu_bigram: true / false`)**:
By default (`auto_qu_bigram: true`), the generator converts raw `q` to `qu` (`quavo`, `quera`, `quilo`), preventing unreadable strings (`qalo`, `qeva`) in standard brand runs. If the user wants raw, unconstrained `q` in `C` slots (e.g. *Qvla*, *Qaro*, *Qraft* for Gen-Z, gaming, or crypto brands), setting `auto_qu_bigram: false` in `config.yaml` or passing `--no-qu-bigram` on CLI grants complete freedom.

---

##### **Default Vowel Pool — `[a, e, i, o, u]`**

All five base vowels are included. This is the only sensible complete set — vowels are the backbone of every phoneme pattern and restricting them at the default level would produce unbalanced or unpronounceable output. What matters is not *which* vowels but their *position* in the pattern template.

Vowel sound symbolism is used at the **filter layer** (via `--vowel-pitch` targeting front/back/central classes), not at the generation layer.

---

##### **Dual Pattern Generation Modes — Dynamic vs. Explicit Templates**

Rather than locking users into static hardcoded templates, Brando provides two pattern generation modes:

```
                                [ Pattern Selection ]
                                          │
                  ┌───────────────────────┴───────────────────────┐
                  ▼                                               ▼
     Mode A: Dynamic Rule-Based                     Mode B: Explicit Custom Templates
     (phoneme_patterns: null)                       (phoneme_patterns: [CVC, CVCV, ...])
     - Dynamic synthesis up to max_segment_letters  - Strict adherence to user-defined
     - Enforces max_consonant_clusters: 0           - Enables structural overrides (e.g. CCVCV)
```

| Mode | Trigger (`config.yaml`) | CLI Parameter | Behavior |
| :--- | :--- | :--- | :--- |
| **Mode A: Dynamic Rule-Based (Default)** | `phoneme_patterns: null` | Default | Dynamically synthesizes ALL valid structural sequences — both **Consonant-Initial** (`CVC`, `CVCV`, `CVCVC`...) AND **Vowel-Initial** (`VCV`, `VCVC`, `VCVCV`, `VCVCVC`...) — up to `max_segment_letters` while enforcing `max_consonant_clusters: 0` (strictly alternating C & V). Zero hardcoding. |
| **Mode B: Explicit Custom List** | `phoneme_patterns: [...]` | `--patterns "CVCV CVVC VCVC"` | Restricts synthesis strictly to the structural sequence templates explicitly listed by the user. Allows opt-in consonant clusters (`CCVCV`, `CVC-CVC`). |

**Common Structural Patterns Reference:**

| Pattern | Initial | Length | Basis / Use Case | Famous Brand Examples |
| :--- | :--- | :--- | :--- | :--- |
| `CVC` | Consonant | 3 chars | Minimum viable brand syllable; segment building block | *Nal*, *Vor*, *Lex* |
| `CVCV` | Consonant | 4 chars | **Primary sweet spot** — 4-letter alternating structure | *Lego*, *Roku*, *Figma*, *Kinet* |
| `VCVC` | Vowel | 4 chars | **Vowel-Initial sweet spot** — high-tech / digital feel | *Uber*, *Etsy*, *Intel*, *Onyx* |
| `CVVC` | Consonant | 4 chars | Diphthong feel for variety without consonant clusters | *Naol*, *Veir*, *Loun* |
| `CVCVC` | Consonant | 5 chars | Extends naturally to 5-char names | *Kodak*, *Xerox*, *Vesal* |
| `VCVCV` | Vowel | 5 chars | Vowel-Initial 5-char melodic structure | *Evolu*, *Oruka*, *Avoni* |
| `CVCVCV` | Consonant | 6 chars | Medium single word | *Spotify*, *Figma* class (*Nalovsa*, *Versali*) |
| `VCVCVC` | Vowel | 6 chars | Vowel-Initial medium single word | *Amazon*, *Oculus*, *Eviter* |
| `CVCVCVC` | Consonant | 7 chars | Long single word (*Dropbox*, *Mailchimp* class) | *Nalovert*, *Versalin* |
| `CVCVCVCV` | Consonant | 8 chars | Max single-word brand length | *Salesforce*, *Accenture* class (*Nalovelsa*) |

**Core design rule — No Consonant Clusters (CC):**
In Dynamic Mode (Mode A), every pattern guarantees a vowel between every pair of consonants (`max_consonant_clusters: 0`). Adjacent consonants (`CC`) are the #1 cause of mispronunciation across world languages. Opt-in patterns with CC clusters (`CVCCV`, `CCVCV`) can be passed via Mode B explicit template lists.

---

##### **Naming Length Modes — Single Word vs Compound vs Separated**

The phoneme engine uses `max_segments` and `segment_separator` to cover all name length scenarios without breaking the no-CC-cluster rule:

| Mode | `max_segments` | `segment_separator` | `max_segment_letters` | Example Output | Max Total Length |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Single invented word** | `1` | `null` | 5–8 | *Nova*, *Kinet*, *Valor* | 8 chars |
| **Long single word** | `1` | `null` | 8–12 | *Accentura*, *Salesvora* | 12 chars |
| **2-block compound** (fused) | `2` | `null` | 4–6 | *Novalink*, *Kinetflux* | 10–12 chars |
| **3-block compound** (fused) | `3` | `null` | 3–5 | *Novalinktel*, *BookMyShow style* | 12–15 chars |
| **Hyphenated 2-segment** | `2` | `"-"` | 4–6 | *nova-link*, *kinet-sys* | 9–13 chars |
| **Hyphenated 3-segment** | `3` | `"-"` | 3–6 | *nova-link-tech* | 11–20 chars |
| **Dotted 2-segment** | `2` | `"."` | 4–8 | *Nova.Search*, *Intel.AI* | 9–17 chars |
| **Snake 2-segment** | `2` | `"_"` | 4–6 | *kinet\_sys*, *nova\_flux* | 9–13 chars |

**Total length formula:**
```
final_length = (segment_length × max_segments) + (separator_length × (max_segments − 1))

Examples:
  max_segments=2, max_segment_letters=5, separator=null  → max 10 chars  ("Novalink")
  max_segments=2, max_segment_letters=5, separator="-"   → max 11 chars  ("Nova-link")
  max_segments=3, max_segment_letters=4, separator=null  → max 12 chars  ("Novalikte")
  max_segments=3, max_segment_letters=5, separator="-"   → max 17 chars  ("Nova-link-tech")
```

**Real brand examples mapped to modes:**

| Real Name | Chars | Mode | Segments | Separator |
| :--- | :--- | :--- | :--- | :--- |
| Lego, Roku | 4 | Single word | 1 | null |
| Kodak, Xerox, Figma | 5–5 | Single word | 1 | null |
| Spotify, Dropbox | 7–8 | Single word | 1 | null |
| Accenture, Salesforce | 9–10 | Long single word | 1 | null |
| Instagram, Snapchat | 9–8 | 2-block compound | 2 | null |
| YouTube, WhatsApp | 7–8 | 2-block compound | 2 | null |
| BookMyShow, MakeMyTrip | 10 | 3-block compound | 3 | null |
| ARMemberPlugin | 14 | 3-block compound | 3 | null |
| nova-link, kinet-sys | 9 | 2-segment hyphenated | 2 | `"-"` |
| neural-search-kit | 16 | 3-segment hyphenated | 3 | `"-"` |
| Nova.Search | 11 | 2-segment dotted | 2 | `"."` |

---

### **Layer 1a: Naming Context + Registry + Industry Context Preset System** ✅ Core Feature

Brando uses a **three-dimension preset system** to automatically resolve generation constraints, legal targets, and verification rules for any naming use case without requiring manual configuration.

- **`naming_context`** — the high-level intent (*what you are naming*: `company`, `product`, `startup`, `software`, `package`, `module`, `repo`, `custom`)
- **`registry`** — the specific ecosystem (*where it will live*: `npm`, `pypi`, `go`, `crates`, `rubygems`, `packagist`, `nuget`, `maven`, `docker`, `homebrew`, `apt`, `github`, `swift`)
- **`industry_context`** — the target commercial sector or hybrid combination (*what industry it serves*: `tech`, `fashion`, `food`, `pharma`, `fintech`, `cosmetics`, `entertainment`, `real_estate`, `custom`, or multi-sector `[finance, tech]`)

Together they resolve the exact character set, length range, case convention, separator rules, target Nice Classes, domain TLD clusters, and registry-specific format validators used across both the **Core Generator** and the **Technical Modules** (Section 6).

#### **Level 1: Context Presets** (What You're Naming)

| `naming_context` | Default Chars | Length | Case | Separator | Pairs With Registry? |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `company` | `a-z` | 4–12 | Title case | None | No — trademark/domain rules |
| `product` | `a-z` | 4–9 | Title case | None | No — consumer brand rules |
| `startup` | `a-z` | 4–8 | Title case | None | No — domain-friendly |
| `software` | `a-z 0-9` | 4–15 | PascalCase | Optional | Yes — pair with registry |
| `package` | `a-z 0-9 -` | 3–214 | lowercase | hyphens | Yes — pair with registry |
| `module` | `a-z 0-9 _` | 3–40 | lowercase | underscores | Yes — pair with registry |
| `repo` | `a-z 0-9 -` | 3–100 | lowercase | hyphens | Yes — pair with registry |
| `custom` | User-defined | — | — | — | No — set raw constraints |

#### **Level 2: Registry Presets** (Where It Lives)

| `registry` | Pairs With | Allowed Chars | Max Len | Case | Separator | Special Rules |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `npm` | `package` | `a-z 0-9 - _` | 214 | lowercase | `-` | No leading `.` or `_`; scoped `@scope/name` allowed |
| `pypi` | `package`, `module` | `a-z A-Z 0-9 - _ .` | 128 | normalized | `-` ≡ `_` ≡ `.` | Case-insensitive; hyphens/underscores/dots normalized |
| `go` | `module` | `a-z 0-9 /` | short | lowercase | none | No underscores in pkg name; module path = `domain/path` |
| `crates` | `package` | `a-z 0-9 - _` | 64 | lowercase | `-` / `_` | Must start with letter; no consecutive `--` or `__` |
| `rubygems` | `package` | `a-z 0-9 - _` | 128 | lowercase | `-` / `_` | Hyphens = namespace; underscores = word separator |
| `packagist` | `package` | `a-z 0-9 - _ .` | 128 | lowercase | `-` | Format: `vendor/package` required |
| `nuget` | `software`, `package` | `a-z A-Z 0-9 - .` | 100 | PascalCase | `.` | Dot-namespaced `Company.Product.Module`; no spaces |
| `maven` | `software`, `package` | `a-z 0-9 - _` | varies | lowercase | `-` | `groupId` = reverse domain; `artifactId` = lowercase-hyphenated |
| `docker` | `software`, `package` | `a-z 0-9 - _` | 128 | lowercase | `-` / `_` | No consecutive `--`; no uppercase |
| `homebrew` | `package` | `a-z 0-9 -` | 64 | lowercase | `-` | No underscores; hyphens only |
| `apt` | `package`, `repo` | `a-z 0-9 + - . ~` | 64 | lowercase | `-` | Hyphens only; no underscores |
| `github` | `repo` | `a-z A-Z 0-9 - _` | 100 | any | `-` / `_` | URL-safe; spaces not allowed |
| `swift` | `package`, `module` | `a-z A-Z 0-9 - _` | 64 | CamelCase | `-` / `_` | Module `import` name uses CamelCase without separators |

#### **Level 3: Industry Context Presets** (What Industry It Serves)

When an `industry_context` is specified, it configures target Nice Classes, primary TLDs, and network channels without deleting candidate names during generation (maximally permissive strategy):

| `industry_context` | Target Nice Classes | Primary TLD Cluster | Key Social Channels |
| :--- | :--- | :--- | :--- |
| `tech` (default) | **Class 9, 35, 42** | `.ai`, `.io`, `.dev`, `.com` | GitHub, Twitter |
| `fashion` | **Class 25, 35** | `.shop`, `.store`, `.co`, `.com` | Instagram, TikTok, Pinterest |
| `food` | **Class 29, 30, 32, 35** | `.shop`, `.store`, `.co`, `.com` | Instagram, Facebook |
| `pharma` | **Class 5, 10, 44** | `.health`, `.care`, `.com` | LinkedIn, Twitter |
| `fintech` | **Class 9, 36, 42** | `.bank`, `.pay`, `.co`, `.com` | Twitter, LinkedIn |
| `cosmetics` | **Class 3, 35** | `.beauty`, `.shop`, `.com` | Instagram, TikTok |
| `entertainment` | **Class 9, 41** | `.media`, `.game`, `.tv`, `.com` | YouTube, Twitch, Twitter |
| `real_estate` | **Class 36, 37** | `.estate`, `.property`, `.com` | LinkedIn, Instagram |
| `custom` | Defined in config | User-specified | User-specified |

---

### **Layer 2: Vocabulary Enrichment Strategies** (Opt-In & Industry-Automated)

These strategies supplement the phoneme core pool with semantically flavored candidates. They are activated by populating their block in the `enrichment:` config section, setting `auto_industry_roots: true`, or via `--strategy` CLI flags. **The core phoneme engine always runs first; enrichment strategies add to the pool, never replace it.**

#### **Vocabulary Data Architecture: Bundled Assets, Build Pipeline & Custom Extension Surface**

To ensure zero-config usability out of the box while supporting arbitrary enterprise vocabulary extensions, Brando divides strategy datasets into two tiers:

1. **Automated Developer Data Prep Pipeline (`scripts/data_prep/`)**:
   - **Harvesting Open Data**: Ingests public domain / permissive open datasets (Princeton WordNet 3.0, Moby Thesaurus, Wiktionary Etymology Gazette, Tranco Top 1M Domains, USPTO Gazette).
   - **Automated Curation Scripts**: Python data-prep scripts (`scripts/data_prep/*.py`) clean profanity, strip diacritics, categorize by theme, and annotate phoneme structures automatically.
   - **Gzip Binary Compression**: All JSON and text dictionaries inside `brando/data/vocabularies/` are stored as compressed binary assets (`.json.gz`). Achieves a 10:1 compression ratio, maintaining total package size at **< 1.8 MB compressed**.
   - **Lazy In-Memory Loading**: Dictionaries are loaded decompressed into RAM in **< 10ms ONLY when their specific strategy is invoked**. Zero memory overhead on default phoneme runs.

2. **Bundled Asset Datasets (`brando/data/vocabularies/`)**:
   - `classical_morphemes.json.gz`: ~2,500 Latin/Greek root morphemes categorized by etymology and meaning.
   - `industry_keywords.json.gz`: ~10,000 technology, commercial, and domain nouns/verbs.
   - `brand_suffixes.json`: ~50 modern brand suffixes (`-ify`, `-ly`, `-io`, `-ex`, `-is`, `-a`, `-verse`, `-pay`, `-fi`).
   - `english_nouns.txt.gz`: ~25,000 concrete and abstract nouns categorized by theme (`space`, `nature`, `security`).
   - `thesaurus_graph.json.gz`: ~50,000 word-similarity edges built from WordNet.

3. **Custom User Extension Surface (`config.yaml`)**:
   - Every strategy supports custom overrides or additions (`custom_prefixes`, `custom_suffixes`, `custom_brand_suffixes`, `custom_word_bank_path`, `custom_rules`, `custom_substitution_map`). User-supplied custom items are appended to bundled datasets without losing zero-config defaults.

#### **Industry Context Root Automation (`auto_industry_roots: true`)**

When `auto_industry_roots: true` (default in `config.yaml`), Brando automatically resolves default enrichment strategies, root morpheme vocabularies, seed words, and modern brand suffixes directly from the selected `industry_context`:

| `industry_context` | Automatic Default Enrichment Strategies | Bundled Root Morphemes & Seed Words | Target Modern Brand Suffixes |
| :--- | :--- | :--- | :--- |
| `tech` (default) | `[neoclassical, portmanteau, analogous_suffix]` | `sys, flux, net, data, byte, sync, logic, pulse, node` | `-ify, -io, -ly, -ex, -a` |
| `fashion` | `[suggestive, metaphorical, neoclassical]` | `maison, noir, silk, vogue, atelier, luxe, couture, aura` | `-is, -ia, -a, -o` |
| `food` | `[compound, suggestive, portmanteau]` | `snack, bite, craft, farm, fresh, brew, taste, harvest` | `-ly, -o, -up` |
| `pharma` | `[neoclassical, truncation]` | `vita, cura, vax, bio, med, gen, san, thera, rx` | `-is, -ex, -a, -us` |
| `fintech` | `[portmanteau, compound, neoclassical]` | `pay, coin, bank, vault, cash, capital, trust, ledger` | `-fi, -pay, -ex, -io` |
| `cosmetics` | `[analogous_suffix, suggestive, neoclassical]` | `luxe, glow, derma, botanica, pure, silk, aura, flora` | `-ify, -a, -ia, -is` |
| `entertainment` | `[suggestive, portmanteau, compound]` | `play, stream, pulse, game, spark, quest, wave, toon` | `-io, -ify, -verse` |
| `real_estate` | `[compound, neoclassical]` | `estate, prop, haven, terra, domain, stone, acre, vault` | `-is, -ia, -ex` |
| `custom` | Defined by user in `config.yaml` | User-defined root lists | User-defined suffixes |

---

#### **Strategy: `neoclassical`** ✅ Implemented
*   **What it is**: Constructs names from Latin and Greek morpheme roots — the naming convention of pharmaceutical, biotech, and enterprise brands.
*   **How it works**: Combines entries from `prefixes` and `suffixes` config lists, where the lists themselves act as etymology morpheme vocabularies. Generates a direct blend (`prefix + suffix`) and optionally a boundary-merged form when the last character of the prefix matches the first character of the suffix.
*   **Trademark advantage**: High — invented words are the easiest to protect and have the broadest scope.
*   **Required config**: `prefixes`, `suffixes` lists (classical root segments such as `nova`, `apex`, `sys`, `flux`).
*   **Examples output**: *Novatech*, *Apexflux*, *Kinetlink*.
*   **Famous real names**: *Novartis* (novae artes), *Altria* (altus), *Sonos* (sonus).

#### **Strategy: `portmanteau`** ✅ Implemented
*   **What it is**: Fuses two complete words together, typically blending the beginning of one with the end of another to create a compound neologism.
*   **How it works**: Shares the same prefix+suffix cross-product path as `neoclassical`. The boundary-merge algorithm (`pref[-1] == suff[0]`) drops the duplicate letter at the join point.
*   **Trademark advantage**: Medium-High — still novel but hints at source words.
*   **Required config**: `prefixes`, `suffixes` lists (real English or domain words).
*   **Examples output**: *Stormlink*, *Forgecraft*, *Aerosys*.
*   **Famous real names**: *Microsoft* (microcomputer + software), *Pinterest* (pin + interest), *FedEx* (Federal + Express).

#### **Strategy: `analogous_suffix`** 🔮 Phase 2 (The Brand Suffix Blender)
*   **What it is**: Blends base root words or phoneme stems with iconic modern tech/consumer brand suffixes (`-ify`, `-ly`, `-io`, `-ex`, `-is`, `-a`).
*   **How it works**: Takes root words or Layer 1 candidate stems and appends entries from `brand_suffixes` list (`[ify, ly, io, ex, is, a]`), applying boundary smoothing (e.g. `shop + ify` $\rightarrow$ *Shopify*, `spot + ify` $\rightarrow$ *Spotify*, `bit + ly` $\rightarrow$ *Bitly*).
*   **Trademark advantage**: Medium-High — creates familiar, memorable SaaS and consumer brand forms.
*   **Required config**: `brand_suffixes` list (e.g. `[ify, ly, io, ex, is, a]`).
*   **Examples output**: *Glowify*, *Kinetio*, *Vaultly*, *Solana*.
*   **Famous real names**: *Shopify*, *Spotify*, *Bitly*, *Solana*, *Grammarly*.

#### **Strategy: `phoneme_pattern`** ✅ Implemented (as fallback)
*   **What it is**: Synthesizes abstract names from configurable phoneme-pattern templates (e.g. CVC, CVVC), producing completely invented words with no dictionary root meaning.
*   **How it works**: Iterates through `phoneme_patterns` templates, filling each `C` slot from `phoneme_consonants` and each `V` slot from `phoneme_vowels` to generate all valid permutations within length and syllable constraints.
*   **Trademark advantage**: Maximum — invented words are blank canvases with no semantic baggage.
*   **Required config**: `phoneme_patterns`, `phoneme_consonants`, `phoneme_vowels`.
*   **Examples output**: *Valor*, *Omenix*, *Setara*.
*   **Famous real names**: *Kodak*, *Xerox*, *Rolex*, *Google*.

#### **Strategy: `metaphorical`** 🔮 Phase 2
*   **What it is**: Selects real dictionary words used completely out of context to create brand associations through abstraction.
*   **How it works**: Seeds the candidate pool from a curated word bank (`.txt` file or theme-filtered vocabulary) of concrete and abstract nouns. Filters output by length, syllable, and linguistic constraints.
*   **Trademark advantage**: Low — generic real words are hard to trademark; requires acquired distinctiveness.
*   **Required config**: `word_bank_path` (path to line-separated word list) or `word_bank_themes`.
*   **Examples output**: *Horizon*, *Summit*, *Ember*.
*   **Famous real names**: *Apple*, *Slack*, *Amazon*, *Oracle*, *Quartz*.

#### **Strategy: `compound`** 🔮 Phase 2
*   **What it is**: Directly concatenates two full dictionary words without morpheme clipping.
*   **How it works**: Cross-product of a `word_bank_path` or inline word list with itself or a second list; applies length/syllable filters.
*   **Trademark advantage**: Low-Medium — compound real words are generally difficult to trademark unless the pairing is distinctive.
*   **Required config**: `word_bank_path` or inline lists.
*   **Examples output**: *Fireforge*, *Cloudstep*, *Ironvault*.
*   **Famous real names**: *Facebook*, *ThinkPad*, *WordPress*, *Snapchat*.

#### **Strategy: `truncation`** 🔮 Phase 2
*   **What it is**: Derives brand names by clipping longer seed words to their most melodic or memorable syllable prefix.
*   **How it works**: Applies syllable splitting to each entry in `truncation_seeds`, retaining the first N syllables defined by `truncation_depth`, then applies standard filters.
*   **Trademark advantage**: Medium — clipped forms can still conflict with the original if famous.
*   **Required config**: `truncation_seeds` (long words), `truncation_depth` (syllable count to retain).
*   **Examples output**: From *Aerospace* → *Aero*; from *Integral* → *Intel*.
*   **Famous real names**: *Intel* (Integrated Electronics), *FedEx*, *Dunkin'*.

#### **Strategy: `acronym`** 🔮 Phase 2
*   **What it is**: Compresses a multi-word descriptive phrase into its initial letters, forming a pronounceable word or initialism.
*   **How it works**: Extracts the first letter of each word in `acronym_phrases`. Validates that the result is pronounceable (vowel-containing) and passes length constraints.
*   **Trademark advantage**: Low for obscure acronyms; medium-high if the result is pronounceable and coined-feeling.
*   **Required config**: `acronym_phrases` (list of source phrases).
*   **Examples output**: From *Advanced Logic Research* → *ALR*; from *Vertex Intelligence Systems* → *VIS*.
*   **Famous real names**: *IBM*, *GEICO*, *ESPN*, *NASA*.

#### **Strategy: `suggestive`** 🔮 Phase 2
*   **What it is**: Generates names that hint at a brand's benefit or quality through thesaurus-proximity associations rather than stating it directly.
*   **How it works**: Uses a configurable concept seed (e.g., `speed`, `intelligence`) and queries a local thesaurus or synonym graph to surface adjacent concept words, then applies filters.
*   **Trademark advantage**: Medium — distinctive suggestive names are protectable but the closer to descriptive the weaker the claim.
*   **Required config**: `word_bank_themes` or `concept_seeds`.
*   **Examples output**: *Velocity* (from speed), *Luminary* (from intelligence).
*   **Famous real names**: *Shopify*, *Swiffer*, *Fitbit*, *Uber*.

---

### **Layer 2a: Orthographic Modification Passes** (Post-Processing Stage)

These post-processing passes execute **AFTER** the base candidate pool has been generated by Layer 1 (Phoneme Engine) and Layer 2 (Vocabulary Enrichment). They take existing candidates as input and generate orthographically transformed variants, writing **BOTH** the original base candidate and the transformed variant into `brand_candidates.csv`.

```
┌────────────────────────────────────────────────────────────────────────┐
│  Layer 1 (Phoneme Core) + Layer 2 (Vocabulary Enrichment) Candidate Pool│
│  Base Candidates: ["Flicker", "Tumbler", "Lift", "Symbol", "Nexus"]    │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │ Input Pool
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│             LAYER 2a: Post-Pass Transformation Engine                  │
│  Config: enrichment.post_passes: [phonetic_spell, letter_sub, ...]     │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │ Transformed Variants
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│   Final Pool: ["Flicker", "Flickr", "Tumbler", "Tumblr", "Lift",       │
│               "Lyft", "Symbol", "Zymbol", "Nexus-21"]                   │
└────────────────────────────────────────────────────────────────────────┘
```

#### **Industry Context Post-Pass Automation (`auto_industry_roots: true`)**
When `auto_industry_roots: true`, `industry_context` automatically enables and configures sensible post-pass defaults:
*   `tech` → Enables `phonetic_spell` (`drop_final_vowel: true`, `i_to_y: true` → *Flickr*, *Lyft*) and `alphanumeric` (`allowed_numerals: [21, 42, 360, 247]`).
*   `fashion` / `cosmetics` → Enables `phonetic_spell` (`i_to_y: true` → *Vybe*, *Luxe*).
*   `entertainment` / `gaming` → Enables `phonetic_spell` (`z_for_s: true` → *Boyz*, *Gamez*, `c_to_k: true` → *Kombat*).
*   `pharma` → Enables `phonetic_spell` (`c_to_k: true` → *Kinetix*, `f_to_ph: true` → *Pharma*).

---

#### **Strategy: `phonetic_spell`** 🔮 Post-Pass (Phonetic Respeller)
*   **What it is**: Respells a candidate using phonetic equivalents to create a unique, trademarkable visual form that sounds identical or near-identical when spoken.
*   **How it works**: Evaluates candidate strings against configurable boolean rules under `enrichment.post_pass_settings.phonetic_spell`:
    - `drop_final_vowel: true`: Truncates unaccented trailing `-er` / `-el` vowels (*Flicker* → *Flickr*, *Tumbler* → *Tumblr*).
    - `i_to_y: true`: Replaces vocalic `i` with `y` (*Lift* → *Lyft*, *Vibe* → *Vybe*).
    - `c_to_k: true`: Converts hard `c` to `k` (*Crispy* → *Krispy*, *Quick* → *Kwik*).
    - `f_to_ph: true`: Converts `f` to `ph` (*Fast* → *Phast*).
    - `z_for_s: true`: Replaces trailing plural `s` with `z` (*Boys* → *Boyz*).
*   **Trademark advantage**: High — the novel spelling is legally distinct even if phonetically similar to a common word.
*   **Required config**: `post_passes: [phonetic_spell]`, `post_pass_settings.phonetic_spell` rules map.
*   **Examples output**: *Flickr*, *Tumblr*, *Lyft*, *Krispy Kreme*, *Vyber*, *Stryke*.
*   **Famous real names**: *Flickr*, *Tumblr*, *Lyft*, *Krispy Kreme*, *Reebok*.

#### **Strategy: `letter_sub`** 🔮 Post-Pass (Character Swap)
*   **What it is**: Swaps one or more characters in a base candidate using a key-value mapping table to alter visual identity and typographic aesthetics.
*   **How it works**: Iterates through `enrichment.post_pass_settings.letter_sub.substitution_map` and applies key-to-value replacements across the candidate string (e.g. `i: y`, `o: oo`, `s: z`, `x: ks`).
*   **Trademark advantage**: High — modified spellings are broadly easier to register as unique marks.
*   **Required config**: `post_passes: [letter_sub]`, `post_pass_settings.letter_sub.substitution_map`.
*   **Examples output**: *Zappos* (from zapatos), *Froot* (from fruit), *Zymbol* (from symbol), *Pixar* (from picsar).
*   **Famous real names**: *Zappos*, *Froot Loops*, *Krispy Kreme*, *Pixar*.

#### **Strategy: `alphanumeric`** 🔮 Post-Pass (Numeral Append)
*   **What it is**: Appends or embeds numerals into a base candidate to create a technology-oriented or branded serial identity.
*   **How it works**: Uses `enrichment.post_pass_settings.alphanumeric` parameters (`placement: suffix`, `separator: "-"`, `allowed_numerals: [21, 42, 360, 247, 7]`). Combines base candidates with specified numbers (e.g. *Nexus-21*, *Xbox-360*, *WD-40*).
*   **Trademark advantage**: Medium — the numeral adds uniqueness but may limit future product line sub-branding.
*   **Required config**: `post_passes: [alphanumeric]`, `post_pass_settings.alphanumeric` configuration map.
*   **Examples output**: *Nexus-21*, *Vault-42*, *Xbox-360*, *Brando-2026*.
*   **Famous real names**: *WD-40*, *7-Eleven*, *Xbox 360*, *Cobalt21*.

---

### **Layer 3: Sound Symbolism Scoring Lens**

Sound symbolism (phonaesthetics) is not a generation strategy — it is a **scoring and filtering lens** evaluated after candidate creation. The Phonetic Sound Symbolism Engine (Section 6B) analyzes the acoustic and cognitive profile of every candidate string and stores the results as queryable database columns. Users then run `brando filter` to target specific emotional or stylistic archetypes.

#### **Phonetic Sound Classes & Brand Perception Rationale**

The engine categorizes speech sounds into acoustic building blocks. Understanding how these sounds affect human perception is key to filtering effectively:

| Sound Class | Character Tokens | Acoustic Behavior | Brand Perception & Psychological Impact | Famous Brand Examples |
| :--- | :--- | :--- | :--- | :--- |
| **Voiceless Plosives** | `p, t, k` | Airflow completely stopped, then released without vocal cord vibration | **Precision, speed, crispness, technical exactness** — feels light, sharp, and agile. | *Kodak*, *Pixar*, *Fitbit*, *TikTok* |
| **Voiced Plosives** | `b, d, g` | Airflow stopped and released WITH vocal cord vibration | **Strength, physical mass, durability, power** — feels heavy, solid, and authoritative. | *Boat*, *Beats*, *Duracell*, *Google*, *GitHub* |
| **Fricatives** | `f, s, v, z` | Continuous airflow forced through a narrow channel | **Flow, innovation, velocity, modern aesthetic** — feels smooth, frictionless, and forward-moving. | *Xerox*, *Vespa*, *Visa*, *Zappos*, *Swift* |
| **Sonorants** | `m, n, l, r` | Continuous non-turbulent airflow; vocal resonance | **Warmth, comfort, premium feel, human connection** — feels approachable, luxurious, and continuous. | *Rolex*, *Lego*, *Lunar*, *Natura*, *Sonos* |
| **Front Vowels** | `i, e, y` | Tongue positioned high and forward in the mouth (high-pitch resonance) | **Smallness, agility, high technology, lightness** — associated with software, precision, and speed. | *Figma*, *Mint*, *Zip*, *Intel*, *Twitter* |
| **Back Vowels** | `o, u` | Tongue retracted back in the mouth (low-pitch resonance) | **Volume, depth, warmth, physical presence** — associated with hardware, space, luxury, and solidity. | *Roku*, *Oculus*, *Volvo*, *Sonos*, *Loom* |
| **Central Vowels** | `a` | Neutral tongue position | **Universal, balanced, accessible** — neutral anchor vowel. | *Amazon*, *NASA*, *Zapier*, *Spanx* |

#### **Sound Profile Archetypes & Filter Parameters**

The `brando filter` command accepts direct parameters or `--archetype` presets to isolate candidates matching desired sound profiles:

| Target Archetype | Dominant Phoneme Classes | Brand Impression | `brando filter` CLI Query Flags | `config.yaml` Filter Key |
| :--- | :--- | :--- | :--- | :--- |
| **Precise & Fast** | Voiceless plosives (`p,t,k`) + Front vowels (`i,e`) | Speed, sharpness, high-tech | `brando filter --consonants voiceless-plosive --vowels front` | `filter.sound_archetype: Precise-Fast` |
| **Bold & Durable** | Voiced plosives (`b,d,g`) + Back vowels (`o,u`) | Mass, power, hardware strength | `brando filter --consonants voiced-plosive --vowels back` | `filter.sound_archetype: Bold-Durable` |
| **Flow & Innovation** | Fricatives (`f,s,v,z`) + Front vowels | Velocity, creativity, modern SaaS | `brando filter --consonants fricative --vowels front` | `filter.sound_archetype: Flow-Innovation` |
| **Warm & Luxurious** | Sonorants (`m,n,l,r`) + Back vowels | Premium, comforting, organic | `brando filter --consonants sonorant --vowels back` | `filter.sound_archetype: Warm-Luxurious` |
| **Smooth Rhythm** | Continuous sounds (vowels/sonorants/fricatives) | Friendly, fluid, easy flow | `brando filter --rhythm smooth --euphony-min 7.0` | `filter.rhythm_class: Smooth` |
| **Staccato Rhythm** | Plosive breaks dominate structural transitions | Energetic, punchy, memorable | `brando filter --rhythm staccato --euphony-max 4.0` | `filter.rhythm_class: Staccato` |
| **Front-Weighted** | Heavy initial syllable emphasis | Assertive, commanding, leading | `brando filter --emphasis front` | `filter.emphasis_weight: Front-Weighted` |
| **End-Weighted** | Heavy final syllable emphasis | Sophisticated, aspirational | `brando filter --emphasis end` | `filter.emphasis_weight: End-Weighted` |
| **Alliterative** | Repeating initial phoneme tokens | Playful, highly memorable | `brando filter --alliterative true` | `filter.is_alliterative: true` |

---

## **6. Detachable Core Technical Feature Modules**

Brando is composed of five core analysis engines. Esoteric and astrological modules are detachable plugins that can be deactivated independently in `config.yaml`.

### **A. Visual Typographical Silhouette Engine**
Analyzes the visual shape (Bouma silhouette) of lowercase character strings:
*   **Character Classification**:
    *   Ascenders: `b, d, f, h, k, l, t`
    *   Descenders: `g, j, p, q, y`
    *   Midlines: `a, c, e, i, m, n, o, r, s, u, v, w, x, z`
    *   Numeric Descenders: `3, 4, 5, 7, 9`
    *   Uppercase Anchors: `A` to `Z`
*   **Linguistic Properties & Balance**:
    *   `midline_ratio`: Calculated as `midline_count / total_letter_count`. A ratio $\ge 0.8$ represents flat visual profiles.
    *   `is_symmetrical`: Checked as `ascender_count == descender_count`.
    *   `is_palindromic`: Checked as true if the lowercase string reads the same backward as forward (e.g. *Vev*, *Level*, *Otto*).
    *   `repeating_patterns`: Identifies duplicate characters or double-consonants (e.g. *Sonos*, *Pixxel*) which improve logo visual balance.
    *   `bouma_silhouette`: Formats characters into a structural sequence string (e.g., `CMMDAM` for *Google*).
*   **Visual Balance Warnings**: Flags naming layouts that combine adjacent ascenders and descenders (such as `df` or `pg`) to warn of potential vertical overlap in tight typographic spacing.

### **B. Phonetic Sound Symbolism & Industry Intelligence Engine**
Categorizes speech sounds into acoustic building blocks and predicts multi-tag industry suitability:
*   **Consonant Dynamics**: Voiceless Plosives (`p,t,k`), Voiced Plosives (`b,d,g`), Fricatives (`f,s,v,z`), Sonorants (`m,n,l,r`).
*   **Vowel Classifications**: Front Vowels (`i,e,y`), Back Vowels (`o,u`), Central Vowels (`a`).
*   **Euphony, Cadence & Archetype Calculations**: `euphony_score` ($0.0 - 10.0$), `rhythm_class` (Smooth/Staccato), `emphasis_weight` (Front/End-weighted), `is_alliterative`, `sound_archetype`.
*   **Industry Intelligence Predictor**:
    *   `suitable_industry_tags`: Multi-tag sector array predicted from acoustic + typographic vectors (e.g. `"fintech, tech, saas"`).
    *   `industry_affinity_score`: Multi-vector weighted suitability score for configured `industry_context` (0.0 - 10.0).
    *   `cjk_friendly`: True if open CVCV structure translates cleanly to CJK (Japanese Katakana/Mandarin) phonotactics.
    *   `romance_friendly`: True if string avoids silent `h` / ambiguous `j` in Romance languages.

### **C. Esoteric & Cultural Alignment Engine (Detachable)**
Integrates numerological and astrological traditions into quantitative database fields:
*   **Pythagorean Numerology Module**:
    *   Maps English characters sequentially from `1` to `9` (`A,J,S`=1, `B,K,T`=2, `C,L,U`=3, `D,M,V`=4, `E,N,W`=5, `F,O,X`=6, `G,P,Y`=7, `H,Q,Z`=8, `I,R`=9).
    *   Sums letter values and reduces to single digit root; halts reduction at Master Numbers (`11, 22, 33`) and flags Karmic Debt numbers (`13, 14, 16, 19`). Calculates `Soul Urge` (vowels) and `Personality` (consonants).
*   **Chaldean Numerology Module**:
    *   Maps characters non-sequentially from `1` to `8` based on spoken sound frequencies (`A,I,J,Q,Y`=1, `B,K,R`=2, `C,G,L,S`=3, `D,M,T`=4, `E,H,N,X`=5, `U,V,W`=6, `O,Z`=7, `F,P`=8). Excludes number `9`.
*   **Vedic Astrology (Nakshatra & 108 Pada) Module**:
    *   *Traditional Principle*: Divides the $360^\circ$ zodiac wheel into 27 Nakshatras (lunar houses) $\times$ 4 Padas (quarters) $= 108$ total sound slots (*Akshara Padas*). Every Pada has a specific starting phoneme root.
    *   *Calculation*: The engine matches a candidate's starting sound root against the 108 Pada sound matrix:
        - **Ashwini** (Ketu/Fire): `chu` (P1), `che` (P2), `cho` (P3), `la` (P4) $\rightarrow$ *Chu-tech*, *Chetra*, *Chola*, *Lego*
        - **Bharani** (Venus/Earth): `lee` (P1), `lu` (P2), `le` (P3), `lo` (P4) $\rightarrow$ *Lee-sys*, *Lumi*, *Lexus*, *Logitech*
        - **Krittika** (Sun/Fire): `a` (P1), `i` (P2), `u` (P3), `e` (P4) $\rightarrow$ *Amazon*, *Intel*, *Uber*, *Etsy*
        - **Rohini** (Moon/Earth): `o` (P1), `va` (P2), `vi` (P3), `vu` (P4) $\rightarrow$ *Onyx*, *Valor*, *Vesa*, *Vu-tech*
        - **Mrigashira** (Mars/Earth): `ve` (P1), `vo` (P2), `ka` (P3), `ki` (P4) $\rightarrow$ *Vektor*, *Vor*, *Kinet*, *Kindle*
    *   *Database Population*: Writes `nakshatra` (e.g. `"Mrigashira"`), `nakshatra_pada` (e.g. `4`), and `ruling_planet` directly into database columns.

*   **Western Zodiac & Elemental Modalities Module**:
    *   *Traditional Principle*: Groups the 12 Zodiac signs into 4 Elemental Modalities:
        - **Fire** (*Aries, Leo, Sagittarius*): Bold, aggressive, fast plosives (`p,t,k`), front vowels $\rightarrow$ Tech, VC, Gaming, Sports.
        - **Earth** (*Taurus, Virgo, Capricorn*): Grounded, heavy, voiced plosives (`b,d,g`), back vowels $\rightarrow$ Real Estate, Banking, Legal.
        - **Air** (*Gemini, Libra, Aquarius*): Agile, communicative, fricatives (`s,f,v,z`) $\rightarrow$ Media, Social Networks, SaaS.
        - **Water** (*Cancer, Scorpio, Pisces*): Fluid, comforting, sonorants (`m,n,l,r`) $\rightarrow$ Healthcare, Beauty, Wellness.
    *   *Letter Mapping Grid*:
        - **Fire Signs** (`A, I, J, P, Q, E, H, N, X, S`)
        - **Earth Signs** (`B, K, R, U, V, W, T`)
        - **Air Signs** (`C, G, L, O, Z`)
        - **Water Signs** (`D, M, F`)
    *   *Dominance Algorithm*: Tally character elemental counts with $+2.0$ priority weighting on the initial letter. Writes `zodiac_sign` and `zodiac_element` (`Fire`, `Earth`, `Air`, `Water`) to database. Users filter via `brando filter --zodiac-element Fire`.

*   **Kabbalistic (Gematria) Module**:
    *   Maps Hebrew Gematria frequencies onto English letter groups: Mother Letters (Air/Water/Fire), Double Letters (Planetary forces), and Simple Letters (Zodiac constellations). Computes `pythagorean_soul_urge` (vowel sum) and `pythagorean_personality` (consonant sum).
*   **Family Legacy / Heritage Logic**:
    *   Requires a configuration block defined under the `generation_alignment` namespace:
        ```yaml
        generation_alignment:
          family_heritage:
            preferred_initials: []     # Founder/family starting initials (e.g. [S, B])
            legacy_roots: []           # Historic family roots to blend/check (e.g. [vance, forge])
        ```
    *   *Additive Metric Scoring Logic (Educational Callout)*:
        Scores are calculated non-destructively on a 0.0 – 10.0 scale:
        - **Initial Match (`+5.0`)**: Candidate starting character matches `preferred_initials` (e.g. starts with `S` or `B`).
        - **Root Match (`+5.0`)**: Candidate contains a substring from `legacy_roots` (e.g. contains `vance` or `forge`).
        - **Dual Match (`10.0 Max`)**: Candidate matches BOTH initial AND legacy root (e.g. *Smithvance*, *Brownforge* $\rightarrow$ 10.0 / 100% max score).
        - **Neither Match (`0.0`)**: Candidate remains in the database with `heritage_score: 0.0`. Zero candidate names are ever dropped or deleted.
        - *User Querying*: Users can filter via `brando filter --heritage-min 5.0` (matches either condition) or `brando filter --heritage-min 10.0` (matches both conditions).
*   **Esoteric Industry Energy Profile Matrix (`esoteric_industry_fit`)**:
    *   *Root 1 (Pioneer)*: Breakthrough Tech, VC, AI (`esoteric_industry_fit: 9.5`).
    *   *Root 2 (Balance)*: Co-working, HR, Consulting.
    *   *Root 3 (Creativity)*: Media, Entertainment, Fashion.
    *   *Root 4 (Bedrock)*: Banking, Real Estate, Accounting, Legal.
    *   *Root 5 (Disruptive)*: Travel, Consumer SaaS, Logistics.
    *   *Root 6 (Nurturing)*: Healthcare, Wellness, Food.
    *   *Root 7 (Analysis)*: Biotech, Deep Tech, Security.
    *   *Root 8 (Wealth/Commerce)*: Investment Banking, Luxury, Conglomerates.
    *   *Root 9 (Universal)*: Non-Profits, Global Platforms, EdTech.

### **D. Nice Class Trademark & Industry Context Engine**
Manages trademark class mapping and commercial category clearance:
*   **Automatic Industry Directory Mapping (`industry_context`)**:
    *   `tech` $\rightarrow$ **Class 9** (Apps), **35** (Biz), **42** (SaaS) | TLDs: `.ai`, `.io`, `.dev`, `.com`
    *   `fashion` $\rightarrow$ **Class 25** (Apparel), **35** (Retail) | TLDs: `.shop`, `.store`, `.co`, `.com`
    *   `food` $\rightarrow$ **Class 29** (Dairy/Meats), **30** (Snacks), **32** (Drinks), **35** (Store)
    *   `pharma` $\rightarrow$ **Class 5** (Pharma), **10** (Medical Devices), **44** (Healthcare)
    *   `fintech` $\rightarrow$ **Class 9** (Banking App), **36** (Financial), **42** (Fintech SaaS)
    *   `cosmetics` $\rightarrow$ **Class 3** (Skincare/Perfumes), **35** (Beauty Retail)
    *   `entertainment` $\rightarrow$ **Class 9** (Gaming Apps), **41** (Media Services)
    *   `real_estate` $\rightarrow$ **Class 36** (Real Estate), **37** (Construction)
    *   `custom` $\rightarrow$ Explicit user list in `validation.nice_classes`.
*   **Madrid Protocol Simulator**: Compiles WIPO MM2 application model and audits 5-year Central Attack risks.

### **E. Ecosystem Security & Phishing Risk Engine (100% Free & Offline)**
Evaluates formatting compliance across 13 package registries (npm, PyPI, Go, crates.io, RubyGems, Packagist, NuGet, Maven, Docker, Homebrew, apt/rpm, GitHub, Swift PM) and runs sub-millisecond phishing risk checks:
*   **Bundled Open Datasets (`brando/data/top_brands/`)**: `top_1000_financial.txt`, `top_1000_tech.txt`, `top_1000_packages.txt`, `top_1000_global.txt` ($<100$ KB, zero API cost).
*   **RapidFuzz C++ SIMD & BK-Tree Engine**: Evaluates 10,000,000 candidate edit distances in **<35 milliseconds**.
*   **Database Risk Output**: Stores `min_levenshtein_distance`, `closest_competing_brand`, and `industry_phishing_risk` (0 - 100) directly in candidate record.
