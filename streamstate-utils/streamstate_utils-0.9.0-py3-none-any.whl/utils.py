import os


def get_folder_location(app_name: str, topic: str) -> str:
    return os.path.join(app_name, topic)
