# Changelog

All notable changes to the Brando naming engine will be documented in this file.

## [2026-08-04] - 2026-08-04

### Features

* implement object-oriented Python SDK API (brando.Pipeline, brando.Database) ([5083cb0](https://github.com/mrxsierra/brando/commit/5083cb06962947a28c12f3013509c46cde24d9f5))
* implement Click CLI command suite for init, build, and verify ([25917a5](https://github.com/mrxsierra/brando/commit/25917a5906d5b70efef1c6198da85645d7beb014))
* implement lazy gzipped asset loader with sub-10ms decompression benchmark ([ac7c872](https://github.com/mrxsierra/brando/commit/ac7c8728d0e5b0ba22ac20c6e3f864791ce0ab6f))
* implement RapidFuzz SIMD security and typosquatting risk engine ([5a28472](https://github.com/mrxsierra/brando/commit/5a28472c377ca4172e66d2a3c8c34a1f08ade3c3))
* implement Nice Class mapping and WIPO Madrid Protocol simulator ([99562ff](https://github.com/mrxsierra/brando/commit/99562ff5604edee137684575471f3a3bd3b9d2cf))
* implement Pythagorean, Chaldean, and 108 Nakshatra Pada calculators ([c7cc2f7](https://github.com/mrxsierra/brando/commit/c7cc2f7189212e3aaaf6ed0b15a1dec897705168))
* implement sound symbolism and euphony scoring engine ([d97722b](https://github.com/mrxsierra/brando/commit/d97722b1298a7f628580fe6833cb6a89de4e8d37))
* implement Bouma silhouette geometry and visual symmetry calculator ([ca02c82](https://github.com/mrxsierra/brando/commit/ca02c827bc78511500cd624449764fceba6d4a35))
* implement Layer 2a orthographic post-pass transforms ([d9d8752](https://github.com/mrxsierra/brando/commit/d9d8752f7e087744543bb509ef95ff79627c2609))
* implement Layer 2 vocabulary enrichment for all 8 strategies ([9e61874](https://github.com/mrxsierra/brando/commit/9e61874aa90b591a6b14387a59ba8651ee186f4d))
* implement Layer 1 Mode A Neoclassical and Mode B Blend generators ([c23c8cb](https://github.com/mrxsierra/brando/commit/c23c8cb18b0800ce6cd1954fc9c48b87b4f7d4cf))
* implement zero-config unbiased config loader and preset maps ([69de8c3](https://github.com/mrxsierra/brando/commit/69de8c3be9065ca690b4a985ce4dedc1438dbbdd))
* establish version constant and unified BrandoError hierarchy ([9addd5b](https://github.com/mrxsierra/brando/commit/9addd5baac62e853f33e0721f48e080380d851bd))

### Other Changes

* ci(hooks): enforce --no-project --isolated on multi-python verification ([0df434e](https://github.com/mrxsierra/brando/commit/0df434e74770a895836f117c5c2b23099d947851))
* ci(hooks): add offline resilience to local pre-push multi-Python script ([53844b3](https://github.com/mrxsierra/brando/commit/53844b32b58474b7047f7c051b2ffd69aba59b28))
* ci(sdlc): configure 2-tier CI/CD architecture, PR fast check gate & 5-step local guardrails (#1) ([933de89](https://github.com/mrxsierra/brando/commit/933de89e0f9ce191f3052165a87b2dfad11c3bfc))
* ci(sdlc): implement 2-tier CI/CD architecture, PR fast check, security audit, and branch protection docs ([f6d94d1](https://github.com/mrxsierra/brando/commit/f6d94d18e1b53bc9dd313a106a1a86a9e62840c9))
* ci(workflows): simplify token binding in sponsors.yml to eliminate IDE warning ([c31e7e3](https://github.com/mrxsierra/brando/commit/c31e7e320d26e0e373b67d53dcd29c69b6ec6139))
* style: apply ruff format and enforce pre-commit linting & testing pipeline ([620fb9d](https://github.com/mrxsierra/brando/commit/620fb9d494e869e4efb690309f908ded51d54c9c))
* ci: fix permissions and secret fallbacks across all 5 GitHub Actions workflows ([8f86879](https://github.com/mrxsierra/brando/commit/8f868797551e6dce364be9d10642ed02c8a74531))

### Documentation

* complete Phase 1 Core Engine stabilization ([0ad149f](https://github.com/mrxsierra/brando/commit/0ad149f92e6f1c54ea8577b9d7c9f6da63362971))
* check off Step 1.6 Object-Oriented Python SDK ([1107574](https://github.com/mrxsierra/brando/commit/110757414f639f8bcc7d4a2e02266c08332374a3))
* check off Step 1.5 Click CLI Command Suite ([c9c15bd](https://github.com/mrxsierra/brando/commit/c9c15bd3a3b488ebe57b3ae339c9d48bf9660602))
* check off Step 1.4 Lazy Data Architecture ([2ce172c](https://github.com/mrxsierra/brando/commit/2ce172c774cbf00108417918e3cebd1729be9bd1))
* check off Step 1.3e Module 6E Security Engine ([7af9d01](https://github.com/mrxsierra/brando/commit/7af9d014d8d9bf4eecadacf3727fccae7cc6d3a9))
* check off Step 1.3d Module 6D Trademark Engine ([3f4f261](https://github.com/mrxsierra/brando/commit/3f4f261c9690ff9d26d40692c74b80540d30124e))
* check off Step 1.3c Module 6C Esoteric Numerology ([7ee9aae](https://github.com/mrxsierra/brando/commit/7ee9aaea8e456355eb7c510e969b6ffd158a3788))
* check off Step 1.3b Module 6B Sound Symbolism ([4a7398c](https://github.com/mrxsierra/brando/commit/4a7398c1a6fc20d348e1871b9fd969565bd1a9dd))
* check off Step 1.3a Module 6A Visual Geometry ([9d892f7](https://github.com/mrxsierra/brando/commit/9d892f74d6eeb8d5a9bb0971124fcc0d6d8ba658))
* check off Step 1.2c Layer 2a Orthographic Post-Pass Engine ([7044b14](https://github.com/mrxsierra/brando/commit/7044b148007293958d74b4a05a6fc60a5e304a88))
* check off Step 1.2b Layer 2 Vocabulary Enrichment Engine ([6b9cef9](https://github.com/mrxsierra/brando/commit/6b9cef9100d8ec67d22901ab8f72ec01b5b2ffa8))
* check off Step 1.2a Layer 1 Core Phoneme Generator ([e8a2fa4](https://github.com/mrxsierra/brando/commit/e8a2fa4820e85441cd66a57d1a459853ea457dd3))
* check off Step 1.1 layout and config loader items ([f5c2f10](https://github.com/mrxsierra/brando/commit/f5c2f100323a9e0065d562c353c543c3b3b8fa07))
* check off Step 1.1a version constant and exception hierarchy ([2686311](https://github.com/mrxsierra/brando/commit/2686311c9e7591233b6029242e2c5480ac803171))
* enforce strict branch isolation and side-by-side test mandate in PRD and CONTRIBUTING.md ([4008bd8](https://github.com/mrxsierra/brando/commit/4008bd8e9ff4255adacd0ba4645cc97e62c39855))
* align PRD Section 2 with v0.1.0 baseline and v0.2.0-v0.5.0 pre-release sequence ([a533f81](https://github.com/mrxsierra/brando/commit/a533f81144d64228ed93dbdcb24943f059d3809d))

### Tests

* establish 5-tier testing suite and validate performance SLAs (<35ms SIMD, <10ms data) ([4c12d38](https://github.com/mrxsierra/brando/commit/4c12d38aeb8f76ec34195716b6101c7c427c2585))

---
## [2026-08-03] - 2026-08-03

### Documentation

* update PRD v2 with pre-release version sequence (v0.1.0 to v0.5.0 to v1.0.0) ([617eaf2](https://github.com/mrxsierra/brando/commit/617eaf219ed5d677c439a21706251146ca8701d9))
* update version lineage progression (v0.1.0 -> v0.5.0 -> v1.0.0) and side-by-side test mandate ([ab805fa](https://github.com/mrxsierra/brando/commit/ab805fad32d661df0239c2b7afbd8d1b8382a185))
* finalize PRD v2 specification, task backlog, and marketing playbook (v0 baseline) ([daa158b](https://github.com/mrxsierra/brando/commit/daa158bd09bb38fe41b25551198927cecd86ad86))

### Other Changes

* ci: add GitHub Actions workflows, issue templates, and funding configs ([24eb6df](https://github.com/mrxsierra/brando/commit/24eb6dfbaaa93b46c09b64ddf48184efaa057bb5))

---
## [2026-07-16] - 2026-07-16

### Features

* add prune script and .env paths configuration support ([ed2008f](https://github.com/mrxsierra/brando/commit/ed2008f55d62b07ab2986cd869b8c590696d7173))

---
## [2026-07-15] - 2026-07-15

### Features

* complete Phase 4 optimization, scenario testing, and usability overrides ([41faf5d](https://github.com/mrxsierra/brando/commit/41faf5d7eb4cf9e40283fc59f697a3392bbc5673))
* run verification checks on all fields and support simple rule-based generation fallback ([61c315c](https://github.com/mrxsierra/brando/commit/61c315cd5c85a1c6565433f940f3a00b1d28a5d8))
* fall back to default built-in configuration if config.yaml is missing ([d84a0ff](https://github.com/mrxsierra/brando/commit/d84a0ff27b2cdb29c1e5cb69de07de137a203497))
* support custom_names configuration to run direct candidate validations ([1ad53db](https://github.com/mrxsierra/brando/commit/1ad53db882b5e3b0f5ef2796d8e2bd2eae0b4db8))
* implement finalist reporter with unit tests ([f431c20](https://github.com/mrxsierra/brando/commit/f431c20153ae994fecef436db05aac1a5aae0587))
* implement filter and scorer engine with unit tests ([d2181ec](https://github.com/mrxsierra/brando/commit/d2181ec5b3209abbb34ec4f175b1b07e335ea1ce))
* implement interactive config wizard with unit tests ([201fc10](https://github.com/mrxsierra/brando/commit/201fc10aae5ed276f9ce464c6ddad75b5fef2c8a))

### Bug Fixes

* resolve RuntimeError in cli build event loop by adopting asyncio.run ([b4764fa](https://github.com/mrxsierra/brando/commit/b4764fad089930fcb5583954347bc87172962a0a))

### Documentation

* upgrade repository documentation suite ([73b1c48](https://github.com/mrxsierra/brando/commit/73b1c48a16870563df6a3be8c98221caf37e53af))
* update implementation plan and task tracking with improved two-step verification, linguistic filtering, and tutorial documentation, and ignore .vscode directory. ([e1506be](https://github.com/mrxsierra/brando/commit/e1506be71fdf3c0270b4fe813ad2739fd2d26fa4))
* define Phase 4 optimization, scenario testing, and tracking roadmap in plan and task list ([115a51c](https://github.com/mrxsierra/brando/commit/115a51c967ef4c7da461750e82aff8224a002db4))
* complete all tasks in the task tracker ([46bfc48](https://github.com/mrxsierra/brando/commit/46bfc4802e95ded91244848eeed941fa4c8e083b))
* complete README documentation for install and CLI usage ([7d6fa07](https://github.com/mrxsierra/brando/commit/7d6fa07362965e78da5f7656017c3aabc91286e7))
* finalize phase 2 task tracker checkboxes ([27d0c3a](https://github.com/mrxsierra/brando/commit/27d0c3a5f9661221215e756982c1832083cc4668))
* update task tracker for Phase 3 progress ([6cdaa39](https://github.com/mrxsierra/brando/commit/6cdaa393b25f7a1ef808b4fe860952a58c7260d0))
* update task tracker for reporter progress ([3a99cba](https://github.com/mrxsierra/brando/commit/3a99cba2dccdf9466a0ec64339fb6541ca458640))
* update task tracker for scorer progress ([b5b1b7f](https://github.com/mrxsierra/brando/commit/b5b1b7f2f245ff37a3e11dd58cce8b0d8dc26534))

### Other Changes

* style: update gitignore to exclude walkthrough ([d643e62](https://github.com/mrxsierra/brando/commit/d643e6232aeed0df9263eec3fdf7fd6867170c80))

---
## [2026-07-14] - 2026-07-14

### Features

* implement Click CLI command suite with unit tests ([d5eabd9](https://github.com/mrxsierra/brando/commit/d5eabd9690864fef63c327f632a491899b120fde))
* implement local database adapter with unit tests ([c0ba6f2](https://github.com/mrxsierra/brando/commit/c0ba6f27a419fdc9203e465ba2beade3a724a65b))
* implement async domain dns and social handle checkers with unit tests ([0ab9523](https://github.com/mrxsierra/brando/commit/0ab9523405e939ba742d23bce33ae180de253dd1))
* implement naming generator and typographics with unit tests ([0018fa9](https://github.com/mrxsierra/brando/commit/0018fa9c550af9843d1d57759019af1995c88383))
* implement chaldean, pythagorean, and vedic esoteric calculations with unit tests ([c410370](https://github.com/mrxsierra/brando/commit/c410370532dcf5f280dde7fe35e7783299e0b42a))

### Documentation

* update task tracker for wizard progress ([62120f4](https://github.com/mrxsierra/brando/commit/62120f4265e468f24e7b9e832a3d4d4dcdee84bd))
* update task tracker for cli progress ([2ea6443](https://github.com/mrxsierra/brando/commit/2ea644318559bd351bbf3413020bab2c833879b8))
* update task tracker for database adapter progress ([10f7802](https://github.com/mrxsierra/brando/commit/10f7802103f6b3d933a05fe4ac097015ba628d15))
* update task tracker for async checker progress ([97a4ad7](https://github.com/mrxsierra/brando/commit/97a4ad789a5b064ff4386201cd6b6a8459402e4b))
* update task tracker for package initialization ([299a598](https://github.com/mrxsierra/brando/commit/299a598db93314f7173d546bd32dba9a1caf332a))

### Maintenance Tasks

* update author details and gitignore rules ([126143a](https://github.com/mrxsierra/brando/commit/126143a5a2bcecb0d390b7bfa43d72a7cdc15a04))
* initialize repository and package metadata ([876a504](https://github.com/mrxsierra/brando/commit/876a50470ac0c76ad57569926d41479ac02e7e55))

---