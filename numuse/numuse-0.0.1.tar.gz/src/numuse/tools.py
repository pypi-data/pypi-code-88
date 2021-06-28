def I(x: int, y: int) -> int:
    """Return the interval between the two notes x, y

    Parameters
    ----------
    x : int
        The first note

    y : int
        The second note

    Returns
    -------
    The interval between x and y

    """
    return y - x


def ranged_modulus_operator(x: int, m: int = 12) -> int:
    """Return what x is congruent to in the range 0 ... m-1

    Parameters
    ----------
    x : int
        The number to be analyzed

    m : int
        The modulus

    Returns
    -------
    The unique number from 0 to m-1 (inclusive) that x is congruent to
    """
    while x < 0:
        x += m

    return x % m
