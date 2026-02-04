# Grammar Module Design

## 🏗️ Architecture

### 1. Protocols
*   **`GrammarAdapterProtocol`**:
    *   `tag_pos(text: str) -> List[Tuple[str, str]]`
        *   Returns list of (token, tag) pairs. Tags should be Universal POS (UPOS) if possible (NOUN, VERB, ADJ).

### 2. Domain Models

Standard `AnalysisResult`.
Signals Payload:
```json
{
  "pos_counts": {"NOUN": 10, "VERB": 5},
  "pos_ratios": {"NOUN": 0.5, "VERB": 0.25}
}
```

### 3. Data Flow
1.  **Input:** Client provides text.
2.  **Adapter:** Tokenizes and tags text.
3.  **Core Logic:** 
    *   Count tags.
    *   Calculate ratios (count / total_tokens).
4.  **Output:** `AnalysisResult`.

## 🔌 Adapters
*   **`RegexGrammarAdapter`:** Extremely limited (heuristic based on endings -ly, -tion). Mostly for testing infrastructure.
*   **`Spacy/NLTK`:** The real deal.
