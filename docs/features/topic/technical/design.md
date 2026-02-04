# Topic Module Design

## 🏗️ Architecture

### 1. Protocols
*   **`TopicAdapterProtocol`**:
    *   `extract_topics(text: str, top_n: int = 5) -> List[str]`
        *   Returns ranked list of keywords/topics.

### 2. Domain Models

Standard `AnalysisResult`.
Signals Payload:
```json
{
  "topics": ["AI", "Robots"],
  "sequence_found": ["Intro", "AI"]
}
```

### 3. Data Flow
1.  **Input:** Client provides text.
2.  **Adapter:** Uses TF-IDF or simple Frequency Count to find top terms.
3.  **Core Logic:** 
    *   **Extraction:** Return top N terms.
    *   **Sequencing:** Check if terms appear in the text in the order specified by `expected_sequence`.
        *   Find index of first occurrence of each expected topic.
        *   Check if indices are monotonic increasing.
4.  **Output:** `AnalysisResult`.

## 🔌 Adapters
*   **`FrequencyTopicAdapter`:** Simple term frequency (stopword aware).
*   **`LDATopicAdapter`:** Latent Dirichlet Allocation (scikit-learn).
