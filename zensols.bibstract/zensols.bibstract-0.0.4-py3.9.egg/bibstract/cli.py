from __future__ import annotations
"""Command line entry point to the application.

"""
__author__ = 'Paul Landes'

from typing import List, Any, Dict
from dataclasses import dataclass
import sys
from pathlib import Path
from zensols.config import DictionaryConfig
from zensols.cli import ApplicationFactory


@dataclass
class BibstractApplicationFactory(ApplicationFactory):
    @classmethod
    def instance(cls: type, root_dir: Path = Path('.'),
                 *args, **kwargs) -> BibstractApplicationFactory:
        dconf = DictionaryConfig({'appenv': {'root_dir': str(root_dir)}})
        return cls(package_resource='zensols.bibstract',
                   children_configs=(dconf,),
                   **kwargs)


def main(args: List[str] = sys.argv[1:], **kwargs: Dict[str, Any]) -> Any:
    cli = BibstractApplicationFactory.instance(**kwargs)
    cli.invoke(args)
