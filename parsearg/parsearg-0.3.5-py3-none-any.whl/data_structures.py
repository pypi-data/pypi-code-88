from collections import deque
from parsearg.utils import (
    is_list_of,
)

# TODO: replace with Queue class that accepts a QueueingPolicy class (mixin?)
class Fifo:
    def __init__(self):
        self.values = deque()

    def insert(self, value):
        self.values.append(value)
     
    def remove(self):
        o = self.values.popleft()
        return o

    def is_empty(self):
        return len(self.values) == 0

    def __str__(self):
        return str(self.values)
        

def is_empty(tree):
    assert isinstance(tree, Tree) or tree is None
    return True if tree is None or tree.is_empty() else False

class Tree:
    class Value:
        def __init__(self, name=None, key=None, d=None):
            def check(x):
                if x is not None:
                    assert isinstance(x, str) 
            check(name)
            check(key)

            self.name    = name
            self.key     = key
            if d is not None:
                assert isinstance(d, dict)
                self.payload = d[key]
            else:
                self.payload = d

        def __str__(self):
            # return f'{self.key!r}: {self.name}'
            # return f'{self.key!r}: {self.name}\n\tpayload = {self.payload}'
            return f'{self.name}'

        __repr__ = __str__


    def __init__(self, value=None, children=None):
        self.value    = value
        self.children = children if children is not None else []

    def __str__(self):
        return str(self.value)

    def is_empty(self):
        return (self.value is None) and \
               len(self.children) == 0
       
    def show(self, level=0, indent = 4 * ' ', quiet=False):
        # depth-first search (DFS)
        def _show(tree, level, indent):
            nonlocal o
            if is_empty(tree):
                return 

            o += ['{}{}'.format(level*indent, tree)]
            for child in tree.children:
                _show(child, level=level+1, indent=indent)

        o = []
        _show(self, level, indent)
        o = '\n'.join(o)

        if not quiet:
            print(o)

        return o
       

class Node:
    def __init__(self, head=None, tail=None):
        if not head is None:
            assert isinstance(head, str)
        if not tail is None:
            assert isinstance(tail, list)

        self.value = (head, tail if tail is not None else [])

    def head(self):
        return self.value[0]

    def tail(self):
        return self.value[1]

    def is_empty(self):
        return True if self.head() is None and not len(self.tail()) else False

    def __str__(self):
        return f'{self.value}'

    def __repr__(self):
        return self.__str__()

    def __eq__(self, rv):
        return True if self.head() == rv.head() and self.tail() == rv.tail() else False

    def __lshift__(self, by=1):
        o = self
        for s in range(by):
            o = o.from_nested_list(o.tail())
        return o

    @classmethod
    def from_nested_list(cls, x):
        assert isinstance(x, list)

        def head(x):
            assert isinstance(x, list)
            if not len(x):
                return x
            return x[0]

        def tail(x):
            assert isinstance(x, list)
            if len(x) <= 1:
                return x
            return x[1]

        if not len(x):
            return cls(head=None, tail=[])

        if len(x)==1:
            if isinstance(head(x), list):
                return to_node(head(x))
            else:
                return cls(head=head(x), tail=[])

        return cls(head=head(x), tail=tail(x))


class Key:
    def __init__(self, key=None, d=None):
        self.key     = key
        self.d       = d
        self.value   = self.Node_from_key(self.key)
        self.payload = None

        if d is not None:
            assert self.key in d
            self.payload = d[key]

    def is_empty(self):
        return self.value.is_empty()

    def is_leaf(self):
        return not self.value.is_empty() and not len(self.value.tail())

    def has_children(self):
        return len(self.value.tail()) > 0

    def __eq__(self, rv):
        return True if self.key == rv.key and self.value == rv.value else False

    def __lshift__(self, by=1):
        o = self
        for s in range(by):
            o = o.shift()
        return o

    def shift(self, by=1):
        o = Key(key=self.key, d=self.d)
        o.value = self.value << by

        return o

    def __str__(self):
        payload = ''
        if self.payload is not None:
            payload = '\n'
            for k, v in self.payload.items():
                payload += f'\t{k}: {v}\n'
        return f'{self.key!r}: {self.value}{payload}'

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def split(s, sep='|'):
        if not len(s):
            return []
        left, sep, right = s.partition(sep)
        return [left] + [sep] + Key.split(right) if len(right) else [left]

    @staticmethod
    def unflatten(x, sep='|'):
        # UNFLATTEN AS LIST
        def _unflatten(x, sep=sep):
            if not len(x):
                return []
            elif x[0]==sep:
                return [_unflatten(x[1:])]
            else:
                return [x[0]]  + _unflatten(x[1:])

        assert is_list_of(x, str)
        return _unflatten(x, sep=sep)

    @staticmethod
    def Node_from_key(key, sep='|'):
        if key is None:
            return Node()

        return Node.from_nested_list(
            Key.unflatten(Key.split(key, sep=sep))
        )
