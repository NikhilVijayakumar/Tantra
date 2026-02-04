from typing import Protocol, runtime_checkable

@runtime_checkable
class AnomalyAdapterProtocol(Protocol):
    """
    Protocol for Statistical Anomaly Detection.
    """
    
    def calculate_z_score(self, value: float, mean: float, std: float) -> float:
        """
        Calculate Absolute Z-Score: |(x - mean) / std|
        """
        ...
        
    def is_outlier(self, z_score: float, threshold: float = 3.0) -> bool:
        """
        Check if Z-Score exceeds threshold.
        """
        ...
