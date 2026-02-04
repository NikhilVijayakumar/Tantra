# Semantic Unit Test Scenarios

## Happy Path

| ID | Scenario | Input | Expected Output |
| :--- | :--- | :--- | :--- |
| **[SEM-UT-001]** | **Identical Texts** | `t1="A"`, `t2="A"` | `similarity_score` ~= 1.0 |
| **[SEM-UT-002]** | **Opposite/Different** | `t1="Day"`, `t2="Night"` | `similarity_score` < 0.5 |
| **[SEM-UT-003]** | **Drift Calculation** | `ref="A"`, `target="B"` | `drift_score` = `1 - similarity` |

## Corner Cases

| ID | Scenario | Input | Expected Output |
| :--- | :--- | :--- | :--- |
| **[SEM-UT-004]** | **Empty Input** | `t1=""` | Raise `ValueError` or return 0.0 (Safe Mode) |
| **[SEM-UT-005]** | **Whitespace Only** | `t1="   "` | Treat as Empty |
| **[SEM-UT-006]** | **Large Text** | `t1` > 1MB | Should process or chunk (performance check) |
