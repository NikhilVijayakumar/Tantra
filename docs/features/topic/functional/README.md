# Topic & Order Module

## 🔎 Overview
The `topic` module observes the thematic content of the text. It answers "What is this about?" and "In what order are ideas presented?"

## 🚀 Capabilities

### 1. Topic Extraction
*   **Goal:** Identify the main themes (keywords) in the text.
*   **Signal:** List of topics `["Space", "Rocket", "Mars"]`.

### 2. Sequence Structure (Ordering)
*   **Goal:** Determine if the order of topics matches a reference.
*   **Metric:** `sequence_match_score` (1.0 = Same order, 0.0 = Reversed/Scrambled).
*   **Use Case:** verifying narrative flow (Intro -> Body -> Conclusion).

## 💻 Usage

```python
from bavans.tantra import initialize_tantra
from bavans.tantra.topic.api import TopicAnalyzer

system = initialize_tantra()
analyzer = TopicAnalyzer(system)

# 1. Extract
result = analyzer.extract_topics("Rockets fly to space.")
print(result.signals['topics']) # ["Rockets", "space", "fly"]

# 2. Check Order
result = analyzer.validate_sequence(
    target="First A, then B.", 
    expected_sequence=["A", "B"]
)
print(result.metrics['sequence_match_score']) # 1.0
```
