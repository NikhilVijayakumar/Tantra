import re
from typing import List, Tuple
from tantra.relation.domain.protocols.relation_adapter import RelationAdapterProtocol

class RegexRelationAdapter:
    """
    Naive Triple Extractor.
    Extracts patterns like "Entity predicate Entity".
    """
    
    def extract_triples(self, text: str) -> List[Tuple[str, str, str]]:
        if not text:
            return []
            
        # Pattern: Capitalized Word + space + lowercase word + space + Capitalized Word
        # Simple heuristic for "A hits B"
        # Matches: "Alice likes Bob"
        pattern = r'\b([A-Z][a-z]*)\s+([a-z]+)\s+([A-Z][a-z]*)\b'
        
        matches = re.findall(pattern, text)
        return matches # Returns list of tuples
