# Semantic Module Design

## 🏗️ Architecture

### 1. Protocols
*   **`SemanticAdapterProtocol`**:
    *   `embed(text: str) -> List[float]`
    *   `cosine_similarity(vec_a, vec_b) -> float`

### 2. Domain Models (`domain/models/semantic_models.py`)

```python
class SemanticResult(AnalysisResult):
    """
    Specialized result for semantic operations.
    """
    reference_text: Optional[str] = None
    target_text: str
```

### 3. Data Flow
1.  **Input:** Client provides `target` and `reference` texts.
2.  **Adapter:** Converts both to Vectors (Embeddings).
3.  **Core Logic:** Calculates Cosine Similarity.
4.  **Output:** `AnalysisResult` with `similarity_score` in metrics.

## 🔌 Adapters
*   **Default:** `SpacyAdapter` (Lightweight).
*   **Advanced:** `TransformerAdapter` (High precision, requires torch).
