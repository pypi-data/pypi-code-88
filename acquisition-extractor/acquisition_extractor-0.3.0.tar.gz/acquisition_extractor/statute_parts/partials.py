import codecs
import re
from pathlib import Path

import yaml


def is_problematic(d: dict):
    if d.get("item", None) and d.get("order", None):
        match = re.search(r"\d+", d["item"])
        digit = int(match.group()) if match else 999
        return digit != d["order"]


def find_problems(loc: Path):
    target_file = loc / "units.yaml"
    if not target_file.exists():
        return False
    with open(target_file, "r") as r:
        data = {}
        data["units"] = yaml.load(r, Loader=yaml.FullLoader)
        return is_problematic(data["units"][-1])


def origin_clause_not_null(loc: Path):
    target_file = loc / "details.yaml"
    if not target_file.exists():
        return False
    with open(target_file, "r") as r:
        data = yaml.load(r, Loader=yaml.FullLoader)
        if not data["origin_clause"]:
            return False
        return (data["origin_clause"], data["origin"])


def lapse_clause_not_null(loc: Path):
    target_file = loc / "details.yaml"
    if not target_file.exists():
        return False
    with open(target_file, "r") as r:
        data = yaml.load(r, Loader=yaml.FullLoader)
        if not data["lapse_into_law_clause"]:
            return False
        return (data["lapse_into_law_clause"], data["origin"])


def first_issue_detected(loc: Path):
    with open(loc / "units.yaml", "r") as r:
        data = {}
        data["units"] = yaml.load(r, Loader=yaml.FullLoader)
        if data["units"][0] and data["units"][0].get("content", None):
            return "SEC. 2" in data["units"][0]["content"]


def order_mismatches():
    folder = Path(".") / "ra"
    locations = folder.glob("*")
    return (loc for loc in locations if find_problems(loc))


def first_item_issues():
    return [loc for loc in order_mismatches() if first_issue_detected(loc)]


def get_body(loc: Path) -> str:
    body_location = loc / "body_statute.html"
    f = codecs.open(str(body_location))
    return f.read()
