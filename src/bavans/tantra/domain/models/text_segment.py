from typing import Dict, Optional
from pydantic import BaseModel, ConfigDict, Field

class TextSegment(BaseModel):
    """
    Standard Usage Unit for all TANTRA analyzers.
    Represents a chunk of text to be analyzed.
    """
    model_config = ConfigDict(
        frozen=True,
        strict=True,
        extra='forbid'
    )

    text: str = Field(..., description="The raw content to analyze")
    source_id: str = Field("unknown", description="ID of the source document")
    sequence_index: int = Field(0, description="Order of this segment in the source stream", ge=0)
    metadata: Dict[str, str] = Field(default_factory=dict, description="Arbitrary metadata (author, timestamp)")
