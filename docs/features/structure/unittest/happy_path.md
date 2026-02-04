# Structure Unit Test Scenarios

## Happy Path

| ID | Scenario | Input | Expected Output |
| :--- | :--- | :--- | :--- |
| **[STR-UT-001]** | **Basic Stats** | `text="One two. Three four."` | `avg`=2.0, `variance`=0.0 |
| **[STR-UT-002]** | **Variance Check** | `text="One. One two three."` | `avg`=2.0, `variance` > 0 |
| **[STR-UT-003]** | **Monotony** | `text="A B. C D. E F."` | `uniformity_score` high (bad?) or alert signals. |

## Corner Cases

| ID | Scenario | Input | Expected Output |
| :--- | :--- | :--- | :--- |
| **[STR-UT-004]** | **No Punctuation** | `text="One two three"` | 1 sentence, length 3. |
| **[STR-UT-005]** | **Empty** | `text=""` | `avg`=0, `variance`=0 |
