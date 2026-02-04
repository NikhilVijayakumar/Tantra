# Structural Analysis Module

## 🔎 Overview
The `structure` module observes the "Rhythm" of text. It ignores *what* is said and focuses on *how* it is shaped (Sentence Length, Variation).

## 🚀 Capabilities

### 1. Rhythm Analysis
*   **Goal:** Measure sentence length distribution.
*   **Metrics:** 
    *   `avg_sentence_length` (Float).
    *   `length_variance` (Float): High variance = Dynamic writing.
*   **Signal:** List of sentence lengths `[10, 15, 8, 40]`.

### 2. Burstiness / Uniformity
*   **Goal:** Detect "Monotony" (e.g., 5 sentences of exactly 10 words).
*   **Metric:** `uniformity_score` (0.0 to 1.0).

## 💻 Usage

```python
from bavans.tantra import initialize_tantra
from bavans.tantra.structure.api import StructureAnalyzer

system = initialize_tantra()
analyzer = StructureAnalyzer(system)

result = analyzer.analyze("Short sentence. Another short one.")
print(result.metrics['avg_sentence_length']) # ~3.0
print(result.metrics['length_variance'])     # Low
```
