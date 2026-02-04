import pytest
from tantra.topic.topic_analyzer import TopicAnalyzer
from tantra.domain.models.text_segment import TextSegment

@pytest.fixture
def analyzer():
    return TopicAnalyzer()

@pytest.mark.integration
def test_top_e2e_01_happy_path(analyzer):
    """
    ID: TOP-E2E-001
    Verify keyword extraction.
    """
    text = "Data data data. Code code."
    segment = TextSegment(text=text)
    result = analyzer.extract_topics(segment) # Fixed API
    
    topics = result.signals.get("topics")
    assert topics
    assert len(topics) > 0

@pytest.mark.integration
def test_top_e2e_03_empty(analyzer):
    """
    ID: TOP-E2E-003
    Verify empty input.
    """
    segment = TextSegment(text="")
    result = analyzer.extract_topics(segment)
    topics = result.signals.get("topics") or []
    assert not topics
