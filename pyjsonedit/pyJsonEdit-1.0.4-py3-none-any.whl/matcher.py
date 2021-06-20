"""
this module alows to freely move throug JsonNode's
"""
import re
from typing import Iterator, List
from pyjsonedit.parser import JsonNode

class MatchException(Exception):
    """failures in maching process"""
    def __eq__(self, other):
        return isinstance(other, MatchException) and \
            other.__str__() == self.__str__()

def _child_by_index(node:JsonNode, node_type:str, child_idx):
    if node.type != node_type:
        raise MatchException(f'unexpected node type: "{node.type}" expected "{node_type}"')
    if child_idx >= len(node.kids):
        raise MatchException(f'not enough kids {child_idx}')
    return node.kids[child_idx]

def _has_child_with_value(node:JsonNode, name, value) -> bool:
    for k in node.kids:
        if name == k.name and k.type=='value' and k.kids[0] == value:
            return True
    return False

def matcher_start(pattern, node):
    """ match child all childeren """
    return node.type != 'value' and pattern == '*'

def match_array_index(pattern, node):
    """ match child by [0] """
    return node.type != 'value' and re.match(r'\[(\d+)\]',pattern)

def match_dict_index(pattern, node):
    """ match child by {0} """
    return node.type != 'value' and re.match(r'\{(\d+)\}',pattern)

def match_dict_by_kid_name(pattern,node):
    """ match child by name  """
    if node.type == 'dict':
        for kid in node.kids:
            if pattern == kid.name:
                return True
    return False

def match_dict_by_kid_value(pattern,node):
    """ match child by value """
    return node.type == 'dict' and '=' in pattern

def _match_node(node:JsonNode, patterns, depth=0):
    """[generator]"""
    try:

        if depth >= len(patterns) or not patterns[depth].strip():
            yield node
            return

        pattern = patterns[depth].strip()

        #before/after
        if depth == len(patterns)-1:
            if pattern in [":after", ":before"]:
                yield JsonNode(pattern,
                                start=node.start,
                                end=node.end)
                return

        # array/dict by index
        if match_array_index(pattern, node) or match_dict_index(pattern, node):
            array_index = re.match(r'[\[\{](\d+)[\]\}]',pattern)
            child_idx = int(array_index.group(1))
            node = _child_by_index(node, 'array' if pattern[0]=='[' else 'dict', child_idx)
            yield from _match_node( node, patterns, depth+1)
            return

        # raw
        if matcher_start(pattern, node) or match_dict_by_kid_name(pattern,node):
            found = False
            for k in node.kids:
                if pattern == '*':
                    found = True
                    yield from _match_node( k, patterns, depth+1)
                elif pattern in k.name:
                    found = True
                    yield from _match_node( k, patterns, depth+1)
            if found:
                return

        # match if dict
        if match_dict_by_kid_value(pattern,node):
            pattern = pattern.split('=')
            assert len(pattern)==2, "malformed equal operation"
            child_name,child_value = pattern
            if _has_child_with_value(node, child_name.strip(), child_value.strip()):
                yield from _match_node(node, patterns, depth+1)
            return

        raise MatchException(f'pattern "{pattern}" not found')
    except MatchException as fail:
        yield fail

def parse_pattern(pattern:str):
    """ tokenize matching patter """
    pattern = pattern.strip()

    tail = None
    for i in [":before",":after"]:
        if pattern.endswith(i):
            pattern = pattern[0:-len(i)].strip()
            tail = i

    ret = []
    for pat in pattern.split('>'):
        pat = pat.strip()
        if pat:
            ret.append(pat)

    if tail:
        ret.append(tail)
    return ret

def match(root: JsonNode, pattern: str) -> Iterator[JsonNode]:
    """ [generator] start node matching"""
    patterns = parse_pattern(pattern)
    yield from _match_node(root, patterns)


def match_as_list(tree:JsonNode, pattern:str) -> List[JsonNode]:
    """ create list of matched JsonNode's using 'pattern' """
    ret = []
    for node in match(tree, pattern):
        if not isinstance(node, JsonNode):
            raise node
        ret.append(node)
    return ret
