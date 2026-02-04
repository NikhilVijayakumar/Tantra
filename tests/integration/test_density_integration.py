import pytest
from tantra.density.density_analyzer import DensityAnalyzer
from tantra.domain.models.text_segment import TextSegment

@pytest.fixture
def analyzer():
    return DensityAnalyzer()

@pytest.mark.integration
def test_den_e2e_01_happy_path(analyzer):
    """
    ID: DEN-E2E-001
    Verify density calculation.
    """
    text = "This is a sentence with information."
    segment = TextSegment(text=text)
    result = analyzer.analyze(segment) # Fixed API
    
    assert "entropy_score" in result.metrics
    assert result.metrics["entropy_score"] > 0

@pytest.mark.integration
def test_den_e2e_02_low_entropy(analyzer):
    """
    ID: DEN-E2E-002
    Verify repetitive text has lower entropy.
    """
    segment_normal = TextSegment(text="Random words here.")
    segment_repeat = TextSegment(text="A A A A A A.")
    
    res_norm = analyzer.analyze(segment_normal)
    res_rep = analyzer.analyze(segment_repeat)
    
    assert res_rep.metrics["entropy_score"] < res_norm.metrics["entropy_score"]

@pytest.mark.integration
def test_den_e2e_03_empty(analyzer):
    """
    ID: DEN-E2E-003
    Verify empty input.
    """
    segment = TextSegment(text="")
    result = analyzer.analyze(segment)
    assert result.metrics.get("entropy_score", 0.0) == 0.0
