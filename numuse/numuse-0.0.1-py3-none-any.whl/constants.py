from fractions import Fraction

GUITAR_STRING_NOTES = [4, 9, 2, 7, 11, 4]
# GUITAR_STRING_NOTES_NAMES = ["L4&#794","9&#794", "2&#794", "7&#794", "11&#794", "H4&#794"]
# GUITAR_STRING_OCTS = [2, 2, 3, 3, 3, 4]

BASE_TRIADS = [
    [0, 4, 7],  # Major
    [0, 3, 7],  # Minor
    [0, 4, 8],  # Augmented
    [0, 3, 6],  # Diminished
]

JAZZ_INTERVAL_COLLECTIONS = [
    {0, 2, 4, 7},  # Xadd9
    {0, 3, 6, 10},  # Xh (half diminshed must be a 7th chord, by def)
    {0, 4, 7, 11},  # X^7
    {0, 3, 7, 10},  # X-7
    {0, 4, 7, 10},  # X7
    {0, 5, 7, 10},  # X7sus
    {0, 3, 6, 10},  # Xh7
    {0, 3, 6, 9},  # Xo7
    {0, 4, 7, 9},  # X6
    {0, 4, 8, 11},  # X^7#5
    {0, 3, 7, 9},  # X-6
    {0, 3, 7, 11},  # X-^7
    {0, 3, 6, 10},  # X-7b5
    {0, 3, 7, 8},  # X-b6
    {0, 4, 6, 10},  # X7b5
    {0, 4, 8, 10},  # X7#5
    {0, 3, 4, 6},  # X7#9b5
]

MAJOR_INTERVALS = [0, 2, 4, 5, 7, 9, 11]

DIATONIC_MAJOR_STRUCTURE = [
    [0, [0, 4, 7, 11]],
    [2, [0, 3, 7, 10]],
    [4, [0, 3, 7, 10]],
    [5, [0, 4, 7, 11]],
    [7, [0, 4, 7, 10]],
    [9, [0, 3, 7, 10]],
    [11, [0, 3, 6, 10]],
]

DIATONIC_MINOR_STRUCTURE = [
    [0, [0, 3, 7, 10]],
    [2, [0, 3, 6, 10]],
    [3, [0, 4, 7, 11]],
    [5, [0, 3, 7, 10]],
    [7, [0, 3, 7, 10]],
    [8, [0, 4, 7, 11]],
    [10, [0, 4, 7, 10]],
]

MINOR_INTERVALS = [0, 2, 3, 5, 7, 8, 10]

JAZZ_CHORDS_WITH_EXTENSIONS = []

"""
A mapping of interval size to the ratio it approximates
in just intonation, the ratio is of them form [x, y] 
where x is the number of cycles the base wave makes
and y is the number of cycles the one with a higher pitch makes
the number of cycles is for a fixed time ratio
 """

JUST_INTERVAL_RATIOS = {
    0: [1, 1],
    1: [11, 12],
    2: [8, 9],
    3: [5, 6],
    4: [4, 5],
    5: [3, 4],
    6: [5, 7],
    7: [2, 3],
    8: [5, 8],
    9: [3, 5],
    10: [5, 9],
    11: [8, 15],
}

INTERVALS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

JUST_INTONATION_RATIOS = [
    Fraction(1, 1),
    Fraction(12, 11),
    Fraction(9, 8),
    Fraction(6, 5),
    Fraction(5, 4),
    Fraction(4, 3),
    Fraction(7, 5),
    Fraction(3, 2),
    Fraction(8, 5),
    Fraction(5, 3),
    Fraction(7, 4),
    Fraction(11, 6),
]
