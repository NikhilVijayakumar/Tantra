# TANTRA Core Protocols

## Overview
TANTRA uses a **Protocol-Oriented Architecture**. Capabilities are defined as stable interfaces (Protocols), allowing users to swap implementations (Adapters) without changing the consumption logic.

## 1. Core Observation Protocols

### `SemanticDriftProtocol`
Responsible for measuring meaning preservation or change between texts.

```python
from typing import Protocol, List, Dict
from pydantic import BaseModel

class DriftSignal(BaseModel):
    similarity_score: float
    segment_changes: List[Dict[str, float]]
    entropy_delta: float

class SemanticDriftProtocol(Protocol):
    def measure_drift(self, reference: str, candidate: str) -> DriftSignal:
        """Calculates semantic distance descriptors."""
        ...
```

### `EntityContinuityProtocol`
Responsible for tracking entity presence across transformations.

```python
class EntitySignal(BaseModel):
    missing_entities: List[str]
    retention_ratio: float
    added_entities: List[str]

class EntityContinuityProtocol(Protocol):
    def check_continuity(self, reference_entities: List[str], candidate_text: str) -> EntitySignal:
        """Observes which entities persisted."""
        ...
```

### `StructureProtocol`
Responsible for measuring sentence-level structure and variance (Rhythm).

```python
class StructureMetrics(BaseModel):
    sentence_length_std_dev: float
    burstiness_score: float
    length_distribution: List[int]

class StructureProtocol(Protocol):
    def analyze_structure(self, text: str) -> StructureMetrics:
        """Calculates structural statistics."""
        ...
```

## 2. Implementation Guidelines
*   **Implementations** reside in `src/bavans/{module}/infrastructure/`.
*   **Injection:** Protocols should be injected via `__init__` for dependency inversion.
*   **State:** Implementations should generally be stateless adapters.
