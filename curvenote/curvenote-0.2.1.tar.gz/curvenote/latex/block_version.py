from curvenote.latex.utils.index import LocalMarker, LocalReferenceItem
from curvenote.latex.utils.links import oxa_path_to_api_url
import logging
from .utils.regex import HREF_COMMAND_OXA_REGEX
from typing import List
from curvenote.latex import utils

from ..client import Session
from ..models import (
    BlockKind,
    BlockVersion,
)
from . import utils

logger = logging.getLogger()

LANG = "___LANG___"
CODE_CONTENT = "___CODE_CONTENT___"

CODE_BLOCK_TPL = rf"""\begin{{minted}}[tabsize=4, linenos, mathescape, numbersep=5pt, framesep=2mm]{{{LANG}}}
{CODE_CONTENT}
\end{{minted}}
"""


class LatexBlockVersion:
    """
    Class to represent an block in the latex project.
    Encapulates operations applied in processing a block's content including
    calls to fetch content that it encapsulates
    """

    def __init__(self, session: Session, version: BlockVersion):
        self.session = session
        self.version = version
        self._content = ""

    @property
    def content(self):
        return self._content

    def _localize_images_in_content(self, assets_folder: str, figure_list: List[LocalMarker], content: str):
        try:
            return utils.localize_images_from_content_block(
                self.session, assets_folder, figure_list, content
            )
        except ValueError as err:
            logging.error(
                f"Caught error trying to localize images for block {str(self.version.id)}, skipping"
            )
            logging.error(err)

    def _localize_references_in_content(self, reference_list: List[str], content):
        try:
            return utils.localize_references_from_content_block(
                self.session, reference_list, content
            )
        except ValueError as err:
            logging.error(
                "Caught error trying to localize references for block %s, skipping",
                str(self.version.id),
            )
            logging.error(err)

    def _localize_href_in_content(self, content):
        try:
            return utils.localize_hrefs_in_content(self.session.site_url, content)
        except ValueError as err:
            logging.error(
                "Caught error trying to localize hrefs for block %s, skipping",
                str(self.version.id),
            )
            logging.error(err)


    def localize(self, assets_folder: str, reference_list: List[LocalReferenceItem], figure_list: List[LocalMarker]):
        content = ""
        kind = self.version.kind
        if kind == BlockKind.content:
            logger.info("Found: Content Block")
            content = self._localize_images_in_content(assets_folder, figure_list, self.version.content)
            content = self._localize_references_in_content(reference_list, content)
            content = self._localize_href_in_content(content)

        elif kind == BlockKind.output:
            logger.info(
                "Found: Output Block - num outputs: %s",
                len(self.version.outputs)
            )
            content = utils.localize_images_from_output_block(
                assets_folder, self.version
            )
        elif kind == BlockKind.code:
            logger.info("Found: Code Block")
            content = CODE_BLOCK_TPL.replace(
                LANG, "python").replace(CODE_CONTENT, self.version.content)
        elif kind == BlockKind.image:
            logger.info("Found: Top Level Image Block")
            content = utils.localize_image_from_top_level_block(
                self.session, assets_folder, figure_list, self.version
            )

        else:
            logger.warning("Can't process block with kind: %s yet", kind)
            raise ValueError(f"Unknown block kind {kind}")
        self._content = content
