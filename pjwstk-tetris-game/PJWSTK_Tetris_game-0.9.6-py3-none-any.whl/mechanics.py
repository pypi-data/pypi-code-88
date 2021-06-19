import model


def clear_rows(grid, locked):
    # need to see if row is clear the shift every other row above down one
    inc = 0
    for i in range(len(grid) -1, -1, -1):
        row = grid[i]
        # check row by row if the it has other color than black = has a piece
        if model.black not in row:
            inc += 1
            # add positions to remove from locked
            ind = i
            for j in range(len(row)):
                try:
                    del locked[(j, i)]
                except:
                    continue
    if inc > 0:
        for key in sorted(list(locked), key=lambda x: x[1])[::-1]:
            x, y = key
            if y < ind:  # checking only rows above the "full line"
                new_key = (x, y + inc)
                locked[new_key] = locked.pop(key)
    return inc

def valid_space(shape, grid):
    accepted_positions = [[(j, i) for j in range(10) if grid[i][j] == model.black] for i in range(20)]
    accepted_positions = [j for sub in accepted_positions for j in sub]
    formatted = convert_shape_format(shape)

    for position in formatted:
        if position not in accepted_positions:
            if position[1] > -1:
                return False
    return True

def convert_shape_format(shape):
    positions = []
    format_shape = shape.shape[shape.rotation % len(shape.shape)]

    for i, line in enumerate(format_shape):
        row = list(line)
        for j, column in enumerate(row):
            if column == 'X':
                positions.append((shape.x + j, shape.y + i))

    for i, pos in enumerate(positions):
        positions[i] = (pos[0] - 2, pos[1] - 4)

    return positions

def check_lost(positions):
    for position in positions:
        x, y = position
        if y < 1:
            return True
    return False