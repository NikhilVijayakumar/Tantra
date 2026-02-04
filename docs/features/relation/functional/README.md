# Entity-Relation Module

## 🔎 Overview
The `relation` module observes the connections between entities. It ensures that the *logic* of the text (who did what to whom) is preserved or consistent.

## 🚀 Capabilities

### 1. Relation Extraction
*   **Goal:** Identify Subject-Verb-Object (SVO) triples or named relationships.
*   **Signal:** List of relations `[("Alice", "works_at", "Google")]`.

### 2. Consistency Checking (Logic Preservation)
*   **Goal:** Compare relations in a Target text against a Reference.
*   **Metric:** `relation_overlap_score` (0.0 to 1.0).
*   **Use Case:** Detecting causal inversions (e.g., "Fire caused smoke" vs "Smoke caused fire").

## 💻 Usage

```python
from bavans.tantra import initialize_tantra
from bavans.tantra.relation.api import RelationAnalyzer

system = initialize_tantra()
analyzer = RelationAnalyzer(system)

# 1. Extract
result = analyzer.extract_relations("Alice joined Google.")
print(result.signals['relations']) # [("Alice", "joined", "Google")]

# 2. Check Consistency
result = analyzer.compare_relations(
    source="Alice joined Google.",
    target="Google was joined by Alice." # Passive voice, same relation?
)
print(result.metrics['relation_overlap_score']) # Should be High
```
