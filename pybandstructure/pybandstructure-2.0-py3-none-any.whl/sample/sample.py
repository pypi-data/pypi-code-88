#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Module containing classes for sampling lattices and vector spaces."""

########## Import modules ##############################################

import numpy as np
import numpy.linalg as lin
import scipy.spatial as spa
from warnings import warn
from itertools import product
import h5py
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d

from pybandstructure.geometry.point_groups import *
from pybandstructure.common import *

######### Basic Sample class ###########################################


class Sample:
    """Class to store samples of a vector space as rational coordinates
    with respect to a basis.
    """

    ##### Initialization and alternative constructors ##################

    def __init__(
        self,
        basis_vectors,
        denominator,
        integer_coords,
        points_db=None,
        special_points=None,
    ):
        """Initialize a sample

        Parameters
        ----------
        basis_vectors : 2D array of floats with shape
            [space_dimension, lattice_dimension]
            basis vectors used to represent samples. The components of
            the i-th vector are stored as basis_vectors[:,i]
        denominator : integer or tuple of integers of length
            lattice_dimension.
            denominators used to express rational coordinates
        integer_coords : 2D array of integers with shape
            [n_samples, lattice_dimension]. Numerators of the rational
            coordinates of the sample points
        points_db : dictionary, optional
            dictionary that maps the integer coordinates to the index,
            by default None, i.e. build the dictionary automatically
        special_points : dictionary, optional
            dictionary associating strings to sample elements
        """
        ### basis vectors, dimensions denominators, sample class name
        self._basis_vectors = self._check_input_vectors(basis_vectors)
        self._space_dimension, self._lattice_dimension = self._basis_vectors.shape
        self._denominator = self._check_denominator(
            self._lattice_dimension, denominator
        )
        ### integer coords
        self._integer_coords = np.atleast_2d(np.array(integer_coords, dtype=np.int32))
        assert (
            self._integer_coords.ndim == 2
        ), "Wrong input for integer_coords: it must have two dimension"
        assert (
            self._integer_coords.shape[1] == self._lattice_dimension
        ), """Wrong input for integer_coords: the number of columns 
            should be equal to the dimension of the model"""
        ### build coordinates array
        self._coords = np.transpose(
            self._basis_vectors @ np.transpose(self._integer_coords / self._denominator)
        )
        ### special points
        if special_points is None:
            special_points = {}
        assert type(special_points) == dict

        assert all([isinstance(label, str) for label in special_points.keys()])
        self._special_points = special_points
        ### points_db
        if points_db is None:
            self._points_db = self._build_db(integer_coords)
        else:
            self._points_db = points_db
        ### Check on the special points. Cannot be put before
        assert all([point in self for point in special_points.values()])

    @classmethod
    def sample(cls, basis_vectors, denominator, integer_coords, special_points=None):
        """Calls the __init__ method."""
        return cls(
            basis_vectors=basis_vectors,
            denominator=denominator,
            integer_coords=integer_coords,
            special_points=special_points,
        )

    @classmethod
    def from_file(cls, file_name, sample_name, file_format="hdf5"):
        """Initialize a new Sample instance using data from file

        Parameters
        ----------
        file_name : str or path
            name of the file from which data are read
        sample_name : str
            name of the sample to read
        file_format : str, optional
            type of format used for saving, by default 'hdf5'.
            Only 'hdf5' currently available.

        Returns
        -------
        Sample
            reconstructed sample object
        """
        if file_format == "hdf5":
            with h5py.File(file_name, "r") as file_to_read:
                basis_vectors = file_to_read[sample_name + "/basis_vectors"][...]
                denominator = file_to_read[sample_name + "/denominator"][...]
                integer_coords = file_to_read[sample_name + "/integer_coords"][...]
                class_name = file_to_read[sample_name].attrs["class_name"]
                ### reconstruct dictionary
                idx_keys = file_to_read[sample_name + "/db_keys"][...]
                idx_values = file_to_read[sample_name + "/db_values"][...]
                points_db = {}
                for i, key in enumerate(idx_keys):
                    points_db[tuple(key)] = eval(idx_values[i])
                ### special points
                special_points = eval(
                    file_to_read[sample_name + "/integer_coords"].attrs[
                        "special_points"
                    ]
                )
                ### weights
                try:
                    weights = file_to_read[sample_name + "/weights"][...]
                except:
                    pass
                ### volume
                try:
                    volume = file_to_read[sample_name + "/weights"].attrs["volume"]
                except:
                    pass
        else:
            warn("invalid file_format")
        print(class_name)
        if class_name == 'Sample':
            return Sample(
                basis_vectors=basis_vectors,
                denominator=denominator,
                integer_coords=integer_coords,
                points_db=points_db,
                special_points=special_points)

        elif class_name == 'Space_Sample':
            return Space_Sample(
            basis_vectors=basis_vectors,
            denominator=denominator,
            integer_coords=integer_coords,
            points_db=points_db,
            special_points=special_points,
            volume=volume,
            weights=weights)

        elif class_name == 'Unit_Cell_Sample':
            return Unit_Cell_Sample(
            basis_vectors=basis_vectors,
            denominator=denominator,
            integer_coords=integer_coords,
            points_db=points_db,
            special_points=special_points,
            weights=weights)
        
        else:
            warn("invalid class_name")

    @classmethod
    def lattice_sample(cls, basis_vectors, cut_off, special_points=None):
        """Build a sample of a Bravais lattice containing all the
        vectors with norm smaller than a specified cut off.
        Denominator used for expressing coordinates is 1.

        Parameters
        ----------
        basis_vectors : 2D array-like
            primitive vectors of the lattice.
            The i-th vector is basis_vectors[:,i].
        cut_off : float
            Maximum norm of vectors included in the sample
        special_points : dictionary, optional
            dictionary associating strings to sample elements

        Returns
        -------
        Sample
            Sample object containing the points of the Bravais lattice
        """
        basis_vectors = cls._check_input_vectors(basis_vectors)
        space_dimension, lattice_dimension = basis_vectors.shape
        M = basis_vectors.T @ basis_vectors
        M_inv = lin.inv(M)
        n_max = [
            int(np.ceil(cut_off * np.sqrt(M_inv[i, i])))
            for i in range(lattice_dimension)
        ]
        integer_coords = []
        iter = product(*[range(-n, n + 1, 1) for n in n_max])
        for x in iter:
            if lin.multi_dot([x, M, x]) <= cut_off ** 2:
                integer_coords.append(x)
        integer_coords.sort(key=lambda x: lin.multi_dot([x, M, x]))
        return cls(
            basis_vectors=basis_vectors,
            denominator=1,
            integer_coords=integer_coords,
            special_points=special_points,
        )

    @classmethod
    def line_sample(cls, basis_vectors, cut_off, direction=0, special_points=None):
        """Build a sample of a 1D sublattice of a given Bravais lattice
        along a specified primitive vector and including vectors with a
        maximum norm given by a cut off.

        Parameters
        ----------
        basis_vectors : 2D array-like
            primitive vectors of the lattice.
            The i-th vector is basis_vectors[:,i].
        cut_off : float
            Maximum norm of vectors included in the sample
        direction : int, by default 0
            primitive vector along which the 1D sample is build
        special_points : dictionary, optional
            dictionary associating strings to sample elements

        Returns
        -------
        Sample
            The 1D sublattice
        """
        basis_vectors = cls._check_input_vectors(basis_vectors)
        space_dimension, lattice_dimension = basis_vectors.shape
        n_max = int(np.floor(cut_off / lin.norm(basis_vectors[:, direction])))
        integer_coords = np.zeros([2 * n_max + 1, lattice_dimension], dtype=int)
        integer_coords[:, direction] = np.arange(-n_max, n_max + 1, dtype=int)
        return cls(
            basis_vectors=basis_vectors,
            denominator=1,
            integer_coords=integer_coords,
            special_points=special_points,
        )

    ######## Properties ################################################

    @property
    def basis_vectors(self):
        return self._basis_vectors

    @basis_vectors.setter
    def basis_vectors(self, _):
        warn("Sample is read only")

    @property
    def space_dimension(self):
        return self._space_dimension

    @space_dimension.setter
    def space_dimension(self, _):
        warn("Sample is read only")

    @property
    def lattice_dimension(self):
        return self._lattice_dimension

    @lattice_dimension.setter
    def lattice_dimension(self, _):
        warn("Sample is read only")

    @property
    def denominator(self):
        return self._denominator

    @denominator.setter
    def denominator(self, _):
        warn("Sample is read only")

    @property
    def integer_coords(self):
        return self._integer_coords

    @integer_coords.setter
    def integer_coords(self, _):
        warn("Sample is read only")

    @property
    def coords(self):
        return self._coords

    @coords.setter
    def coords(self, _):
        warn("Sample is read only")

    @property
    def special_points(self):
        return self._special_points

    @special_points.setter
    def special_points(self, _):
        raise warn("Sample is read only")

    ######## Methods ###################################################

    def __call__(self, point):
        """Return a dictionary with informations about a specific point.

        Parameters
        ----------
        point : tuple of ints of length lattice_dimension, or int,
        or sequence of ints of length 1, or str
            integer coords of the requested point
            or index of the point or string identifying a special point

        Returns
        -------
        dictionary
            dictionary containing informations of the specified point

        Raises
        ------
        TypeError if key is not of the correct type

        """
        ### calling with integer coordinates
        if (
            isinstance(point, tuple)
            and len(point) == self._lattice_dimension
            and all(isinstance(n, (int, np.integer)) for n in point)
        ):
            return self._points_db[point]
        ### calling with index
        elif isinstance(point, (int, np.integer)) or (
            len(point) == 1 and isinstance(point[0], (int, np.integer))
        ):
            return self._points_db[tuple(self._integer_coords[int(point)])]
        ### calling with special point string
        elif isinstance(point, str):
            return self._points_db[self._special_points[point]]
        else:
            raise TypeError(
                """Given argument should be either 
                   a tuple of ints of length lattice_dimension 
                   a single int or int sequence or length 1
                   a string representing a special point"""
            )

    def __getitem__(self, point):
        """Return the index corresponding to a given point.

        Parameters
        ----------
        point : tuple of ints of length lattice_dimension, or int,
        or sequence of ints of length 1, or str
            integer coords of the requested point
            or index of the point or string identifying a special point

        Returns
        -------
        int
            the index corresponding to the given coordinates
        """
        return self(point)["index"]

    def __contains__(self, point):
        """Whether an index or a tuple of coordinates is contained in
        the sample.

        Parameters
        ----------
        point : tuple of ints of length lattice_dimension, or int,
        or sequence of ints of length 1, or str
            integer coords of the requested point
            or index of the point or string identifying a special point

        Returns
        -------
        boolean : result of the test
        """
        ### calling with integer coordinates
        if (
            isinstance(point, tuple)
            and len(point) == self._lattice_dimension
            and all(isinstance(n, (int, np.integer)) for n in point)
        ):
            return point in self._points_db
        ### calling with index
        elif isinstance(point, (int, np.integer)) or (
            len(point) == 1 and isinstance(point[0], (int, np.integer))
        ):
            point = int(point)
            return point < self.__len__() and point >= 0
        ### calling with special point string
        elif isinstance(point, str):
            return point in self._special_points
        else:
            raise TypeError("Given key should be a tuple of ints or a single int")

    def __len__(self):
        """Number of points in the sample

        Returns
        -------
        int
            the number of points in the sample
        """
        return self._integer_coords.shape[0]

    def __iter__(self):
        """Iterates over the integer coords"""
        for v in self._integer_coords:
            yield tuple(v)

    def get_coords(self, point):
        """Get the real coordinates corresponding to a point.

        Parameters
        ----------
        point : int or tuple of ints
            index or integer coordinates

        Returns
        -------
        1D array of float
            the real coordinates of the selected point
        """
        return self._coords[self[point]]

    def get_integer_coords(self, point):
        """Get the integer coordinates corresponding to a point.

        Parameters
        ----------
        point : int or tuple of ints
            index or integer coordinates

        Returns
        -------
        1D array of int
            the integer coordinates of the selected point
        """
        return self._integer_coords[self[point]]

    def get_integer_part(self, point):
        """Return the integer part of a point.

        Parameters
        ----------
        point : tuple of ints of length lattice_dimension, or int,
        or sequence of ints of length 1, or str
            integer coords of the requested point
            or index of the point or string identifying a special point

        Returns
        -------
        tuple
            integer part of point
        """
        ####### Note that does not depend on other functions
        ### calling with integer coordinates
        if (
            isinstance(point, tuple)
            and len(point) == self._lattice_dimension
            and all(isinstance(n, (int, np.integer)) for n in point)
        ):
            c = point
        ### calling with index
        elif isinstance(point, (int, np.integer)) or (
            len(point) == 1 and isinstance(point[0], (int, np.integer))
        ):
            c = self._integer_coords[int(point)]
        ### calling with special point string
        elif isinstance(point, str):
            c = self._special_points[point]
        return tint_div(c, self._denominator)

    def get_fractional_part(self, point):
        """Return the fractional part of a point.

        Parameters
        ----------
        point : tuple of ints of length lattice_dimension, or int,
        or sequence of ints of length 1, or str
            integer coords of the requested point
            or index of the point or string identifying a special point

        Returns
        -------
        tuple
            fractional part of point
        """
        ####### Note that does not depend on other functions
        ### calling with integer coordinates
        if (
            isinstance(point, tuple)
            and len(point) == self._lattice_dimension
            and all(isinstance(n, (int, np.integer)) for n in point)
        ):
            c = point
        ### calling with index
        elif isinstance(point, (int, np.integer)) or (
            len(point) == 1 and isinstance(point[0], (int, np.integer))
        ):
            c = self._integer_coords[int(point)]
        ### calling with special point string
        elif isinstance(point, str):
            c = self._special_points[point]
        return tmod(c, self._denominator)

    def save(self, file_name, sample_name, file_format="hdf5"):
        """Save the sample to file.

        Parameters
        ----------
        file_name : string or path
            name of the file
        sample_name : string
            name of the sample
        file_format : str, optional
            file format, by default 'hdf5'.
            Only hdf5 available.
        """
        if file_format == "hdf5":
            with h5py.File(file_name, "a") as file_to_write:
                file_to_write[sample_name + "/basis_vectors"] = self._basis_vectors
                file_to_write[sample_name + "/denominator"] = self._denominator
                file_to_write[sample_name + "/integer_coords"] = self._integer_coords
                file_to_write[sample_name].attrs["class_name"] = self.__class__.__name__
                ### saving dictionary
                keys = []
                vals = []
                for key in self._points_db:
                    keys.append(key)
                    vals.append(repr(self._points_db[key]))
                file_to_write[sample_name + "/db_keys"] = np.array(keys, dtype=int)
                file_to_write[sample_name + "/db_values"] = np.array(vals, dtype="S")
                ### saving special points
                file_to_write[sample_name + "/integer_coords"].attrs[
                    "special_points"
                ] = repr(self._special_points)
                ### alternative for saving special points
                # dt = h5py.special_dtype(vlen=str)
                # file_to_write[sample_name +'/special_points_keys'] = np.array(list(self._special_points.keys()),dtype=dt)
                # file_to_write[sample_name + '/special_points_values'] = np.array(list(self._special_points.values()))
        else:
            warn("invalid file_format")

    def plot(self, **kwargs):
        """Plot the sample using matplotlib.

        Returns
        -------
        tuple
            plot of the sample and basis vectors

        Returns
        -------
            matplotlib.axes
        """
        if self._lattice_dimension == 1:
            ax = plt.axes()
            v = self._basis_vectors[:, 0]
            v_origin = np.vstack(([0, 0], v))
            ax.plot(v_origin[:, 0], v_origin[:, 1], "r-")
            ax.plot(
                self._coords[:, 0], np.zeros_like(self._coords[:, 0]), "o", **kwargs
            )
            return ax

        elif self._lattice_dimension == 2:
            ax = plt.axes()
            for i in range(2):
                v = self._basis_vectors[:, i]
                v_origin = np.vstack(([0, 0], v))
                ax.plot(v_origin[:, 0], v_origin[:, 1], "r-")
            plt.axis("equal")
            ax.plot(self._coords[:, 0], self._coords[:, 1], "o", **kwargs)
            return ax

        elif self._lattice_dimension == 3:
            ax = plt.axes(projection="3d")
            for i in range(3):
                v = self._basis_vectors[:, i]
                v_origin = np.vstack(([0, 0, 0], v))
                ax.plot(v_origin[:, 0], v_origin[:, 1], v_origin[:, 2], "r-")
            ax.plot(
                self._coords[:, 0],
                self._coords[:, 1],
                self._coords[:, 2],
                "o",
                **kwargs
            )
            return ax
        else:
            warn("Impossible to plot a {}D object".format(self._lattice_dimension))

    def contour(self, point_list):
        """Create a contour in the sample space given a list of points.

        Parameters
        ----------
        point_list : list of points
            Each element can be a tuple of ints of length
            lattice_dimension, or int, or sequence of ints of length 1, or str.

        Returns
        -------
        dictionary containing
            indices : array of integers containing the indices of the
            points along the path
            x : array of float containing coordinates of points measured
             along the path
            vertices : array containing vertices positions
        """
        point_list_tuples = []
        for point in point_list:
            ### calling with integer coordinates
            if (
                isinstance(point, tuple)
                and len(point) == self._lattice_dimension
                and all(isinstance(n, (int, np.integer)) for n in point)
            ):
                c = point
            ### calling with index
            elif isinstance(point, (int, np.integer)) or (
                len(point) == 1 and isinstance(point[0], (int, np.integer))
            ):
                c = self._integer_coords[int(point)]
            ### calling with special point string
            elif isinstance(point, str):
                c = self._special_points[point]
            point_list_tuples.append(c)
        cont = []
        distances = []
        points = [0]
        for i in range(len(point_list) - 1):
            pts = self._points_on_line(point_list_tuples[i], point_list_tuples[i + 1])
            points.append(len(pts))
            cont += pts
            l = tdiv(
                tdif(point_list_tuples[i], point_list_tuples[i + 1]), self.denominator
            )
            distances.append(
                lin.norm(self.basis_vectors @ l) / len(pts) * np.ones([len(pts)])
            )
        cont += self._points_on_line(point_list_tuples[-1], point_list_tuples[-1])
        points = np.cumsum(points)
        x = np.concatenate(([0.0], np.cumsum(np.concatenate(distances))))
        index = []
        for key in cont:
            index.append(self[key])
        index = np.array(index, dtype=int)
        return {"indices": index, "x": x, "vertices": points, "list" : point_list}

    ######### Internal methods #########################################

    @staticmethod
    def _build_db(integer_coords):
        """Build the sample database in the standard case."""
        dict_ = {}
        for i, key in enumerate(integer_coords):
            dict_[tuple(key)] = {"index": i}
        return dict_

    @staticmethod
    def _points_on_line(p1, p2):
        """Return all the integer points on a specified line."""
        dimension = len(p1)
        if len(p2) != dimension:
            raise ValueError("Non-matching dimensions")
        dist = [p2[i] - p1[i] for i in range(dimension)]
        div = np.gcd.reduce(dist)
        if div != 0:
            return [
                tuple([p1[j] + i * dist[j] // div for j in range(dimension)])
                for i in range(div)
            ]
        else:
            return [tuple([p1[j] for j in range(dimension)])]

    @staticmethod
    def _check_input_vectors(vecs):
        """Check and return the input vectors.

        Parameters
        ----------
        vecs : 2D array-like
            Arrays to be checked

        Returns
        -------
        2D array
            basis vectors

        Raises
        ------
        ValueError
            Linearly dependent translation vectors
        ValueError
            Input vectors shape is not equal to (space_dimension, lattice_dimension)
        """
        # Convert to Numpy Array with definite type
        vecs = np.array(vecs, dtype=np.float64)
        # Check shape and rank
        if vecs.ndim == 2 and vecs.shape[0] >= vecs.shape[1]:
            if vecs.shape[0] > vecs.shape[1]:
                warn("Lattice dimension different from space dimension")
            if lin.matrix_rank(vecs[: vecs.shape[1], :]) < vecs.shape[1]:
                raise ValueError("Linearly dependent translation vectors")
            return vecs
        else:
            raise ValueError(
                """Input vectors shape is not equal to (space_dimension, lattice_dimension)"""
            )

    @staticmethod
    def _check_denominator(dim, n_sites):
        """Check and return the denominator."""
        if isinstance(n_sites, (int, np.integer)):
            return np.array([n_sites for _ in range(dim)], dtype=np.int32)
        elif len(n_sites) == dim and all(
            [isinstance(ni, (int, np.integer)) for ni in n_sites]
        ):
            return np.array(n_sites, dtype=np.int32)
        else:
            raise ValueError(
                """n_sites should be an integer or a sequence of integers of length dim"""
            )


########################################################################

####### Space_Sample class #############################################


class Space_Sample(Sample):
    """Class to store sample of a continuous region of a vector space.
    The main difference with Sample is that it has the notion of
    integration over the sample points."""

    ####### Initialization and alternative constructors ################

    def __init__(
        self,
        basis_vectors,
        denominator,
        integer_coords,
        volume,
        points_db=None,
        special_points={},
        weights=None,
    ):
        """Initialize a Space_Sample object

        Parameters
        ----------
        basis_vectors : 2D array of floats with shape
            [space_dimension, lattice_dimension]
            basis vectors used to represent samples. The components of
            the i-th vector are stored as basis_vectors[:,i]
        denominator : integer or tuple of integers of length
            lattice_dimension.
            denominators used to express rational coordinates
        integer_coords : 2D array of integers with shape
            [n_samples, lattice_dimension]. Numerators of the rational
            coordinates of the sample points
        volume : float
            volume of the sample
        points_db : dictionary, optional
            dictionary that maps the integer coordinates to the index,
            by default None, i.e. build the dictionary automatically
        special_points : dictionary, optional
            dictionary associating strings to sample elements
        weights : 1D array of floats, same length as integer_coords,
        optional
            Integration weights, by default None, i.e. uniform weights
        """
        ### check and store weights
        if weights is None:
            weights = self._build_weights(integer_coords)
        assert np.allclose(np.sum(weights), 1)
        assert len(weights) == len(integer_coords)
        self._weights = weights
        ### check and store sample volume
        assert isinstance(volume, (float, np.float))
        self._volume = volume
        ### build dictionary if not present
        if points_db is None:
            points_db = self._build_db(integer_coords)
        ### Call superclass __init__
        Sample.__init__(
            self,
            basis_vectors=basis_vectors,
            denominator=denominator,
            integer_coords=integer_coords,
            points_db=points_db,
            special_points=special_points,
        )

    # @classmethod
    # def from_file(cls, file_name, sample_name, file_format="hdf5"):
    #     """Initialize a new Space_Sample instance using data from file

    #     Parameters
    #     ----------
    #     file_name : str or path
    #         name of the file from which data are read
    #     sample_name : str
    #         name of the sample to read
    #     file_format : str, optional
    #         type of format used for saving, by default 'hdf5'.
    #         Only 'hdf5' currently available.

    #     Returns
    #     -------
    #     Space_Sample
    #         reconstructed sample object
    #     """
    #     if file_format == "hdf5":
    #         with h5py.File(file_name, "r") as file_to_read:
    #             basis_vectors = file_to_read[sample_name + "/basis_vectors"][...]
    #             denominator = file_to_read[sample_name + "/denominator"][...]
    #             integer_coords = file_to_read[sample_name + "/integer_coords"][...]
    #             ### reconstruct dictionary
    #             idx_keys = file_to_read[sample_name + "/db_keys"][...]
    #             idx_values = file_to_read[sample_name + "/db_values"][...]
    #             points_db = {}
    #             for i, key in enumerate(idx_keys):
    #                 points_db[tuple(key)] = eval(idx_values[i])
    #             ### special points
    #             special_points = eval(
    #                 file_to_read[sample_name + "/integer_coords"].attrs[
    #                     "special_points"
    #                 ]
    #             )
    #             ### weights
    #             weights = file_to_read[sample_name + "/weights"][...]
    #             ### volume
    #             volume = file_to_read[sample_name + "/weights"].attrs["volume"]
    #     else:
    #         warn("invalid file_format")
    #     return cls(
    #         basis_vectors=basis_vectors,
    #         denominator=denominator,
    #         integer_coords=integer_coords,
    #         points_db=points_db,
    #         special_points=special_points,
    #         volume=volume,
    #         weights=weights,
    #     )

    @classmethod
    def cubic_sample(cls, basis_vectors, denominator, special_points=None):
        """Create a centered cubic sample in N dimensions.

        Parameters
        ----------
        basis_vectors : 2D array of floats.
            Basis vectors used to represent samples. The components of
            the i-th vector are stored as basis_vectors[:,i].
            All The vectors must be mutually orthogonal and must have
            the same norm.
        denominator : integer or tuple of integers of length
        lattice_dimension.
            denominators used to express rational coordinates
            All the denominators must be equal and odd.
        special_points : dictionary, optional
            Dictionary associating strings to sample elements.

        Returns
        -------
        Space_Sample
            A uniform square sample.
        """
        basis_vectors = cls._check_input_vectors(basis_vectors)
        space_dimension, lattice_dimension = basis_vectors.shape
        denominator = cls._check_denominator(lattice_dimension, denominator)
        assert all(ni == denominator[0] for ni in denominator)
        assert denominator[0] % 2 == 1
        for i in range(lattice_dimension):
            for j in range(i, lattice_dimension):
                if i == j:
                    assert np.allclose(
                        lin.norm(basis_vectors[:, 0]), lin.norm(basis_vectors[:, i])
                    )
                else:
                    assert np.allclose(
                        np.dot(basis_vectors[:, i], basis_vectors[:, j]), 0
                    )
        # create integer coords
        arrs = np.meshgrid(
            *[np.arange(-(den // 2), den // 2 + 1) for den in denominator]
        )
        integer_coords = np.stack([arr.flatten() for arr in arrs], axis=-1)
        volume = (lin.norm(basis_vectors[:, 0])) ** lattice_dimension
        return cls(
            basis_vectors=basis_vectors,
            denominator=denominator,
            integer_coords=integer_coords,
            volume=volume,
            special_points=special_points,
        )

    @classmethod
    def spherical_sample(cls, basis_vectors, denominator, cut_off, special_points=None):
        """Build a sample of the space containing all the
        vectors with norm smaller than a specified cut off.

        Parameters
        ----------
        basis_vectors : 2D array-like
            primitive vectors of the lattice.
            The i-th vector is basis_vectors[:,i].
        denominator : integer or tuple of integers of length
            lattice_dimension.
            denominators used to express rational coordinates
        cut_off : float
            Maximum norm of vectors included in the sample
        special_points : dictionary, optional
            dictionary associating strings to sample elements

        Returns
        -------
        Sample
            Sample object containing the points of the Bravais lattice
        """
        basis_vectors = cls._check_input_vectors(basis_vectors)
        space_dimension, lattice_dimension = basis_vectors.shape
        denominator = cls._check_denominator(lattice_dimension, denominator)
        M = basis_vectors.T @ basis_vectors
        M_inv = lin.inv(M)
        n_max = [
            int(np.ceil(cut_off * denominator[i] * np.sqrt(M_inv[i, i])))
            for i in range(lattice_dimension)
        ]
        integer_coords = []
        iter = product(*[range(-n, n + 1, 1) for n in n_max])
        for x in iter:
            if lin.multi_dot([x / denominator, M, x / denominator]) <= cut_off ** 2:
                integer_coords.append(x)
        integer_coords.sort(
            key=lambda x: lin.multi_dot([x / denominator, M, x / denominator])
        )
        return cls(
            basis_vectors=basis_vectors,
            denominator=denominator,
            integer_coords=integer_coords,
            volume=np.sqrt(abs(lin.det(M)))
            / np.prod(denominator)
            * len(integer_coords),
            special_points=special_points,
        )

    ###### Properties ##################################################

    @property
    def weights(self):
        return self._weights

    @weights.setter
    def weights(self, _):
        raise warn("Space_Sample is read only")

    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, _):
        raise warn("Space_Sample is read only")

    ####### Methods ####################################################

    def save(self, file_name, sample_name, file_format="hdf5"):
        """Save the sample to file.

        Parameters
        ----------
        file_name : string or path
            name of the file
        sample_name : string
            name of the sample
        file_format : str, optional
            file format, by default 'hdf5'.
            Only hdf5 available.
        """
        Sample.save(self, file_name, sample_name, file_format)
        if file_format == "hdf5":
            with h5py.File(file_name, "a") as file_to_write:
                file_to_write[sample_name + "/weights"] = self._weights
                file_to_write[sample_name + "/weights"].attrs["volume"] = self._volume
        else:
            warn("Invalid file_format.")

    def get_weight(self, point):
        """Get the integration weight corresponding to a point.

        Parameters
        ----------
        point : int or tuple of ints
            index or integer coordinates

        Returns
        -------
        float
            the integration weight corresponding to the selected point
        """
        return self._weights[self[point]]

    def integrate(self, array, axis):
        """Integrate an array over the sample.

        Parameters
        ----------
        array : ndarray
            array to integrate
        axis : int
            axis of the array to integrate over.
            The length of the corresponding dimension must match the
            length of the sample.

        Returns
        -------
        float
            the integral of the array
        """
        return self._volume * np.tensordot(array, self._weights, axes=(axis, 0))

    ####### Internal methods ###########################################

    @staticmethod
    def _build_weights(integer_coords):
        """Build uniform weights"""
        return np.ones([len(integer_coords)]) / float(len(integer_coords))


########################################################################

######## Unit_Cell_Sample class ########################################


class Unit_Cell_Sample(Space_Sample):
    """Class for storing samples of unit cells. With respect to
    Space_Sample adds the notion of identification for points that
    differ by an integer number of basis vectors."""

    ######## Initialization and alternative constructors ###################

    def __init__(
        self,
        basis_vectors,
        denominator,
        integer_coords,
        points_db,
        special_points,
        weights,
    ):
        """Initialize a Unit_Cell_Sample
        Parameters
        ----------
        basis_vectors : 2D array of floats with shape
            [space_dimension, lattice_dimension]
            basis vectors used to represent samples. The components of
            the i-th vector are stored as basis_vectors[:,i]
        denominator : integer or tuple of integers of length
            lattice_dimension.
            denominators used to express rational coordinates
        integer_coords : 2D array of integers with shape
            [n_samples, lattice_dimension]. Numerators of the rational
            coordinates of the sample points
        volume : float, optional
            volume of the unit cell. If not provided it is calculated
            from basis vectors.
        points_db : dictionary, optional
            dictionary that maps the integer coordinates to the index,
            by default None, i.e. build the dictionary automatically
        special_points : dictionary, optional
            dictionary associating strings to sample elements
        weights : 1D array of floats, same length as integer_coords,
        optional
            Integration weights, by default None, i.e. uniform weights
        """
        cell_volume = np.sqrt(np.abs(lin.det(basis_vectors.T @ basis_vectors)))

        Space_Sample.__init__(
            self,
            basis_vectors=basis_vectors,
            denominator=denominator,
            integer_coords=integer_coords,
            volume=cell_volume,
            points_db=points_db,
            special_points=special_points,
            weights=weights,
        )

    # @classmethod
    # def from_file(cls, file_name, sample_name, file_format="hdf5"):
    #     """Initialize a new Space_Sample instance using data from file

    #     Parameters
    #     ----------
    #     file_name : str or path
    #         name of the file from which data are read
    #     sample_name : str
    #         name of the sample to read
    #     file_format : str, optional
    #         type of format used for saving, by default 'hdf5'.
    #         Only 'hdf5' currently available.

    #     Returns
    #     -------
    #     Space_Sample
    #         reconstructed sample object
    #     """
    #     if file_format == "hdf5":
    #         with h5py.File(file_name, "r") as file_to_read:
    #             basis_vectors = file_to_read[sample_name + "/basis_vectors"][...]
    #             denominator = file_to_read[sample_name + "/denominator"][...]
    #             integer_coords = file_to_read[sample_name + "/integer_coords"][...]
    #             ### reconstruct dictionary
    #             idx_keys = file_to_read[sample_name + "/db_keys"][...]
    #             idx_values = file_to_read[sample_name + "/db_values"][...]
    #             points_db = {}
    #             for i, key in enumerate(idx_keys):
    #                 points_db[tuple(key)] = eval(idx_values[i])
    #             ### special points
    #             special_points = eval(
    #                 file_to_read[sample_name + "/integer_coords"].attrs[
    #                     "special_points"
    #                 ]
    #             )
    #             ### weights
    #             weights = file_to_read[sample_name + "/weights"][...]
    #     else:
    #         warn("invalid file_format")
    #     return cls(
    #         basis_vectors=basis_vectors,
    #         denominator=denominator,
    #         integer_coords=integer_coords,
    #         points_db=points_db,
    #         special_points=special_points,
    #         weights=weights,
    #     )

    @classmethod
    def default_unit_cell(cls, basis_vectors, denominator, special_points=None):
        """Initialize a sample of the default unit cell. i.e. the
        parallelepiped described by the primitive vectors.

        Parameters
        ----------
        basis_vectors : 2D array of floats with shape
            [space_dimension, lattice_dimension]
            basis vectors used to represent samples. The components of
            the i-th vector are stored as basis_vectors[:,i]
        denominator : integer or tuple of integers of length
            lattice_dimension.
            denominators used to express rational coordinates
        special_points : dictionary
            dictionary mapping strings to tuples of integer coordinates

        Returns
        -------
        Unit_Cell_Sample
            The initialized sample.
        """
        basis_vectors = cls._check_input_vectors(basis_vectors)
        space_dimension, lattice_dimension = basis_vectors.shape
        denominator = cls._check_denominator(lattice_dimension, denominator)
        ### integer_coords
        arrs = np.meshgrid(*[np.arange(den) for den in denominator])
        integer_coords = np.stack([arr.flatten() for arr in arrs], axis=-1)
        ### points_db
        points_db = {}
        for i, key in enumerate(integer_coords):
            points_db[tuple(key)] = {
                "index": i,
                "operation": 0,
                "translation": tuple([0 for _ in range(lattice_dimension)]),
            }
        ### weights
        weights = np.ones(len(integer_coords)) / np.prod(denominator)
        return cls(
            basis_vectors=basis_vectors,
            denominator=denominator,
            integer_coords=integer_coords,
            points_db=points_db,
            weights=weights,
            special_points=special_points,
        )

    @classmethod
    def wigner_seitz_cell(cls, basis_vectors, denominator, special_points=None):
        """Uniform sampling of the W-S cell of the given lattice.

        Parameters
        ----------
        basis_vectors : 2D array of floats with shape
            [space_dimension, lattice_dimension]
            basis vectors used to represent samples. The components of
            the i-th vector are stored as basis_vectors[:,i]
        denominator : integer or tuple of integers of length
            lattice_dimension.
            denominators used to express rational coordinates
        special_points : dictionary
            dictionary mapping strings to tuples of integer coordinates

        Returns
        -------
        Unit_Cell_Sample
            uniform sample of the Wigner-Seitz cell of the given lattice
        """
        basis_vectors = cls._check_input_vectors(basis_vectors)
        space_dimension, lattice_dimension = basis_vectors.shape
        denominator = cls._check_denominator(lattice_dimension, denominator)
        ### integer_coords
        integer_coords = cls._wigner_seitz_points(
            basis_vectors=basis_vectors, denominator=denominator
        )
        ### points_db
        point_group = Point_Group.trivial_group(space_dimension)
        symmetry_repr = point_group.integer_representation(basis_vectors)
        points_db = cls._build_db(denominator, integer_coords, symmetry_repr)
        ### weights
        weights = np.ones(len(integer_coords)) / np.prod(denominator)

        return cls(
            basis_vectors=basis_vectors,
            denominator=denominator,
            integer_coords=integer_coords,
            points_db=points_db,
            weights=weights,
            special_points=special_points,
        )

    @classmethod
    def irreducible_wigner_seitz_cell(
        cls, basis_vectors, denominator, point_group, special_points=None
    ):
        """Uniform sampling of the irreducible wedge of the Wigner-Seitz
        cell of the given lattice.

         Parameters
        ----------
        basis_vectors : 2D array of floats with shape
            [space_dimension, lattice_dimension]
            basis vectors used to represent samples. The components of
            the i-th vector are stored as basis_vectors[:,i]
        denominator : integer or tuple of integers of length
            lattice_dimension.
            denominators used to express rational coordinates
        point_group : Point_Group
            Point group of the lattice
        special_points : dictionary
            dictionary mapping strings to tuples of integer coordinates

        Returns
        -------
        Unit_Cell_Sample
            uniform sample of the irreducible wedge of the Wigner-Seitz
            cell of the given lattice
        """
        basis_vectors = cls._check_input_vectors(basis_vectors)
        space_dimension, lattice_dimension = basis_vectors.shape
        denominator = cls._check_denominator(lattice_dimension, denominator)
        assert isinstance(point_group, Point_Group)
        symmetry_repr = point_group.integer_representation(basis_vectors)
        ### integer_coords
        ### ### points in the full wigner seitz cell
        points = cls._wigner_seitz_points(
            basis_vectors=basis_vectors, denominator=denominator
        )
        ### ### calculate orbits
        orbits = []
        for p in points:
            orbit = set()
            for g in range(symmetry_repr.shape[0]):
                # careful with transpose
                gp = symmetry_repr[g, :, :].T @ p
                orbit.add(tuple(gp))
            if not orbit in orbits:
                orbits.append(orbit)
        ### ### join equivalent orbits
        for i in range(len(orbits)):
            for j in range(i + 1, len(orbits)):
                equal = False
                for element2 in orbits[j]:
                    break
                for element in orbits[i]:
                    equal = equal or (not np.any(tdif(element, element2) % denominator))
                    if equal:
                        break
                if equal:
                    orbits[i] = orbits[i].union(orbits[j])
                    orbits[j] = set()
        ### ### delete empty orbits
        orbits = [orbit for orbit in orbits if len(orbit) > 0]
        ### ### select one point per orbit
        integer_coords = []
        for i, orbit in enumerate(orbits):
            integer_coords.append(sorted(orbit, reverse=True)[0])
        integer_coords = np.array(integer_coords, dtype=int)
        ### points_db
        points_db = cls._build_db(denominator, integer_coords, symmetry_repr)
        ### weights
        weights = cls._build_weights(denominator, integer_coords, points_db)

        return cls(
            basis_vectors=basis_vectors,
            denominator=denominator,
            integer_coords=integer_coords,
            points_db=points_db,
            weights=weights,
            special_points=special_points,
        )

    @classmethod
    def irreducible_sample(cls, name, basis_vectors, denominator):
        """Precompiled samples of the irreducible Wigner-Seitz cell for
        the most commmon lattices.

        Parameters
        ----------
        name : str
            name of the lattice. Implemented ones are:
            '2D_Hexagonal_D6' requires scalar denominator divisible by 6
            '2D_Hexagonal_D3_Axes' requires scalar denominator divisible by 6
            '2D_Square_D4' requires scalar denominator divisible by 2
            '2D_Rectangular_D2' requires denominator divisible by 2
        basis_vectors : 2D array of floats with shape
            [space_dimension, lattice_dimension]
            basis vectors used to represent samples. The components of
            the i-th vector are stored as basis_vectors[:,i].
            Must be compatible with the lattice chosen.
        denominator : integer or tuple of integers of length
            lattice_dimension.
            denominators used to express rational coordinates.
            Must match lattice-dependent conditions.
        Returns
        -------
        Unit_Cell_Sample
            The initialized sample.
        """
        basis_vectors = cls._check_input_vectors(basis_vectors)
        space_dimension, lattice_dimension = basis_vectors.shape
        denominator = cls._check_denominator(lattice_dimension, denominator)

        if name == "2D_Hexagonal_D6":
            assert lattice_dimension == 2
            assert space_dimension == 2
            assert all(ni == denominator[0] for ni in denominator)
            assert denominator[0] % 6 == 0
            assert np.allclose(
                lin.norm(basis_vectors[:, 0]), lin.norm(basis_vectors[:, 1])
            )
            if np.allclose(
                np.dot(basis_vectors[:, 0], basis_vectors[:, 1]),
                0.5 * lin.norm(basis_vectors[:, 0]) ** 2,
            ):
                wide_angle = False
            elif np.allclose(
                np.dot(basis_vectors[:, 0], basis_vectors[:, 1]),
                -0.5 * lin.norm(basis_vectors[:, 0]) ** 2,
            ):
                wide_angle = True
            else:
                raise ValueError("vectors not compatible with hexagonal symmetry")
            # create integer coords
            N = denominator[0]
            # These are valid if wide_config == False
            v1 = np.array(
                np.concatenate(
                    [
                        np.arange(j, N / 2 + 1 - np.ceil(j / 2), dtype=int)
                        for j in range(N // 3 + 1)
                    ]
                ),
                dtype=np.int32,
            )
            v2 = np.array(
                np.concatenate(
                    [
                        j * np.ones(int(N / 2 + 1 - np.ceil(j / 2) - j), dtype=int)
                        for j in range(N // 3 + 1)
                    ]
                ),
                dtype=np.int32,
            )
            # If wide_config = True (p, q) -> (p + q, q)
            if wide_angle:
                v1 += v2
            integer_coords = np.column_stack([v1, v2])
            # set point group and special points
            point_group = Point_Group.dihedral_group(n =6, theta0 = np.arctan2(basis_vectors[1, 0], basis_vectors[0, 0]) )
            special_points = {"$\Gamma$": (0, 0)}
            if wide_angle:
                special_points["$M$"] = (N // 2, 0)
                special_points["$K$"] = (2 * N // 3, N // 3)
            else:
                special_points["$M$"] = (N // 2, 0)
                special_points["$K$"] = (N // 3, N // 3)

        elif name == "2D_Hexagonal_D3_Axes":
            # checks hexagonal
            assert lattice_dimension == 2
            assert space_dimension == 2
            assert all(ni == denominator[0] for ni in denominator)
            assert denominator[0] % 6 == 0
            assert np.allclose(
                lin.norm(basis_vectors[:, 0]), lin.norm(basis_vectors[:, 1])
            )
            if np.allclose(
                np.dot(basis_vectors[:, 0], basis_vectors[:, 1]),
                0.5 * lin.norm(basis_vectors[:, 0]) ** 2,
            ):
                wide_angle = False
            elif np.allclose(
                np.dot(basis_vectors[:, 0], basis_vectors[:, 1]),
                -0.5 * lin.norm(basis_vectors[:, 0]) ** 2,
            ):
                wide_angle = True
            else:
                raise ValueError("vectors not compatible with hexagonal symmetry")
            # create integer coords
            N = denominator[0]  # Already checked to be uniform and multiple of 6
            idx_1 = np.concatenate(
                [
                    np.arange(j, N / 2 + 1 - np.ceil(j / 2), dtype=int)
                    for j in range(N // 3 + 1)
                ]
            )
            idx_1_nodiag = np.concatenate(
                [
                    np.arange(
                        j + 1, N / 2 + 1 - np.ceil(j / 2) - (j + 1) % 2, dtype=int
                    )
                    for j in range(N // 3)
                ]
            )
            idx_2 = np.concatenate(
                [
                    j * np.ones(int(N / 2 + 1 - np.ceil(j / 2) - j), dtype=int)
                    for j in range(N // 3 + 1)
                ]
            )
            idx_2_nodiag = np.concatenate(
                [
                    j
                    * np.ones(
                        int(N / 2 + 1 - np.ceil(j / 2) - j - 1 - (j + 1) % 2), dtype=int
                    )
                    for j in range(N // 3)
                ]
            )
            # There are duplicate points on the diagonal
            # These are valid if wide_config == False
            v1 = np.array(np.concatenate([idx_1, idx_2_nodiag]), dtype=np.int32)
            v2 = np.array(np.concatenate([idx_2, idx_1_nodiag]), dtype=np.int32)
            # If wide_config = True (p, q) -> (p + q, q)
            if wide_angle:
                v1 += v2
            integer_coords = np.column_stack([v1, v2])
            # set point group and special points
            point_group = Point_Group.dihedral_group( n =3,
                theta0=np.arctan2(basis_vectors[1, 0], basis_vectors[0, 0])
            )
            special_points = {"$\Gamma$": (0, 0), "$M$": (N // 2, 0)}
            if wide_angle:
                special_points["$M^\prime$"] = (N // 2, N // 2)
                special_points["$K$"] = (2 * N // 3, N // 3)

            else:
                special_points["$M^\prime$"] = (0, N // 2)
                special_points["$K$"] = (N // 3, N // 3)

        elif name == "2D_Square_D4":
            # checks square
            assert lattice_dimension == 2
            assert space_dimension == 2
            assert all(ni == denominator[0] for ni in denominator)
            assert denominator[0] % 2 == 0
            assert np.allclose(
                lin.norm(basis_vectors[:, 0]), lin.norm(basis_vectors[:, 1])
            )
            assert np.allclose(np.dot(basis_vectors[:, 0], basis_vectors[:, 1]), 0.0)
            # create integer coords
            N = denominator[0]  # Already checked to be uniform and multiple of 6
            v1 = np.concatenate(
                [np.arange(j, N // 2 + 1, dtype=int) for j in range(N // 2 + 1)]
            )
            v2 = np.concatenate(
                [j * np.ones([N // 2 + 1 - j], dtype=int) for j in range(N // 2 + 1)]
            )
            integer_coords = np.column_stack([v1, v2])
            # set point group and special points
            point_group = Point_Group.dihedral_group(n=4, 
                theta0=np.arctan2(basis_vectors[1, 0], basis_vectors[0, 0])
            )
            special_points = {
                "$\Gamma$": (0, 0),
                "$X$": (N // 2, 0),
                "$M$": (N // 2, N // 2),
            }

        elif name == "2D_Rectangular_D2":
            assert lattice_dimension == 2
            assert space_dimension == 2
            assert all(ni % 2 == 0 for ni in denominator)
            assert np.allclose(np.dot(basis_vectors[:, 0], basis_vectors[:, 1]), 0.0)
            # create integer coords
            v1 = np.concatenate(
                [
                    np.arange(0, denominator[0] // 2 + 1, dtype=int)
                    for j in range(denominator[1] // 2 + 1)
                ]
            )
            v2 = np.concatenate(
                [
                    j * np.ones([denominator[0] // 2 + 1], dtype=int)
                    for j in range(denominator[1] // 2 + 1)
                ]
            )
            integer_coords = np.column_stack([v1, v2])
            # set point group and special points
            point_group = Point_Group.dihedral_group(n=2,
                theta0=np.arctan2(basis_vectors[1, 0], basis_vectors[0, 0])
            )
            special_points = {"$\Gamma$": (0, 0)}

        else:
            raise ValueError

        symmetry_repr = point_group.integer_representation(basis_vectors)
        points_db = cls._build_db(denominator, integer_coords, symmetry_repr)
        weights = cls._build_weights(denominator, integer_coords, points_db)
        return cls(
            basis_vectors=basis_vectors,
            denominator=denominator,
            integer_coords=integer_coords,
            points_db=points_db,
            weights=weights,
            special_points=special_points,
        )

    ####### Properties #####################################################

    @property
    def cell_volume(self):
        return self._volume

    @cell_volume.setter
    def cell_volume(self, _):
        raise warn("Unit_Cell_Sample is read only")

    ###### Methods #########################################################

    def __call__(self, point):
        """
        Returns the decomposition of a generic vector q = R k + G
        with k in the unit cell, R a symmetry operation, G an integer
        combination of basis vectors.

        Parameters
        ----------
        point : tuple of ints of length lattice_dimension, or int,
        or sequence of ints of length 1, or str
            integer coords of the requested point
            or index of the point or string identifying a special point

        Returns
        -------
        dictionary
            dictionary containing the decomposition
        """
        integer_part = self.get_integer_part(point)
        fractional_part = self.get_fractional_part(point)
        d = self._points_db[fractional_part]
        return {
            "index": d["index"],
            "operation": d["operation"],
            "integer_part": tsum(integer_part, d["translation"]),
        }

    def __contains__(self, point):
        if (
            isinstance(point, tuple)
            and len(point) == self._lattice_dimension
            and all(isinstance(n, (int, np.integer)) for n in point)
        ):
            point = self.get_fractional_part(point)
        return Sample.__contains__(self, point)
    ########## Internal methods ############################################

    @classmethod
    def _build_db(cls, denominator, integer_coords, symmetry_repr):
        """Build the point database given the representation of the
        symmetry group."""
        db = {}
        for g in range(symmetry_repr.shape[0] - 1, -1, -1):
            for i, key in enumerate(integer_coords):
                # careful with transpose
                vector = symmetry_repr[g, :, :].T @ np.array(key, dtype=int)
                db[tmod(vector, denominator)] = {
                    "index": i,
                    "operation": g,
                    "translation": tneg(tint_div(vector, denominator)),
                }
        ### check that all the standard unit cell is covered
        standard_unit_cell = product(*[range(den) for den in denominator])
        for k in standard_unit_cell:
            assert k in db
        return db

    @classmethod
    def _build_weights(cls, denominator, integer_coords, points_db):
        """Build the weights given the point database."""
        integration_weights = np.zeros([len(integer_coords)], dtype=float)
        standard_unit_cell = product(*[range(den) for den in denominator])
        for k in standard_unit_cell:
            integration_weights[points_db[k]["index"]] += 1
        return integration_weights / np.prod(denominator)

    @classmethod
    def _wigner_seitz_points(cls, basis_vectors, denominator):
        space_dimension, lattice_dimension = basis_vectors.shape
        # cut_off = upper bound to the length of a vector that can be obtained by summing the basis vectors
        cut_off = (
            max([lin.norm(basis_vectors[:, i]) for i in range(lattice_dimension)])
            * lattice_dimension
        )
        # create sample of lattice vectors close to the origin
        nn = Sample.lattice_sample(basis_vectors, cut_off)
        tree = spa.KDTree(nn.coords)
        standard_unit_cell = product(*[range(0, den, 1) for den in denominator])
        integer_coords = np.zeros(
            [np.prod(denominator), basis_vectors.shape[1]], dtype=int
        )
        for j, k in enumerate(standard_unit_cell):
            v = nn.basis_vectors @ (k / denominator)
            index = tree.query(v)[1]
            integer_coords[j, :] = k - (nn.integer_coords[index] * denominator)

        return integer_coords


########################################################################

########################################################################
# To do list
# Clean load from file
# Implement gradients
# Implement interpolation
# Non-uniform samplings (Baldereschi points)
############### compare with this implementation ###############################
# class Irreducible_BZ_Sampling(Builder):
#     def __init__(self, reciprocal_vectors, n_sites, symmetry_group):
#         Builder.__init__(self, reciprocal_vectors, n_sites)
#         self._symmetry_group = symmetry_group
#     @property
#     def make(self):
#         warnings.warn("Highly experimental feature")
#         #Check reciprocal vectors and n_sites
#         reciprocal_vectors = self.reciprocal_vectors
#         n_sites = self.n_sites
#         #Get integer representations on group operator, get the trasnspose because
#         integer_representation = np.swapaxes(self._symmetry_group.integer_representation(reciprocal_vectors), 1,2)
#         #Create auxiliary full BZ sample with no symmetry specified
#         integer_coords = np.array(list(np.ndindex(n_sites)))
#         sample = Sample(reciprocal_vectors,integer_coords,n_sites)
#         #Transform the sample points with the symmetry group operations
#         integer_transformed = np.moveaxis(integer_representation@(sample.integer_coords.T), 1,2)
#         #Fold them back on the 1^st BZ
#         _, integer_folded = np.divmod(integer_transformed, np.array(n_sites, dtype=np.int32))
#         #Make an ndarray of ints with shape [k, R] of the index of the transformed vector q = Rk
#         index_table = np.empty(integer_folded.shape[0:2], dtype=np.int)
#         for pt_idx in np.ndindex(index_table.shape[0:2]):
#             index_table[pt_idx] = sample[tuple(integer_folded[pt_idx])]
#         index_table = index_table.T
#         #Permute sample points so to be ordered according to their norm
#         norms = lin.norm(sample.points, axis = 1)
#         min_dist = np.empty(len(index_table), np.int32)
#         for x_idx, x in enumerate(index_table):
#             temp_index_table = np.array(sorted(set(x)), np.int32)
#             temp_norms = norms[temp_index_table]
#             min_norm = np.argmin(temp_norms)
#             min_dist[x_idx] = temp_index_table[min_norm]
#         #Finally get the Irreducible BZ and integration weights
#         idxs, weights = np.unique(min_dist, return_counts=True)
#         return Sample(reciprocal_vectors, sample.integer_coords[idxs], n_sites, weights/np.sum(weights), self.signature)
#     @property
#     def signature(self):
#         return self._symmetry_group.__class__.__name__ + "_Irreducible_BZ"
