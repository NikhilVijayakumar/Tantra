import re
from typing import List, Counter
from tantra.topic.domain.protocols.topic_adapter import TopicAdapterProtocol

class FrequencyTopicAdapter:
    """
    Naive Frequency-Based Topic Extractor.
    """
    
    STOPWORDS = {"the", "a", "an", "and", "or", "but", "in", "on", "at", "to", "of", "is", "are"}

    def extract_topics(self, text: str, top_n: int = 5) -> List[str]:
        if not text:
            return []
            
        # Normalize: Lower, remove punctuation
        clean = re.sub(r'[^\w\s]', '', text.lower())
        words = clean.split()
        
        # Filter stopwords
        keywords = [w for w in words if w not in self.STOPWORDS and len(w) > 1]
        
        # Count
        counts = Counter(keywords)
        
        # Return top N
        return [item[0] for item in counts.most_common(top_n)]
