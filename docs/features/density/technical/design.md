# Density Module Design

## 🏗️ Architecture

### 1. Protocols
*   **`DensityAdapterProtocol`**:
    *   `calculate_entropy(text: str) -> float`
        *   Calculates Shannon Entropy.

### 2. Domain Models

Standard `AnalysisResult`.

### 3. Data Flow
1.  **Input:** Client provides text.
2.  **Adapter:** 
    *   Count character frequencies.
    *   Apply Shannon Entropy Formula: `H = -sum(p(x) * log2(p(x)))`.
3.  **Output:** `AnalysisResult` with `entropy_score`.

## 🔌 Adapters
*   **`ShannonEntropyAdapter`:** Standard Character-level entropy.
*   **`WordEntropyAdapter`:** Word-level (optional future).
