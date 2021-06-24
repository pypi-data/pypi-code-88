"""Utils related to lists and dicts."""


def dict_list_to_index(dict_list, key):
    """Given a list of dicts, returns an index mapping each dict item
    to the dict.

    Args:
        dict_list (list of dicts): list of dicts
        key (str): key

    Return:
        index (dict)

    .. code-block:: python

        >>> from utils.ds import dict_list_to_index
        >>> dict_list = [
            {'name': 'Alice', 'age': 20},
            {'name': 'Bob', 'age': 25},
            {'name': 'Charlie', 'age': 55},
        ]
        >>> print(dict_list_to_index(dict_list, 'name'))
        {
            'Alice': {'name': 'Alice', 'age': 20},
            'Bob': {'name': 'Bob', 'age': 25},
            'Charlie': {'name': 'Charlie', 'age': 55},
        }


    """
    return dict(zip(
        list(map(
            lambda d: d.get(key, None),
            dict_list,
        )),
        dict_list,
    ))


def unique(lst):
    """Get unique values from list.

    Args:
        lst (list): List

    Return:
        list of unique values

    .. code-block:: python

        >>> from utils.ds import unique
        >>> lst = [1, 1, 1, 2]
        >>> print(unique(lst))
        [1, 2]

    """
    return list(set(lst))


def flatten(list_of_list):
    """Flatten list of lists.

    Args:
        list_of_list(list): list of lists

    Return:
        flattened list

    .. code-block:: python

    >>> print(flatten([[1, 2], [3, 4, 5], [6], []]))
    [1, 2, 3, 4, 5, 6]

    """
    flattened_list = []
    for lst in list_of_list:
        flattened_list += lst
    return flattened_list


def sort_dict_items_by_key(_dict):
    """Sort dict items by key."""
    return sorted(
        _dict.items(),
        key=lambda item: item[0],
    )
