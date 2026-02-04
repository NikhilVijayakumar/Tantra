# Anomaly Detection Module

## 🔎 Overview
The `anomaly` module observes whether a specific metric (e.g., Sentence Length, Entropy) is "normal" relative to a baseline.

## 🚀 Capabilities

### 1. Z-Score / Outlier Detection
*   **Goal:** Flag values that are > N standard deviations from the mean.
*   **Metric:** `anomaly_score` (Absolute Z-Score).
*   **Signal:** `is_anomaly` (Boolean).
*   **Use Case:** Flagging a sudden drop in complexity or a spike in sentence length.

## 💻 Usage

```python
from bavans.tantra import initialize_tantra
from bavans.tantra.anomaly.api import AnomalyAnalyzer

system = initialize_tantra()
analyzer = AnomalyAnalyzer(system)

# Detect if "50" is an outlier in a distribution with Mean=10, Std=2
result = analyzer.detect_outlier(value=50, reference_stats={"mean": 10, "std": 2})
print(result.signals['is_anomaly']) # True
```
