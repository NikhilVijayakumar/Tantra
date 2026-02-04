import pytest
from unittest.mock import MagicMock
from tantra.domain.models.text_segment import TextSegment

# Optimistic Import (RED Phase)
try:
    from tantra.structure.structure_analyzer import StructureAnalyzer
    from tantra.structure.domain.protocols.structure_adapter import StructureAdapterProtocol
except ImportError:
    pass

@pytest.fixture
def mock_struct_adapter():
    adapter = MagicMock()
    # Default: "One two. Three four."
    # sentences=["One two", "Three four"]
    # word_counts=[2, 2]
    adapter.tokenize_sentences.return_value = ["One two", "Three four"]
    adapter.count_words.side_effect = lambda t: len(t.split())
    return adapter

@pytest.mark.unit
def test_str_ut_001_basic_stats(mock_struct_adapter):
    """[STR-UT-001] Basic Stats: Avg=2.0, Variance=0.0"""
    try:
        analyzer = StructureAnalyzer(adapter=mock_struct_adapter)
    except NameError:
        pytest.fail("StructureAnalyzer not implemented")

    segment = TextSegment(text="One two. Three four.")
    result = analyzer.analyze(segment)
    
    # 2 terms, lengths [2, 2] -> Avg 2, Var 0
    assert result.metrics['avg_sentence_length'] == 2.0
    assert result.metrics['length_variance'] == 0.0

@pytest.mark.unit
def test_str_ut_002_variance_check(mock_struct_adapter):
    """[STR-UT-002] Variance Check: Avg=2.5, Variance > 0"""
    # "One. One two three." -> [1, 3] -> Avg 2.0, Var (1-2)^2 + (3-2)^2 / 2 = 1.0
    try:
        analyzer = StructureAnalyzer(adapter=mock_struct_adapter)
    except NameError:
        pytest.fail("StructureAnalyzer not implemented")

    mock_struct_adapter.tokenize_sentences.return_value = ["One", "One two three"]
    
    segment = TextSegment(text="One. One two three.")
    result = analyzer.analyze(segment)
    
    assert result.metrics['avg_sentence_length'] == 2.0
    assert result.metrics['length_variance'] > 0.0

@pytest.mark.unit
def test_str_ut_005_empty_text(mock_struct_adapter):
    """[STR-UT-005] Empty text should return 0 stats"""
    try:
        analyzer = StructureAnalyzer(adapter=mock_struct_adapter)
    except NameError:
        pytest.fail("StructureAnalyzer not implemented")

    mock_struct_adapter.tokenize_sentences.return_value = []
    
    segment = TextSegment(text="")
    result = analyzer.analyze(segment)
    
    assert result.metrics['avg_sentence_length'] == 0.0
    assert result.metrics['length_variance'] == 0.0
