from typing import Dict, Any, List, Optional
from pydantic import BaseModel, ConfigDict, Field

class AnalysisResult(BaseModel):
    """
    Universal Output Container for TANTRA protocols.
    Designed to be serializable and consistent across all modules.
    """
    model_config = ConfigDict(
        frozen=True,
        strict=True,
        extra='forbid'
    )

    # 1. Identity
    analyzer_name: str = Field(..., description="Name of the analyzer producing this result")
    timestamp: float = Field(..., description="UTC timestamp of analysis completion")
    
    # 2. Quantitative (Metrics)
    metrics: Dict[str, float] = Field(
        default_factory=dict, 
        description="Key-Value pairs of numerical scores (e.g. {'entropy': 0.45, 'sentiment': -0.2})"
    )

    # 3. Qualitative (Signals) - Structured Data
    signals: Dict[str, Any] = Field(
        default_factory=dict,
        description="Structured observations (e.g. {'missing_topics': ['A', 'B'], 'detected_entities': [...]})"
    )

    # 4. Artifacts (Raw/Blob)
    artifacts: Dict[str, str] = Field(
        default_factory=dict,
        description="Paths or references to generated files (graphs, images)"
    )

    # 5. Diagnostics
    warnings: List[str] = Field(default_factory=list, description="Non-blocking issues encountered")
