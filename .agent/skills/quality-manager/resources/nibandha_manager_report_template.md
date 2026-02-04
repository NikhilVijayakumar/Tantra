### 📂 `.agent\skills\nibandha-manager\resources\nibandha_manager_report_template.md`

# 📋 TANTRA Manager State Report: [MODULE_NAME]

## 🌍 Stage 0: Environment Health

* **Interpreter:** `./.venv/bin/python` (Verified: [🟢/🔴])
* **Source Root:** `{root}` (Parsed from `pyproject.toml`)
* **Dependency Sync:** `pyproject.toml` vs `.venv` (Status: [🟢/🔴])

## 🏗️ Foundation Status (The TDD Loop)

| Stage | Artifact Check | Status | Verification Tool |
| --- | --- | --- | --- |
| **1. Design** | `docs/features/[module]/README.md` | [🟢/🔴] | `check_foundations.py` |
| **2. Test** | `tests/unit/[module]/test_unit.py` | [🟢/🔴] | `pytest` via `.venv` |
| **3. Build** | `src/bavans/tantra/[module]/core.py` | [🟢/🔴] | `project_doctor.py` |

## 📝 Quality Audit (Pillars of TANTRA)

* **Absolute Imports:** [Verified/Pending]
* **Frozen Pydantic Models:** [Verified/Pending]
* **Traceability IDs (XX-UT-00X):** [Mapped/Missing]
* **Zero-Print Policy:** [Enforced/Violation Found]

---

## ⏭️ Next Step

**Current State:** [e.g., Stage 2 Verified]
**Action:** Triggering **Clean-Implementation** with `{root}` absolute import context.

---

