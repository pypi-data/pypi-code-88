import json
from rich import print
from rich.console import Console
from pathlib import Path

console = Console()

json_path = f"{Path(__file__).parent}"

with open(f'{json_path}/ascii.json', 'r') as f:
    ascii_dict = json.load(f)
