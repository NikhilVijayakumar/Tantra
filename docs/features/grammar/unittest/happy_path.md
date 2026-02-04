# Grammar Unit Test Scenarios

## Happy Path

| ID | Scenario | Input | Expected Output |
| :--- | :--- | :--- | :--- |
| **[GRA-UT-001]** | **Basic Tagging** | `text="Cat runs"` | `counts`={"NOUN": 1, "VERB": 1} |
| **[GRA-UT-002]** | **Ratios** | `text="Cat runs"` | `ratios`={"NOUN": 0.5, "VERB": 0.5} |

## Corner Cases

| ID | Scenario | Input | Expected Output |
| :--- | :--- | :--- | :--- |
| **[GRA-UT-003]** | **Unknown Tags** | `text="X Y Z"` | `counts`={"UNK": 3} (if adapter fails) |
| **[GRA-UT-004]** | **Empty Text** | `text=""` | `counts`={}, `ratios`={} |
