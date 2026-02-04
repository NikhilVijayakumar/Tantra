# Refactor Agent ( The Renovator )

## 🛠️ What is it?
The **Refactor Agent** is the "Fixer". It is triggered when code works but is "messy" (High Complexity) or "tangled" (Circular Dependencies). It improves the health of the codebase without changing external behavior.

## 🎯 Triggers
*   `"Refactor [File]"`
*   `"Reduce complexity in [Function]"`
*   `"Fix circular dependency"`

## ⚙️ Capabilities

### 1. Complexity Crusher
If a function has too many `if/else` statements (Cyclomatic Complexity > 10), the agent will:
*   Extract logic into private methods.
*   Move logic to a dedicated Strategy or Service class.
*   **Result:** Smaller, readable functions.

### 2. Dependency Untangling
If Module A imports B, and B imports A, the agent will:
*   Identify the shared logic.
*   Extract it to a third location (e.g., `domain/models/common.py`).
*   Update imports to break the cycle.

### 3. Safety First
The Refactor Agent **always** runs the Unit Tests before and after the change. If the tests fail after refactoring, it automatically reverts the changes.