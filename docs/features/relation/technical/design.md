# Relation Module Design

## 🏗️ Architecture

### 1. Protocols
*   **`RelationAdapterProtocol`**:
    *   `extract_triples(text: str) -> List[Tuple[str, str, str]]`
        *   Returns list of (Subject, Predicate, Object).

### 2. Domain Models

Standard `AnalysisResult`.
Signals Payload:
```json
{
  "relations": [["Alice", "works_at", "Google"]],
  "inverted_relations": [] 
}
```

### 3. Data Flow
1.  **Input:** Client provides text.
2.  **Adapter:** Parses dependency tree (or heuristic) to find triples.
3.  **Core Logic:** 
    *   **Normalization:** Verify if "A -> B" exists.
    *   **Comparison:** Check overlap between sets of triples.
4.  **Output:** `AnalysisResult`.

## 🔌 Adapters
*   **`RegexRelationAdapter`:** Very limited (detects "X implies Y").
*   **`SpacyRelationAdapter`:** Dependency parsing based extraction.
