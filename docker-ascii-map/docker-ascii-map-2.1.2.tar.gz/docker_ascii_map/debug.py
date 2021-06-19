import pickle

from docker_ascii_map.docker_config import Configuration


def dump_configuration(config: Configuration) -> bytes:
    return pickle.dumps(config)


def restore_configuration(text: bytes) -> Configuration:
    return pickle.loads(text)
