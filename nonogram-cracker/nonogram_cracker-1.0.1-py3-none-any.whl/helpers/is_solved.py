import re
from .identifiers import is_group, is_cross


def is_solved(cells_str):
    return all([is_group(x) or is_cross(x) for x in cells_str])


def can_clues_fit_with_solution(solution, clues):
    groups_pattern = "[x ]+".join([f"[█ ]{{{group_size}}}" for group_size in clues])
    pattern = f"^[x ]*{groups_pattern}[x ]*$"
    regex = re.compile(pattern)
    match = regex.match(solution)
    return True if match else False
