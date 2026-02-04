from typing import Optional
from nibandha.unified_root.bootstrap import Nibandha
from nibandha.configuration.domain.models.app_config import AppConfig

# Singleton reference
_system: Optional[Nibandha] = None

def initialize_tantra(env: str = "dev") -> Nibandha:
    """
    Bootstraps the TANTRA system using the Nibandha core.
    
    1. Sets up the Unified Root at .Tantra/
    2. Configures logging via Nibandha.
    3. Returns the initialized system facade.
    """
    global _system
    
    if _system:
        return _system
        
    config = AppConfig(
        name="Tantra",
        env=env,
        log_level="INFO"
    )
    
    _system = Nibandha(config=config, root_name=".Tantra")
    _system.bind()
    
    return _system

def get_system() -> Nibandha:
    """Returns the active system instance or raises error if not initialized."""
    if not _system:
        raise RuntimeError("TANTRA is not initialized. Call initialize_tantra() first.")
    return _system
