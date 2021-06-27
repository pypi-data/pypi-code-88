from pkgutil import extend_path
from typing import List
from concurrent.futures import ThreadPoolExecutor

from .validators import validate_node

__path__ = extend_path(__path__, __name__)


def validate(nodes: List[dict]):
    """
    Validates a list of Hestia JSON-Nodes against a list of rules.

    Parameters
    ----------
    nodes : List[dict]
        The list of JSON-Nodes to validate.

    Returns
    -------
    List
        The list of errors for each node, which can be empty if no errors detected.
    """
    with ThreadPoolExecutor() as executor:
        return list(executor.map(validate_node(nodes), nodes))
