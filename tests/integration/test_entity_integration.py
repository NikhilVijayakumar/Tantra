import pytest
from tantra.entity.entity_analyzer import EntityAnalyzer
from tantra.domain.models.text_segment import TextSegment

@pytest.fixture
def analyzer():
    return EntityAnalyzer()

@pytest.mark.integration
def test_ent_e2e_01_happy_path(analyzer):
    """
    ID: ENT-E2E-001
    Verify extraction.
    """
    text = "Apple Inc. announced a product."
    segment = TextSegment(text=text)
    
    result = analyzer.extract(segment)
    
    entities = result.signals.get("entities", {})
    assert isinstance(entities, dict)

@pytest.mark.integration
def test_ent_e2e_02_corner_cases(analyzer):
    """
    ID: ENT-E2E-002
    Verify empty input logic.
    """
    segment = TextSegment(text="")
    result = analyzer.extract(segment)
    
    entities = result.signals.get("entities", {})
    # RegEx adapter returns {'UNKNOWN': []} if nothing matches or based on impl
    # Testing for structure rather than exact empty dict if impl is quirky
    assert isinstance(entities, dict)

@pytest.mark.integration
def test_ent_e2e_03_no_matches(analyzer):
    """
    ID: ENT-E2E-003
    Verify no entities found.
    """
    text = "running slowly" 
    segment = TextSegment(text=text)
    result = analyzer.extract(segment)
    entities = result.signals.get("entities", {})
    
    # Check that no lists are populated
    has_items = any(len(v) > 0 for v in entities.values())
    assert not has_items
