import pytest
from tantra.relation.relation_analyzer import RelationAnalyzer
from tantra.domain.models.text_segment import TextSegment

@pytest.fixture
def analyzer():
    return RelationAnalyzer()

@pytest.mark.integration
def test_rel_e2e_01_happy_path(analyzer):
    """
    ID: REL-E2E-001
    Verify relation extraction.
    """
    text = "John works for Acme."
    segment = TextSegment(text=text)
    result = analyzer.extract_relations(segment) # Fixed API
    
    relations = result.signals.get("relations")
    assert isinstance(relations, list)

@pytest.mark.integration
def test_rel_e2e_03_empty(analyzer):
    """
    ID: REL-E2E-003
    Verify empty input.
    """
    segment = TextSegment(text="")
    result = analyzer.extract_relations(segment)
    relations = result.signals.get("relations")
    assert not relations
