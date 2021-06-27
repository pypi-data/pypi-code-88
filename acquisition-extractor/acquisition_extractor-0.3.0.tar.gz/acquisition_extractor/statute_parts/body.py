from pathlib import Path
from typing import Optional

import yaml
from yaml.parser import ParserError
from yaml.scanner import ScannerError

from .helpers import fix_absent_signer_problem, fix_multiple_sections_in_first


def get_sections(filename: Path) -> Optional[dict]:
    """The existence of the path having been previously verified, this implies
    prior processing from the `dblegacy` library which produces a yaml file
    whose contents are in list format.

    Args:
        filename (Path): The legacy file

    Returns:
        dict: The list of section data, populated from the legacy file.
    """
    try:
        with open(filename, "r") as r:
            return yaml.load(r, Loader=yaml.FullLoader)
    except ScannerError as e:
        print(f"See error {e}")
    except ParserError as e:
        print(f"See error {e}")
    return None


def set_units(folder: Path, data: dict):
    """
    If a preformatted file exists, i.e. data sourced from the old nightshade "Republic Act" repository,
    or formatted manually for use (see rawlaw repository), use the data contained in this file. The file is uniformly named as follows: `category` + `serial_number`.`yaml`, e.g. `ra11054.yaml` for Republic Act No. 11054;

    If a preformatted file is absent,  use the unformatted `units.yaml` file contained within the statute folder. The contents of this file is contained
    in the data dictionary passed.

    Args:
        folder (Path): [description]
        data (dict): [description]

    Returns:
        [type]: [description]
    """
    preformatted = folder / f"{data['category']}{folder.parts[-1]}.yaml"
    unformatted = folder / "units.yaml"

    if preformatted.exists():
        print(f"Provisions found (preformatted): {preformatted}.")
        data["units"] = get_sections(preformatted)

    elif unformatted.exists():
        print(f"Provisions found (unformatted): {unformatted}.")
        with open(unformatted, "r") as r:
            data["units"] = yaml.load(r, Loader=yaml.FullLoader)
            data = fix_absent_signer_problem(data)
            data = fix_multiple_sections_in_first(data)

    return data
