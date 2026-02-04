# Doc Architect Agent ( The Planner )

## 🏗️ What is it?
The **Doc Architect** is the "Feature Planner". Before a single line of code is written, this agent designs the **Functional**, **Technical**, and **Test** specifications (The Trinity).

It ensures that every feature is well-thought-out, strictly scoped, and ready for implementation.

## 🎯 Triggers
*   `"Document [Module]"`
*   `"Plan a new [Feature]"`
*   `"Scaffold the docs for [Task]"`

## ⚙️ Key Concepts

### 1. The Trinity Strategy
For every feature, the Architect creates three documentation types in `docs/features/{module}/`:

1.  **Functional (`functional/README.md`):**
    *   **Audience:** Users / Product Owners.
    *   **Content:** What does it do? How do I use it?

2.  **Technical (`technical/design.md`):**
    *   **Audience:** Developers.
    *   **Content:** Data schemas (Pydantic), Protocols, and Data Flow.

3.  **Test Plan (`unittest/happy_path.md`, `e2etest/scenarios.md`):**
    *   **Audience:** QA / Automation.
    *   **Content:** Specific scenarios with strict IDs (e.g., `[AUTH-UT-001]`).

### 2. Platform Agnosticism
The blueprints are written in plain English + Pseudo-Schema. They can be implemented in Python, Kotlin, or TypeScript without changing the design document.

### 3. Traceability
The Architect assigns a unique **ID** to every requirement. The **Verified** later checks if these IDs appear in the logs and tests.