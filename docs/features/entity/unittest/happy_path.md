# Entity Unit Test Scenarios

## Happy Path

| ID | Scenario | Input | Expected Output |
| :--- | :--- | :--- | :--- |
| **[ENT-UT-001]** | **Basic Extraction** | `text="Alice runs"` | `signals['entities']` contains "Alice" |
| **[ENT-UT-002]** | **Full Retention** | `text="A B"`, `required=["A", "B"]` | `retention_ratio` = 1.0, `missing` = [] |
| **[ENT-UT-003]** | **Partial Retention** | `text="A"`, `required=["A", "B"]` | `retention_ratio` = 0.5, `missing` = ["B"] |

## Corner Cases

| ID | Scenario | Input | Expected Output |
| :--- | :--- | :--- | :--- |
| **[ENT-UT-004]** | **Case Sensitivity** | `text="alice"`, `required=["Alice"]` | Depends on config (Default: Strict/False?) Let's assume Case-Insensitive for robustness? **Correction:** NER is usually Case Sensitive. Retention should probably be strict by default. |
| **[ENT-UT-005]** | **Empty Text** | `text=""` | `entities` = {}, `retention` = 0.0 |
