from collections import deque

from .scopes import ScopeRegistry


__all__ = (
    'export_nested_tree',
    'nested_tree_to_leaves',
    'export_nested_tree_leaves',
)


VALUE_KEY = 'v'
CHILDREN_KEY = 'c'


def export_nested_tree(
    registry: ScopeRegistry,
    value_key: str = VALUE_KEY,
    children_key: str = CHILDREN_KEY
) -> dict:
    current = registry._domain
    maps = {}
    state = deque(((None, current, current._definition[-1]),))
    h = registry._hierarchy
    s = registry._sets

    while True:
        try:
            parent, current, key = state.popleft()
        except IndexError:
            break

        maps[parent] = maps.get(parent, {
            value_key: parent, children_key: {},
        })
        maps[current] = {
            value_key: current, children_key: {},
        }
        maps[parent][children_key][key] = maps[current]

        if current in h:
            for scope in h[current]:
                state.append((current, scope, scope._definition[-1]))

        if current in s:
            for e in s[current]:
                state.append((current, e, e._name_))

    return maps[None][children_key]


def nested_tree_to_leaves(
    tree: dict,
    value_key: str = VALUE_KEY,
    children_key: str = CHILDREN_KEY
) -> dict:
    return {
        key: (
            values[value_key]
            if len(values[children_key].keys()) == 0
            else nested_tree_to_leaves(values[children_key])
        )
        for key, values in tree.items()
    }


def export_nested_tree_leaves(registry: ScopeRegistry) -> dict:
    exported = export_nested_tree(registry)

    return nested_tree_to_leaves(exported)
