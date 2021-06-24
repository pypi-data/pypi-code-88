from amazondax.CborSExprGenerator import (
    encode_condition_expression,
    encode_update_expression,
    encode_projection_expression)

from tests.Util import sexp, av

import pytest

TEST_CONDITION = [
    # Comparison
    pytest.param(('#a < :b', {'#a': 'c'}, {':b': av(5)}),   ('(< (. c) (: 0))', [av(5)]), id='LT'),
    pytest.param(('b <= c', {}, {}),                        ('(<= (. b) (. c))', []),  id='LE'),
    pytest.param(('b > e', {}, {}),                         ('(> (. b) (. e))', []),  id='GT'),
    pytest.param(('#b >= c', {'#b': 'a'}, {}),              ('(>= (. a) (. c))', []),  id='GE'),
    pytest.param(('#a <> :b', {'#a': 'c'}, {':b': av(5)}),  ('(<> (. c) (: 0))', [av(5)]),  id='NE'),

    # Logical
    pytest.param(('a < b OR c > d', {}, {}),    ('(or (< (. a) (. b)) (> (. c) (. d)))', []),  id='OR'),
    pytest.param(('a < b And c > d', {}, {}),   ('(and (< (. a) (. b)) (> (. c) (. d)))', []), id='AND'),
    pytest.param(('not (a < b)', {}, {}),       ('(not (< (. a) (. b)))', []), id='NOT'),

    # In
    pytest.param(('a in (:b,:c,:d)', {}, {':b': av(5), ':c': av(10), ':d': av(15)}), ('(in (. a) ((: 0) (: 1) (: 2)))', [av(5), av(10), av(15)]), id='IN'),

    # Between
    pytest.param(('a between :b and :d', {}, {':b': av(5), ':d': av(15)}), ('(between (. a) (: 0) (: 1))', [av(5), av(15)]), id='BETWEEN'),

    # Function
    pytest.param(('attribute_exists(a)', {}, {}),                   ('(attribute_exists (. a))', []), id='ATTR_EXISTS'),
    pytest.param(('attribute_not_exists(#a.c)', {'#a': 'b'}, {}),   ('(attribute_not_exists (. b c))', []), id='ATTR_NOT_EXISTS'),
    pytest.param(('attribute_type(a, S)', {}, {}),                  ('(attribute_type (. a) (. S))', []), id='ATTR_TYPE'),
    pytest.param(('begins_with(a, substr)', {}, {}),                ('(begins_with (. a) (. substr))', []), id='BEGINS_WITH'),
    pytest.param(('CONTAINS(a, :b)', {}, {':b': av(5)}),            ('(contains (. a) (: 0))', [av(5)]), id='CONTAINS'),
    pytest.param(('a > size(c)', {}, {}),                           ('(> (. a) (size (. c)))', []), id='SIZE'),

    # Document Path
    pytest.param(('a.b.c < :v', {}, {':v': av(5)}), ('(< (. a b c) (: 0))', [av(5)]), id='SIMPLE DP'),
    pytest.param(('#a.b.c < :v', {'#a': 'd'}, {':v': av(5)}), ('(< (. d b c) (: 0))', [av(5)]), id='# DP'),
    pytest.param(('a.b.c[0].d.e[1] < :v', {}, {':v': av(5)}), ('(< (. a b c [0] d e [1]) (: 0))', [av(5)]), id='INDEX DP'),
]

@pytest.mark.parametrize("data,expected", TEST_CONDITION)
def test_condition_expression(data, expected):
    actual = encode_condition_expression(*data)
    assert sexp(actual) == expected

TEST_PROJECTION = [
    (('a.b.#c, #d', {'#c': 'g', '#d': 'e.f'}, {}), ('((. a b g) (. e.f))', [])),
]
@pytest.mark.parametrize("data,expected", TEST_PROJECTION)
def test_projection_expression(data, expected):
    actual = encode_projection_expression(*data)
    assert sexp(actual) == expected

TEST_UPDATE = [
    pytest.param(('SET a = :b, c = c + :d', {}, {':b': av(5), ':d': av(15)}),   ('((SET (. a) (: 0)) (SET (. c) (+ (. c) (: 1))))', [av(5), av(15)]), id='SET +'),
    pytest.param(('SET a = a - :b', {}, {':b': av(5)}),                         ('((SET (. a) (- (. a) (: 0))))', [av(5)]),  id='SET -'),
    pytest.param(('REMOVE a, b, c', {}, {}),                                    ('((REMOVE (. a)) (REMOVE (. b)) (REMOVE (. c)))', []), id='REMOVE'),
    pytest.param(('ADD a :b, c :d', {}, {':b': av(5), ':d': av(15)}),           ('((ADD (. a) (: 0)) (ADD (. c) (: 1)))', [av(5), av(15)]), id='ADD'),
    pytest.param(('DELETE a :b', {}, {':b': {'SS': ['Yellow', 'Purple']}}),     ('((DELETE (. a) (: 0)))', [{'SS': ['Yellow', 'Purple']}]), id='DELETE'),
    pytest.param(('SET a = if_not_exists(a, :b)', {}, {':b': av(5)}),           ('((SET (. a) (if_not_exists (. a) (: 0))))', [av(5)]), id='SET if_not_exists'),
    pytest.param(('Set #a = list_append(#a, :b)', {'#a': 'c'}, {':b': av(5)}),  ('((SET (. c) (list_append (. c) (: 0))))', [av(5)]), id='SET list_append'),
]
@pytest.mark.parametrize("data,expected", TEST_UPDATE)
def test_update_expression(data, expected):
    actual = encode_update_expression(*data)
    assert sexp(actual) == expected


