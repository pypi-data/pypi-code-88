import os
from deta import Deta
from pydantic import BaseSettings, PrivateAttr
from dotenv import (load_dotenv, find_dotenv)

load_dotenv(find_dotenv('../.env'))

__all__ = ['aconnect']

class DetaSettings(BaseSettings):
    _DETA_KEY: str = PrivateAttr(os.getenv('DETA_KEY'))
    _KEY_NAME: str = PrivateAttr(os.getenv('KEY_NAME'))


async def aconnect(model: str) -> Deta.Base:
    settings: DetaSettings = DetaSettings()
    return Deta(settings._DETA_KEY).Base(model)



