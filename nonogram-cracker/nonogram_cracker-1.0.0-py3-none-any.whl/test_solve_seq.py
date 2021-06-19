from .solve_seq import solve_seq

# starting with empty string
def test_solve_seq_empty():
  assert solve_seq('          ', []) == 'xxxxxxxxxx'
def test_solve_seq_full():
  assert solve_seq('          ', [10]) == '██████████'
def test_solve_seq_full_split():
  assert solve_seq('          ', [4, 5]) == '████x█████'
def test_solve_seq_full_split2():
  assert solve_seq('          ', [3, 2, 3]) == '███x██x███'
def test_solve_seq_almost_full():
  assert solve_seq('          ', [4, 4]) == ' ███  ███ '

# starting with some filled
def test_solve_seq_full_from_partial():
  assert solve_seq('   █    ', [3, 2]) == 'x ██  █ '
def test_solve_seq_full_split_from_partial():
  assert solve_seq(' █      ', [1, 1, 1, 1]) == 'x█x█x█x█'
def test_solve_seq_full_split2_from_partial():
  assert solve_seq('  █     ', [1, 1, 1, 1]) == '█x█x    '
def test_solve_seq_almost_full_from_partial():
  assert solve_seq('    █     ', [2, 2, 2]) == ' █  █     '

# Bugs
def test_solve_seq_bug1():
  assert solve_seq('  xx ', [2]) == '██xxx'
def test_solve_seq_bug2():
  assert solve_seq('     ', [2]) == '     '
