import time
from typing import Optional
from tantra.domain.models.text_segment import TextSegment
from tantra.domain.models.analysis_result import AnalysisResult
from tantra.density.domain.protocols.density_adapter import DensityAdapterProtocol
from tantra.density.infrastructure.shannon_adapter import ShannonEntropyAdapter

class DensityAnalyzer:
    """
    Core Logic for Density/Entropy Analysis.
    """
    
    def __init__(self, adapter: Optional[DensityAdapterProtocol] = None):
        self.adapter = adapter or ShannonEntropyAdapter()
        
    def analyze(self, segment: TextSegment) -> AnalysisResult:
        """
        Calculates Entropy.
        """
        score = self.adapter.calculate_entropy(segment.text)
        
        return AnalysisResult(
            analyzer_name="DensityAnalyzer",
            timestamp=time.time(),
            metrics={"entropy_score": score},
            signals={}
        )
