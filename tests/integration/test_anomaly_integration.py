import pytest
from tantra.anomaly.anomaly_analyzer import AnomalyAnalyzer
# AnomalyAnalyzer operates on numeric values, not TextSegments

@pytest.fixture
def analyzer():
    return AnomalyAnalyzer()

@pytest.mark.integration
def test_ano_e2e_01_happy_path(analyzer):
    """
    ID: ANO-E2E-001
    Verify normal value detection.
    """
    val = 5.0
    stats = {"mean": 5.0, "std": 1.0}
    
    result = analyzer.detect_outlier(val, stats, threshold=3.0)
    
    assert result.signals["is_anomaly"] is False
    assert result.metrics["anomaly_score"] == 0.0

@pytest.mark.integration
def test_ano_e2e_02_outlier(analyzer):
    """
    ID: ANO-E2E-002
    Verify outlier detection.
    """
    val = 100.0
    stats = {"mean": 10.0, "std": 5.0} # 100 is (100-10)/5 = 18 sigma away
    
    result = analyzer.detect_outlier(val, stats)
    
    assert result.signals["is_anomaly"] is True

@pytest.mark.integration
def test_ano_e2e_03_no_crash(analyzer):
    """
    ID: ANO-E2E-003
    Verify robustness.
    """
    # Std 0 case?
    result = analyzer.detect_outlier(5.0, {"mean": 5.0, "std": 0.0})
    # Should not crash, Z-score might be handled gracefully by adapter
    assert result.metrics["anomaly_score"] is not None
