import math
from collections import Counter
from tantra.density.domain.protocols.density_adapter import DensityAdapterProtocol

class ShannonEntropyAdapter:
    """
    Standard Shannon Entropy Implementation.
    """
    
    def calculate_entropy(self, text: str) -> float:
        if not text:
            return 0.0
            
        # 1. Frequency
        counts = Counter(text)
        total = len(text)
        
        # 2. Probability & Log Sum
        entropy = 0.0
        for count in counts.values():
            p = count / total
            if p > 0:
                entropy -= p * math.log2(p)
                
        return entropy
