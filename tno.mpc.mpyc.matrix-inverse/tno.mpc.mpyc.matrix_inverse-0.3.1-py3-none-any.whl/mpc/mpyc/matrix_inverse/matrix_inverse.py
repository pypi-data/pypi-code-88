"""
The code below is based on the demo ridgeregression.py from the MPyC library on Feb 26th, 2020,
as implemented by Frank Blom.
https://github.com/lschoe/mpyc/blob/2de1dd76db632bdc2a48acfbbaab841fa73cf8bd/demos/ridgeregression.py.
The underlying theory is published in the paper 'Efficient Secure Ridge Regression from
Randomized Gaussian Elimination' by Frank Blom, Niek J. Bouman, Berry
Schoenmakers, and Niels de Vreede, presented at TPMPC 2019 by Frank Blom.
See https://eprint.iacr.org/2019/773 (or https://ia.cr/2019/773).
"""
from typing import List, Tuple, Type, TypeVar, Union

from mpyc.finfields import PrimeFieldElement
from mpyc.runtime import mpc
from mpyc.sectypes import SecureFixedPoint, SecureInteger, SecureNumber
from numpy import array, concatenate, diagflat, reshape, tril_indices, triu_indices

from .asyncoro import mpc_coro_ignore, returnType

SecureFixedPointMatrix = List[List[SecureFixedPoint]]
FixedPointMatrix = List[List[float]]
SecureNumberType = TypeVar("SecureNumberType", bound=SecureNumber)


def bareiss_gaussian_elimination(
    prime_field: Type[PrimeFieldElement], matrix: List[List[SecureNumberType]]
) -> Tuple[List[List[SecureNumberType]], SecureNumberType]:
    """
    Bareiss-like integer-preserving Gaussian elimination adapted for Zp.
    Using exactly one modular inverse in Zp per row of the provided matrix.
    Apart from variable names, this is an unmodified copy of the code in the demo.

    :param prime_field: Zp
    :param matrix: input matrix containing secure values
    :return: inverse matrix of the input matrix
    """
    field_modulus = prime_field.modulus
    numpy_matrix = array(matrix)
    height, width = numpy_matrix.shape  # d by d+e matrix A

    # convert A elementwise from Zp to int
    for i in range(height):
        for j in range(width):
            numpy_matrix[i, j] = numpy_matrix[i, j].value

    # division-free Gaussian elimination
    for k in range(height):
        for i in range(k + 1, height):
            for j in range(k + 1, width):
                numpy_matrix[i, j] = (
                    numpy_matrix[k, k] * numpy_matrix[i, j]
                    - numpy_matrix[k, j] * numpy_matrix[i, k]
                ) % field_modulus

    # back substitution
    for i in range(height - 1, -1, -1):
        inv = (1 / prime_field(numpy_matrix[i, i])).value
        if i < height - 2:
            # keep reciprocal for determinant
            numpy_matrix[i, i] = inv
        for j in range(height, width):
            element = numpy_matrix[i, j]
            for k in range(i + 1, height):
                element -= numpy_matrix[i, k] * numpy_matrix[k, j]
            element %= field_modulus
            numpy_matrix[i, j] = (element * inv) % field_modulus

    # postponed division for determinant
    inv = 1
    det = numpy_matrix[height - 1, height - 1]
    for i in range(height - 2):
        inv = (inv * numpy_matrix[i, i]) % field_modulus
        det = (det * inv) % field_modulus

    numpy_inverse = numpy_matrix[:, height:]
    return numpy_inverse.tolist(), det


def random_matrix_determinant(
    secure_object_type: Type[SecureNumberType], dimension: int
) -> Tuple[List[List[SecureNumberType]], SecureNumberType]:
    """
    Generate a random d x d matrix from the set of LU decomposable matrices over a given field.
    Apart from variable names, this is an unmodified copy of the code in the demo.

    :param secure_object_type: Secure type
    :param dimension: The dimension d
    :return: A random invertible matrix and the determinant of its inverse
    """
    d_2: int = dimension * (dimension - 1) // 2
    # Generate a random lower triangular matrix (L) with 1s on the diagonal uniformly random from
    # the set of such matrices
    rand_lower_tri_matrix = diagflat([secure_object_type(1)] * dimension)

    rand_lower_tri_matrix[
        tril_indices(dimension, -1)
    ] = mpc._randoms(  # pylint: disable=protected-access # we need the protected method
        secure_object_type, d_2
    )
    rand_lower_tri_matrix[triu_indices(dimension, 1)] = [secure_object_type(0)] * d_2

    diag = (
        mpc._randoms(  # pylint: disable=protected-access # we need the protected method
            secure_object_type, dimension
        )
    )

    # Generate a random upper triangular matrix (U) uniformly random from the set of such matrices
    rand_upper_tri_matrix = diagflat(diag)
    rand_upper_tri_matrix[tril_indices(dimension, -1)] = [secure_object_type(0)] * d_2

    rand_upper_tri_matrix[
        triu_indices(dimension, 1)
    ] = mpc._randoms(  # pylint: disable=protected-access # we need the protected method
        secure_object_type, d_2
    )

    # noinspection PyTypeChecker
    # The missing annotations give type errors here
    rand_lower_tri_matrix_list: List[
        List[SecureNumberType]
    ] = rand_lower_tri_matrix.tolist()
    # noinspection PyTypeChecker
    # The missing annotations give type errors here
    rand_upper_tri_matrix_list: List[
        List[SecureNumberType]
    ] = rand_upper_tri_matrix.tolist()
    # Compute the result R = L * U
    random_invertible_matrix = mpc.matrix_prod(
        rand_lower_tri_matrix_list, rand_upper_tri_matrix_list
    )

    # The determinant of R is nonzero with overwhelming probability
    inverse_determinant = mpc.prod(diag)
    return random_invertible_matrix, inverse_determinant


@mpc_coro_ignore
async def _matrix_inverse(
    input_matrix: List[List[SecureNumberType]],
) -> List[SecureNumberType]:
    """
    Securely compute the matrix inverse of a given matrix.
    This is based on the linear_solve function from the demo.

    :param input_matrix: Matrix for which we want to know the inverse
    :return: Adjugate and determinant of the input matrix, which represents the inverse
    :raises ValueError: when the provided matrix is not square
    """

    # Assume that each element is from the same field
    secure_object_type: Type[SecureNumberType] = type(input_matrix[0][0])

    # Dimension of the matrix
    dimension = len(input_matrix)
    if not all(len(row) == dimension for row in input_matrix):
        raise ValueError("The matrix is not square.")
    await returnType(secure_object_type, dimension * dimension + 1)

    # securely sample a random matrix R and the determinant of its inverse
    random_invertible_matrix, inverse_determinant = random_matrix_determinant(
        secure_object_type, dimension
    )

    # Mask the input matrix using R
    masked_input_matrix: List[List[SecureNumberType]] = mpc.matrix_prod(
        random_invertible_matrix, input_matrix
    )

    flattened_secure_masked_input_matrix: List[SecureNumberType] = [
        a for row in masked_input_matrix for a in row
    ]
    # Open the masked input matrix
    flattened_masked_input_matrix: List[Union[int, float]] = await mpc.output(
        flattened_secure_masked_input_matrix, raw=True
    )
    # Reshape to d x d matrix
    reshaped_masked_input_matrix = reshape(
        flattened_masked_input_matrix, (dimension, dimension)
    )
    random_invertible_matrix = await mpc.gather(random_invertible_matrix)

    sec_field: Type[PrimeFieldElement] = secure_object_type.field  # type: ignore # This copied code
    # structure makes it hard for the inspection tool to understand that the class contained in
    # sec_field does in fact have a field variable.
    # Use Gaussian elimination to obtain the inverse and determinant of the masked matrix
    # noinspection PyTypeChecker
    inverse, masked_matrix_determinant = bareiss_gaussian_elimination(
        sec_field,
        concatenate(
            (reshaped_masked_input_matrix, random_invertible_matrix), axis=1
        ).tolist(),
    )
    input_matrix_determinant = masked_matrix_determinant / inverse_determinant
    input_matrix_adjugate = [
        secure_object_type(a) * input_matrix_determinant for row in inverse for a in row
    ]
    return input_matrix_adjugate + [input_matrix_determinant]


def determine_order_secfld(bit_length: int, dimension: int) -> int:
    """
    Function to determine the minimal order of a field, based on the bit length and dimension.
    Based on main() and paper

    :param bit_length: bit length of each element in the field
    :param dimension: dimension of the original matrix
    :return: minimal order
    """

    beta = 2 ** bit_length
    gamma = dimension * beta ** 2
    bound: int = round(dimension ** (dimension / 2)) * gamma ** dimension
    return 2 * bound + 1


@mpc_coro_ignore
async def scale_and_convert_to_secint(
    to_convert: Union[List[SecureNumber], SecureNumber]
) -> Union[List[SecureInteger], SecureInteger]:
    """
    Function that scales and converts secure fixed points to secure integers with the same modulus.
    Effectively removes the point in the fixed point notation.

    :param to_convert: secure fixed point or list of secure fixed points
    :return: secure integer or list of secure integers (depending on the input)
    """
    is_list = isinstance(to_convert, list)
    to_convert_list: List[SecureNumber]
    if is_list:
        to_convert_list = to_convert[:]  # type: ignore # The statement ensures to_convert is a list
    else:
        to_convert_list = [to_convert]  # type: ignore # The statement ensures to_convert is not a
        # list and the return type is a list
    stype: Type[SecureNumber] = type(to_convert_list[0])
    field_modulus = stype.field.modulus  # type: ignore # The structure of the mpyc code
    # makes it hard for the inspection tool to understand that the class contained in
    # stype does in fact have a field class which has a modulus variable.
    secint = mpc.SecInt(l=stype.bit_length, p=field_modulus)
    if is_list:
        await returnType(secint, len(to_convert_list))
    else:
        await returnType(secint)
    to_convert_list = await mpc.gather(to_convert_list)
    result = [secint.field(int(xx.value)) for xx in to_convert_list]  # type: ignore # The structure
    # of the mpyc code makes it hard for the inspection tool to understand that the class
    # elements in to_convert_list have a value variable.
    if not is_list:
        result = result[0]
    return result


def scale_and_convert_matrix_to_sec_fld(
    input_matrix: SecureFixedPointMatrix,
) -> SecureFixedPointMatrix:
    """
    Function that scales and converts each element of a matrix with secure fixed point elements
    to a secure integer.

    :param input_matrix: matrix containing secure fixed point numbers
    :return: matrix containing secure integers
    """

    # Convert secnum to scaled secnum
    a_matrix_secint = [scale_and_convert_to_secint(entry) for entry in input_matrix]

    # Convert secint to secfld
    sec_type_bit_length: int = (
        0 if input_matrix[0][0].bit_length is None else input_matrix[0][0].bit_length
    )
    min_order = determine_order_secfld(sec_type_bit_length, len(input_matrix))
    secfld = mpc.SecFld(min_order=min_order, signed=True)
    return [mpc.convert(_, secfld) for _ in a_matrix_secint]


def convert_matrix_to_large_sec_fxp(
    input_matrix: List[SecureNumber],
) -> List[SecureFixedPoint]:
    """
    Convert a matrix with secure elements to a matrix with secure fixed points with twice as large
    bit lengths.

    :param input_matrix: input matrix
    :return: the input matrix with each element converted to a fixed point number with large bit
        length
    """
    # Convert secnum to secfxp with twice as many bits
    total_bit_length: int = input_matrix[0].bit_length  # type: ignore#  The structure of the mpyc
    # code makes it hard for the inspection tool to understand that bit_length is in fact an int.
    return [mpc.convert(_, mpc.SecFxp(2 * total_bit_length)) for _ in input_matrix]


def reciprocal_sec_num(sec_num: SecureNumberType) -> SecureNumberType:
    """
    compute the reciprocal of a secure number.

    :param sec_num: secure number
    :return: the reciprocal of the input
    """
    return mpc.div(1, sec_num)


@mpc_coro_ignore
async def matrix_inverse(
    input_matrix: SecureFixedPointMatrix,
) -> SecureFixedPointMatrix:
    """
    Function that securely computes the inverse of a matrix with secure fixed point elements.

    :param input_matrix: input matrix
    :return: inverse of the input matrix
    """
    secure_type = type(input_matrix[0][0])
    dimension = len(input_matrix)
    fractional_length: int = secure_type.frac_length
    await returnType(secure_type, dimension, dimension)

    # Convert to secfld
    a_matrix_secfld = scale_and_convert_matrix_to_sec_fld(input_matrix)

    # Find Ainv
    adj_a_matrix_det_secfld = _matrix_inverse(a_matrix_secfld)
    del a_matrix_secfld

    # Convert to large-field secfxp to support divisions
    # noinspection PyTypeChecker
    adj_a_matrix_det_secfxp = convert_matrix_to_large_sec_fxp(adj_a_matrix_det_secfld)
    adj_a_matrix_secfxp, det = adj_a_matrix_det_secfxp[:-1], adj_a_matrix_det_secfxp[-1]
    del adj_a_matrix_det_secfld, adj_a_matrix_det_secfxp

    # Correct determinant for earlier scaling
    det >>= fractional_length

    # Compute 1/det * adjA
    det_inv = reciprocal_sec_num(det)
    inv_a_matrix_secfxp = mpc.scalar_mul(det_inv, adj_a_matrix_secfxp)
    del det_inv, adj_a_matrix_secfxp

    # Convert inverse back to original secure type
    inv_a_matrix = mpc.convert(inv_a_matrix_secfxp, secure_type)
    del inv_a_matrix_secfxp

    # Return invA as matrix (list of lists)
    return [
        inv_a_matrix[i * dimension : i * dimension + dimension]
        for i in range(dimension)
    ]
