import time
import math
from typing import Optional, Dict, Any, List
from tantra.domain.models.text_segment import TextSegment
from tantra.domain.models.analysis_result import AnalysisResult
from tantra.structure.domain.protocols.structure_adapter import StructureAdapterProtocol
from tantra.structure.infrastructure.regex_adapter import RegexStructureAdapter

class StructureAnalyzer:
    """
    Core Logic for Structural Analysis (Rhythm).
    """
    
    def __init__(self, adapter: Optional[StructureAdapterProtocol] = None):
        self.adapter = adapter or RegexStructureAdapter()
        
    def analyze(self, segment: TextSegment) -> AnalysisResult:
        """
        Calculates Sentence Length stats.
        """
        sentences = self.adapter.tokenize_sentences(segment.text)
        
        if not sentences:
            return AnalysisResult(
                analyzer_name="StructureAnalyzer",
                timestamp=time.time(),
                metrics={"avg_sentence_length": 0.0, "length_variance": 0.0},
                signals={"sentence_lengths": [], "sentence_count": 0}
            )
            
        # Calculate lengths
        lengths: List[int] = [self.adapter.count_words(s) for s in sentences]
        
        # Mean
        total_words = sum(lengths)
        count = len(lengths)
        mean = total_words / count
        
        # Variance
        variance = 0.0
        if count > 1:
            variance = sum((x - mean) ** 2 for x in lengths) / count # Population variance or sample?
            # Let's use simple population variance for descriptive stats
        
        return AnalysisResult(
            analyzer_name="StructureAnalyzer",
            timestamp=time.time(),
            metrics={
                "avg_sentence_length": mean,
                "length_variance": variance
            },
            signals={
                "sentence_lengths": lengths,
                "sentence_count": count
            }
        )
