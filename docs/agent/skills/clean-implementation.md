# Clean Implementation Agent ( The Builder )

## 🧱 What is it?
The **Clean Implementation** agent is the "General Contractor" of the TANTRA system. It takes the blueprints from the **Doc Architect** and the test scaffolding from the **Test Scaffolder** to write the actual production code.

It strictly adheres to **Clean Architecture**, **SOLID principles**, and **TANTRA's Constitution** (Zero-Print, Absolute Imports, Frozen Models).

## 🎯 Triggers
*   `"Implement [Module]"`
*   `"Fix the implementation of [File]"`
*   `"Refactor [File] to use Pydantic"`

## ⚙️ How it works
1.  **Reads the Plan:** It looks at `docs/features/{module}/technical/` to understand the architecture.
2.  **Reads the Tests:** It analyzes `tests/unit/{module}/` to understand the expected behavior.
3.  **Writes Code:** It creates the source files in `src/bavans/tantra/{module}/`.
    *   **Domain:** Pure Python logic, Pydantic models (`frozen=True`), Protocols.
    *   **Infrastructure:** Concrete implementations injected via constructors.
4.  **Validates:** It runs the tests to ensure green-light status.

## 📦 Outputs
*   `src/bavans/tantra/{module}/domain/models/*.py`
*   `src/bavans/tantra/{module}/domain/protocols/*.py`
*   `src/bavans/tantra/{module}/core.py` (The main logic)

## 🛡️ The "Constitution" Enforced
*   **Absolute Imports Only:** `from bavans.tantra.core import X` (No relative imports).
*   **No Print Statements:** only `logger` via injected Protocol.
*   **Immutable Config:** All settings via `TantraBaseSettings` (Pydantic).
*   **One Class, One File:** Strict file separation.