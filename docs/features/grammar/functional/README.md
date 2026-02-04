# Grammar & POS Module

## 🔎 Overview
The `grammar` module observes the grammatical composition of the text. It ignores specific words and focuses on their roles (Nouns, Verbs, Adjectives).

## 🚀 Capabilities

### 1. POS Distribution
*   **Goal:** Measure the ratio of different parts of speech.
*   **Metric:** `pos_ratios` (Dict: "NOUN": 0.4, "VERB": 0.2).
*   **Signal:** Raw counts `{"NOUN": 10, "VERB": 5}`.
*   **Use Case:** Analyzing excessive abstraction (too many nouns) or passive voice.

## 💻 Usage

```python
from bavans.tantra import initialize_tantra
from bavans.tantra.grammar.api import GrammarAnalyzer

system = initialize_tantra()
analyzer = GrammarAnalyzer(system)

result = analyzer.analyze("The cat runs fast.")
print(result.signals['pos_counts']) # {'DET': 1, 'NOUN': 1, 'VERB': 1, 'ADV': 1}
```
