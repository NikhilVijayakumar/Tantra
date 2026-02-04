import pytest
from unittest.mock import MagicMock
from tantra.domain.models.text_segment import TextSegment

# Optimistic Import (RED Phase)
try:
    from tantra.entity.entity_analyzer import EntityAnalyzer
    from tantra.entity.domain.protocols.entity_adapter import EntityAdapterProtocol
except ImportError:
    pass

@pytest.fixture
def mock_entity_adapter():
    adapter = MagicMock()
    # Default behavior: Returns Alice and Google
    adapter.extract_entities.return_value = {"PERSON": ["Alice"], "ORG": ["Google"]}
    return adapter

@pytest.mark.unit
def test_ent_ut_001_basic_extraction(mock_entity_adapter):
    """[ENT-UT-001] Basic Extraction should return raw signals"""
    try:
        analyzer = EntityAnalyzer(adapter=mock_entity_adapter)
    except NameError:
        pytest.fail("EntityAnalyzer not implemented")

    segment = TextSegment(text="Alice went to Google")
    result = analyzer.extract(segment)
    
    assert "Alice" in result.signals['entities']['PERSON']
    assert "Google" in result.signals['entities']['ORG']

@pytest.mark.unit
def test_ent_ut_002_full_retention(mock_entity_adapter):
    """[ENT-UT-002] Full Retention should be 1.0"""
    try:
        analyzer = EntityAnalyzer(adapter=mock_entity_adapter)
    except NameError:
        pytest.fail("EntityAnalyzer not implemented")

    segment = TextSegment(text="Alice at Google")
    # We mock the extractor to find them
    mock_entity_adapter.extract_entities.return_value = {"PERSON": ["Alice"], "ORG": ["Google"]}
    
    result = analyzer.track_presence(segment, required_entities=["Alice", "Google"])
    
    assert result.metrics['retention_ratio'] == 1.0
    assert result.signals['missing_entities'] == []

@pytest.mark.unit
def test_ent_ut_003_partial_retention(mock_entity_adapter):
    """[ENT-UT-003] Partial Retention should identify missing terms"""
    try:
        analyzer = EntityAnalyzer(adapter=mock_entity_adapter)
    except NameError:
        pytest.fail("EntityAnalyzer not implemented")

    segment = TextSegment(text="Alice here")
    # Adapter only finds Alice
    mock_entity_adapter.extract_entities.return_value = {"PERSON": ["Alice"]}
    
    result = analyzer.track_presence(segment, required_entities=["Alice", "Bob"])
    
    assert result.metrics['retention_ratio'] == 0.5
    assert "Bob" in result.signals['missing_entities']

@pytest.mark.unit
def test_ent_ut_005_empty_text(mock_entity_adapter):
    """[ENT-UT-005] Empty text should return 0 results safely"""
    try:
        analyzer = EntityAnalyzer(adapter=mock_entity_adapter)
    except NameError:
        pytest.fail("EntityAnalyzer not implemented")

    segment = TextSegment(text="")
    mock_entity_adapter.extract_entities.return_value = {}
    
    result = analyzer.extract(segment)
    assert not result.signals['entities'] # Empty dict
