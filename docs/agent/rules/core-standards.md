# TANTRA Core Standards ( The Constitution )

This document defines the "Gold Standard" rules that all Agents enforce. If you write code manually, you **must** follow these rules to avoid auto-refactoring triggers.

## 1. Project Structure & Naming
*   **Root:** The project data lives in `.{ProjectName}/` (e.g., `.Tantra/`).
*   **Source:** Code lives in `src/bavans/tantra/` (or your configured root).
*   **Naming:**
    *   Files: `snake_case.py` (e.g., `user_manager.py`)
    *   Classes: `PascalCase` (e.g., `UserManager`)
    *   Variables: `snake_case` (e.g., `user_id`)
    *   **NO** Hungarian notation or "Interface" prefixes (e.g., `IUser`).

## 2. Architecture (DDD + Clean)
*   **Protocol-First:** Always define a `Protocol` in `domain/protocols/` before writing the implementation.
*   **Domain Isolation:** The `domain/` folder must be **Pure Python**. No imports from `infrastructure/`, `django`, `flask`, or external IO libs.
*   **One Class, One File:** Strict separation. No 500-line "utils.py" files.

## 3. Pydantic & Configuration
*   **Immutable Contracts:** All data models must be **Frozen** Pydantic models.
    ```python
    model_config = ConfigDict(frozen=True, strict=True, extra='forbid')
    ```
*   **No Magic Dicts:** Never pass `kwargs` or raw dictionaries. Use typed Models.

## 4. Imports (Absolute Only)
*   **Rule:** **NO** relative imports (`from . import x`).
*   **Constraint:** Always use the full path: `from bavans.tantra.domain.models import User`.
*   **Why?** This allows code to be moved refactored by agents without breaking pathing.

## 5. Logging (Zero-Print)
*   **Forbidden:** `print("DEBUG")` is strictly banned.
*   **Required:** Use `self.logger.info("[ID-001] Message")`.
*   **Injection:** Loggers are always injected via `__init__`, never instantiated globally.

## 6. Testing
*   **Traceability:** Every test must reference a Requirement ID (`AR-UT-001`).
*   **Location:**
    *   Unit Tests: `tests/unit/{module}/`
    *   E2E Tests: `tests/e2e/{module}/`
*   **Mocking:** Unit tests must mock ALL IO. E2E tests use `tmp_path`.