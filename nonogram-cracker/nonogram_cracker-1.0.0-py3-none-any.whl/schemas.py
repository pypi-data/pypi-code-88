from marshmallow import fields, Schema, validate, validates_schema, ValidationError

def is_valid_row_or_col(row_or_col):
  return type(row_or_col) is list and [type(cell) is int for cell in row_or_col]

class PuzzleSchema(Schema):
  name = fields.String(required=True)

  rows = fields.List(
    fields.List(
      fields.Integer(),
      required=True
    ),
    required=True,
    validate=validate.Length(min=1)
  )

  cols = fields.List(
    fields.List(
      fields.Integer(),
      required=True
    ),
    required=True,
    validate=validate.Length(min=1)
  )

  @validates_schema
  def validate_array_lengths(self, data, **kwargs):
    if (
      'rows' in data and type(data['rows']) is list and
      'cols' in data and type(data['cols']) is list
    ):
      rows = data['rows']
      cols = data['cols']
      height = len(rows)
      width = len(cols)
  
      # Only perform these checks if valid datatypes, all other cases are handled by schema
      for i, row in enumerate(filter(is_valid_row_or_col, rows)):
        min_width_for_clues = len(row) - 1 + sum(row)
        if min_width_for_clues > width:
          raise ValidationError(f"Row #{i + 1} with clues {row} cannot fit in {width} columns")
      for i, col in enumerate(filter(is_valid_row_or_col, cols)):
        min_height_for_clues = len(col) - 1 + sum(col)
        if min_height_for_clues > height:
          raise ValidationError(f"Col #{i + 1} with clues {col} cannot fit in {height} rows")
