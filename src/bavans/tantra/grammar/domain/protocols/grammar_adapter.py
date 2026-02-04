from typing import List, Tuple, Protocol, runtime_checkable

@runtime_checkable
class GrammarAdapterProtocol(Protocol):
    """
    Protocol for Grammar/POS Tagging Adapters.
    """
    
    def tag_pos(self, text: str) -> List[Tuple[str, str]]:
        """
        Tag parts of speech.
        Returns: [('Cat', 'NOUN'), ('runs', 'VERB')]
        """
        ...
