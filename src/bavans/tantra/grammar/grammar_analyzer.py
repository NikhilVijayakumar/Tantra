import time
from typing import Optional, Dict, List, Tuple
from collections import Counter
from tantra.domain.models.text_segment import TextSegment
from tantra.domain.models.analysis_result import AnalysisResult
from tantra.grammar.domain.protocols.grammar_adapter import GrammarAdapterProtocol
from tantra.grammar.infrastructure.regex_adapter import RegexGrammarAdapter

class GrammarAnalyzer:
    """
    Core Logic for Grammar Analysis (POS).
    """
    
    def __init__(self, adapter: Optional[GrammarAdapterProtocol] = None):
        self.adapter = adapter or RegexGrammarAdapter()
        
    def analyze(self, segment: TextSegment) -> AnalysisResult:
        """
        Analyzes POS distribution.
        """
        tagged = self.adapter.tag_pos(segment.text)
        
        counts = Counter(tag for token, tag in tagged)
        total = sum(counts.values())
        
        ratios = {}
        if total > 0:
            for tag, count in counts.items():
                ratios[tag] = count / total
                
        return AnalysisResult(
            analyzer_name="GrammarAnalyzer",
            timestamp=time.time(),
            metrics={}, # No scalar metric? maybe entropy?
            signals={
                "pos_counts": dict(counts),
                "pos_ratios": ratios,
                "tagged_tokens": tagged
            }
        )
