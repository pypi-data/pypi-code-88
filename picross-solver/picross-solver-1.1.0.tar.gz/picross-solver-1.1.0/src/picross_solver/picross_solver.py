import numpy as np


def _push_solve(rule, arr):
    def invalid(block):
        nonlocal valid_states_found
        solid[block] = -1
        if pos[block] + rule[block] > len(arr):
            return False
        for i in range(pos[block], pos[block] + rule[block]):
            if arr[i] == 0:
                if solid[block] != -1:
                    return drawing(block)
                pos[block] = i + 1
                return invalid(block)
            if solid[block] == -1 and arr[i] == 1:
                solid[block] = i - pos[block]

        if solid[block] == -1 and pos[block] + rule[block] < len(arr) and arr[pos[block] + rule[block]] == 1:
            solid[block] = rule[block]
        while pos[block] + rule[block] < len(arr) and arr[pos[block] + rule[block]] == 1:
            if solid[block] == 0:
                return drawing(block)
            pos[block] += 1
            solid[block] -= 1

        if block != len(rule) - 1:
            if pos[block + 1] < pos[block] + rule[block] + 1:
                pos[block + 1] = pos[block] + rule[block] + 1
            block += 1
            return invalid(block)
        trailing_solid_pos = -1
        for i in range(pos[block] + rule[block] + 1, len(arr)):
            if arr[i] == 1:
                trailing_solid_pos = i
                break
        if trailing_solid_pos != -1:
            if solid[block] > 0:
                pos[block] += 1
                solid[block] -= 1
                return invalid(block)
            elif solid[block] == 0:
                return drawing(block)
            else:
                pos[block] = trailing_solid_pos - rule[block] + 1
                return invalid(block)
        valid_states_found += 1
        for b in range(0, len(rule)):
            for i in range(pos[b], pos[b] + rule[b]):
                valid_state_accumulation[i] += 1
        return True

    def sliding():
        for i in range(len(rule) - 1, -1, -1):
            lim = len(arr)
            if i < len(rule) - 1:
                lim = pos[i + 1] - 1
            while pos[i] + rule[i] < lim \
                    and (solid[i] == -1 or solid[i] > 0) \
                    and (arr[pos[i] + rule[i]] != 0 or solid[i] == -1):
                if arr[pos[i] + rule[i]] == 0:
                    index = pos[i] + rule[i] + 1
                    while index + rule[i] <= lim:
                        enough_room = True
                        for j in range(index, index + rule[i]):
                            if arr[j] == 0:
                                index = j + 1
                                enough_room = False
                                break
                        if enough_room:
                            for b in range(pos[i], pos[i] + rule[i]):
                                valid_state_accumulation[b] = 999999
                            pos[i] = index
                            for b in range(pos[i], pos[i] + rule[i]):
                                valid_state_accumulation[b] = 999999
                            break
                    if index + rule[i] > lim:
                        break
                else:
                    if solid[i] != -1:
                        solid[i] -= 1
                    valid_state_accumulation[pos[i]] = 999999
                    valid_state_accumulation[pos[i] + rule[i]] = 999999
                    pos[i] += 1

    def drawing(block):
        while True:
            block -= 1
            if block < 0:
                return False
            if solid[block] != 0:
                break
        if solid[block] > 0:
            pos[block] += 1
            solid[block] -= 1
            return invalid(block)
        pos[block] = pos[block + 1] + solid[block + 1] - rule[block] + 1
        return invalid(block)

    changed_indices = []
    if len(rule) == 0 or rule[0] == 0:
        for cell in range(0, len(arr)):
            if arr[cell] == -1:
                arr[cell] = 0
                changed_indices.append(cell)
        return changed_indices

    pos = np.full(len(rule), 0)
    solid = np.full(len(rule), -1)
    valid_state_accumulation = np.full(len(arr), 0)
    valid_states_found = 0

    if not invalid(0):
        return [-1]
    sliding()
    for block_to_free in range(len(rule) - 1, 0, -1):
        while solid[block_to_free] != -1:
            old_pos = np.copy(pos)
            old_solid = np.copy(solid)
            if drawing(block_to_free):
                sliding()
            else:
                pos = np.copy(old_pos)
                solid = np.copy(old_solid)
                break
    for cell in range(0, len(valid_state_accumulation)):
        if valid_state_accumulation[cell] == valid_states_found and arr[cell] == -1:
            arr[cell] = 1
            changed_indices.append(cell)
        elif valid_state_accumulation[cell] == 0 and arr[cell] == -1:
            arr[cell] = 0
            changed_indices.append(cell)
    return changed_indices


def solve(row_constraints, col_constraints, puzzle):
    """
    Overwrites the given puzzle variable with a solution to the nonogram.

    Parameters
    ----------
    row_constraints : list[list[int]], np.ndarray
        Defines all of the constraints in each row of the puzzle.
    col_constraints : list[list[int]], np.ndarray
        Defines all of the constraints in each column of the puzzle.
    puzzle : np.ndarray
        Overwritten with the nonogram solution. Should only contain values -1
         (unknown), 0 (empty), or 1 (filled).

    Returns
    -------
    is_solved : boolean
        Returns a boolean representing if the function was able to solve the
         nonogram or not. True means it was able to be solved with no issues;
         False means the puzzle was unable to be solved.

    Examples
    --------
    >>> puz = np.array([[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]])
    >>> rows = [[1, 1], [0], [3]]
    >>> cols = [[1, 1], [1], [1, 1]]
    >>> solve(rows, cols, puz)
    Variable 'puz' will now be [[1, 0, 1], [0, 0, 0], [1, 1, 1]]

    >>> puz = np.full((2, 3), -1)
    >>> rows = [[3], [1]]
    >>> cols = [[1], [2], [1]]
    >>> solve(rows, cols, puz)
    Variable 'puz' will now be [[1, 1, 1], [0, 1, 0]]

    >>> puz = np.full((2, 2), 0)
    >>> rows = [[2], [2]]
    >>> cols = [[2], [2]]
    >>> solve(rows, cols, puz)
    Puzzle can't be solved; returns False
    """

    puzzle_height = len(puzzle)
    puzzle_width = len(puzzle[0])

    # iterate through each updated row and column until no more progress has been made with the push solver
    # if no progress has been made, the puzzle is either solved or a guess is required to continue
    first_pass = True
    update_row_indices = np.full(puzzle_height, True)
    update_col_indices = np.full(puzzle_width, True)
    while True:
        for i in range(0, 2):
            update_indices = update_row_indices if i else update_col_indices
            if not first_pass:
                for j in range(0, len(update_indices)):
                    update_indices[j] = False
            first_pass = False
            for j in range(0, puzzle_width if i else puzzle_height):
                arr = puzzle[:, j] if i else puzzle[j, :]
                if (update_col_indices if i else update_row_indices)[j]:
                    changed_indices = _push_solve((col_constraints if i else row_constraints)[j], arr)
                    if changed_indices == [-1]:
                        return False
                    for k in changed_indices:
                        update_indices[k] = True
            no_progress = all(not x for x in update_indices)
            if no_progress:
                guess_point = [-1, -1]
                for j in range(0, puzzle_height):
                    for k in range(0, puzzle_width):
                        if puzzle[j][k] == -1:
                            guess_point = [j, k]
                            break
                    if guess_point[0] != -1:
                        break
                if guess_point[0] == -1:
                    return True
                puzzle_state = puzzle.copy()
                puzzle[guess_point[0]][guess_point[1]] = 1
                if solve(row_constraints, col_constraints, puzzle):
                    return True
                for j in range(0, puzzle_height):
                    for k in range(0, puzzle_width):
                        puzzle[j][k] = puzzle_state[j][k]
                puzzle[guess_point[0]][guess_point[1]] = 0
                update_row_indices[guess_point[0]] = True
                update_col_indices[guess_point[1]] = True
