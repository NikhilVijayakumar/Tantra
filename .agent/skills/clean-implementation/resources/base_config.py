from pydantic import BaseModel, ConfigDict, Field

class TantraBaseConfig(BaseModel):
    """
    The Immutable Contract for all Tantra Modules.
    """
    model_config = ConfigDict(
        frozen=True,        # Prevents runtime tampering
        strict=True,        # Prevents '1' becoming 1
        extra='forbid',     # Prevents unknown configuration leakage
        validate_assignment=True
    )