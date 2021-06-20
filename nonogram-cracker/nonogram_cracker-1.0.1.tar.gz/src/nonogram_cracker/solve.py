from marshmallow import ValidationError
from .schemas import PuzzleSchema
from .solve_seq import solve_seq
from .helpers.is_solved import is_solved, can_clues_fit_with_solution
from .solution_response import SolutionResponse


def solve(puzzle):
    try:
        solution, found_solution = do_solve(puzzle)
        return SolutionResponse(
            solution=solution,
            is_solved=found_solution,
            is_unsolvable=False,
            has_error=False,
            error=None
        )._asdict()
    except ValidationError as err:
        return SolutionResponse(
            solution=None,
            is_solved=False,
            is_unsolvable=True,
            has_error=True,
            error=err.messages
        )._asdict()
    except BaseException as err:
        print(str(err))
        return SolutionResponse(
            solution=None,
            is_solved=False,
            is_unsolvable=False,
            has_error=True,
            error="An unknown exception occurred"
        )._asdict()


def do_solve(puzzle):
    PuzzleSchema().load(puzzle)

    width = len(puzzle['cols'])
    height = len(puzzle['rows'])

    solution = [' ' * width] * height
    changed = True

    # while anything is being changed, continue
    # if a contradiction is found between working solution and clues then throw error
    while changed:
        changed = False
        # iterate through rows running solver fn
        for i in range(height):
            row = solution[i]
            row_clues = puzzle['rows'][i]
            if not can_clues_fit_with_solution(row, row_clues):
                raise ValidationError('Cannot solve - puzzle contains a contradiction')
            next_row = solve_seq(row, row_clues)
            if row != next_row:
                changed = True
                solution[i] = next_row
        # iterate through cols running solver fn
        for i in range(width):
            col = ''.join([solution[j][i] for j in range(height)])
            col_clues = puzzle['cols'][i]
            if not can_clues_fit_with_solution(col, col_clues):
                raise ValidationError('Cannot solve - puzzle contains a contradiction')
            next_col = solve_seq(col, col_clues)
            if col != next_col:
                changed = True
                for j in range(height):
                    solution[j] = solution[j][:i] + next_col[j] + solution[j][i + 1:]

    # if things stopped changing check if solution was found
    found_solution = True
    for i in range(height):
        row = solution[i]
        found_solution = found_solution and is_solved(row)
    for i in range(width):
        col = ''.join([solution[j][i] for j in range(height)])
        found_solution = found_solution and is_solved(col)

    return solution, found_solution
