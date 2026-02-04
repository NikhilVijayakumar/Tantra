# Density Unit Test Scenarios

## Happy Path

| ID | Scenario | Input | Expected Output |
| :--- | :--- | :--- | :--- |
| **[DEN-UT-001]** | **Zero Entropy** | `text="AAAA"` | `entropy_score` = 0.0 |
| **[DEN-UT-002]** | **High Entropy** | `text="ABCDE"` | `entropy_score` > `text="AABBC"` |

## Corner Cases

| ID | Scenario | Input | Expected Output |
| :--- | :--- | :--- | :--- |
| **[DEN-UT-003]** | **Empty Text** | `text=""` | `entropy_score` = 0.0 |
