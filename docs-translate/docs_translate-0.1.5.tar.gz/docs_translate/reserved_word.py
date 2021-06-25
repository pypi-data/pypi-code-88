from pathlib import Path
import json
import re


class ReservedWords:
    def __init__(self, path: Path):
        with open(path, encoding='UTF8') as json_file:
            json_data = json.load(json_file)
        self.data = json_data

    def translate(self, line: str):
        for key in sorted({word for word in self.data.keys() if word in line}, key=len, reverse=True):
            regex = re.compile(key, re.S)
            line = regex.sub(lambda m: m.group().replace(key, self.data[key], 1), line)
        return line
