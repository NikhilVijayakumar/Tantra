from typing import Dict, List, Protocol, runtime_checkable

@runtime_checkable
class EntityAdapterProtocol(Protocol):
    """
    Protocol for Entity Extraction Adapters.
    """
    
    def extract_entities(self, text: str) -> Dict[str, List[str]]:
        """
        Extract entities from text.
        Returns: {'PERSON': ['Alice', 'Bob'], 'ORG': ['Google']}
        """
        ...
