from .segmentation import Segmentation

def puzzle_to_internals(cells_str, clues):
  solution = [cell_str_to_marker(x) for x in cells_str]
  left_bounded_seq = Segmentation(len(cells_str), clues, True)
  right_bounded_seq = Segmentation(len(cells_str), clues, False)
  return solution, left_bounded_seq, right_bounded_seq

def internals_to_puzzle(solution):
  return ''.join([marker_to_cell_str(x) for x in solution])

def cell_str_to_marker(cell_str):
  if cell_str == '█':
    return 'g'
  if cell_str == 'x':
    return 'x'
  return 'e'

def marker_to_cell_str(marker):
  if 'g' in marker:
    return '█'
  if 'x' in marker:
    return 'x'
  return ' '
