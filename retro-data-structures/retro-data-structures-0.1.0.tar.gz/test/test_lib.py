from pathlib import Path

from retro_data_structures.construct_extensions import convert_to_raw_python


def parse_and_build_compare(module, game: int, file_path: Path):
    raw = file_path.read_bytes()

    data = module.parse(raw, target_game=game)
    data_as_dict = convert_to_raw_python(data)
    encoded = module.build(data_as_dict, target_game=game)

    assert encoded == raw
