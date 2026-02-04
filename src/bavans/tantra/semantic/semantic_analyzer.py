import time
from typing import Optional, Dict, Any
from tantra.domain.models.text_segment import TextSegment
from tantra.domain.models.analysis_result import AnalysisResult
from tantra.semantic.domain.protocols.semantic_adapter import SemanticAdapterProtocol
from tantra.semantic.infrastructure.basic_adapter import BasicSemanticAdapter

class SemanticAnalyzer:
    """
    Core Logic for Semantic Analysis.
    """
    
    def __init__(self, adapter: Optional[SemanticAdapterProtocol] = None):
        self.adapter = adapter or BasicSemanticAdapter()
        
    def analyze(self, segment: TextSegment, context: Optional[Dict[str, Any]] = None) -> AnalysisResult:
        """
        Analyzes the segment against a target in the context.
        """
        if not segment.text or not segment.text.strip():
            raise ValueError("Input text is empty")
            
        context = context or {}
        target_obj = context.get("target") # Expecting TextSegment or str?
        
        # Normalize target
        target_text = ""
        if isinstance(target_obj, TextSegment):
            target_text = target_obj.text
        elif isinstance(target_obj, str):
            target_text = target_obj
            
        if not target_text:
             # If no target, we can't do similarity. Return empty result or specific signal?
             # For now, let's assume target is required for "Compare" mode.
             pass

        # 1. Embed Source
        vec_source = self.adapter.embed(segment.text)
        
        # 2. Embed Target
        vec_target = self.adapter.embed(target_text)
        
        # 3. Calculate
        sim = self.adapter.cosine_similarity(vec_source, vec_target)
        drift = 1.0 - sim
        
        return AnalysisResult(
            analyzer_name="SemanticAnalyzer",
            timestamp=time.time(),
            metrics={
                "similarity_score": sim,
                "drift_score": drift
            },
            signals={
                "vector_dims": len(vec_source)
            }
        )
