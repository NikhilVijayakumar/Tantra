# Anomaly Unit Test Scenarios

## Happy Path

| ID | Scenario | Input | Expected Output |
| :--- | :--- | :--- | :--- |
| **[ANO-UT-001]** | **Normal Value** | `val=10`, `mean=10`, `std=1` | `z_score`=0.0, `is_anomaly`=False |
| **[ANO-UT-002]** | **Outlier High** | `val=20`, `mean=10`, `std=2` | `z_score`=5.0, `is_anomaly`=True |

## Corner Cases

| ID | Scenario | Input | Expected Output |
| :--- | :--- | :--- | :--- |
| **[ANO-UT-003]** | **Zero Std Dev** | `val=10`, `mean=10`, `std=0` | `z_score`=0.0 (Avoid Div/0) |
