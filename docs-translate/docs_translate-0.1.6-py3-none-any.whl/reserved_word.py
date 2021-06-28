from pathlib import Path
import json
import re


class ReservedWords:
    def __init__(self, path: Path):
        with open(path, encoding='UTF8') as json_file:
            json_data = json.load(json_file)
        self.data = json_data
        self.keys = list(self.data.keys())
        self.compile = re.compile("("+")|(".join(self.keys)+")")

    def translate(self, line: str):
        for group, idx in sorted([(m.group(), m.groups().index(m.group())) for m in self.compile.finditer(line)], key=lambda x: x[0], reverse=True):
            line = re.sub(group, self.data[self.keys[idx]], line)
        return line
