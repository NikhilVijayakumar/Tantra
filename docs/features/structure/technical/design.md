# Structure Module Design

## 🏗️ Architecture

### 1. Protocols
*   **`StructureAdapterProtocol`**:
    *   `tokenize_sentences(text: str) -> List[str]`
    *   `count_words(text: str) -> int`

### 2. Domain Models

Standard `AnalysisResult`.
Signals Payload:
```json
{
  "sentence_lengths": [10, 15, 8],
  "monotony_alerts": [2] # Index of monotonous blocks
}
```

### 3. Data Flow
1.  **Input:** Client provides text.
2.  **Adapter:** Splits text into sentences. Counts words per sentence.
3.  **Core Logic:** 
    *   Calculate Mean, Variance (Std Dev).
    *   Detect consecutive identical lengths.
4.  **Output:** `AnalysisResult`.

## 🔌 Adapters
*   **`RegexStructureAdapter`:** Split on `[.!?]`.
*   **`NLTK/Spacy`:** Better sentence segmentation.
