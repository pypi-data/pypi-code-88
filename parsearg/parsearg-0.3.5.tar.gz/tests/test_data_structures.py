import pytest
from parsearg.data_structures import (
    Fifo,
    Tree,
    is_empty,
    Node,
    Key,
)
from parsearg.utils import (
    print_list,
    is_list_of,
)

def test_Fifo():
    import collections 
    assert isinstance(Fifo().values, collections.deque)
    assert len(Fifo().values)==0

def test_Fifo_is_empty():
    assert Fifo().is_empty()

def test_Fifo_insert():
    fifo = Fifo()
    fifo.insert('A')
    fifo.insert('B')
    assert fifo.values[0]=='A'
    assert fifo.values[1]=='B'

def test_Fifo_remove():
    fifo = Fifo()
    fifo.insert('A')
    fifo.insert('B')
    assert fifo.remove()=='A'
    assert fifo.remove()=='B'
    assert fifo.is_empty()

def test_Fifo_str():
    fifo = Fifo()
    fifo.insert('A')
    fifo.insert('B')
    assert fifo.__str__()=="deque(['A', 'B'])"


def test_Tree():
    tree = Tree()
    assert tree.value is None
    assert len(tree.children)==0

def test_Tree_is_empty():
    tree = Tree()
    assert tree.is_empty()

def test_is_empty_Tree():
    assert is_empty(None)
    assert is_empty(Tree())

def test_Tree_show(get_a_tree, get_a_aa_tree):
    tab = 4 * ' '

    s = 'A\n'               \
        + tab + 'B\n'       \
        + tab + 'BB\n'      \
        + 2 * tab + 'C\n'   \
        + 2 * tab + 'CC\n'  \
        + 2 * tab + 'CCC\n' \
        + tab + 'BBB'

    tree = get_a_tree
    assert tree.show(quiet=True)==s

    s = \
        'root\n'            \
        + tab + 'A\n'       \
        + 2 * tab + 'B\n'   \
        + 2 * tab + 'BB\n'  \
        + 3 * tab + 'C\n'   \
        + 3 * tab + 'CC\n'  \
        + 3 * tab + 'CCC\n' \
        + 2 * tab + 'BBB\n' \
        + tab + 'AA\n'      \
        + 2 * tab + 'B\n'   \
        + 2 * tab + 'BB\n'  \
        + 3 * tab + 'C\n'   \
        + 3 * tab + 'CC\n'  \
        + 3 * tab + 'CCC\n' \
        + 2 * tab + 'BBB'

    tree = get_a_aa_tree
    assert tree.show(quiet=True)==s

def test_Tree_Value():
    value = Tree.Value()
    assert value.name is None
    assert value.key is None
    assert value.payload is None

    d = {
        'A|B|C': {
            'arg1': {},
            'arg2': {},
            'arg3': {},
        }
    }

    value = Tree.Value(name='C', key=set(d.keys()).pop(), d=d)

    assert value.name=='C'
    assert value.key=='A|B|C'
    assert value.payload==d['A|B|C']


def test_Node():
    node = Node()
    assert Node().value==(None, [])

    node = Node(head='A', tail=['B', ['C']])
    assert node.value == ('A', ['B', ['C']])

def test_Node_head():
    node = Node(head='A', tail=['B', ['C']])
    assert node.head() == 'A' 

def test_Node_tail():
    node = Node(head='A', tail=['B', ['C']])
    assert node.tail() == ['B', ['C']]

def test_Node_is_empty():
    assert Node().is_empty()
    assert not Node('A').is_empty() 
    assert not Node('A', []).is_empty() 

def test_Node_lsfhift():
    node = Node(head='A', tail=['B', ['C']])
    assert (node << 1).head() == 'B'
    assert (node << 2).head() == 'C'

def test_Node_eq():
    assert Node() == Node()
    assert Node('A') == Node('A', [])

def test_Node_from_nested_list():
    # e.g. split from key:
    #     'A|B|C' -> ['A', '|', 'B', '|', 'C'] -> ['A', ['B', ['C']]]
    ll = ['A', ['B', ['C']]]
    assert Node.from_nested_list(ll) == Node(head='A', tail=['B', ['C']])


def test_Key():
    key = Key()
    assert key.key is None
    assert key.value == Node()
    assert key.payload is None

def test_Key_split():
    key = 'A|B|C'
    assert Key.split(key) == ['A', '|', 'B', '|', 'C']

def test_Key_unflatten():
    key = 'A|B|C'
    assert Key.unflatten(Key.split(key)) == ['A', ['B', ['C']]]

def test_Key_Node_from_key():
    assert Key.Node_from_key('A|B|C') == Node(head='A', tail=['B', ['C']])

def test_Key_is_empty():
    assert Key().is_empty()
    assert not Key('A').is_empty()

def test_Key_has_children():
    assert not Key().has_children()
    assert not Key('A').has_children()

    assert Key('A|B').has_children()

def test_Key_shift():
    # because the Key class preserves the key captured at object
    # instantiation you have to deliberately tamper with the Key's value
    # to make it equal to the shifted Node

    key = Key('A|B')
    key.value = Node(head='B', tail=[])

    assert (Key('A|B') << 1) == key

    key.value = Node(head=None, tail=[])
    assert (Key('A|B') << 2) == key

def test_Key_is_leaf():
    assert Key('A').is_leaf()

    assert not Key('A|B').is_leaf()
    assert (Key('A|B') << 1).is_leaf()

    d = {
        'A': {
            'arg1': {}, 'arg2': {}, 'arg3': {},
        },
        'A|B': {
            'arg1': {}, 'arg2': {}, 'arg3': {},
        },
        'A|B|C': {
            'arg1': {}, 'arg2': {}, 'arg3': {},
        },
    }

    keys = list(map(lambda key: Key(key), list(d.keys())))
    leaves = list(filter(lambda key: key.is_leaf(), keys))
    assert len(leaves)==1 and leaves[0] == Key('A')

    leaves = list(filter(lambda key: (key << 1).is_leaf(), keys))
    assert len(leaves)==1 and leaves[0] == Key('A|B')

    leaves = list(filter(lambda key: (key << 2).is_leaf(), keys))
    assert len(leaves)==1 and leaves[0] == Key('A|B|C')
