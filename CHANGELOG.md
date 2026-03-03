# Changelog

## 1.1.0 (2026-03-03)

Full Changelog: [v1.0.5...v1.1.0](https://github.com/Blooio/blooio-python-sdk/compare/v1.0.5...v1.1.0)

### Features

* **client:** add custom JSON encoder for extended type support ([c02699e](https://github.com/Blooio/blooio-python-sdk/commit/c02699e0bb5a7411efe9ba37898f74bce58fc4a8))
* **client:** add support for binary request streaming ([0a46f0a](https://github.com/Blooio/blooio-python-sdk/commit/0a46f0a17f78a2a21aae637af66fb6b5671c12c5))


### Chores

* **ci:** upgrade `actions/github-script` ([5e006c2](https://github.com/Blooio/blooio-python-sdk/commit/5e006c28777fae0e393b573d148432644a5d181b))
* format all `api.md` files ([3d045e8](https://github.com/Blooio/blooio-python-sdk/commit/3d045e8d5b9cc2afca1d6c85ded4b0e531c28228))
* **internal:** add request options to SSE classes ([3d004d8](https://github.com/Blooio/blooio-python-sdk/commit/3d004d8b3892f4f8a212ef00745919dc59a2e099))
* **internal:** bump dependencies ([e6b7ec8](https://github.com/Blooio/blooio-python-sdk/commit/e6b7ec8b91ed416baf78c830519f226a4a361a98))
* **internal:** codegen related update ([bdc07aa](https://github.com/Blooio/blooio-python-sdk/commit/bdc07aa8716f9de74bebb431a448dbf1f19a0837))
* **internal:** fix lint error on Python 3.14 ([34988f7](https://github.com/Blooio/blooio-python-sdk/commit/34988f7b47fd8e01bbb8a0ba61abf52d66a9598a))
* **internal:** make `test_proxy_environment_variables` more resilient ([fa78df3](https://github.com/Blooio/blooio-python-sdk/commit/fa78df3c42ab33e1f47de28ff366be72c2732134))
* **internal:** make `test_proxy_environment_variables` more resilient to env ([a70f1e5](https://github.com/Blooio/blooio-python-sdk/commit/a70f1e597d63bd7c03f5262d29b32a16ca7eff4f))
* **internal:** remove mock server code ([6d1b141](https://github.com/Blooio/blooio-python-sdk/commit/6d1b141349ac7e1eefe21ef50dc3b5d8de6707d6))
* **internal:** update `actions/checkout` version ([3f2ef54](https://github.com/Blooio/blooio-python-sdk/commit/3f2ef546ebf7281cfca3d17255de0cdc288e1013))
* update mock server docs ([b1c88e2](https://github.com/Blooio/blooio-python-sdk/commit/b1c88e2d8f1aac114dac3b288d540cae6f35d70c))

## 1.0.5 (2025-12-19)

Full Changelog: [v1.0.4...v1.0.5](https://github.com/Blooio/blooio-python-sdk/compare/v1.0.4...v1.0.5)

### Bug Fixes

* use async_to_httpx_files in patch method ([b6502ac](https://github.com/Blooio/blooio-python-sdk/commit/b6502acc9bf7d875b8c122b4560ca6f592ccb07f))


### Chores

* **internal:** add `--fix` argument to lint script ([18f419d](https://github.com/Blooio/blooio-python-sdk/commit/18f419d1a0fa01d20d635c848ed33f78d0fefda9))
* **internal:** add missing files argument to base client ([ba6fc65](https://github.com/Blooio/blooio-python-sdk/commit/ba6fc65657b77abc6fc59aed3053e3d3d4c6ec84))
* speedup initial import ([512dd39](https://github.com/Blooio/blooio-python-sdk/commit/512dd3980296e17dcc7e02f508a295ff5e498d8d))

## 1.0.4 (2025-12-09)

Full Changelog: [v1.0.3...v1.0.4](https://github.com/Blooio/blooio-python-sdk/compare/v1.0.3...v1.0.4)

### Bug Fixes

* **types:** allow pyright to infer TypedDict types within SequenceNotStr ([eee935c](https://github.com/Blooio/blooio-python-sdk/commit/eee935c823f2d2df52d1baa7c64f2ba4d037a6d4))


### Chores

* add missing docstrings ([13eb515](https://github.com/Blooio/blooio-python-sdk/commit/13eb515f29ad4b006df09013e4a491c65c00e6cd))

## 1.0.3 (2025-12-03)

Full Changelog: [v1.0.2...v1.0.3](https://github.com/Blooio/blooio-python-sdk/compare/v1.0.2...v1.0.3)

### Bug Fixes

* ensure streams are always closed ([3a2cc70](https://github.com/Blooio/blooio-python-sdk/commit/3a2cc70ea5a7a492ae9b404e6305bd5deb7d3e0d))


### Chores

* **deps:** mypy 1.18.1 has a regression, pin to 1.17 ([a7853af](https://github.com/Blooio/blooio-python-sdk/commit/a7853af591c6af19cce4ed7c04fe953dbfb957bb))
* **docs:** use environment variables for authentication in code snippets ([9558d99](https://github.com/Blooio/blooio-python-sdk/commit/9558d99532c57a9a4b712a5ed575ebdae753a052))
* update lockfile ([e7f0120](https://github.com/Blooio/blooio-python-sdk/commit/e7f0120b8b56fb9b73bda0ebc32510fef7fe6701))

## 1.0.2 (2025-11-22)

Full Changelog: [v1.0.1...v1.0.2](https://github.com/Blooio/blooio-python-sdk/compare/v1.0.1...v1.0.2)

### Bug Fixes

* compat with Python 3.14 ([2c8e789](https://github.com/Blooio/blooio-python-sdk/commit/2c8e789b083bf5f4049214cc475de071495f902f))
* **compat:** update signatures of `model_dump` and `model_dump_json` for Pydantic v1 ([efacbb6](https://github.com/Blooio/blooio-python-sdk/commit/efacbb66a2b9329eb4461561e38f5838d37b1087))


### Chores

* add Python 3.14 classifier and testing ([dd2ed6b](https://github.com/Blooio/blooio-python-sdk/commit/dd2ed6bc4918462d334a869270f496e5dce653a5))
* **package:** drop Python 3.8 support ([19cbcd0](https://github.com/Blooio/blooio-python-sdk/commit/19cbcd0ce4d5dd3626fff4cd02094b3d9bf69f48))

## 1.0.1 (2025-11-04)

Full Changelog: [v1.0.0...v1.0.1](https://github.com/Blooio/blooio-python-sdk/compare/v1.0.0...v1.0.1)

### Bug Fixes

* **client:** close streams without requiring full consumption ([145afcd](https://github.com/Blooio/blooio-python-sdk/commit/145afcd5e6669103ed6066ebcfae0c4930f3d82b))


### Chores

* **internal/tests:** avoid race condition with implicit client cleanup ([3d808c8](https://github.com/Blooio/blooio-python-sdk/commit/3d808c8070ccca32d19887b0dddf965ea53bcd04))
* **internal:** grammar fix (it's -&gt; its) ([be60d3b](https://github.com/Blooio/blooio-python-sdk/commit/be60d3b2f9cd4f51c92472a16e8153595aa1c8dd))

## 1.0.0 (2025-10-17)

Full Changelog: [v0.0.1...v1.0.0](https://github.com/Blooio/blooio-python-sdk/compare/v0.0.1...v1.0.0)

### Chores

* configure new SDK language ([8f81881](https://github.com/Blooio/blooio-python-sdk/commit/8f8188186e7367438a7d5f311a21499384056275))
* update SDK settings ([3a67436](https://github.com/Blooio/blooio-python-sdk/commit/3a67436282797fe0406e4cbcf4ecce9d523d8b5e))
* update SDK settings ([c8fc4f6](https://github.com/Blooio/blooio-python-sdk/commit/c8fc4f61c3028509ea520a92b56246a29edd9b3e))
