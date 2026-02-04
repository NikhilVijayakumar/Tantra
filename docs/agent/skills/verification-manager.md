# Verification Manager ( The Quality Gatekeeper )

## 📏 What is it?
The **Verification Manager** is the ultimate judge. It checks if the software meets the "Gold Standard" by analyzing machine-readable reports. It does not guess—it looks at the data.

## 🎯 Triggers
*   `"Verify [Module]"`
*   `"Run full verification"`
*   `"Check system health"`

## 📊 The 8 Dimensions of Quality
This agent ensures your project is "All Green" across these metrics:

| Report | Checks For... | Remediation Owner |
| :--- | :--- | :--- |
| **Unit Tests** | Logic bugs, regressions. | **Clean Implementation** |
| **E2E Tests** | Broken user flows. | **Clean Implementation** |
| **Architecture** | Layer violations (Domain importing Infra). | **Refactor Agent** |
| **Complexity** | Functions that are too hard to read. | **Refactor Agent** |
| **Type Safety** | Python type errors (MyPy). | **Clean Implementation** |
| **Dependencies** | Circular imports. | **Refactor Agent** |
| **Packages** | Security vulnerabilities in libraries. | **Package Maintainer** |
| **Documentation**| Missing docs vs code (Drift). | **Doc Architect** |

## ⚙️ Workflow
1.  **Generate:** Runs the scanning tools (`pytest`, `mypy`, `ruff`).
2.  **Analyze:** detailed JSON reports.
3.  **Delegate:** If a check fails, it calls the **Remediation Owner** to fix it automatically.
4.  **Confirm:** Re-runs the check to prove the fix worked.
