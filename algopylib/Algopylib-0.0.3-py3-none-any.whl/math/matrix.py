from __future__ import annotations

from decimal import Decimal
def det2(matrix: list[list[float]]) -> float:
    ''' Determinant of a 2x2 matrix. '''
    return matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
def det3(matrix: list[list[float]]) -> float:
    ''' Determinant of a 3x3 matrix. '''
    return ( matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[2][1] * matrix[1][2]) -
            matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0]) +
            matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0]) )

def inverse_of_matrix_2(matrix: list[list[float]]) -> list[list[float]]:
    """
    A matrix multiplied with its inverse gives the identity matrix.
    This function finds the inverse of a 2x2 matrix.
    If the determinant of a matrix is 0, its inverse does not exist.
    Sources for fixing inaccurate float arithmetic:
    https://stackoverflow.com/questions/6563058/how-do-i-use-accurate-float-arithmetic-in-python
    https://docs.python.org/3/library/decimal.html
    >>> inverse_of_matrix([[2, 5], [2, 0]])
    [[0.0, 0.5], [0.2, -0.2]]
    >>> inverse_of_matrix([[2.5, 5], [1, 2]])
    Traceback (most recent call last):
    ...
    ValueError: This matrix has no inverse.
   
    >>> inverse_of_matrix([[10, 5], [3, 2.5]])
    [[0.25, -0.5], [-0.3, 1.0]]
    """

    D = Decimal  # An abbreviation to be conciseness
    # Calculate the determinant of the matrix
    determinant = D(det2(matrix))
    if determinant == 0:
        raise ValueError("This matrix has no inverse.")
    # Creates a copy of the matrix with swapped positions of the elements
    swapped_matrix = [[0.0, 0.0], [0.0, 0.0]]
    swapped_matrix[0][0], swapped_matrix[1][1] = matrix[1][1], matrix[0][0]
    swapped_matrix[1][0], swapped_matrix[0][1] = -matrix[1][0], -matrix[0][1]
    # Calculate the inverse of the matrix
    return [[float(D(n) / determinant) or 0.0 for n in row] for row in swapped_matrix]

def inverse_of_matrix_3(matrix: list[list[float]]) -> list[list[float]]:
    
    invDet = 1 / det3;
    D = Decimal  # An abbreviation to be conciseness
    # Calculate the determinant of the matrix
    determinant = D(det3(matrix))
    if determinant == 0:
        raise ValueError("This matrix has no inverse.")
    temp = [[0.0, 0.0,0.0],[0.0, 0.0,0.0], [0.0, 0.0,0.0]]

    temp[0][0] = (matrix[1][1] * matrix[2][2] - matrix[2][1] * matrix[1][2]) * invDet
    temp[0][1] = (matrix[0][2] * matrix[2][1] - matrix[0][1] * matrix[2][2]) * invDet
    temp[0][2] = (matrix[0][1] * matrix[1][2] - matrix[0][2] * matrix[1][1]) * invDet
    temp[1][0] = (matrix[1][2] * matrix[2][0] - matrix[1][0] * matrix[2][2]) * invDet
    temp[1][1] = (matrix[0][0] * matrix[2][2] - matrix[0][2] * matrix[2][0]) * invDet
    temp[1][2] = (matrix[1][0] * matrix[0][2] - matrix[0][0] * matrix[1][2]) * invDet
    temp[2][0] = (matrix[1][0] * matrix[2][1] - matrix[2][0] * matrix[1][1]) * invDet
    temp[2][1] = (matrix[2][0] * matrix[0][1] - matrix[0][0] * matrix[2][1]) * invDet
    temp[2][2] = (matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]) * invDet

    return temp
