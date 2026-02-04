import pytest
from unittest.mock import MagicMock
from tantra.domain.models.text_segment import TextSegment

# Optimistic Import (RED Phase)
try:
    from tantra.relation.relation_analyzer import RelationAnalyzer
    from tantra.relation.domain.protocols.relation_adapter import RelationAdapterProtocol
except ImportError:
    pass

@pytest.fixture
def mock_relation_adapter():
    adapter = MagicMock()
    # Default: "A hits B" -> [("A", "hits", "B")]
    adapter.extract_triples.return_value = [("A", "hits", "B")]
    return adapter

@pytest.mark.unit
def test_rel_ut_001_basic_extraction(mock_relation_adapter):
    """[REL-UT-001] Basic Extraction should return triples"""
    try:
        analyzer = RelationAnalyzer(adapter=mock_relation_adapter)
    except NameError:
        pytest.fail("RelationAnalyzer not implemented")

    segment = TextSegment(text="A hits B")
    result = analyzer.extract_relations(segment)
    
    assert result.signals['relations'] == [("A", "hits", "B")]

@pytest.mark.unit
def test_rel_ut_002_perfect_overlap(mock_relation_adapter):
    """[REL-UT-002] Perfect Overlap should match 1.0"""
    try:
        analyzer = RelationAnalyzer(adapter=mock_relation_adapter)
    except NameError:
        pytest.fail("RelationAnalyzer not implemented")

    # Both calls return same triple
    mock_relation_adapter.extract_triples.return_value = [("A", "hits", "B")]
    
    seg1 = TextSegment(text="A hits B")
    seg2 = TextSegment(text="A hits B")
    
    result = analyzer.compare_relations(seg1, seg2)
    assert result.metrics['relation_overlap_score'] == 1.0

@pytest.mark.unit
def test_rel_ut_003_logic_change_mismatch(mock_relation_adapter):
    """[REL-UT-003] Logic Change should reduce score"""
    try:
        analyzer = RelationAnalyzer(adapter=mock_relation_adapter)
    except NameError:
        pytest.fail("RelationAnalyzer not implemented")

    # Source: A hits B
    # Target: B hits A
    # Mock behavior depending on input arg?
    # MagicMock side_effect with dict lookup
    
    def side_effect(text):
        if "A hits B" in text: return [("A", "hits", "B")]
        if "B hits A" in text: return [("B", "hits", "A")]
        return []
    
    mock_relation_adapter.extract_triples.side_effect = side_effect
    
    seg1 = TextSegment(text="A hits B")
    seg2 = TextSegment(text="B hits A")
    
    result = analyzer.compare_relations(seg1, seg2)
    assert result.metrics['relation_overlap_score'] == 0.0

@pytest.mark.unit
def test_rel_ut_004_no_relations(mock_relation_adapter):
    """[REL-UT-004] No Relations should return safe defaults"""
    try:
        analyzer = RelationAnalyzer(adapter=mock_relation_adapter)
    except NameError:
        pytest.fail("RelationAnalyzer not implemented")

    mock_relation_adapter.extract_triples.return_value = []
    
    segment = TextSegment(text="Hello world")
    result = analyzer.extract_relations(segment)
    
    assert result.signals['relations'] == []
