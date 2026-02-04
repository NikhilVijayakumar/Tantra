import time
from typing import Optional, Dict, Any
from tantra.domain.models.analysis_result import AnalysisResult
from tantra.anomaly.domain.protocols.anomaly_adapter import AnomalyAdapterProtocol
from tantra.anomaly.infrastructure.statistical_adapter import StatisticalAdapter

class AnomalyAnalyzer:
    """
    Core Logic for Anomaly Detection.
    """
    
    def __init__(self, adapter: Optional[AnomalyAdapterProtocol] = None):
        self.adapter = adapter or StatisticalAdapter()
        
    # Note: This Analyzer deviates from standard `analyze(TextSegment)` pattern
    # because it analyzes Numbers (Metrics), not Text.
    # This is fine for a "Derivative" module.
    
    def detect_outlier(self, value: float, reference_stats: Dict[str, float], threshold: float = 3.0) -> AnalysisResult:
        """
        Detects if value is an outlier.
        reference_stats must contain 'mean' and 'std'.
        """
        mean = reference_stats.get("mean", 0.0)
        std = reference_stats.get("std", 1.0)
        
        z_score = self.adapter.calculate_z_score(value, mean, std)
        is_anom = self.adapter.is_outlier(z_score, threshold)
        
        return AnalysisResult(
            analyzer_name="AnomalyAnalyzer",
            timestamp=time.time(),
            metrics={"anomaly_score": z_score},
            signals={"is_anomaly": is_anom}
        )
