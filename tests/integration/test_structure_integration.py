import pytest
from tantra.structure.structure_analyzer import StructureAnalyzer
from tantra.domain.models.text_segment import TextSegment

@pytest.fixture
def analyzer():
    return StructureAnalyzer()

@pytest.mark.integration
def test_str_e2e_01_happy_path(analyzer):
    """
    ID: STR-E2E-001
    Verify multi-sentence structure.
    """
    text = "Sentence one. Sentence two."
    segment = TextSegment(text=text)
    result = analyzer.analyze(segment) # Fixed API
    
    metrics = result.metrics
    assert metrics.get("avg_sentence_length", 0) > 0
    assert result.signals.get("sentence_count", 0) == 2

@pytest.mark.integration
def test_str_e2e_02_single_sentence(analyzer):
    """
    ID: STR-E2E-002
    Verify single sentence.
    """
    text = "Hi."
    segment = TextSegment(text=text)
    result = analyzer.analyze(segment)
    
    assert result.signals.get("sentence_count") == 1

@pytest.mark.integration
def test_str_e2e_03_empty(analyzer):
    """
    ID: STR-E2E-003
    Verify empty input.
    """
    segment = TextSegment(text="")
    result = analyzer.analyze(segment)
    
    assert result.signals.get("sentence_count") == 0
    assert result.metrics.get("avg_sentence_length") == 0.0
