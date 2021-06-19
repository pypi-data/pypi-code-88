from .helpers.is_already_solved import is_already_solved
from .helpers.converter import puzzle_to_internals, internals_to_puzzle
from .helpers.identifiers import is_group, is_cross, is_empty, is_unidentified

def solve_seq(cells_str, clues):
  if is_already_solved(cells_str):
    return cells_str

  solution, left_seg, right_seg = puzzle_to_internals(cells_str, clues)
  changed = True

  while changed:
    changed = False
    left_seg.align_with_solution(solution)
    right_seg.align_with_solution(solution)

    sus_solution_1 = left_seg.flat_internals()
    sus_solution_2 = right_seg.flat_internals()

    for i in range(len(solution)):
      sol_val = solution[i]
      if is_unidentified(sol_val) or is_empty(sol_val):
        sus_val_1 = sus_solution_1[i]
        sus_val_2 = sus_solution_2[i]

        has_prime_suspect = sus_val_1 == sus_val_2
        suspect_matches_known_solution = (
          ((is_group(sol_val) or is_empty(sol_val)) and is_group(sus_val_1)) or
          ((is_cross(sol_val) or is_empty(sol_val)) and is_cross(sus_val_1))
        )
        if has_prime_suspect and suspect_matches_known_solution:
          solution[i] = sus_val_1
          changed = True

  return internals_to_puzzle(solution)
