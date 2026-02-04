from typing import List, Tuple, Protocol, runtime_checkable

@runtime_checkable
class RelationAdapterProtocol(Protocol):
    """
    Protocol for Entity-Relation Extraction.
    """
    
    def extract_triples(self, text: str) -> List[Tuple[str, str, str]]:
        """
        Extract Subject-Verb-Object triples.
        Returns: [('A', 'hits', 'B')]
        """
        ...
