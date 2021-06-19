from .is_already_solved import is_already_solved, is_correct, can_clues_fit_with_solution

def test_is_already_solved_false_1():
  assert not is_already_solved('     ')
def test_is_already_solved_false_2():
  assert not is_already_solved('xxxx ')
def test_is_already_solved_false_3():
  assert not is_already_solved('xgxg ')
def test_is_already_solved_false_4():
  assert not is_already_solved(' gggg')

def test_is_already_solved_true1():
  assert is_already_solved('ggggg')
def test_is_already_solved_true2():
  assert is_already_solved('xxxxx')
def test_is_already_solved_true3():
  assert is_already_solved('xgxgx')

def test_is_correct_solved():
  assert is_correct('x█x█x', [1, 1])
def test_is_not_correct_not_yet_solved():
  assert not is_correct(' █x█x', [1, 1])
def test_is_not_correct_doesnt_match_clues():
  assert not is_correct(' █ ██', [1, 1])

def test_can_clues_fit_with_solution_1():
  assert can_clues_fit_with_solution('x█x█x', [1, 1])
def test_can_clues_fit_with_solution_2():
  assert not can_clues_fit_with_solution('x█x█x', [1, 2])
def test_can_clues_fit_with_solution_3():
  assert can_clues_fit_with_solution('     ', [1, 2])
def test_can_clues_fit_with_solution_4():
  assert not can_clues_fit_with_solution('     ', [6])
def test_can_clues_fit_with_solution_5():
  assert not can_clues_fit_with_solution('     ', [3, 2])
def test_can_clues_fit_with_solution_6():
  assert can_clues_fit_with_solution('██ ██', [5])
