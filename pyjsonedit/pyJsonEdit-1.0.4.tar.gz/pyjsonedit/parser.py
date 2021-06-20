"""parse token list to recursive JsonNodes"""
from typing import List
from pyjsonedit.token_list import TokenList

class JsonNode:
    """ json node with begin end end children"""
    def __init__(self, obj_type, **kwargs):
        self.type = obj_type
        self.start = kwargs['start']
        self.end = kwargs['end']
        self.name = kwargs.get('name','')
        self.kids = kwargs.get('kids',[])
        if 'value' in kwargs:
            self.kids = [kwargs['value']]

    def append(self,obj):
        """add one child"""
        self.kids.append( obj )

    def __repr__(self):
        return self.to_string()

    def to_string(self,depth=0):
        """this object as string"""
        prefix=' '*(2*depth)
        if self.type=='value':
            return f'JsonNode::{self.type}[{self.start}..{self.end}] = {self.kids[0]}'

        return f'JsonNode::{self.type}[{self.start}..{self.end}] ' +\
               f'\n{prefix}{{\n' +\
               ',\n'.join([ ' '*(2*(depth+1))+
                             str(i)+
                             ( '="'+child.name+'"' if child.name else '' )+
                             ": "+child.to_string(depth+1) for i,child in enumerate(self.kids)]) +\
               f'\n{prefix}}}'

    def __eq__(self, obj):
        return isinstance(obj, JsonNode) and\
                obj.start == self.start and\
                obj.end == self.end and\
                obj.type == self.type and\
                obj.kids == self.kids and\
                obj.name == self.name


def __string_token_get_text(token):
    """ get names without quotes"""
    return token[2].strip("'\"")

def eat_value(tok: TokenList) -> JsonNode:
    """
    convert value tokens to object
    V -> JsonNode
    """
    begin = tok.expect_pop('v', 'not a value')
    return JsonNode('value',
                    start= begin[1],
                    end  =(begin[1] + len(begin[2])),
                    value= begin[2])

def eat_string(tok: TokenList) -> JsonNode:
    """
    convert stirng tokens to object
    V -> JsonNode
    """
    token = tok.expect_pop('s', 'not a string')
    return JsonNode('value',
                    start = token[1],
                    end   =(token[1] + len(token[2])),
                    value = __string_token_get_text(token))

def eat_child(tok: TokenList) -> JsonNode:
    """
    (V|S|A|D)
    """
    ret = None
    if   tok.next_is('v'):
        ret = eat_value(tok)
    elif tok.next_is('s'):
        ret = eat_string(tok)
    elif tok.next_is('['):
        ret = eat_array(tok)
    elif tok.next_is('{'):
        ret = eat_dict(tok)
    return ret

def eat_dict(tok:TokenList) -> JsonNode:
    """
    convert dict tokens to object,
    basicalyy array with named items
    '{' 's':(V|A|D)* '}'
    """
    begin = tok.expect_pop('{', 'not object')
    ret = JsonNode('dict',
                   start=begin[1],
                   end=False)

    while tok.peek():

        if tok.next_is('s'):

            token_name = tok.pop()
            if len(token_name) != 3 or not token_name[2]:
                tok.raise_token_error('string token is missing value')
            tok.expect_pop(':', 'missing ":"')
            child = eat_child(tok)
            if not child:
                tok.raise_token_error('missing child')
            child.name = __string_token_get_text(token_name)
            ret.append(child)

            if tok.next_is(','):
                tok.pop()
                continue

        end = tok.expect_pop('}', 'object error, unexpectd token: {}'.format( str(tok.peek()) ))
        ret.end = end[1]+1
        return ret

    tok.raise_token_error('object not closed')


def eat_array(tok:TokenList) -> JsonNode:
    """
    convert array tokens to object
    '[' ( S|V|A|D )* ']'
    """
    begin = tok.expect_pop('[', 'not array')

    ret = JsonNode('array',
                   start=begin[1],
                   end=False)
    while tok.peek():

        child = eat_child(tok)
        if child:
            ret.append(child)
            if tok.next_is(','):
                tok.pop()
                continue

        end = tok.expect_pop(']', 'array error unexpectd token: {}'.format( str(tok.peek()) ))
        ret.end = end[1]+1
        return ret

    tok.raise_token_error('array error, object not closed')

def parse(tokens:List) -> JsonNode:
    """
    Conver tokens into object (dict)
    """
    tok = TokenList(tokens)
    return eat_dict(tok)
