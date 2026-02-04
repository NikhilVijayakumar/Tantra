import re
from typing import Dict, List, Any
from tantra.entity.domain.protocols.entity_adapter import EntityAdapterProtocol

class RegexEntityAdapter:
    """
    Naive Regex-Based NER.
    Reliable for simple testing or specific patterns.
    """
    
    def extract_entities(self, text: str) -> Dict[str, List[str]]:
        # Naive: Find capitalized words in middle of sentences?
        # Better: Just find words starting with Capital (simplistic Proper Noun detection)
        # Note: This is just a fallback/placeholder. Real NER needs Spacy.
        
        entities: Dict[str, List[str]] = {"UNKNOWN": []}
        
        # Regex for capitalized words
        matches = re.findall(r'\b[A-Z][a-z]*\b', text)
        if matches:
            entities["UNKNOWN"] = matches
            
        return entities
