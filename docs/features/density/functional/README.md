# Information Density Module

## 🔎 Overview
The `density` module observes the "richness" of the text. It uses Information Theory (Shannon Entropy) to measure how predictable the text is.

## 🚀 Capabilities

### 1. Entropy Calculation
*   **Goal:** Measure the randomness/information content.
*   **Metric:** `entropy_score` (Float, typically 0.0 to ~5.0 for English char-level).
*   **Use Case:** Detecting repetition or "fluff" (Low Entropy) vs dense technical text (High Entropy).

## 💻 Usage

```python
from bavans.tantra import initialize_tantra
from bavans.tantra.density.api import DensityAnalyzer

system = initialize_tantra()
analyzer = DensityAnalyzer(system)

result = analyzer.analyze("AAAAA") 
print(result.metrics['entropy_score']) # Close to 0.0 (Very predictable)

result = analyzer.analyze("XyZ1@")
print(result.metrics['entropy_score']) # High (Unpredictable)
```
