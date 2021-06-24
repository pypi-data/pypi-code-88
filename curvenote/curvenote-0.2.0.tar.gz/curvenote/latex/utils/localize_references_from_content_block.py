import re
import logging
from typing import List
from curvenote.models import Block
from .parse_cite_tag_from_bibtex import parse_cite_tag_from_bibtex
from .links import block_hash_to_api_url, oxa_path_to_api_url, unpin_oxa_path
from .index import (
    LocalReferenceItem,
    get_model,
)
from ...client import Session
from .regex import INLINE_CITATION_BLOCK_REGEX, INLINE_CITATION_OXA_REGEX, UNPIN_OXA_REGEX
from .run_regex_matchers import run_regex_matchers


def localize_references_from_content_block(
    session: Session, reference_list: List[LocalReferenceItem], content: str
):
    """Looks for cite TeX commands in the content then replaces the block ids
    with locally unique identifiers based on the local reference list.

    The reference list is extended as new references are found (side effect)

    Appends a unique hash to each new reference encountered
    """
    patched_content = content

    matches = run_regex_matchers(
        [INLINE_CITATION_BLOCK_REGEX, INLINE_CITATION_OXA_REGEX], content)
    remote_paths = [m[1] for m in matches]

    for remote_path in remote_paths:
        logging.info("processing remote path: %s", remote_path)
        # check for the reference in the reference list based on the block_path
        matched_references = [r for r in reference_list if r.block_path == remote_path]
        existing_reference = (
            matched_references[0] if (len(matched_references) > 0) else None
        )

        if existing_reference is None:
            if remote_path.startswith("oxa:"):
                unpinned_path = unpin_oxa_path(remote_path)
                url = oxa_path_to_api_url(session.api_url, unpinned_path)
            else:
                url = block_hash_to_api_url(session.api_url, remote_path)

            logging.info("fetching reference block %s", url)
            block = get_model(session, url, Block)
            logging.info("got reference block")

            # get latest version
            version_url = f"{url}/versions/{block.latest_version}?format=bibtex"
            logging.info("fetching reference version %s", version_url)
            version = get_model(session, version_url)
            logging.info("got reference version")

            # update the list
            local_tag, plain_tag = parse_cite_tag_from_bibtex(version.content)
            bibtex = version.content.replace(plain_tag, local_tag)

            reference_item = LocalReferenceItem(remote_path, local_tag, bibtex)
            reference_list.append(reference_item)
            existing_reference = reference_item
            logging.info("using new reference %s", existing_reference.local_tag)
        else:
            logging.info("using existing reference %s", existing_reference.local_tag)

        # patch the content and move on
        patched_content = patched_content.replace(
            remote_path, existing_reference.local_tag
        )

    return patched_content
