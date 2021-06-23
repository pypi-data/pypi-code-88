from collections import deque

from .scopes import ScopeRegistry


def dict_tree(registry: ScopeRegistry):
    current = registry._domain
    tree = {}
    maps = {None: tree}
    state = deque(((None, current,),))
    h = registry._hierarchy

    # while True:
    #     try:
    #         parent, current = state.popleft()
    #     except IndexError:
    #         break

    #     children = []
    #     maps[parent] = maps.get(parent, {})
    #     maps[parent][current] = current
    #     for scope in current:


    return tree
