from typing import Protocol, Any, Dict, List, Optional, runtime_checkable

from tantra.domain.models.text_segment import TextSegment
from tantra.domain.models.analysis_result import AnalysisResult

@runtime_checkable
class AnalyzerProtocol(Protocol):
    """
    The Core Protocol for any TANTRA analysis module.
    Each capability (Semantic, Entity, etc.) will implement a specialized version of this
    or usage this directly.
    """
    
    def analyze(self, segment: TextSegment, context: Optional[Dict[str, Any]] = None) -> AnalysisResult:
        """
        Perform the analysis on the given text segment.
        
        Args:
            segment: The standardized text input.
            context: Optional context for the analysis (e.g. reference text for drift).
            
        Returns:
            AnalysisResult: The standardized output containing metrics and signals.
        """
        ...

@runtime_checkable
class AdapterProtocol(Protocol):
    """
    The Protocol for underlying adapters (e.g., SpaCy, Transformers, NLTK).
    Allows swapping the 'How' without changing the 'What'.
    """
    
    def process(self, text: str, **kwargs) -> Any:
        """
        Process raw text and return implementation-specific raw data.
        """
        ...
