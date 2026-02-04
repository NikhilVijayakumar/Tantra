from typing import List, Tuple
from tantra.grammar.domain.protocols.grammar_adapter import GrammarAdapterProtocol

class RegexGrammarAdapter:
    """
    Naive Heuristic POS Tagger.
    """
    
    def tag_pos(self, text: str) -> List[Tuple[str, str]]:
        if not text:
            return []
            
        words = text.split()
        tagged = []
        
        for w in words:
            tag = "NOUN" # Default
            lower = w.lower()
            
            # Simple Rules
            if lower.endswith("ly"):
                tag = "ADV"
            elif lower.endswith("ing") or lower.endswith("ed") or lower in ["runs", "eats"]:
                tag = "VERB"
            elif lower in ["the", "a", "an"]:
                tag = "DET"
                
            tagged.append((w, tag))
            
        return tagged
