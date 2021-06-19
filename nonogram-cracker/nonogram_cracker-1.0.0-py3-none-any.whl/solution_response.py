from collections import namedtuple

SolutionResponse = namedtuple(
  'SolutionResponse',
  ['solution','is_solved', 'is_unsolvable', 'has_error', 'error']
)
