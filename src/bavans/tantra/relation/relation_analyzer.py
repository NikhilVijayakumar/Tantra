import time
from typing import Optional, List, Set, Tuple
from tantra.domain.models.text_segment import TextSegment
from tantra.domain.models.analysis_result import AnalysisResult
from tantra.relation.domain.protocols.relation_adapter import RelationAdapterProtocol
from tantra.relation.infrastructure.regex_adapter import RegexRelationAdapter

class RelationAnalyzer:
    """
    Core Logic for Relation Analysis.
    """
    
    def __init__(self, adapter: Optional[RelationAdapterProtocol] = None):
        self.adapter = adapter or RegexRelationAdapter()
        
    def extract_relations(self, segment: TextSegment) -> AnalysisResult:
        """
        Extracts SVO triples.
        """
        triples = self.adapter.extract_triples(segment.text)
        
        return AnalysisResult(
            analyzer_name="RelationAnalyzer",
            timestamp=time.time(),
            metrics={"relation_count": float(len(triples))},
            signals={"relations": triples}
        )

    def compare_relations(self, source: TextSegment, target: TextSegment) -> AnalysisResult:
        """
        Checks relation overlap between two texts.
        """
        source_triples = set(self.adapter.extract_triples(source.text))
        target_triples = set(self.adapter.extract_triples(target.text))
        
        if not source_triples:
             # If source had no relations, target having none is perfect match? Or irrelevant?
             # Let's say if source is empty, score is 1.0 (trivial consistency).
             score = 1.0 if not target_triples else 0.0 # If target adds relations where source had none? allowed?
             return AnalysisResult(
                analyzer_name="RelationAnalyzer",
                timestamp=time.time(),
                metrics={"relation_overlap_score": 1.0}, # Trivial pass
                signals={"relations": []}
            )

        # Intersection
        common = source_triples.intersection(target_triples)
        
        # Jaccard? Or Recall?
        # Usually we care about "Did we PRESERVE the source?" -> Recall.
        # Score = Common / Source
        score = len(common) / len(source_triples)
        
        return AnalysisResult(
            analyzer_name="RelationAnalyzer",
            timestamp=time.time(),
            metrics={"relation_overlap_score": score},
            signals={
                "common_relations": list(common),
                "source_count": len(source_triples),
                "target_count": len(target_triples)
            }
        )
