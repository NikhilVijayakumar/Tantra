# TANTRA System Architecture

## 1. Architectural Philosophy
TANTRA is a **Protocol-Oriented NLP Library** designed for observation, structural analysis, and logical validation. Unlike pipelines that enforce a workflow, TANTRA provides **reusable primitives** that can be composed to build analysis tools.

### Core Principles
1.  **Observation over Intervention**: TANTRA measures and reports; it does not rewrite or judge.
2.  **Protocol-First**: Capabilities are defined as stable interfaces (Protocols). Implementations (Adapters) are interchangeable.
3.  **Domain Neutrality**: The core logic assumes no specific genre (technical, narrative, academic).

## 2. The Trinity: Protocol, Adapter, Signal

### A. Protocols (The Contract)
Located in `src/bavans/tantra/{feature}/domain/protocols/`.
Protocols define *what* can be observed, not *how* it is observed. They are pure Python `typing.Protocol` definitions depending only on Domain Models.

### B. Adapters (The Implementation)
Located in `src/bavans/tantra/{feature}/infrastructure/adapters/`.
Adapters implement the protocols using specific technologies (e.g., Spacy, NLTK, Transformers). Multiple adapters can exist for a single protocol.

### C. Signals (The Output)
Located in `src/bavans/tantra/{feature}/domain/models/`.
Signals are strict, immutable Pydantic models that encapsulate the observation results. They are the "Language" of TANTRA.

## 3. High-Level Dependency Graph

```mermaid
graph TD
    Client[Client Application] --> API[Public API (Builders/Factories)]
    API --> Domain[Domain Layer (Protocols + Models)]
    Infra[Infrastructure Layer (Adapters)] -- Implements --> Domain
    API -- Injects --> Infra
    
    subgraph "TANTRA Core"
        Domain
    end
    
    subgraph "External World"
        Spacy
        NLTK
        Transformers
    end
    
    Infra --> Spacy
    Infra --> NLTK
```

## 4. Analysis Capabilities (The 8 Pillars)
Each pillar corresponds to a module in `src/bavans/tantra/`:

1.  **Semantic Drift**: Measuring meaning shifts.
2.  **Entity Continuity**: Tracking named entities.
3.  **Relation Consistency**: Preserving graph structures.
4.  **Topic Structure**: Ordering and hierarchy of topics.
5.  **Rhythm & Structure**: Sentence variance and flow.
6.  **Information Density**: Entropy and term richness.
7.  **Grammatical Distribution**: POS balance.
8.  **Structural Deviations**: Anomaly detection.

## 5. Integration Pattern
Clients allow TANTRA to "observe" text. 
1.  Client instantiates an **Adapter** (or uses a Factory).
2.  Client invokes a **Protocol** method with text input.
3.  TANTRA returns a **Signal**.
4.  Client decides action (Report, Reject, Warn).

---
*For detailed folder structure standards, see `docs/architecture/project-structure.md`.*
