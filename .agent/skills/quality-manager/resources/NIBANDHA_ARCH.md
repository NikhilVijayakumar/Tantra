### 📂 `.agent\skills\nibandha-manager\resources\NIBANDHA_ARCH.md`

# 🏛️ TANTRA Quality & Process Standards

**Version:** 1.0.0
**Status:** Canonical (Source of Truth)
**Philosophy:** Environmental Sovereignty, TDD-First, Zero-Print, Deep Traceability.

---

## 1. The Foundational Four (Orchestration Workflow)

The **Quality Manager** orchestrates development in a strict sequence. Every stage must be validated by `scripts/check_foundations.py` using the local virtual environment.

| Stage | Mission | Primary Artifacts |
| --- | --- | --- |
| **0. Env** | **Environmental Sovereignty** | `.venv/`, `pyproject.toml` |
| **1. Design** | **Platform-Agnostic Blueprint** | `docs/modules/`, `docs/test/` |
| **2. Test** | **Red Phase (Failing Stubs)** | `tests/{module}/` |
| **3. Build** | **Green Phase (Implementation)** | `src/bavans/{module}/` |

---

## 2. Technical & Logging Standards

### 🛠️ Core Implementation Rules

* **Environmental Lock:** All execution must occur via `{project_root}/.venv/bin/python`.
* **Absolute Imports:** Use `from bavans.tantra.{module}` (e.g., `from bavans.tantra.core`).
* **Atomic Classes:** **One Class, One File.**
* **Data Integrity:** Use **Pydantic** (`frozen=True`, `strict=True`) for all models.
* **Interface First:** Depend on **Protocols** to remain platform-agnostic.

### 📝 Deep Traceability (Logging)

* **Zero-Print Policy:** Absolute ban on `print()`. Use `logging`.
* **Blueprint Mapping:** Every logic gate MUST log its **Blueprint ID** (e.g., `logger.info("[AR-UT-001] ...")`).
* **Safe Init:** No side-effects during module import.

---

## 3. Directory Topology

```text
tantra/
├── .venv/               # Stage 0: The Environment (Local Python)
├── docs/                # Stage 1: The Blueprints (Language Neutral)
│   ├── features/        # Functional Specs & Data Schemas
│   └── test/            # Scenarios (UT/E2E) with [XX-UT-00X] IDs
├── tests/               # Stage 2: The Verification (Pytest)
│   └── {module}/        # Test stubs mapping to Blueprint IDs
├── src/                 # Stage 3: The Reality
│   └── bavans/          # Absolute Package Root
│       └── tantra/      # Clean logic + Traceable logging
└── pyproject.toml       # The Manifest (Root & Dependency Truth)

```

---

## 4. Test ID & Mapping

* **Format:** `[PREFIX]-[TYPE]-[ID]` (e.g., `FR-UT-001`).
* **Traceability:** Every ID in `docs/test/` must exist as a **test function** in `tests/` and a **log entry** in `src/`.

---

## 5. Orchestration Gates

1. **Idempotency:** The Manager skips stages if artifacts are verified.
2. **Venv Enforcement:** The Manager aborts if `.venv` is not active or missing.
3. **Doctor Audit:** Every handover requires a passing grade from `nibandha_doctor.py`.

---
