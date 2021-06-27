import codecs
from pathlib import Path
from typing import Iterator, Optional

import yaml


def extract_htmls(loc: Path) -> Optional[Iterator[dict]]:
    """If files are found in the path, extract the content

    Args:
        loc (Path): Folder location

    Returns:
        Optional[Iterator[dict]]: [description]

    Yields:
        Iterator[Optional[Iterator[dict]]]: [description]
    """
    labels = ["annex", "ponencia", "fallo"]
    for label in labels:
        location = loc / f"{label}.html"
        if location.exists():
            f = codecs.open(str(location), "r")
            yield {label: f.read()}


def define_data(loc: Path) -> dict:
    """Given a folder's path, open the `details.yaml` file
    This describes the different metadata for the case.

    The folder path may also contain `html` files such as:
    1. The ponencia
    2. The annex
    3. The fallo

    If html files exist, extract content and combine
    all such html files in a single dictionary.

    Combined this with the data from the detail.yaml.

    Args:
        loc (Path): Folder location

    Returns:
        dict: A  dictionary containing content of folder path submitted.
    """
    result = {}
    with open(loc / "details.yaml", "r") as readfile:
        result = yaml.load(readfile, Loader=yaml.FullLoader)

    if extracted := extract_htmls(loc):
        for extract in extracted:
            result.update(extract)

    return result
