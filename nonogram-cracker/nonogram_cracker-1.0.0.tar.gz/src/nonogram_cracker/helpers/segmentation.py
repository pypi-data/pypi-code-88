from marshmallow.exceptions import ValidationError
from . import converter
from .identifiers import is_satisfied, is_group, is_cross

class Segment():
  def __init__(self, char, id, size, is_edge = False):
    self.char = char
    self.id = id
    self.size = size
    self.is_group = char == 'g'
    self.is_cross = char == 'x'
    self.is_edge = is_edge
  
  def can_shrink(self):
    return self.size > 1 or (self.is_edge and self.size > 0)

  def __repr__(self):
    return str(self)
  
  def __len__(self):
    return self.size
  
  def __eq__(self, other):
    return str(self) == str(other)
  
  def resolve(self):
    return [f'{self.char}{self.id}'] * self.size

  def __str__(self):
    return f'({self.char}{self.id} * {self.size})'

class Segmentation():
  def __init__(self, length, clues, is_left):
    self.clues = clues
    self.is_left = is_left
    self.segments = []

    if is_left:
      self.segments += [Segment('x', 0, 0, True)]
      for group_num, group_size in enumerate(clues):
        group_id = group_num
        cross_id = group_num + 1
        self.segments += [Segment('g', group_id, group_size), Segment('x', cross_id, 1)]
    else:
      self.segments += [Segment('x', len(clues), 0, True)]
      for group_num, group_size in enumerate(reversed(clues)):
        group_id = len(clues) - 1 - group_num
        cross_id = len(clues) - 1 - group_num
        self.segments += [Segment('g', group_id, group_size), Segment('x', cross_id, 1)]
    
    self.segments[-1].is_edge = True
    len_diff = length - sum([len(s) for s in self.segments])
    if len_diff != 0:
      self.segments[-1].size += len_diff
    
    if not is_left:
      self.segments.reverse()

  def internals(self):
    return f"[ {' '.join(str(segment) for segment in self.segments)} ]"

  def flat_internals(self):
    result = []
    for segment in self.segments:
      if len(segment):
        result += segment.resolve()
    return result
  
  def resolve(self):
    return [converter.marker_to_cell_str(marker) for marker in self.flat_internals()]

  def __str__(self):
    return str(self.flat_internals())

  # All the important logic below

  def align_with_solution(self, solution):
    """
    Best-effort to align with solution.
    """
    first_unsatisfied_cell_index = self.get_first_unsatisfied_cell_index(solution)
    changed = True

    while changed and first_unsatisfied_cell_index != None:
      changed = False
      unsatisfied_cell = solution[first_unsatisfied_cell_index]
      unsatisfying_segment_index = self.get_corresponding_segment_index(first_unsatisfied_cell_index)
      
      if is_cross(unsatisfied_cell):
        changed = self.shift_group(unsatisfying_segment_index)
      elif is_group(unsatisfied_cell):
        if self.is_left:
          # move group closest to it but still to its left to the right by 1. restart scan
          changed = self.shift_group(unsatisfying_segment_index - 1)
        else:
          # move group closest to it but still to its right to the left by 1. restart scan
          changed = self.shift_group(unsatisfying_segment_index + 1)

      first_unsatisfied_cell_index = self.get_first_unsatisfied_cell_index(solution)

  def can_group_shift(self, group_segment_index):
    """
    Returns segments arr index of cross segment that can collapse if group can move
    otherwise returns False.
    """
    shifting_to_left = not self.is_left
    if (
      0 <= group_segment_index < len(self.segments) and
      self.segments[group_segment_index].is_group
    ):
      start_index = group_segment_index - 1 if shifting_to_left else group_segment_index + 1
      stop_index = -1 if shifting_to_left else len(self.segments)
      search_delta = -1 if shifting_to_left else 1

      for index in range(start_index, stop_index, search_delta):
        segment = self.segments[index]
        if segment.is_cross and segment.can_shrink():
          return index

  def shift_group(self, group_segment_index):
    """
    Returns bool indicating if group successfully shifted.
    """
    shifting_to_left = not self.is_left
    cross_segment_to_shrink_index = self.can_group_shift(group_segment_index)
    if cross_segment_to_shrink_index == None:
      return False
    # shrink size of one cross segment on the side group is shifting
    self.segments[cross_segment_to_shrink_index].size -= 1
    # grow size of nearest cross segment on the other side
    cross_segment_to_grow_index = group_segment_index + 1 if shifting_to_left else group_segment_index - 1
    self.segments[cross_segment_to_grow_index].size += 1
    return True

  def get_corresponding_segment_index(self, cell_index):
    cell = self.flat_internals()[cell_index]
    for index, segment in enumerate(self.segments):
      if cell == f'{segment.char}{segment.id}':
        return index

  def get_first_unsatisfied_cell_index(self, solution):
    cells = self.flat_internals()
    scan_from_left = not self.is_left
    if scan_from_left:
      for i in range(len(solution)):
        if not is_satisfied(solution[i], cells[i]):
          return i
    else:
      for i in range(len(solution) - 1, -1, -1):
        if not is_satisfied(solution[i], cells[i]):
          return i
