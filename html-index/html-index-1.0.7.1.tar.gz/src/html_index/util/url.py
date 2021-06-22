import re
from pathlib import Path

__url_pattern = re.compile('URL=(.*)')


def get_url_from_path(path: Path) -> str:
    return __url_pattern.search(path.read_text()).group(1)
