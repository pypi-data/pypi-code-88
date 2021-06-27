"""This module contains miscellaneous utility functions."""
import os
from typing import Any, Callable, Dict, List, Type

from dotenv import dotenv_values


def get_project_folder(env_path: str = ".env") -> str:
    """Obtains the project directory using the `PROJECT_DIR` value from the supplied .env file."""
    values = dotenv_values(env_path)
    potential_path = values.get("PROJECT_DIR", "./")
    if os.path.isdir(potential_path):
        return os.path.abspath(potential_path)
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def get_abs_path(rel_path: str) -> str:
    """Constructs the absolute path from a relative path."""
    return os.path.abspath(os.path.join(get_project_folder(), rel_path))


def get_misty(env_path: str = ".env") -> Callable:
    """Obtains a Misty instance using the `MISTY_IP_ADDRESS` in the supplied .env file."""
    from misty2py.robot import Misty
    from misty2py.utils.env_loader import EnvLoader

    env_loader = EnvLoader(get_abs_path(env_path))
    return Misty(env_loader.get_ip())


def get_files_in_dir(abs_dir: str) -> List[str]:
    """Lists files in the supplied directory specified with an absolute path."""
    return [
        os.path.join(abs_dir, f)
        for f in os.listdir(abs_dir)
        if os.path.isfile(os.path.join(abs_dir, f))
    ]


def get_base_fname_without_ext(fname: str) -> str:
    """Returns the file name without the extension (or without extensions if multiple) from the supplied path."""
    base = os.path.basename(fname)
    return os.path.splitext(base)[0]


def query_dict_with_fallback(
    data: Dict, query: str, fallback: Any, required_type: Type = None
) -> Any:
    """Safely queries a dictionary, returns the queried value if it passes type check and the `fallback` otherwise.

    Args:
        data (Dict): The dictionary to query.
        query (str): The query.
        fallback (Any): The fallback value to return if the key does not exist or the queried value does not pass the type check.
        required_type (Type, optional): The required type of the queried value. `None` if there is no required type. Defaults to `None`.

    Returns:
        Any: The query result.
    """
    result = data.get(query)

    if result is None:
        return fallback

    if required_type is not None:
        if not isinstance(result, required_type):
            return fallback

    return result
