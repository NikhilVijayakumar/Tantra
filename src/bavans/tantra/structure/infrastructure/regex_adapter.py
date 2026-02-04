import re
from typing import List
from tantra.structure.domain.protocols.structure_adapter import StructureAdapterProtocol

class RegexStructureAdapter:
    """
    Naive Regex-Based Sentence Splitter.
    """
    
    def tokenize_sentences(self, text: str) -> List[str]:
        if not text:
            return []
        # Split on .!? followed by whitespace or EOL
        # Simple regex: (?<=[.!?])\s+
        # But this removes the delimiter? Or keeps it?
        # NLTK is better, but here we just want a rough split.
        
        sentences = re.split(r'(?<=[.!?])\s+', text)
        return [s.strip() for s in sentences if s.strip()]

    def count_words(self, text: str) -> int:
        if not text:
            return 0
        return len(text.split())
