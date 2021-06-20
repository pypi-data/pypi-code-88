# This file is part of pybib2web, a translator of BibTeX to HTML.
# https://gitlab.com/sosy-lab/software/pybib2web
#
# SPDX-FileCopyrightText: 2021 Dirk Beyer <https://www.sosy-lab.org>
#
# SPDX-License-Identifier: Apache-2.0

"""Utility methods for pybib2web."""

import re
from typing import Optional, Tuple, List


def equal_author(author1, author2) -> bool:
    """Return whether the two given authors are the same.

    Takes care of BibTeX short-forms.

    Example:
        equal_author("Dirk Beyer", "D. Beyer") = True
    """
    return get_shortform(author1) == get_shortform(author2)


def split_name(author: str) -> Tuple[str, str]:
    """Split author name into first name(s) and last name."""
    parts = get_all_name_parts(author)
    return " ".join(parts[:-1]), parts[-1]


def get_all_name_parts(name: str) -> List[str]:
    """Split given name into all of its parts.

    Examples:
        "Dirk Beyer" -> ["Dirk", "Beyer"]
        "Mehmet Erkan Keremoglu" -> ["Mehmet", "Erkan", "Keremoglu"]
    """
    return re.split(r" |~|-", name.strip())


def get_shortform(author_name: str) -> str:
    """Get shortform of author name.

    Examples:
        "Dirk Beyer" -> "D. Beyer"
        "Mehmet Erkan Keremoglu" -> "M. E. Keremoglu"
    """
    first_names, last_name = split_name(author_name)
    first_names = get_all_name_parts(first_names)
    if [f for f in first_names if f]:
        first_names_short = [f"{name[0]}." for name in first_names]
    else:
        first_names_short = []
    return " ".join(first_names_short + [last_name])


def get_download_link(doi: str) -> Optional[str]:
    """Compute a link for downloading the paper PDF for the given DOI."""
    link = None
    if doi.startswith("10.1007/"):
        link = f"https://link.springer.com/content/pdf/{doi}.pdf"
    if doi.startswith("10.1145/"):
        link = f"https://dl.acm.org/doi/pdf/{doi}"
    return link
