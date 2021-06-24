from warnings import warn

import numpy as np
import numpy.linalg as lin

from pybandstructure.common import rotation_matrix as R
from pybandstructure.common import reflection_matrix as S


class Point_Group:
    """Class for finite point groups"""
    def __init__(self, group_matrices, name):
        """Initalize a point group given matrices

        Parameters
        ----------
        group_matrices : list of matrices
            matrices representing the group operations
            They must be all square and with same size
            The first element must be the identity matrix
        name : str
            name of the group
        """
        self._group_matrices, self._space_dimension = self._check_group_matrices(
            group_matrices
        )
        self._name = name
        self._cardinality = len(group_matrices)
        self._group_table = self._build_group_table()
        self._inverse_table = self._build_inverse_table()
        self._abelian = not np.any(self._group_table - self._group_table.T)

    ################## Alternative constructors ########################
    @classmethod
    def trivial_group(cls, space_dimension):
        return cls(group_matrices= [np.identity(space_dimension, dtype=float)], name = 'trivial group')

    @classmethod
    def cyclic_group(cls, n, space_dimension=2):
        if space_dimension != 2:
            raise NotImplemented('only 2D cyclic group')
        if not n in [1,2,3,4,6]:
            warn('Group forbidden by crystallographic restriction')
        matrices = [R(i * 2. * np.pi / n, True) for i in range(n)] 
        return cls(group_matrices=matrices, name = 'C_{}'.format(n))

    @classmethod
    def dihedral_group(cls, n, space_dimension=2, theta0=0):
        if space_dimension != 2:
            raise NotImplemented('only 2D cyclic group')
        if not n in [1,2,3,4,6]:
            warn('Group forbidden by crystallographic restriction')
        matrices = [R(i * 2. * np.pi / n, True) for i in range(n)] + [S(i * np.pi / n + theta0, True) for i in range(n)]
        return cls(group_matrices=matrices, name = 'D_{}'.format(n))

    ####################################################################
    def _identify_matrix(self, matrix):
        index = []
        for i in range(self._cardinality):
            if np.allclose(matrix, self._group_matrices[i]):
                index.append(i)
        if len(index) != 1:
            raise ValueError(
                "none or more than one element of the group is close to given matrix"
            )
        else:
            return index[0]

    def _build_group_table(self):
        table = np.empty([self._cardinality, self._cardinality], dtype=int)
        for i in range(self._cardinality):
            for j in range(self._cardinality):
                table[i, j] = self._identify_matrix(
                    self._group_matrices[i] @ self._group_matrices[j]
                )
        return table

    def _build_inverse_table(self):
        table = np.empty([self._cardinality], dtype=int)
        for i in range(self._cardinality):
            table[i] = self._identify_matrix(lin.inv(self._group_matrices[i]))
        return table

    def _check_group_matrices(self, group_matrices):
        dimension = group_matrices[0].shape[0]
        if np.any(
            [
                g.shape != (dimension, dimension) or lin.det(g) == 0.0
                for g in group_matrices
            ]
        ):
            raise ValueError("nonuniform set of matrices or non invertible matrix")
        else:
            return group_matrices, dimension

    def compose(self, a, b):
        return self._group_table[a, b]

    def inverse(self, a):
        return self._inverse_table[a]

    def action_on_vectors(self, vectors):
        """given a set of vectors v that is closed under group operations return the matrix
        A[alpha, i], such that R[alpha] v[:,i] = v[:, A[alpha, i]]"""
        if vectors.shape[0] != self._space_dimension:
            raise ValueError("wrong vector dimension")
        vectors_number = vectors.shape[1]
        result = np.empty([self._cardinality, vectors_number], dtype=int)
        for i in range(vectors_number):
            for alpha in range(self._cardinality):
                index = []
                for j in range(vectors_number):
                    if np.allclose(
                        vectors[:, j], self._group_matrices[alpha] @ vectors[:, i]
                    ):
                        index.append(j)
                if len(index) != 1:
                    raise ValueError("not a closed set or redundant set")
                else:
                    result[alpha, i] = index[0]
        return result

    def integer_representation(self, vectors):
        if vectors.shape[0] != self._space_dimension:
            raise ValueError("wrong vector dimension")
        vectors_number = vectors.shape[1]
        scalar_product_mat = np.empty([vectors_number, vectors_number], dtype=float)
        for i in range(vectors_number):
            for j in range(vectors_number):
                scalar_product_mat[i, j] = np.dot(vectors[:, i], vectors[:, j])
        inv_scalar_product_mat = lin.inv(scalar_product_mat)
        A = np.empty([self._cardinality, vectors_number, vectors_number], dtype=int)
        for alpha in range(self._cardinality):
            matrix = lin.multi_dot(
                [
                    inv_scalar_product_mat,
                    vectors.T,
                    self._group_matrices[alpha],
                    vectors,
                ]
            ).T
            matrix_int = np.rint(matrix).astype(np.int)
            if np.allclose(matrix, matrix_int):
                A[alpha, :, :] = matrix_int
            else:
                print(matrix, matrix_int)
                raise ValueError("vectors not compatible with symmetry")
        return A

    @property
    def group_matrices(self):
        return self._group_matrices

    @group_matrices.setter
    def group_matrices(self, value):
        warnings.warn("cannot change group matrices. Ignoring")

    @property
    def cardinality(self):
        return self._cardinality

    @cardinality.setter
    def cardinality(self, value):
        warnings.warn("cannot change group order")


# class C1_2D(Point_Group):
#     def __init__(self):
#         Point_Group.__init__(self, space_dimension=2, name="C1_2D")


# class D6_2D(Point_Group):
#     def __init__(self, theta0=0):
#         Point_Group.__init__(
#             self,
#             space_dimension=2,
#             group_matrices=[
#                 R(0, True),
#                 R(2 * np.pi / 3, True),
#                 R(-2 * np.pi / 3, True),
#                 S(theta0, True),
#                 S(theta0 + np.pi / 3.0, True),
#                 S(theta0 - np.pi / 3.0, True),
#                 R(np.pi / 3, True),
#                 R(-np.pi / 3, True),
#                 R(np.pi, True),
#                 S(theta0 + np.pi / 2.0, True),
#                 S(theta0 + np.pi / 6.0, True),
#                 S(theta0 - np.pi / 6.0, True),
#             ],
#             name="D6_2",
#         )


# class D3_2D(Point_Group):
#     def __init__(self, theta0=0):
#         Point_Group.__init__(
#             self,
#             space_dimension=2,
#             group_matrices=[
#                 R(0, True),
#                 R(2 * np.pi / 3, True),
#                 R(-2 * np.pi / 3, True),
#                 S(theta0, True),
#                 S(theta0 + np.pi / 3.0, True),
#                 S(theta0 - np.pi / 3.0, True),
#             ],
#             name="D3_2",
#         )


# class D4_2D(Point_Group):
#     def __init__(self, theta0=0):
#         Point_Group.__init__(
#             self,
#             space_dimension=2,
#             group_matrices=[
#                 R(0, True),
#                 R(np.pi / 2, True),
#                 R(np.pi, True),
#                 R(-np.pi / 2, True),
#                 S(theta0, True),
#                 S(theta0 + np.pi / 4, True),
#                 S(theta0 + np.pi / 2, True),
#                 S(theta0 - np.pi / 4, True),
#             ],
#             name="D4_2",
#         )


# class D2_2D(Point_Group):
#     def __init__(self, theta0=0):
#         Point_Group.__init__(
#             self,
#             space_dimension=2,
#             group_matrices=[
#                 R(0, True),
#                 R(np.pi, True),
#                 S(theta0, True),
#                 S(theta0 + np.pi / 2, True),
#             ],
#             name="D2_2",
#         )
