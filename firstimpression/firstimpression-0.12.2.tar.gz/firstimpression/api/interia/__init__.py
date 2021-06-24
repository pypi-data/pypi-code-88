import os

from firstimpression.file import download_media
from firstimpression.scala import install_content
from firstimpression.xml import get_attrib_from_element
from firstimpression.constants import PICTURE_FORMATS


def install_picture_content_wrap(picture_format, subdirectory, temp_folder, element, tag, attrib):
    # Installs content to LocalIntegratedContent folder and returns mediapath
    if not picture_format in PICTURE_FORMATS:
        return None

    media_link = get_attrib_from_element(
        element, tag, attrib).replace("_sqr256", "")

    media_path = download_media(
        PICTURE_FORMATS[picture_format] + media_link, subdirectory, temp_folder)

    install_content(media_path, subdirectory)

    media_filename = media_path.split('\\').pop()

    return os.path.join('Content:\\', subdirectory, media_filename)
