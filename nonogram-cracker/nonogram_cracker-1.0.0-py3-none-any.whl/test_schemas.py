import pytest
from marshmallow import ValidationError
from .schemas import PuzzleSchema

# Happy Test
def test_one_by_one_empty():
  PuzzleSchema().load({
    "name": "name",
    "rows": [[]],
    "cols": [[]],
  })
def test_one_by_one_filled():
  PuzzleSchema().load({
    "name": "name",
    "rows": [[1]],
    "cols": [[1]],
  })
def test_three_by_three():
  PuzzleSchema().load({
    "name": "name",
    "rows": [[1, 1], [], [1, 1]],
    "cols": [[1, 1], [], [1, 1]],
  })

# Test Nulls

def test_none_0():
  with pytest.raises(ValidationError):
    PuzzleSchema().load(None)
def test_none_1():
  with pytest.raises(ValidationError):
    PuzzleSchema().load({
      "name": None,
      "rows": [[]],
      "cols": [[]],
    })
def test_none_2():
  with pytest.raises(ValidationError):
    PuzzleSchema().load({
      "name": "name",
      "rows": [None],
      "cols": [[]],
    })
def test_none_3():
  with pytest.raises(ValidationError):
    PuzzleSchema().load({
      "name": "name",
      "rows": None,
      "cols": [[]],
    })
def test_none_4():
  with pytest.raises(ValidationError):
    PuzzleSchema().load({
      "name": "name",
      "rows": [[]],
      "cols": [None],
    })
def test_none_5():
  with pytest.raises(ValidationError):
    PuzzleSchema().load({
      "name": "name",
      "rows": [[]],
      "cols": None,
    })

# Test Arrays Positive

def test_row_fits_in_width_1():
  PuzzleSchema().load({
    "name": "name",
    "rows": [[2]],
    "cols": [[], []],
  })
def test_row_fits_in_width_2():
  PuzzleSchema().load({
    "name": "name",
    "rows": [[1, 1]],
    "cols": [[], [], []],
  })
def test_col_fits_in_height_1():
  PuzzleSchema().load({
    "name": "name",
    "rows": [[], []],
    "cols": [[2]],
  })
def test_col_fits_in_height_2():
  PuzzleSchema().load({
    "name": "name",
    "rows": [[], [], []],
    "cols": [[1, 1]],
  })

# Test Arrays Negative

def test_row_too_big_for_width_1():
  with pytest.raises(ValidationError):
    PuzzleSchema().load({
      "name": "name",
      "rows": [[2]],
      "cols": [[]],
    })
def test_row_too_big_for_width_2():
  with pytest.raises(ValidationError):
    PuzzleSchema().load({
      "name": "name",
      "rows": [[1, 1]],
      "cols": [[], []],
    })
def test_col_too_big_for_height_1():
  with pytest.raises(ValidationError):
    PuzzleSchema().load({
      "name": "name",
      "rows": [[]],
      "cols": [[2]],
    })
def test_col_too_big_for_height_2():
  with pytest.raises(ValidationError):
    PuzzleSchema().load({
      "name": "name",
      "rows": [[], []],
      "cols": [[1, 1]],
    })
