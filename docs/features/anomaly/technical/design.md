# Anomaly Module Design

## 🏗️ Architecture

### 1. Protocols
*   **`AnomalyAdapterProtocol`**:
    *   `calculate_z_score(value: float, mean: float, std: float) -> float`
    *   `is_outlier(z_score: float, threshold: float = 3.0) -> bool`

### 2. Domain Models

Standard `AnalysisResult`.

### 3. Data Flow
1.  **Input:** Client provides `value` and `reference_stats`.
2.  **Adapter:** Computes Z-Score `(x - mean) / std`.
3.  **Core Logic:** compares against Threshold (default 3.0).
4.  **Output:** `AnalysisResult` with `anomaly_score`.

## 🔌 Adapters
*   **`StatisticalAdapter`:** Pure math implementation.
