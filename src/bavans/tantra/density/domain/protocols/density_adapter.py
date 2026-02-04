from typing import Protocol, runtime_checkable

@runtime_checkable
class DensityAdapterProtocol(Protocol):
    """
    Protocol for Information Density/Entropy Calculation.
    """
    
    def calculate_entropy(self, text: str) -> float:
        """
        Calculate Shannon Entropy.
        Returns: float (>= 0.0)
        """
        ...
