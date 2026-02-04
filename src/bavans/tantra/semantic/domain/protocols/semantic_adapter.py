from typing import List, Protocol, runtime_checkable

@runtime_checkable
class SemanticAdapterProtocol(Protocol):
    """
    Protocol for Semantic Vector Operations.
    Adapters (Spacy, Transformers) must implement this.
    """
    
    def embed(self, text: str) -> List[float]:
        """Convert text to a vector embedding."""
        ...
        
    def cosine_similarity(self, vec_a: List[float], vec_b: List[float]) -> float:
        """Calculate cosine similarity between two vectors."""
        ...
