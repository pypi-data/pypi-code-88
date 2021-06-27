import codecs
from pathlib import Path
from typing import Optional

import yaml


def set_whereas(loc: Path) -> dict:
    target = loc / "extra.html"
    if target.exists():
        f = codecs.open(str(target), "r")
        extra_content = f.read()
        title_case = "Whereas" in extra_content
        all_caps = "WHEREAS" in extra_content
        if title_case or all_caps:
            return {"whereas_clause": extra_content}
    return {"whereas_clause": None}


def set_meta(loc: Path) -> Optional[dict]:
    """The high-level config file for a statute is the `details.yaml`
    See sample `details.yaml` under the folder ../pd/1

    - numeral: '1'
    - category: pd
    - origin: [url]
    - publications: []
    - enacting_clause: 'NOW, THEREFORE, I, FERDINAND E. MARCOS, x x x'
    - signers_of_law: 'Done in the City of Manila, x x x'
    - lapse_into_law_clause: null
    - law_title: Reorganizing The Executive Branch Of The National Government
    - date: September 24, 1972
    - item: Presidential Decree No. 1

    Args:
        loc (Path): [description]

    Returns:
        Optional[dict]: [description]
    """
    try:
        details = loc / "details.yaml"
        if not details.exists():
            return None
        with open(details, "r") as r:
            return yaml.load(r, Loader=yaml.FullLoader) | set_whereas(loc)

    except FileNotFoundError:
        return None
