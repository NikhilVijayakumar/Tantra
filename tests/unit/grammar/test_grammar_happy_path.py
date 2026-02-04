import pytest
from unittest.mock import MagicMock
from tantra.domain.models.text_segment import TextSegment

# Optimistic Import (RED Phase)
try:
    from tantra.grammar.grammar_analyzer import GrammarAnalyzer
    from tantra.grammar.domain.protocols.grammar_adapter import GrammarAdapterProtocol
except ImportError:
    pass

@pytest.fixture
def mock_grammar_adapter():
    adapter = MagicMock()
    # Default: "Cat runs" -> [("Cat", "NOUN"), ("runs", "VERB")]
    adapter.tag_pos.return_value = [("Cat", "NOUN"), ("runs", "VERB")]
    return adapter

@pytest.mark.unit
def test_gra_ut_001_basic_tagging(mock_grammar_adapter):
    """[GRA-UT-001] Basic Tagging should return counts"""
    try:
        analyzer = GrammarAnalyzer(adapter=mock_grammar_adapter)
    except NameError:
        pytest.fail("GrammarAnalyzer not implemented")

    segment = TextSegment(text="Cat runs")
    result = analyzer.analyze(segment)
    
    assert result.signals['pos_counts']['NOUN'] == 1
    assert result.signals['pos_counts']['VERB'] == 1

@pytest.mark.unit
def test_gra_ut_002_ratios(mock_grammar_adapter):
    """[GRA-UT-002] Ratios should be calculated correctly"""
    try:
        analyzer = GrammarAnalyzer(adapter=mock_grammar_adapter)
    except NameError:
        pytest.fail("GrammarAnalyzer not implemented")

    segment = TextSegment(text="Cat runs")
    result = analyzer.analyze(segment)
    
    assert result.signals['pos_ratios']['NOUN'] == 0.5
    assert result.signals['pos_ratios']['VERB'] == 0.5

@pytest.mark.unit
def test_gra_ut_004_empty_text(mock_grammar_adapter):
    """[GRA-UT-004] Empty text should return empty dicts"""
    try:
        analyzer = GrammarAnalyzer(adapter=mock_grammar_adapter)
    except NameError:
        pytest.fail("GrammarAnalyzer not implemented")

    mock_grammar_adapter.tag_pos.return_value = []
    
    segment = TextSegment(text="")
    result = analyzer.analyze(segment)
    
    assert result.signals['pos_counts'] == {}
    assert result.signals['pos_ratios'] == {}
