# Entity Module Design

## 🏗️ Architecture

### 1. Protocols
*   **`EntityAdapterProtocol`**:
    *   `extract_entities(text: str) -> Dict[str, List[str]]`
        *   Returns map of `Label -> [Values]`.

### 2. Domain Models (`domain/models/entity_models.py`)

No complex custom models needed yet, standard `AnalysisResult` is sufficient. 
Signals will carry the payload:
```json
{
  "entities": {
    "PERSON": ["Alice"],
    "DATE": ["2023-01-01"]
  },
  "missing": ["Bob"]
}
```

### 3. Data Flow
1.  **Input:** Client provides text and optional `required_entities`.
2.  **Adapter:** Scans text (using Regex or Spacy).
3.  **Core Logic:** 
    *   If `required_entities` provided: Calculate intersection.
    *   Else: Return raw extraction.
4.  **Output:** `AnalysisResult`.

## 🔌 Adapters
*   **`RegexEntityAdapter`:** Simple pattern matching (fallback).
*   **`SpacyEntityAdapter`:** Full NLP model.
