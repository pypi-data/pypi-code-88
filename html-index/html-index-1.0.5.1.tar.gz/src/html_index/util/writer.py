import logging
from typing import List

from .assets import Assets
from .index import Index


class Writer:
    def __init__(self, assets: Assets, title, parent_dir, filename, size, modified):
        self.__icon_folder = assets.icon_folder()

        self.__index_template = assets.index_template() \
            .read_text() \
            .replace("{TITLE}", title) \
            .replace("{PARENT}", parent_dir) \
            .replace("{FILENAME}", filename) \
            .replace("{SIZE}", size) \
            .replace("{MODIFIED}", modified)
        self.__file_template = assets.file_template().read_text()

    def write(self, indexes: List[Index]):
        for index in indexes:
            path = index.path.joinpath('index.html')
            logging.info(f"Writing {path}")

            html = index.to_html(self.__index_template, self.__file_template)

            path.write_text(html)

            index.remove_junk()

    def write_deep(self, indexes: List[Index]):
        if len(indexes) <= 0:
            return

        self.write(indexes)

        for index in indexes:
            self.write_deep(index.list_sub_indexes())
