"""
Test file that uses pytest to ensure that the MPyC implementation of the matrix inverse
correctly computes the matrix inverse.
"""

from typing import Any, List, Tuple, Type, Union

import pytest
from mpyc.runtime import mpc
from mpyc.sectypes import SecureFixedPoint
from numpy import abs as abs_
from numpy import array, divide, linalg, random, zeros_like

from tno.mpc.mpyc.matrix_inverse.matrix_inverse import (
    SecureFixedPointMatrix,
    matrix_inverse,
)

Matrix = List[List[Union[float, int]]]
matrices: List[Matrix] = [
    [[2, 0], [0, 3]],
    [[1 / 2, 0], [0, 1 / 3]],
    [[-2, 0], [0, 3]],
    [[-1 / 2, 0], [0, 1 / 3]],
    (random.randint(low=-1000, high=1000, size=(5, 5)) / 10).tolist(),
]


async def async_test_matrix_inverse(testcase: Tuple[Matrix, Any]) -> None:
    """
    Test that checks whether the secure application of the matrix inverse returns the same result
    as the regular matrix inverse up to a certain margin.

    :param testcase: tuple of a matrix and its correct inverse
    """
    matrix, correct_matrix_inverse = testcase
    bit_length = 32
    frac_length = 16

    await mpc.start()

    secfxp: Type[SecureFixedPoint] = mpc.SecFxp(l=bit_length, f=frac_length)
    secure_matrix: SecureFixedPointMatrix = [[secfxp(x) for x in row] for row in matrix]
    secure_matrix = [mpc.input(row, 0) for row in secure_matrix]

    # noinspection PyTypeChecker
    secure_inverse: SecureFixedPointMatrix = matrix_inverse(secure_matrix)
    inverse: List[List[float]] = [await mpc.output(row) for row in secure_inverse]

    secure_checker = mpc.matrix_prod(secure_matrix, secure_inverse)
    checker: List[List[float]] = [await mpc.output(row) for row in secure_checker]

    diff = array(correct_matrix_inverse) - array(inverse)
    rel_diff = divide(
        diff,
        array(correct_matrix_inverse),
        out=zeros_like(diff),
        where=array(correct_matrix_inverse) != 0,
    )

    await mpc.shutdown()
    max_abs_diff = abs_(diff).max()
    max_rel_diff = abs_(rel_diff).max()

    print(f"X = \n{array(matrix)}\n")
    print(f"Xinv = \n{array(correct_matrix_inverse)}\n")
    print(f"Xinv_mpc = \n{array(inverse)}\n")
    print(f"X * Xinv_mpc = \n{array(checker)}\n")
    print(f"max absolute diff = {max_abs_diff}")
    print(f"max relative diff (nonzero entries) = {max_rel_diff}")
    assert max_abs_diff < 0.05 and max_rel_diff < 0.5


@pytest.mark.parametrize(
    "test_case", [(matrix, linalg.inv(matrix).tolist()) for matrix in matrices]
)
def test_matrix_inverse(test_case: Tuple[Matrix, Any]) -> None:
    """
    Test that runs the async test code.

    :param test_case: tuple containing a matrix and its inverse
    """
    mpc.run(async_test_matrix_inverse(test_case))
