import pytest
from tantra.semantic.semantic_analyzer import SemanticAnalyzer
from tantra.domain.models.text_segment import TextSegment

@pytest.fixture
def analyzer():
    return SemanticAnalyzer()

@pytest.mark.integration
def test_sem_e2e_01_happy_path(analyzer):
    """
    ID: SEM-E2E-001
    Verify standard analysis flow.
    SemanticAnalyzer is Drift/Similarity based.
    """
    text = "The quick brown fox."
    segment = TextSegment(text=text)
    
    # 1. Self-Analysis (Drift against self should be 0)
    # Context requires a target for similarity
    context = {"target": text}
    result = analyzer.analyze(segment, context)
    
    metrics = result.metrics
    assert "similarity_score" in metrics
    assert metrics["similarity_score"] > 0.99 # Should be 1.0

@pytest.mark.integration
def test_sem_e2e_02_corner_cases(analyzer):
    """
    ID: SEM-E2E-002
    Verify empty input handling.
    """
    # Analyzer raises ValueError on empty input? Code says:
    # if not segment.text: raise ValueError
    segment = TextSegment(text="")
    
    with pytest.raises(ValueError):
        analyzer.analyze(segment)

@pytest.mark.integration
def test_sem_e2e_03_max_coverage(analyzer):
    """
    ID: SEM-E2E-003
    Verify distinct texts.
    """
    segment = TextSegment(text="Apple")
    context = {"target": "Orange"}
    
    result = analyzer.analyze(segment, context)
    
    # Depending on embedding (BasicAdapter uses dummy logic?), sim might be < 1.0
    assert result.metrics["similarity_score"] < 1.0
