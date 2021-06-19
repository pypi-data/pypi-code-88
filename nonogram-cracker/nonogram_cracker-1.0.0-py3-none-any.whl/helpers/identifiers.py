def is_empty(cell_str):
  return cell_str == 'e'

def is_group(cell_str):
  return 'g' in cell_str or cell_str == '█'

def is_cross(cell_str):
  return 'x' in cell_str

def is_unidentified(cell_str):
  return cell_str == 'g' or cell_str == 'x'

def is_satisfied(solution_cell, segmentation_cell):
  if is_group(solution_cell):
    return is_group(segmentation_cell) if is_unidentified(solution_cell) else solution_cell == segmentation_cell
  elif is_cross(solution_cell):
    return is_cross(segmentation_cell) if is_unidentified(solution_cell) else solution_cell == segmentation_cell
  return is_empty(solution_cell)
