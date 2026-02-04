from tantra.anomaly.domain.protocols.anomaly_adapter import AnomalyAdapterProtocol

class StatisticalAdapter:
    """
    Standard Z-Score Implementation.
    """
    
    def calculate_z_score(self, value: float, mean: float, std: float) -> float:
        if std == 0:
            return 0.0 # Cannot deviate from a point-mass distribution? Or Infinite?
            # For robustness, returning 0.0 avoids crashes.
            
        z = (value - mean) / std
        return abs(z)

    def is_outlier(self, z_score: float, threshold: float = 3.0) -> bool:
        return z_score > threshold
