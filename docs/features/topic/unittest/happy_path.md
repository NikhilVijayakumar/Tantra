# Topic Unit Test Scenarios

## Happy Path

| ID | Scenario | Input | Expected Output |
| :--- | :--- | :--- | :--- |
| **[TOP-UT-001]** | **Basic Extraction** | `text="Apple apple orange"` | `topics`=["apple", "orange"] (ranked) |
| **[TOP-UT-002]** | **Sequence Match** | `text="First A then B"`, `expected=["A", "B"]` | `sequence_match_score` = 1.0 |
| **[TOP-UT-003]** | **Sequence Mismatch** | `text="First B then A"`, `expected=["A", "B"]` | `sequence_match_score` < 1.0 (0.0 if strict) |

## Corner Cases

| ID | Scenario | Input | Expected Output |
| :--- | :--- | :--- | :--- |
| **[TOP-UT-004]** | **Topic Not Found** | `text="Only A"`, `expected=["A", "B"]` | `missing_topics`=["B"], score penalty. |
| **[TOP-UT-005]** | **Empty Text** | `text=""` | `topics`=[], `sequence_score`=0.0 |
