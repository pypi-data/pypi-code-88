import sys
import argparse
from parsearg.data_structures import (
    is_empty,
    Tree,
    Key,
)
from parsearg.utils import (
    print_list,
    is_list_of,
)


class ParseArg:
    def __init__(self, d, root_name=None):
        assert isinstance(d, dict)

        self.d       = d
        self.tree    = ParseArg.to_tree(self.d, root_name=root_name)
        self.parser  = argparse.ArgumentParser(add_help=True)
        ParseArg.make_subparsers(self.tree, self.parser)

    def parse_args(self, args):
        args   = args.split() if isinstance(args, str) else args
        return self.parser.parse_args(args)

    @staticmethod
    def make_subparsers(tree, parser):
        def argparse_argument_name_or_flags(keys):
            keys = keys.split('|')
            keys = list(map(lambda x: x.strip(' \t\n\r'), keys))

            return keys

        def make_parser(node, subparsers):
            assert type(node.value) == Tree.Value
            parser = subparsers.add_parser(node.value.name)

            # print(f'node = {node.value}')
            if node.value.payload is not None:
                for key, value in node.value.payload.items():
                    if key == 'callback':
                        parser.set_defaults(
                            callback=value
                        )
                    else:
                        parser.add_argument(
                            *argparse_argument_name_or_flags(key), **value
                        )

            if len(node.children):
                subparsers = parser.add_subparsers()
                for child in node.children:
                    make_parser(child, subparsers)

        if not tree.is_empty():
            subparsers = parser.add_subparsers()
            for child in tree.children:
                make_parser(child, subparsers)

    @staticmethod
    def to_tree(d, root_name=None):
        assert isinstance(d, dict)
        root_name = 'root' if root_name is None else root_name

        nodes = map(lambda key: Key(key), d.keys())
        nodes = list(filter(lambda x: not x.is_empty(), nodes))

        def _to_tree(x):
            if isinstance(x, list) and len(x)==1 and x[0].is_leaf():
                x = x[0]

                return Tree(
                    Tree.Value(name=x.value.head(), key=x.key, d=d)
                )

            else:
                name = set(map(lambda x: x.value.head(), x))
                assert len(name)==1
                name = name.pop()

                o       = []
                shifted = list(map(lambda x: x << 1, x))

                # optional arguments added to node itself
                tree = None
                empty   = list(filter(lambda x: x.is_empty(), shifted))
                assert len(empty) <= 1
                if len(empty):
                    x = empty[0]
                    tree = Tree(
                        Tree.Value(name = name, key=x.key, d=d)
                    )

                # arguments added to child nodes
                children    = list(filter(lambda x: not x.is_empty(), shifted))
                child_names = set(map(lambda x: x.value.head(), children))

                for child_name in child_names:
                    child = list(filter(lambda x: x.value.head() == child_name, children))
                    o    += [_to_tree(child)]

                if tree is not None:
                    tree.children = o 
                else:
                    tree = Tree(Tree.Value(name=name, key=None), children=o)

                return tree

        o = []
        for name in set(map(lambda x: x.value.head(), nodes)):
            node = list(filter(lambda x: x.value.head()==name, nodes))
            o += [_to_tree(node)]

        return Tree(root_name, children=o)
