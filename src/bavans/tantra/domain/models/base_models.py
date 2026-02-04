from pydantic import BaseModel, ConfigDict

class TantraBaseModels(BaseModel):
    """
    The Immutable Contract for all TANTRA Domain Models.
    """
    model_config = ConfigDict(
        frozen=True,        # Prevents runtime tampering
        strict=True,        # No type coercion
        extra='forbid'      # No extra fields allowed
    )

class TantraBaseSettings(BaseModel):
    """
    Standard Base for all Configuration Settings.
    - Frozen: Ensures no runtime tampering.
    - Strict: Prevents type coercion.
    """
    model_config = ConfigDict(
        frozen=True,
        strict=True,
        extra='forbid'
    )
