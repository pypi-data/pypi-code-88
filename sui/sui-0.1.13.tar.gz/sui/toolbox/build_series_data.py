"""Convert user's log data into series data
Date: 02/Mar/2021
Author: Li Tang
"""
from typing import Union
import random

__author__ = ['Li Tang']
__copyright__ = 'Li Tang'
__credits__ = ['Li Tang']
__license__ = 'MIT'
__version__ = '0.1.11'
__maintainer__ = ['Li Tang']
__email__ = 'litang1025@gmail.com'
__status__ = 'Production'


def build_session(data: Union[list, tuple], user_idx: Union[int, None], item_idx: int, timestamp_idx: int, session_gap: int):
    """Function to split data into multiple sessions

    Args:
        data: user's log data sorted input data consists of lists or tuples, including user id, item id, and timestamp
        user_idx: index of the user id in each user's log data; set user_idx to None can build session without user id
        item_idx: index of the item id in each user's log data
        timestamp_idx: index of the timestamp in each user's log data
        session_gap: the threshold to split user's activities into multiple sessions based the gap of adjacent timestamps

    Returns:
        a list sorted by target dimension with length no greater than k

    Examples:
        >>> log_data = (('user_867as8e', 'v9d8cv8272lk', 1614652639000),
        ...             ('user_867as8e', 'v8d4ln9834kj', 1614653499000),
        ...             ('user_868yu82', 'n0s3mn43k4n3', 1614653646000),
        ...             ('user_868yu82', 'v987d3n5l89n', 1614653702246))
        >>> build_session(data=log_data, user_idx=0, item_idx=1, timestamp_idx=2, session_gap=600000)
        [('user_867as8e', ['v9d8cv8272lk']), ('user_867as8e', ['v8d4ln9834kj']), ('user_868yu82', ['n0s3mn43k4n3', 'v987d3n5l89n'])]
        >>> log_data = (('v9d8cv8272lk', 1614652639000),
        ...             ('v8d4ln9834kj', 1614653499000),
        ...             ('n0s3mn43k4n3', 1614653646000),
        ...             ('v987d3n5l89n', 1614653702246))
        >>> build_session(data=log_data, user_idx=None, item_idx=0, timestamp_idx=1, session_gap=100000)
        [['v9d8cv8272lk'], ['v8d4ln9834kj'], ['n0s3mn43k4n3', 'v987d3n5l89n']]

    """
    is_first_log = True
    result = []
    current_ts = 0
    session = []

    # if user id exists
    if user_idx is not None:
        user_id = ''
        for log in data:
            # if this is the first log
            if is_first_log:
                user_id = log[user_idx]
                current_ts = log[timestamp_idx]
                is_first_log = False

            if user_id == log[user_idx] and log[timestamp_idx] - current_ts <= session_gap:
                session.append(log[item_idx])
            else:
                result.append((user_id, session))
                session = [log[item_idx]]
                user_id = log[user_idx]
                current_ts = log[timestamp_idx]
        result.append((user_id, session))

        return result

    # else build sessions with no user id
    else:
        for log in data:
            if is_first_log:
                current_ts = log[timestamp_idx]
                is_first_log = False

            if log[timestamp_idx] - current_ts <= session_gap:
                session.append(log[item_idx])
            else:
                result.append(session)
                session = [log[item_idx]]
                current_ts = log[timestamp_idx]
        result.append(session)

        return result


def random_walk(G, walk_depth: int, walk_path: list) -> list:
    """Function to generate a series data by walking in the input graph data randomly

    Args:
        G: input graph data
        walk_depth: the length of the walking result
        walk_path: the existing walking history; walking will start at the last element in walk_path

    Returns:
        a list consisting of every passed vertex

    Examples:
        >>> import networkx as nx
        >>> G = nx.Graph()
        >>> G.add_nodes_from([
        ...     ('Beijing', {'Country': 'CN'}),
        ...     ('London', {'Country': 'UK'}),
        ...     ('Zhuzhou', {'Country': 'CN'}),
        ...     ('Manchester', {'Country': 'UK'}),
        ...     ('New York', {'Country': 'US'}),
        ...     ('Michigan', {'Country': 'US'}),
        ...     ('Shanghai', {'Country': 'CN'})
        ... ])
        >>> G.add_edges_from([
        ...     ('Beijing', 'Zhuzhou'),
        ...     ('Beijing', 'London'),
        ...     ('Beijing', 'New York'),
        ...     ('Beijing', 'Shanghai'),
        ...     ('Zhuzhou', 'Shanghai'),
        ...     ('Shanghai', 'London'),
        ...     ('Shanghai', 'New York'),
        ...     ('Shanghai', 'Michigan'),
        ...     ('London', 'Manchester'),
        ...     ('London', 'New York'),
        ...     ('New York', 'Michigan')
        ... ])
        >>> result = []
        >>> for vertex in G.nodes:
        ...     result.append(random_walk(G=G, walk_depth=5, walk_path=[vertex]))
        >>> len(result), len(result[0])
        (7, 5)
        >>> [_[0] for _ in result]
        ['Beijing', 'London', 'Zhuzhou', 'Manchester', 'New York', 'Michigan', 'Shanghai']

    """
    if len(walk_path) < 1:
        raise ValueError("'walk_path' should include at least 1 vertex to start walking.")
    while len(walk_path) < walk_depth:
        current_vertex = walk_path[-1]
        neighbors_list = list(G.neighbors(current_vertex))
        if len(neighbors_list) > 0:
            walk_path.append(random.choice(neighbors_list))
        else:
            break

    return walk_path
