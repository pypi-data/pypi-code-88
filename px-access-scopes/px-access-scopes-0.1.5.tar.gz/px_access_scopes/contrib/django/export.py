from px_access_scopes import export_nested_tree, nested_tree_to_leaves

from .globals import registries


__all__ = 'export_scopes',


def export_scopes(as_leaves: bool = False):
    tree = {}

    for root in registries:
        tree.update(export_nested_tree(root))

    return tree if not as_leaves else nested_tree_to_leaves(tree)
