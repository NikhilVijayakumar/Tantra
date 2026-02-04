import pytest
from unittest.mock import MagicMock
from tantra.domain.models.text_segment import TextSegment

# Optimistic Import (RED Phase)
try:
    from tantra.anomaly.anomaly_analyzer import AnomalyAnalyzer
    from tantra.anomaly.domain.protocols.anomaly_adapter import AnomalyAdapterProtocol
except ImportError:
    pass

@pytest.fixture
def mock_anomaly_adapter():
    adapter = MagicMock()
    return adapter

@pytest.mark.unit
def test_ano_ut_001_normal_value(mock_anomaly_adapter):
    """[ANO-UT-001] Normal value should return low score"""
    try:
        analyzer = AnomalyAnalyzer(adapter=mock_anomaly_adapter)
    except NameError:
        pytest.fail("AnomalyAnalyzer not implemented")

    # Mean=10, Std=1, Val=10 -> Z=0
    mock_anomaly_adapter.calculate_z_score.return_value = 0.0
    mock_anomaly_adapter.is_outlier.return_value = False
    
    # We pass a 'dummy' text segment because our interface demands it, 
    # but AnomalyAnalyzer is 'Derivative' - it analyzes stats.
    # How do we pass stats? Through context? Or special method?
    # Spec said "Usage: analyzer.detect_outlier(value, ref)".
    # So we should test that method, not analyze().
    
    result = analyzer.detect_outlier(value=10.0, reference_stats={"mean": 10.0, "std": 1.0})
    
    assert result.metrics['anomaly_score'] == 0.0
    assert result.signals['is_anomaly'] is False

@pytest.mark.unit
def test_ano_ut_002_outlier_high(mock_anomaly_adapter):
    """[ANO-UT-002] High value should normally be outlier"""
    try:
        analyzer = AnomalyAnalyzer(adapter=mock_anomaly_adapter)
    except NameError:
        pytest.fail("AnomalyAnalyzer not implemented")

    # Mean=10, Std=2, Val=20 -> Z=5
    mock_anomaly_adapter.calculate_z_score.return_value = 5.0
    mock_anomaly_adapter.is_outlier.return_value = True
    
    result = analyzer.detect_outlier(value=20.0, reference_stats={"mean": 10.0, "std": 2.0})
    
    assert result.metrics['anomaly_score'] == 5.0
    assert result.signals['is_anomaly'] is True

@pytest.mark.unit
def test_ano_ut_003_zero_std(mock_anomaly_adapter):
    """[ANO-UT-003] Zero Std Dev should handle gracefully"""
    try:
        analyzer = AnomalyAnalyzer(adapter=mock_anomaly_adapter)
    except NameError:
        pytest.fail("AnomalyAnalyzer not implemented")

    mock_anomaly_adapter.calculate_z_score.return_value = 0.0
    
    result = analyzer.detect_outlier(value=10.0, reference_stats={"mean": 10.0, "std": 0.0})
    
    assert result.metrics['anomaly_score'] == 0.0
