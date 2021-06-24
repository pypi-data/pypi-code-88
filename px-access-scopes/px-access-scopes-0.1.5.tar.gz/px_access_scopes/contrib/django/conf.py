from dataclasses import dataclass
from typing import List, Optional
from px_settings.contrib.django import settings as s


__all__ = 'Settings', 'settings'


@s('PX_ACCESS_TOKENS')
@dataclass
class Settings:
    AUTOLOAD_MODULE: str = 'access_scopes'
    REGISTRIES: Optional[List[str]] = None
    AGGREGATES: Optional[List[str]] = None


settings = Settings()
