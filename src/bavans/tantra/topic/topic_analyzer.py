import time
from typing import Optional, List, Dict, Any
from tantra.domain.models.text_segment import TextSegment
from tantra.domain.models.analysis_result import AnalysisResult
from tantra.topic.domain.protocols.topic_adapter import TopicAdapterProtocol
from tantra.topic.infrastructure.frequency_adapter import FrequencyTopicAdapter

class TopicAnalyzer:
    """
    Core Logic for Topic Analysis.
    """
    
    def __init__(self, adapter: Optional[TopicAdapterProtocol] = None):
        self.adapter = adapter or FrequencyTopicAdapter()
        
    def extract_topics(self, segment: TextSegment, top_n: int = 5) -> AnalysisResult:
        """
        Extracts key topics.
        """
        topics = self.adapter.extract_topics(segment.text, top_n)
        
        return AnalysisResult(
            analyzer_name="TopicAnalyzer",
            timestamp=time.time(),
            metrics={"topic_count": float(len(topics))},
            signals={"topics": topics}
        )

    def validate_sequence(self, segment: TextSegment, expected_sequence: List[str]) -> AnalysisResult:
        """
        Verifies if expected topics appear in order.
        """
        text = segment.text
        if not text:
            return AnalysisResult(
                analyzer_name="TopicAnalyzer",
                timestamp=time.time(),
                metrics={"sequence_match_score": 0.0},
                signals={"sequence_found": []}
            )

        # Simple string search logic
        last_index = -1
        found_in_order = []
        is_valid = True
        
        for topic in expected_sequence:
            # We search from the *beginning* or from *last_index*?
            # "Sequence": Order of availability.
            # If I say "A B A", and verify "A A", it matches 0, 4?
            # Let's search from last_index to ensure temporal order.
            
            # Note: find() returns -1 if not found.
            # We assume case-sensitive or insensitive? TextSegment assumes raw text.
            # Logic: We search for the term.
            
            current_index = text.find(topic, last_index + 1)
            
            if current_index != -1:
                last_index = current_index
                found_in_order.append(topic)
            else:
                # Not found AFTER the previous term
                is_valid = False
                break
                
        metrics = {
            "sequence_match_score": 1.0 if is_valid else 0.0
        }
        
        return AnalysisResult(
            analyzer_name="TopicAnalyzer",
            timestamp=time.time(),
            metrics=metrics,
            signals={"sequence_found": found_in_order}
        )
