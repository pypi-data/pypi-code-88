import re
from pathlib import Path
from typing import Iterator, Optional

from .decisions import define_data
from .statute_parts.title import ALLOWED_CATEGORIES
from .statutes import data_from_folder


def define_statute(parent: Path, child: Path, context: str) -> Optional[dict]:
    """

    Args:
        parent (Path): The parent path
        child (Path): The path to the statute
        context (str): The kind of statute

    Returns:
        Optional[dict]: [description]
    """
    # Is the folder digit-like, e.g. 209 or 209-A or 12-34-SC
    if not re.search(r"(^\d+-[A-C]$)|(^\d+$)|[a-zA-Z0-9-]+", child.name):
        print(f"Not digit-like: {child}")
        return None

    print(f"Processing: {child}")
    if data := data_from_folder(parent, context, child.name):
        return data
    else:
        print(f"Missing data: {child}")
        return None


def decode_statutes(parent: Path, context: str) -> Optional[Iterator[dict]]:
    """Given a parent directory `parent` with a subfolder `context`, generate statute-like data from entries of the subfolder, or the grandchildren of the parent directory.

    Args:
        parent (Path): The parent local directory, e.g. rawlaw
        context (str): Possible options include "ra", "eo", "pd", "ca", "bp", "act", "const"

    Returns:
        Optional[Iterator[dict]]: [description]

    Yields:
        Iterator[Optional[Iterator[dict]]]: [description]
    """
    if context not in ALLOWED_CATEGORIES:
        return None

    folder = parent / "statutes"
    if not folder.exists():
        return None

    subfolder = folder / context
    if not subfolder.exists():
        return None

    for child in subfolder.glob("*"):
        yield define_statute(folder, child, context)


def decode_decisions(loc: Path, context: str) -> Optional[Iterator[dict]]:
    """Given a parent directory "location" with a subfolder named "context",
    generate decision-like data from entries of the subfolder, or the grandchildren of the parent directory.

    Args:
        loc (Path): The parent local directory
        context (str): Either "legacy" or "sc"

    Returns:
        Optional[Iterator[dict]]: [description]

    Yields:
        Iterator[Optional[Iterator[dict]]]: [description]
    """
    if context not in ["legacy", "sc"]:
        return None

    folder = loc / "decisions" / context
    if not folder.exists():
        return None

    locations = folder.glob("*")
    for location in locations:
        yield define_data(location)
