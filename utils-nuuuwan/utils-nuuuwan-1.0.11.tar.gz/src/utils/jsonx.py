"""JSON utils.

.. code-block:: python

    >>> from utils import jsonx
    >>> data = {'name': 'Alice', 'age': 20}
    >>> file_name = '/tmp/data.json'
    >>> jsonx.write(file_name, data)
    >>> data2 = jsonx.read(file_name)
    >>> data == data2
    True

"""
import json

from utils import filex


def read(file_name):
    """Read JSON from file.

    Args:
        file_name (str): file name

    Returns:
        Parsed JSON data

    """
    return json.loads(filex.read(file_name))


def write(file_name, data):
    """Write data as JSON to file.

    Args:
        file_name (str): file name
        data: data as serializable object

    """
    filex.write(file_name, json.dumps(data, indent=2))
