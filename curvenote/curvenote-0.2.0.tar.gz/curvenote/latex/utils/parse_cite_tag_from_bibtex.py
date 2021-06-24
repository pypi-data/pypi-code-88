import re
from .get_fast_hash import get_fast_hash

def parse_cite_tag_from_bibtex(content: str):
    tag = "ref"
    match = re.match("@article{([0-9a-zA-Z_]+),*\n", content)
    if match is not None:
        tag = match[1].replace(",", "")
    # adding quasi-random hash to save de-duping work
    hash_id = get_fast_hash()
    tag_with_hash = f"{tag}_{hash_id}"

    return tag_with_hash, tag
