import time
from typing import Optional, List, Dict, Any, Set
from tantra.domain.models.text_segment import TextSegment
from tantra.domain.models.analysis_result import AnalysisResult
from tantra.entity.domain.protocols.entity_adapter import EntityAdapterProtocol
from tantra.entity.infrastructure.regex_adapter import RegexEntityAdapter

class EntityAnalyzer:
    """
    Core Logic for Entity Analysis.
    """
    
    def __init__(self, adapter: Optional[EntityAdapterProtocol] = None):
        self.adapter = adapter or RegexEntityAdapter()
        
    def extract(self, segment: TextSegment) -> AnalysisResult:
        """
        Performs basic NER extraction.
        """
        entities = self.adapter.extract_entities(segment.text)
        
        # Count total
        total = sum(len(v) for v in entities.values())
        
        return AnalysisResult(
            analyzer_name="EntityAnalyzer",
            timestamp=time.time(),
            metrics={"entity_count": float(total)},
            signals={"entities": entities} 
        )

    def track_presence(self, segment: TextSegment, required_entities: List[str]) -> AnalysisResult:
        """
        Calculates retention of required entities.
        """
        extracted_map = self.adapter.extract_entities(segment.text)
        
        # Flatten detected entities into a single set for lookup (Case sensitive?)
        # Let's assume strict case for now as per test spec.
        detected_set: Set[str] = set()
        for v in extracted_map.values():
            detected_set.update(v)
            
        missing: List[str] = []
        found_count = 0
        
        for req in required_entities:
            if req in detected_set: # or any(req in d for d in detected_set)?
                found_count += 1
            else:
                missing.append(req)
                
        ratio = 0.0
        if required_entities:
            ratio = found_count / len(required_entities)
            
        return AnalysisResult(
            analyzer_name="EntityAnalyzer",
            timestamp=time.time(),
            metrics={"retention_ratio": ratio},
            signals={
                "missing_entities": missing,
                "found_count": found_count
            }
        )
