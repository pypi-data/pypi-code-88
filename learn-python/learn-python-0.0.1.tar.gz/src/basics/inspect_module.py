import re
from static_class_method import Person
from collections import defaultdict

from typing import List, Optional, NamedTuple, Dict, Tuple
from inspect import signature


class FileSyntaxError(NamedTuple):
    line_no: Optional[int]
    message: str

    def __str__(self):
        return f"{self.message}. Line number: {str(self.line_no)}"


def get_object_parameters_names():
    return {
        k for k in signature(Person.__init__).parameters.keys() if k != "self"
    }


COMMENT_PATTERN = re.compile(r"\s*#.*")


def parse_env_file(file_path: str) -> Tuple[Dict[str, List[str]], List[FileSyntaxError]]:
    with open(file_path) as f:
        content = f.read()

    errors: List[FileSyntaxError] = []
    secrets: Dict[str, List[str]] = defaultdict(list)

    for line_no, line in enumerate(content.splitlines(), 1):
        if not line or COMMENT_PATTERN.match(line):
            continue
        var_parts = line.split("=", 2)
        if len(var_parts) != 2:
            errors.append(
                FileSyntaxError(
                    line_no=line_no,
                    message='Invalid line format. Line should contains at least one sign ("=")',
                )
            )
            continue
        key, value = var_parts
        if not key:
            errors.append(
                FileSyntaxError(
                    line_no=line_no,
                    message='Invalid line format. Empty key',
                )
            )
        secrets[key].append(value)
        return secrets, errors


if __name__ == '__main__':
    print(get_object_parameters_names())
    l1 = ["one", "two", "three"]
    print(list(enumerate(l1)))

    print('*' * 80)
    print(parse_env_file("myapp.log"))

