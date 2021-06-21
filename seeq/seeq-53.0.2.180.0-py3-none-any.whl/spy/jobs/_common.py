import os


def running_in_datalab():
    return os.environ.get('SEEQ_SDL_CONTAINER_IS_DATALAB') == 'true'


def running_in_executor():
    return os.environ.get('SEEQ_SDL_CONTAINER_IS_EXECUTOR') == 'true'


def get_label_from_executor():
    return os.environ.get('SEEQ_SDL_LABEL') or ''
