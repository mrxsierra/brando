# Changelog

All notable changes to the Brando naming engine will be documented in this file.

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

### Other Changes

* style: update gitignore to exclude walkthrough ([2e8c5e3](https://github.com/mrxsierra/brando/commit/2e8c5e379a66569e26a378ffa8e4c8a741ca1e54))

### Documentation

* update implementation plan and task tracking with improved two-step verification, linguistic filtering, and tutorial documentation, and ignore .vscode directory. ([e1506be](https://github.com/mrxsierra/brando/commit/e1506be71fdf3c0270b4fe813ad2739fd2d26fa4))
* define Phase 4 optimization, scenario testing, and tracking roadmap in plan and task list ([115a51c](https://github.com/mrxsierra/brando/commit/115a51c967ef4c7da461750e82aff8224a002db4))
* complete all tasks in the task tracker ([46bfc48](https://github.com/mrxsierra/brando/commit/46bfc4802e95ded91244848eeed941fa4c8e083b))
* complete README documentation for install and CLI usage ([7d6fa07](https://github.com/mrxsierra/brando/commit/7d6fa07362965e78da5f7656017c3aabc91286e7))
* finalize phase 2 task tracker checkboxes ([27d0c3a](https://github.com/mrxsierra/brando/commit/27d0c3a5f9661221215e756982c1832083cc4668))
* update task tracker for Phase 3 progress ([6cdaa39](https://github.com/mrxsierra/brando/commit/6cdaa393b25f7a1ef808b4fe860952a58c7260d0))
* update task tracker for reporter progress ([3a99cba](https://github.com/mrxsierra/brando/commit/3a99cba2dccdf9466a0ec64339fb6541ca458640))
* update task tracker for scorer progress ([b5b1b7f](https://github.com/mrxsierra/brando/commit/b5b1b7f2f245ff37a3e11dd58cce8b0d8dc26534))

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