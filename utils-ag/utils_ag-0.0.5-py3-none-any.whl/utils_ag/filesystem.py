import json
from typing import Dict, List


def get_file_content_lines(filename: str) -> List[str]:
    content = get_file_content(filename)
    return content.split("\n")


def get_file_content(filename: str) -> str:
    f = open(filename, 'r', encoding="utf8")
    res = f.read()
    f.close()
    return res


def save_file_content(filepath: str, content: str) -> None:
    f = open(filepath, "w", encoding="utf8")
    f.write(content)
    f.close()


def get_json_file_content(filename: str) -> Dict:
    content = get_file_content(filename)
    return json.loads(content)