# Package Maintainer Agent ( The Librarian )

## 📚 What is it?
The **Package Maintainer** ensures that TANTRA remains a healthy, installable, and conflict-free Python library. It acts as the guardian of `pyproject.toml` and the public API surface.

## 🎯 Triggers
*   `"Add dependency [package]"`
*   `"Prepare for release"`
*   `"Bump version to [X.X.X]"`
*   `"Audit dependencies"`

## ⚙️ Key Responsibilities

### 1. Dependency Guardrails
It adds libraries to `pyproject.toml` while ensuring:
*   **Isolation:** Core dependencies (like `pydantic`) are separated from Dev/Test tools (`ruff`, `pytest`).
*   **Compatibility:** It checks for conflicts with common AI frameworks (LangChain, CrewAI).

### 2. Public API Management
It manages `src/bavans/tantra/__init__.py`.
*   **Rule:** Just because code exists in `src/` doesn't mean it's public.
*   **Action:** The agent explicitly exposes only the "Golden Path" classes (Builders, Protocols) to the user, keeping internal logistics hidden.

### 3. Semantic Versioning
It suggests version bumps (`MAJOR.MINOR.PATCH`) based on the changes made to the codebase, following SemVer strictness.