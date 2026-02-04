import pytest
import shutil
from pathlib import Path

@pytest.fixture
def nibandha_env(tmp_path):
    """
    Standard fixture for E2E tests.
    Creates a sandboxed .Tantra directory in a temporary path.
    """
    env_path = tmp_path / ".Tantra"
    env_path.mkdir()
    yield env_path
    # Teardown: Environment is automatically cleaned up by tmp_path