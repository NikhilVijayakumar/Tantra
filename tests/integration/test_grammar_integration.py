import pytest
from tantra.grammar.grammar_analyzer import GrammarAnalyzer
from tantra.domain.models.text_segment import TextSegment

@pytest.fixture
def analyzer():
    return GrammarAnalyzer()

@pytest.mark.integration
def test_gra_e2e_01_happy_path(analyzer):
    """
    ID: GRA-E2E-001
    Verify POS tagging.
    """
    text = "The cat sat."
    segment = TextSegment(text=text)
    result = analyzer.analyze(segment) # Fixed API
    
    counts = result.signals.get("pos_counts")
    assert counts
    assert counts.get("NOUN", 0) > 0 or counts.get("PROPN", 0) > 0

@pytest.mark.integration
def test_gra_e2e_02_empty(analyzer):
    """
    ID: GRA-E2E-002
    Verify empty input.
    """
    segment = TextSegment(text="")
    result = analyzer.analyze(segment)
    counts = result.signals.get("pos_counts") or {}
    assert sum(counts.values()) == 0
