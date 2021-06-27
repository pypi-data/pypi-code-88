import re
from pathlib import Path
from typing import Optional

import arrow

from .statute_parts.body import set_units
from .statute_parts.meta import set_meta
from .statute_parts.title import ALLOWED_CATEGORIES, get_title


def uniform_section_label(raw: str):
    """Replace the SECTION | SEC. | Sec. format with the word Section, if applicable."""
    regex = r"""
        ^\s*
        S
        (
            ECTION|
            EC|
            ec
        )
        [\s.,]+
    """
    pattern = re.compile(regex, re.X)
    if pattern.search(raw):
        text = pattern.sub("Section ", raw)
        text = text.strip("., ")
        return text
    return raw


def process_units(nodes: list[dict]) -> None:
    """Recursive function to ensure that the nested units comply with the database constraints.
    Each item should be limited to 500 characters. Each caption should be limited to 500 characters.
    For items which contain a variant of the "section" label, e.g. "SEC. 1", apply uniform label,
    i.e. "Section 1".

    Args:
        nodes (list[dict]): [description]
    """
    for node in nodes:
        if node.get("item", None):
            # deal with items where the input is an integer
            # only strings can be matched in the `uniform_section_label` function
            converted = str(node["item"])

            # for SEC., # SECTION text, convert to uniform "Section"
            node["item"] = uniform_section_label(converted)

            # ensure that item text is sound, 500 as arbitrary number check
            if len(node["item"]) > 500:
                node["item"] = node["item"][:500]

        if caption := node.get("caption", None):

            # ensure that caption text is sound, 500 as arbitrary number check
            if len(node["caption"]) > 500:
                node["caption"] = caption[:500]

        if node.get("units", None):
            process_units(node["units"])


def load_statute(loc: Path) -> Optional[dict]:
    """With the passed directory, get the relevant files.

    The following files in the directory, i.e. ("pd1") are processed, if they exist

    1. `details.yaml`
    2. `extra.html`
    3. `units.yaml` (unformatted)
    4. `pd1.yaml` (preformatted Presidential Decree No. 1)

    This function combines the contents of the `details.yaml` file
    with the contents of either the `units.yaml` file or the `pd1.yaml` file.
    The resulting combination is a dictionary of key value pairs.

    Args:
        loc (Path): The source directory of the files mentioned above.

    Returns:
        Optional[dict]: The combined data found in the folder.
    """
    if not (data := set_meta(loc)):
        print(f"No details.yaml file: {loc}.")
        return None
    print(f"Details found: {loc}.")
    return set_units(loc, data)


def get_directory(
    location: Path,
    law_category: str,
    serial_num: str,
) -> Optional[Path]:
    """With the location of the files, check if a specific folder exists with the given parameters

    Args:
        location (Path): Where the source material is stored
        law_category (str): Must be either "ra", "eo", "pd", "ca", "bp", "act", "const"
        serial_num (str): A digit-like identifier, e.g. 209, 158-a, etc.

    Returns:
        Path: [description]
    """
    if law_category not in ALLOWED_CATEGORIES:
        return None

    directory = location / f"{law_category}" / f"{serial_num}"
    if not directory.exists():
        return None

    return directory


def data_from_folder(
    location: Path,
    law_category: str,
    serial_num: str,
) -> Optional[dict]:
    """If the location exists and there is data processed from such location,
    determine whether the important fields are present and then process (clean) the
    fields.

    Args:
        location (Path): Where the source material is stored
        law_category (str): Must be either "ra", "eo", "pd", "ca", "bp", "act", "const"
        serial_num (str): A digit-like identifier, e.g. 209, 158-a, etc.

    Returns:
        Optional[dict]: Cleaned data dictionary
    """

    if not (folder := get_directory(location, law_category, serial_num)):
        return None

    if not (source := load_statute(folder)):
        return None

    if source.get("units", None):
        process_units(source["units"])

    return map_to_model(law_category, source)


def map_to_model(law_category: str, source: dict) -> Optional[dict]:
    """The dictionary found in source needs to be mapped to the schema of the database.

    Args:
        law_category (str): Must be either "ra", "eo", "pd", "ca", "bp", "act", "const"
        source (dict): Pre-processed content

    Returns:
        Optional[dict]: Segregated data that matches the database schema for Statutes
    """
    for field in ["numeral", "law_title", "date", "units"]:
        if not source.get(field, None):
            print(f"Missing field: {field=}")
            return None

    # The database limit should be less than 1000 characters
    if len(source["law_title"]) > 1000:
        source["law_title"] = source["law_title"][:1000]

    if not (title_text := get_title(law_category, source["numeral"])):
        print(
            f"Could not create title text with {law_category=} and {source['numeral']=}"
        )
        return None

    return {
        "category": source["category"],
        "identifier": source["numeral"],
        "title": title_text,
        "full_title": source["law_title"],
        "specified_date": arrow.get(source["date"], "MMMM D, YYYY").date(),
        "publications": source.get("publications", None),
        "enacting_clause": source.get("enacting_clause", None),
        "whereas_clause": source.get("whereas_clause", None),
        "signers_of_law": source.get("signers_of_law", None),
        "lapse_into_law_clause": source.get("lapse_into_law_clause", None),
        "units": source["units"],
    }
