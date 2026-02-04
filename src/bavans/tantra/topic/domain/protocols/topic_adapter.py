from typing import List, Protocol, runtime_checkable

@runtime_checkable
class TopicAdapterProtocol(Protocol):
    """
    Protocol for Topic Extraction Adapters.
    """
    
    def extract_topics(self, text: str, top_n: int = 5) -> List[str]:
        """
        Extract the top N topics/keywords from the text.
        Returns ordered list (most important first).
        """
        ...
