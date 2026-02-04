import pytest
from typing import Dict, List
from tantra.entity.entity_analyzer import EntityAnalyzer
from tantra.entity.domain.protocols.entity_adapter import EntityAdapterProtocol
from tantra.domain.models.text_segment import TextSegment

# 1. Define a "Alternative" Adapter (e.g., simulating Spacy or LLM)
class HighPrecisionEntityAdapter:
    """
    Simulates a 'Smarter' Adapter that might be in an optional module.
    """
    def extract_entities(self, text: str) -> Dict[str, List[str]]:
        # Simulating advanced recognition that Regex misses
        if "apple" in text.lower():
            return {"ORG": ["Apple Inc."]} # Smarter normalization
        return {}

@pytest.mark.integration
def test_adapter_switching_capability():
    """
    Demonstrates that TANTRA supports multiple implementations
    via dependency injection.
    """
    segment = TextSegment(text="I bought an apple phone.")

    # A. Default Behavior (Regex)
    # The default adapter (Regex) likely misses "apple" as it's lowercase here,
    # or finds nothing.
    analyzer_default = EntityAnalyzer() 
    result_default = analyzer_default.extract(segment)
    
    # B. Swapped Behavior (High Precision)
    # Client creates specific adapter (maybe from optional imports)
    smart_adapter = HighPrecisionEntityAdapter()
    analyzer_smart = EntityAnalyzer(adapter=smart_adapter)
    
    result_smart = analyzer_smart.extract(segment)
    
    # C. Verification
    # Default (Regex) finds nothing for lowercase 'apple'
    assert "Apple Inc." not in result_default.signals['entities'].get("ORG", [])
    
    # Smart Adapter finds it
    assert "Apple Inc." in result_smart.signals['entities']['ORG']
    
    # Proof: The Analyzer Logic (metrics, timestamp, envelope) remains consistent,
    # but the Intelligence source (Signal) was swapped.
