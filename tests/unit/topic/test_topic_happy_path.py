import pytest
from unittest.mock import MagicMock
from tantra.domain.models.text_segment import TextSegment

# Optimistic Import (RED Phase)
try:
    from tantra.topic.topic_analyzer import TopicAnalyzer
    from tantra.topic.domain.protocols.topic_adapter import TopicAdapterProtocol
except ImportError:
    pass

@pytest.fixture
def mock_topic_adapter():
    adapter = MagicMock()
    # Default: "Apple apple orange" -> ["apple", "orange"]
    adapter.extract_topics.return_value = ["apple", "orange"] # Sorted by frequency
    return adapter

@pytest.mark.unit
def test_top_ut_001_basic_extraction(mock_topic_adapter):
    """[TOP-UT-001] Basic Extraction should return ranked topics"""
    try:
        analyzer = TopicAnalyzer(adapter=mock_topic_adapter)
    except NameError:
        pytest.fail("TopicAnalyzer not implemented")

    segment = TextSegment(text="Apple apple orange")
    result = analyzer.extract_topics(segment, top_n=2)
    
    assert result.signals['topics'] == ["apple", "orange"]

@pytest.mark.unit
def test_top_ut_002_sequence_match(mock_topic_adapter):
    """[TOP-UT-002] Sequence Match should return 1.0 for correct order"""
    try:
        analyzer = TopicAnalyzer(adapter=mock_topic_adapter)
    except NameError:
        pytest.fail("TopicAnalyzer not implemented")

    segment = TextSegment(text="First A then B")
    # For sequence check, we need to know WHERE topics are.
    # The Analyzer logic needs to find them in text.
    # So extraction alone isn't enough, we need positions? Or simple regex search in Analyzer?
    # Spec says "Sequencing: Check if terms appear in text in order".
    # Implementation decision: Analyzer does the search, Adapter gives the terms?
    # Or Adapter gives terms + positions?
    # Let's assume Analyzer simply searches for the strings in `expected_sequence`.
    
    result = analyzer.validate_sequence(segment, expected_sequence=["A", "B"])
    
    assert result.metrics['sequence_match_score'] == 1.0

@pytest.mark.unit
def test_top_ut_003_sequence_mismatch(mock_topic_adapter):
    """[TOP-UT-003] Sequence Mismatch should return 0.0"""
    try:
        analyzer = TopicAnalyzer(adapter=mock_topic_adapter)
    except NameError:
        pytest.fail("TopicAnalyzer not implemented")

    segment = TextSegment(text="First B then A")
    result = analyzer.validate_sequence(segment, expected_sequence=["A", "B"])
    
    assert result.metrics['sequence_match_score'] == 0.0 # B comes before A

@pytest.mark.unit
def test_top_ut_005_empty_text(mock_topic_adapter):
    """[TOP-UT-005] Empty text should return safe defaults"""
    try:
        analyzer = TopicAnalyzer(adapter=mock_topic_adapter)
    except NameError:
        pytest.fail("TopicAnalyzer not implemented")

    mock_topic_adapter.extract_topics.return_value = []
    
    segment = TextSegment(text="")
    result = analyzer.extract_topics(segment)
    
    assert result.signals['topics'] == []
