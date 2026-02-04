# Semantic Analysis Module

## 🔎 Overview
The `semantic` module observes meaning preservation or change between texts. It uses vector embeddings (via adapters) to quantify how similar two segments are.

## 🚀 Capabilities

### 1. Drift Detection
*   **Goal:** Measure how much a text has "moved" from a reference point.
*   **Metric:** `drift_score` (0.0 = Identical, 1.0 = Completely Different).
*   **Use Case:** Tracking edit distance in meaning during content revision.

### 2. Similarity Scoring
*   **Goal:** Compare two distinct texts for equivalence.
*   **Metric:** `similarity_score` (Cosine Similarity: -1.0 to 1.0).

## 💻 Usage

```python
from bavans.tantra import initialize_tantra
from bavans.tantra.semantic.api import SemanticAnalyzer

# 1. Init
system = initialize_tantra()
analyzer = SemanticAnalyzer(system)

# 2. Analyze
result = analyzer.compare("Hello World", "Hi Earth")
print(result.metrics['similarity_score'])
```
