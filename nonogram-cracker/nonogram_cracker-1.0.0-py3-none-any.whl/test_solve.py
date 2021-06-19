from os import listdir
from os.path import isfile, join
import json
from .solve import solve

root_dir = '../../puzzles'
infiles = [f for f in listdir(root_dir) if isfile(join(root_dir, f)) and 'solution' not in f]

def test_solve_puzzle():
  for file in infiles:
    with open(f'{root_dir}/{file}') as puzzle_f:
      puzzle = json.load(puzzle_f)
      solution_file = file.replace('.json', '.solution.json')
      with open(f'{root_dir}/{solution_file}', encoding="utf-8") as solution_f:
        solution = json.load(solution_f)
        assert solve(puzzle) == solution
