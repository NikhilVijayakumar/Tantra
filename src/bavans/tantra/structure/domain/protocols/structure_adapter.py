from typing import List, Protocol, runtime_checkable

@runtime_checkable
class StructureAdapterProtocol(Protocol):
    """
    Protocol for Structure Analysis Adapters.
    Responsible for breaking text into structural units (sentences).
    """
    
    def tokenize_sentences(self, text: str) -> List[str]:
        """Split text into sentences."""
        ...
        
    def count_words(self, text: str) -> int:
        """Count words in a text segment."""
        ...
