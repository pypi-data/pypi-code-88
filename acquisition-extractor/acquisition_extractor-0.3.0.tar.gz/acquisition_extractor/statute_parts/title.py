from typing import Optional

ALLOWED_CATEGORIES = [
    "ra",
    "eo",
    "pd",
    "ca",
    "bp",
    "act",
    "const",
    "veto",
    "roc",
    "am",
    "bm",
    "es",
    "res",
    "roc",
]


def get_title(category: str, num: str) -> Optional[str]:
    """Combine two strings after formatting the category

    Args:
        category (str): Determines (generally) the first part of the string; see exceptions in "roc" and "const"
        num (str): The serialized identifier of the category

    Returns:
        Optional[str]:
    """
    cat = category.lower()
    if cat not in ALLOWED_CATEGORIES:
        return None

    if cat == "ra":
        return f"Republic Act No. {num.upper()}"

    elif cat == "eo":
        return f"Executive Order No. {num.upper()}"

    elif cat == "pd":
        return f"Presidential Decree No. {num.upper()}"

    elif cat == "bp":
        return f"Batas Pambansa Blg. {num.upper()}"

    elif cat == "ca":
        return f"Commonwealth Act No. {num.upper()}"

    elif cat == "act":
        return f"Act No. {num.upper()}"

    elif cat == "bm":
        return f"Bar Matter No. {num.upper()}"

    elif cat == "am":
        return f"Administrative Matter No. {num.upper()}"

    elif cat == "roc":
        return f"{num} Rules of Court"

    elif cat == "res":
        return f"Resolution of the Court En Banc dated {num}"

    elif cat == "cir":
        return f"Circular No. {num}"

    elif cat == "const":
        return f"{num} Constitution"

    elif cat == "es":
        return f"Spanish {num}"

    elif cat == "veto":
        return f"Veto Message of Republic Act No. {num}"

    return None
