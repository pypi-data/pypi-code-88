from .identifiers import is_group, is_cross, is_unidentified, is_satisfied

def test_is_group_identified():
  assert is_group('g2')
def test_is_group_unidentified():
  assert is_group('g')
def test_is_not_group():
  assert not is_group(' ')
  assert not is_group('x')
  assert not is_group('x2')

def test_is_cross_identified():
  assert is_cross('x1')
def test_is_cross_unidentified():
  assert is_cross('x')
def test_is_not_cross():
  assert not is_cross(' ')
  assert not is_cross('g')
  assert not is_cross('g2')

def test_is_unidentified_group():
  assert is_unidentified('g')
def test_is_unidentified_cross():
  assert is_unidentified('x')
def test_is_not_unidentified():
  assert not is_unidentified('g1')
  assert not is_unidentified('x2')

def test_is_satisfied():
  assert is_satisfied('g', 'g')
  assert is_satisfied('g', 'g1')
  assert is_satisfied('g1', 'g1')
  assert is_satisfied('x', 'x')
  assert is_satisfied('x', 'x1')
  assert is_satisfied('x1', 'x1')
  assert is_satisfied('e', 'g')
  assert is_satisfied('e', 'g1')
  assert is_satisfied('e', 'x')
  assert is_satisfied('e', 'x1')

def test_is_not_satisfied():
  assert not is_satisfied('g', 'x')
  assert not is_satisfied('g', 'x1')
  assert not is_satisfied('g1', 'x')
  assert not is_satisfied('g1', 'x1')
  assert not is_satisfied('g1', 'g2')
  assert not is_satisfied('x', 'g')
  assert not is_satisfied('x', 'g1')
  assert not is_satisfied('x1', 'g')
  assert not is_satisfied('x1', 'g1')
  assert not is_satisfied('x1', 'x2')
