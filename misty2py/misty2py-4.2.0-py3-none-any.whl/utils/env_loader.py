"""This module contains the EnvLoader class for loading environmental values."""
from typing import Optional

from dotenv import dotenv_values


class EnvLoader:
    """Loads environmental values.

    Attributes:
        values [OrderedDict]: The loaded environmental values, might be empty.
    """

    def __init__(self, env_path: str = ".env") -> None:
        self.values = dotenv_values(env_path)

    def get_ip(self) -> Optional[str]:
        """Obtains `MISTY_IP_ADDRESS` from environmental values."""
        return self.values.get("MISTY_IP_ADDRESS")
