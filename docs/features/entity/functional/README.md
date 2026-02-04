# Entity Presence Module

## 🔎 Overview
The `entity` module tracks whether important terms, names, or concepts persist across transformations. It answers "Are the key characters/terms still there?"

## 🚀 Capabilities

### 1. Entity Extraction (NER)
*   **Goal:** Identify proper nouns, technical terms, or specific patterns.
*   **Metric:** `entity_count`.
*   **Signal:** List of detected entities `{ "PERSON": ["Alice"], "ORG": ["Google"] }`.

### 2. Presence Tracking (Continuity)
*   **Goal:** Verify if a specific list of "Must Have" entities exists in the text.
*   **Metric:** `retention_ratio` (0.0 to 1.0).
*   **Use Case:** Ensuring legal terms or character names aren't lost in summarization.

## 💻 Usage

```python
from bavans.tantra import initialize_tantra
from bavans.tantra.entity.api import EntityAnalyzer

system = initialize_tantra()
analyzer = EntityAnalyzer(system)

# 1. Extract
result = analyzer.extract("Alice went to Google.")
print(result.signals['entities']) # {'PERSON': ['Alice'], 'ORG': ['Google']}

# 2. Track Continuity
result = analyzer.track_presence(
    target="Alice went there.", 
    required_entities=["Alice", "Google"]
)
print(result.metrics['retention_ratio']) # 0.5 (Alice found, Google lost)
```
