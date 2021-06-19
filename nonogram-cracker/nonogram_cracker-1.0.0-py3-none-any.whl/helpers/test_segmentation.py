from .segmentation import Segmentation

def test_segmentation_empty():
  assert Segmentation(5, [], True).internals() ==  '[ (x0 * 5) ]'
  assert Segmentation(5, [], False).internals() == '[ (x0 * 5) ]'
  assert Segmentation(5, [], True).flat_internals() ==  ['x0', 'x0', 'x0', 'x0', 'x0']
  assert Segmentation(5, [], False).flat_internals() == ['x0', 'x0', 'x0', 'x0', 'x0']

def test_segmentation_full():
  assert Segmentation(5, [5], True).internals() ==  '[ (x0 * 0) (g0 * 5) (x1 * 0) ]'
  assert Segmentation(5, [5], False).internals() == '[ (x0 * 0) (g0 * 5) (x1 * 0) ]'
  assert Segmentation(5, [5], True).flat_internals() ==  ['g0', 'g0', 'g0', 'g0', 'g0']
  assert Segmentation(5, [5], False).flat_internals() == ['g0', 'g0', 'g0', 'g0', 'g0']

def test_segmentation_single_cell():
  assert Segmentation(5, [1], True).internals() ==  '[ (x0 * 0) (g0 * 1) (x1 * 4) ]'
  assert Segmentation(5, [1], False).internals() == '[ (x0 * 4) (g0 * 1) (x1 * 0) ]'
  assert Segmentation(5, [1], True).flat_internals() ==  ['g0', 'x1', 'x1', 'x1', 'x1']
  assert Segmentation(5, [1], False).flat_internals() == ['x0', 'x0', 'x0', 'x0', 'g0']

def test_segmentation_mostly_full():
  assert Segmentation(5, [4], True).internals() ==  '[ (x0 * 0) (g0 * 4) (x1 * 1) ]'
  assert Segmentation(5, [4], False).internals() == '[ (x0 * 1) (g0 * 4) (x1 * 0) ]'
  assert Segmentation(5, [4], True).flat_internals() ==  ['g0', 'g0', 'g0', 'g0', 'x1']
  assert Segmentation(5, [4], False).flat_internals() == ['x0', 'g0', 'g0', 'g0', 'g0']

def test_segmentation_split():
  assert Segmentation(5, [1, 1], True).internals() ==  '[ (x0 * 0) (g0 * 1) (x1 * 1) (g1 * 1) (x2 * 2) ]'
  assert Segmentation(5, [1, 1], False).internals() == '[ (x0 * 2) (g0 * 1) (x1 * 1) (g1 * 1) (x2 * 0) ]'
  assert Segmentation(5, [1, 1], True).flat_internals() ==  ['g0', 'x1', 'g1', 'x2', 'x2']
  assert Segmentation(5, [1, 1], False).flat_internals() == ['x0', 'x0', 'g0', 'x1', 'g1']

def test_segmentation_can_group_shift_1():
  assert Segmentation(5, [1, 1], True).can_group_shift(1) ==  4 #  ['g0', 'x1', 'g1', 'x2', 'x2']
  assert Segmentation(5, [1, 1], True).can_group_shift(3) ==  4 #  ['g0', 'x1', 'g1', 'x2', 'x2']
  
  assert Segmentation(5, [1, 1], False).can_group_shift(1) ==  0 #  ['x0', 'x0', 'g0', 'x1', 'g1']
  assert Segmentation(5, [1, 1], False).can_group_shift(3) ==  0 #  ['x0', 'x0', 'g0', 'x1', 'g1']

def test_segmentation_can_group_shift_2():
  assert Segmentation(5, [4], True).can_group_shift(1) == 2 # ['g0', 'g0', 'g0', 'g0', 'x1']
  assert Segmentation(5, [4], False).can_group_shift(1) == 0 #  ['g0', 'g0', 'g0', 'g0', 'x1']

def test_segmentation_shift_group_1():
  s = Segmentation(5, [1, 1], True) # ['g0', 'x1', 'g1', 'x2', 'x2']
  assert s.shift_group(1) == True
  assert s.flat_internals() == ['x0', 'g0', 'x1', 'g1', 'x2']
  assert s.shift_group(1) == True
  assert s.flat_internals() == ['x0', 'x0', 'g0', 'x1', 'g1']
  assert s.shift_group(1) == False

  s = Segmentation(5, [1, 1], True) # ['g0', 'x1', 'g1', 'x2', 'x2']
  assert s.shift_group(3) == True
  assert s.flat_internals() == ['g0', 'x1', 'x1', 'g1', 'x2']
  assert s.shift_group(3) == True
  assert s.flat_internals() == ['g0', 'x1', 'x1', 'x1', 'g1']
  assert s.shift_group(3) == False

  s = Segmentation(5, [1, 1], False) # ['x0', 'x0', 'g0', 'x1', 'g1']
  assert s.shift_group(1) == True
  assert s.flat_internals() == ['x0', 'g0', 'x1', 'x1', 'g1']
  assert s.shift_group(1) == True
  assert s.flat_internals() == ['g0', 'x1', 'x1', 'x1', 'g1']
  assert s.shift_group(1) == False

  s = Segmentation(5, [1, 1], False) # ['x0', 'x0', 'g0', 'x1', 'g1']
  assert s.shift_group(3) == True
  assert s.flat_internals() == ['x0', 'g0', 'x1', 'g1', 'x2']
  assert s.shift_group(3) == True
  assert s.flat_internals() == ['g0', 'x1', 'g1', 'x2', 'x2']
  assert s.shift_group(3) == False

def test_get_first_unsatisfied_cell_index_empty_clues_none():
  s = Segmentation(5, [], True) # ['x0', 'x0', 'x0', 'x0', 'x0']
  assert s.get_first_unsatisfied_cell_index(['e', 'e', 'e', 'e', 'e']) ==  None
  assert s.get_first_unsatisfied_cell_index(['x', 'x', 'x', 'x', 'x']) ==  None
  s = Segmentation(5, [], False) # ['x0', 'x0', 'x0', 'x0', 'x0']
  assert s.get_first_unsatisfied_cell_index(['e', 'e', 'e', 'e', 'e']) ==  None
  assert s.get_first_unsatisfied_cell_index(['x', 'x', 'x', 'x', 'x']) ==  None

def test_get_first_unsatisfied_cell_index_empty_clues():
  s = Segmentation(5, [], True) # ['x0', 'x0', 'x0', 'x0', 'x0']
  assert s.get_first_unsatisfied_cell_index(['x', 'g', 'e', 'e', 'e']) ==  1
  assert s.get_first_unsatisfied_cell_index(['x', 'e', 'e', 'g', 'e']) ==  3
  assert s.get_first_unsatisfied_cell_index(['x', 'g', 'x', 'g', 'x']) ==  3
  s = Segmentation(5, [], False) # ['x0', 'x0', 'x0', 'x0', 'x0']
  assert s.get_first_unsatisfied_cell_index(['x', 'g', 'e', 'e', 'e']) ==  1
  assert s.get_first_unsatisfied_cell_index(['x', 'e', 'e', 'g', 'e']) ==  3
  assert s.get_first_unsatisfied_cell_index(['x', 'g', 'x', 'g', 'x']) ==  1

def test_get_first_unsatisfied_cell_index_mostly_full_clues_none():
  s = Segmentation(5, [4], True) # ['g0', 'g0', 'g0', 'g0', 'x1']
  assert s.get_first_unsatisfied_cell_index(['e', 'e', 'e', 'e', 'e']) ==  None
  assert s.get_first_unsatisfied_cell_index(['g', 'g', 'g', 'g', 'e']) ==  None
  assert s.get_first_unsatisfied_cell_index(['e', 'e', 'e', 'e', 'x']) ==  None
  assert s.get_first_unsatisfied_cell_index(['g', 'g', 'g', 'g', 'x']) ==  None
  s = Segmentation(5, [4], False) # ['x0', 'g0', 'g0', 'g0', 'g0']
  assert s.get_first_unsatisfied_cell_index(['e', 'e', 'e', 'e', 'e']) ==  None
  assert s.get_first_unsatisfied_cell_index(['e', 'g', 'g', 'g', 'g']) ==  None
  assert s.get_first_unsatisfied_cell_index(['x', 'e', 'e', 'e', 'e']) ==  None
  assert s.get_first_unsatisfied_cell_index(['x', 'g', 'g', 'g', 'g']) ==  None

def test_get_corresponding_segment_index():
  s = Segmentation(5, [1, 1], True) # ['g0', 'x1', 'g1', 'x2', 'x2']
  assert s.get_corresponding_segment_index(0) == 1
  assert s.get_corresponding_segment_index(1) == 2
  assert s.get_corresponding_segment_index(2) == 3
  assert s.get_corresponding_segment_index(3) == 4
  assert s.get_corresponding_segment_index(4) == 4
  
  s = Segmentation(5, [1, 1], False) # ['x0', 'x0', 'g0', 'x1', 'g1']
  assert s.get_corresponding_segment_index(0) == 0
  assert s.get_corresponding_segment_index(1) == 0
  assert s.get_corresponding_segment_index(2) == 1
  assert s.get_corresponding_segment_index(3) == 2
  assert s.get_corresponding_segment_index(4) == 3
