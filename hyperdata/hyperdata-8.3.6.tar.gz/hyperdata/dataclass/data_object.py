from dataclasses import dataclass
from typing import List, Dict

# example
# "name": "TEST",
# "sourceTableName": "TEST",
# "subtype": "Table",
# "outCols": [
#     {
#         "name": "C1"
#     },
#     {
#         "name": "C2"
#     }
# ],
# "shareRelation": [
# ]


@dataclass
class DataObject:
    id: int = 0
    name: str = ""
    outCols: List[Dict[str, str]] = None
    shareRelation: List[str] = None
    sourceTableName: str = ""
    subtype: str = ""
    author: str = ""
    description: str = ""
    createdOn: str = "1970.01.01 00.00.00"
    lastEdited: str = "1970.01.01 00.00.00"

    def __post_init__(self):
        self.id = int(self.id)
