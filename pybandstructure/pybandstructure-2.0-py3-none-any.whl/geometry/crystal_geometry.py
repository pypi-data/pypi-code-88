import numpy as np
import numpy.linalg as lin
from .point_groups import Point_Group


class Crystal_Geometry:
    def __init__(self, **kwargs):
        if "translation_vectors" in kwargs:
            self._translation_vectors = self._check_translation_vectors(
                kwargs["translation_vectors"]
            )
            (
                self._space_dimension,
                self._lattice_dimension,
            ) = self._translation_vectors.shape
            self._reciprocal_lattice_basis = (
                2.0
                * np.pi
                * lin.inv(self._translation_vectors[: self._lattice_dimension, :]).T
            )
        if "reciprocal_lattice_basis" in kwargs:
            if "translation_vectors" in kwargs:
                if not np.allclose(
                    self._reciprocal_lattice_basis, kwargs["reciprocal_lattice_basis"]
                ):
                    raise ValueError("direct and reciprocal vectors not compatible")
            else:
                if (
                    kwargs["reciprocal_lattice_basis"].ndim != 2
                    or kwargs["reciprocal_lattice_basis"].shape[0]
                    != kwargs["reciprocal_lattice_basis"].shape[1]
                ):
                    raise ValueError("reciprocal vectors must be a square matrix")
                self._reciprocal_lattice_basis = kwargs["reciprocal_lattice_basis"]
                (
                    self._space_dimension,
                    self._lattice_dimension,
                ) = self._reciprocal_lattice_basis.shape
                self._translation_vectors = (
                    2.0 * np.pi * lin.inv(self._reciprocal_lattice_basis).T
                )
        if (
            not "translation_vectors" in kwargs
            and not "reciprocal_lattice_basis" in kwargs
        ):
            raise ValueError(
                "at least one between translation_vectors and reciprocal_lattice_basis"
            )
        if "basis_vectors" in kwargs:
            self._basis_vectors = kwargs["basis_vectors"]
        else:
            self._basis_vectors = np.zeros([self.space_dimension, 1])
        if "point_group" in kwargs:
            if isinstance(kwargs["point_group"], Point_Group):
                self._point_group = kwargs["point_group"]
            else:
                raise TypeError("Not a valid point group")
        else:
            self._point_group = Point_Group(space_dimension=self._space_dimension)
        self._unit_cell_volume = np.abs(
            lin.det(self.translation_vectors[: self.lattice_dimension, :])
        )
        self._reciprocal_cell_volume = (
            2.0 * np.pi
        ) ** self.lattice_dimension / self.unit_cell_volume

    @property
    def translation_vectors(self):
        return self._translation_vectors

    @translation_vectors.setter
    def translation_vectors(self, value):
        warnings.warn("Geometrical properties cannot be changed.")

    @property
    def basis_vectors(self):
        return self._basis_vectors

    @basis_vectors.setter
    def basis_vectors(self, value):
        warnings.warn("Geometrical properties cannot be changed.")

    @property
    def reciprocal_lattice_basis(self):
        return self._reciprocal_lattice_basis

    @reciprocal_lattice_basis.setter
    def reciprocal_lattice_basis(self, value):
        warnings.warn("Geometrical properties cannot be changed.")

    @property
    def lattice_dimension(self):
        return self._lattice_dimension

    @lattice_dimension.setter
    def lattice_dimension(self, value):
        warnings.warn("Geometrical properties cannot be changed.")

    @property
    def space_dimension(self):
        return self._space_dimension

    @space_dimension.setter
    def space_dimension(self, value):
        warnings.warn("Geometrical properties cannot be changed.")

    @property
    def unit_cell_volume(self):
        return self._unit_cell_volume

    @unit_cell_volume.setter
    def unit_cell_volume(self, value):
        warnings.warn("Geometrical properties cannot be changed.")

    @property
    def reciprocal_cell_volume(self):
        return self._reciprocal_cell_volume

    @reciprocal_cell_volume.setter
    def reciprocal_cell_volume(self, value):
        warnings.warn("Geometrical properties cannot be changed.")

    @property
    def point_group(self):
        return self._point_group

    @point_group.setter
    def point_group(self, value):
        warnings.warn("Geometrical properties cannot be changed.")

    def _check_translation_vectors(self, vecs):
        # Convert to Numpy Array with definite type
        vecs = np.array(vecs, dtype=np.float64)
        # Check shape and extract dimetions
        if vecs.ndim == 2 and vecs.shape[0] >= vecs.shape[1]:
            if vecs.shape[0] > vecs.shape[1]:
                warnings.warn("Lattice dimension different from space dimension")
                if np.any(vecs[vecs.shape[1] :, :]):
                    raise ValueError("Lattice should lie in the first dimensions")
            if lin.matrix_rank(vecs[: vecs.shape[1], :]) < vecs.shape[1]:
                raise ValueError("Linearly dependent translation vectors")
            # Return array and number of dimentions
            return vecs
        else:
            raise ValueError(
                """the input vectors shape is not equal to (space_dimension, lattice_dimension)"""
            )


# identify the Bravais lattice type and the Point group
# Check compatibility between Point group and Bravais lattice
