import logging
from curvenote.latex.utils.links import version_id_to_local_path, version_id_to_oxa_path
from .get_image_block import get_image_block
from ...models import BlockVersion
from ...client import Session
from .get_fast_hash import get_fast_hash
from .snippets import (
    IMAGE_LATEX_SNIPPET,
    VERSION_ID,
    CAPTION,
    LABEL
)

def localize_image_from_top_level_block(
    session: Session,
    assets_folder: str,
    version: BlockVersion
):
    """
         - get the image block
         - download the image to the assets_folder using teh local_path as name
         - build the LaTeX content snippet and return it
    """
    try:
        oxa_path = version_id_to_oxa_path(version.id)
        local_path = version_id_to_local_path(version.id)

        image_block, local_path_with_extension = get_image_block(
            session, assets_folder, oxa_path, local_path
        )

        content = (
            IMAGE_LATEX_SNIPPET.replace(VERSION_ID, local_path_with_extension)
            .replace(CAPTION, image_block.caption)
            .replace(LABEL, get_fast_hash())
        )

        return f"\n\n{content}\n"
    except ValueError as err:
        logging.error(
            "Caught error trying to localize top level image %s, skipping",
            str(self.version.id),
        )
        logging.error(err)
