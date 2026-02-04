# Relation Unit Test Scenarios

## Happy Path

| ID | Scenario | Input | Expected Output |
| :--- | :--- | :--- | :--- |
| **[REL-UT-001]** | **Basic Extraction** | `text="A hits B"` | `relations`=[("A", "hits", "B")] |
| **[REL-UT-002]** | **Perfect Overlap** | `ref="A hits B"`, `target="A hits B"` | `overlap_score` = 1.0 |
| **[REL-UT-003]** | **Logic Change** | `ref="A hits B"`, `target="B hits A"` | `overlap_score` < 1.0 (Directionality matters) |

## Corner Cases

| ID | Scenario | Input | Expected Output |
| :--- | :--- | :--- | :--- |
| **[REL-UT-004]** | **No Relations** | `text="Hello world"` | `relations`=[] |
