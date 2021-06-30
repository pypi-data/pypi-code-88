import requests

from .settings import settings


def download_file_from_stream(url, out_file):
    try:
        with requests.get(url, stream=True) as r:
            # based on https://stackoverflow.com/a/16696317
            r.raise_for_status()
            settings.logger.info("Downloading results...")
            for chunk in r.iter_content(chunk_size=8192):
                out_file.write(chunk)
    except requests.exceptions.HTTPError:
        return False
    return True
