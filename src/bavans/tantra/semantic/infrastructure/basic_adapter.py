import math
from typing import List
from tantra.semantic.domain.protocols.semantic_adapter import SemanticAdapterProtocol

class BasicSemanticAdapter:
    """
    A basic, dependency-free adapter for testing/fallback.
    Does NOT use DL models. Uses simple word overlap or deterministic hashing for 'embedding'.
    """
    
    def embed(self, text: str) -> List[float]:
        # Dummy Implementation: Character frequency vector (toy example)
        # In real world, this would verify Spacy is installed and use it.
        vec = [0.0] * 26
        for char in text.lower():
            if 'a' <= char <= 'z':
                vec[ord(char) - ord('a')] += 1.0
        return vec

    def cosine_similarity(self, v1: List[float], v2: List[float]) -> float:
        dot_product = sum(a * b for a, b in zip(v1, v2))
        norm_a = math.sqrt(sum(a * a for a in v1))
        norm_b = math.sqrt(sum(b * b for b in v2))
        
        if norm_a == 0 or norm_b == 0:
            return 0.0
            
        return dot_product / (norm_a * norm_b)
