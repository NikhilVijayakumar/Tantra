import pytest
from unittest.mock import MagicMock
from tantra.domain.models.text_segment import TextSegment

# Optimistic Import (RED Phase)
try:
    from tantra.density.density_analyzer import DensityAnalyzer
    from tantra.density.domain.protocols.density_adapter import DensityAdapterProtocol
except ImportError:
    pass

@pytest.fixture
def mock_density_adapter():
    adapter = MagicMock()
    # Default behavior not strictly needed if we test per case
    return adapter

@pytest.mark.unit
def test_den_ut_001_zero_entropy(mock_density_adapter):
    """[DEN-UT-001] AAAA should have 0 entropy"""
    try:
        analyzer = DensityAnalyzer(adapter=mock_density_adapter)
    except NameError:
        pytest.fail("DensityAnalyzer not implemented")

    mock_density_adapter.calculate_entropy.return_value = 0.0
    
    segment = TextSegment(text="AAAA")
    result = analyzer.analyze(segment)
    
    assert result.metrics['entropy_score'] == 0.0

@pytest.mark.unit
def test_den_ut_002_high_entropy(mock_density_adapter):
    """[DEN-UT-002] ABCDE > AABBC"""
    try:
        analyzer = DensityAnalyzer(adapter=mock_density_adapter)
    except NameError:
        pytest.fail("DensityAnalyzer not implemented")

    # Mock behavior: Higher text variation -> Higher float
    def side_effect(text):
        if text == "ABCDE": return 2.32
        if text == "AABBC": return 1.52
        return 0.0
        
    mock_density_adapter.calculate_entropy.side_effect = side_effect
    
    seg1 = TextSegment(text="ABCDE")
    seg2 = TextSegment(text="AABBC")
    
    res1 = analyzer.analyze(seg1)
    res2 = analyzer.analyze(seg2)
    
    assert res1.metrics['entropy_score'] > res2.metrics['entropy_score']

@pytest.mark.unit
def test_den_ut_003_empty_text(mock_density_adapter):
    """[DEN-UT-003] Empty text should be 0.0"""
    try:
        analyzer = DensityAnalyzer(adapter=mock_density_adapter)
    except NameError:
        pytest.fail("DensityAnalyzer not implemented")

    mock_density_adapter.calculate_entropy.return_value = 0.0
    
    segment = TextSegment(text="")
    result = analyzer.analyze(segment)
    
    assert result.metrics['entropy_score'] == 0.0
