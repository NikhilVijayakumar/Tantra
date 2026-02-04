# Quality Manager (Execution Protocol)

## 0. Environmental Sovereignty (Pre-Flight Check)

Before any action, the Manager MUST establish the execution context:
# Quality Manager Agent ( The Boss )

## 🧠 What is it?
The **Quality Manager** is the Orchestrator. It doesn't write code itself; it manages the entire team of agents to ensure the project moves forward according to the **TANTRA Constitution**.

It acts as the "State Machine", deciding which agent needs to work next based on the current state of your project.

## 🎯 Triggers
*   `"Act as Quality Manager"`
*   `"Create [Module]"` (The Manager will plan, test, and build it)
*   `"Audit the system"`
*   `"Fix all issues in [Module]"`

## ⚙️ How it works (The State Machine)

The Manager evaluates the project state in stages:

| Stage | Agent | Goal |
| :--- | :--- | :--- |
| **0. Environment** | **System** | Checks `.venv` and `pyproject.toml` are healthy. |
| **1. Planning** | **Doc Architect** | Ensures `docs/features/` exist and are valid. |
| **2. Scaffolding**| **Test Scaffolder**| Ensures `tests/unit/` exist and match the plan. |
| **3. Execution** | **Clean Impl.** | Ensures `src/` exists and passes tests. |
| **4. Verification**| **Verifier** | Ensures all reports (Coverage, Complexity) are Green. |

## 🕹️ Self-Healing
If you ask the Manager to "Create Auth", and it sees that Docs already exist, it will **skip** Step 1 and move to Step 2 (Tests). It adapts to your manual work seamlessly. (The Doctor's Audit)

Do not proceed to a handover if `scripts/project_doctor.py` identifies:

* **Relative Imports:** (`from .` or `import .` are banned).
* **Print Statements:** (Strict Zero-Print Policy).
* **Traceability Gaps:** (Missing `logger.info('[XX-UT-00X] ...')` in core logic).
* **Pydantic Violations:** (Models must be `frozen=True` and `strict=True`).
