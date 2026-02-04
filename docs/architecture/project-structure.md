# Project Architecture: Structure & Standards

## 1. Directory Structure (The "Physical" Architecture)
We follow a strict **Domain-Driven Design (DDD)** layout for code and a **Feature-Based** layout for documentation.

### A. Source Code (`src/bavans/`)
*   **Pattern:** `src/bavans/{module}/{layer}`
*   **Root:** The project config `pyproject.toml` defines `src/bavans` as the package root.
*   **Rules:**
    *   **Modules:** Feature-based isolation (e.g., `src/bavans/auth`).
    *   **Sub-Modules:** Recursive structure allowed (e.g., `src/bavans/auth/sso`).
    *   **Layers**:
        *   `domain/`: Pure business logic, Pydantic models, Protocols. **NO external dependencies.**
        *   `infrastructure/`: Database, API clients, File IO. Implements Domain Protocols.

### B. Documentation (`docs/`)
*   **Pattern:** `docs/features/{module}/{type}/`
*   **Rules:**
    *   **Root:** `docs/features/`
    *   **Module:** Folder matching the source module name (recursive for sub-modules).
    *   **The Documentation Suite:** Every module MUST have exactly these 4 sub-folders. Each folder can contain **multiple files** based on complexity and use cases.
        1.  `functional/`: What it does. (e.g., `README.md`, `workflows.md`, `permissions.md`)
        2.  `technical/`: How it works. (e.g., `architecture.md`, `schemas.md`, `api_spec.md`)
        3.  `unittest/`: Isolated logic verification.
            *   Must include files for: **Happy Path**, **Corner Cases**, and **Code Coverage** strategy.
            *   Example: `happy_path.md`, `edge_cases.md`, `coverage_plan.md`.
        4.  `e2etest/`: Integrated workflow verification.
            *   Must include files for: **Happy Path**, **Corner Cases**, and **System Coverage**.
            *   Example: `user_flow_A.md`, `error_handling_flow.md`.

---

## 2. Coding Standards (The "Logical" Architecture)

### A. Strict Pydantic Models
All data structures must be immutable, validated, and strict.

```python
from pydantic import BaseModel, ConfigDict

class DomainEntity(BaseModel):
    model_config = ConfigDict(
        frozen=True,        # Immutable (like Kotlin val)
        strict=True,        # No implicit type coercion
        extra='forbid'      # No unknown fields
    )
    id: str
    name: str
```

### B. Clean Architecture Compliance
*   **Dependency Rule:** `Domain` layer depends on NOTHING. `Infrastructure` depends on `Domain`.
*   **Protocols:** Use `typing.Protocol` to define interfaces in `Domain`.
*   **No Magic:** Explicit constructor injection for all dependencies.

### C. Testing Strategy
*   **Location:** `docs/features/{module}/test/` contains the *Plan*.
*   **Execution:** `tests/unit/{module}` and `tests/e2e/{module}` contain the *Code*.
*   **Mapping:** Every feature must have at least one corresponding Unit Test file and one E2E Test file.

---

## 3. Sub-Module Recursion
If a module has sub-modules (e.g., `reporting` -> `reporting/pdf_export`):
*   **Code:** `src/bavans/reporting/pdf_export/`
*   **Docs:** `docs/features/reporting/pdf_export/{functional,technical,test}/`
*   **Rule:** Treat sub-modules as fully independent components with their own Trinity.
