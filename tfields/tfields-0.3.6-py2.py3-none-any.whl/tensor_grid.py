import numpy as np
from .lib import grid
from .core import TensorFields


class TensorGrid(TensorFields):
    """
    A Tensor Grid is a TensorField which is aware of it's grid nature, which is order of iteration
    (iter-order) over the base vectors (base_vectors).

    Args:
        *base_vectors (tuple): indices of the axes which should be iterated
        **kwargs:
            iter_order (np.array): index order of building the grid.
            further: see TensorFields class
    """

    __slots__ = ["coord_sys", "name", "fields", "base_vectors", "iter_order"]
    __slot_setters__ = TensorFields.__slot_setters__ + [
        None,
        None,
    ]

    def __new__(cls, tensors, *fields, **kwargs):
        if issubclass(type(tensors), TensorGrid):
            default_base_vectors = tensors.base_vectors
            default_iter_order = tensors.iter_order
        else:
            default_base_vectors = kwargs.pop("base_vectors", None)
            default_iter_order = np.arange(len(default_base_vectors))
        base_vectors = kwargs.pop("base_vectors", default_base_vectors)
        iter_order = kwargs.pop("iter_order", default_iter_order)
        base_vectors = grid.ensure_complex(*base_vectors)
        obj = super(TensorGrid, cls).__new__(cls, tensors, *fields, **kwargs)
        obj.base_vectors = base_vectors
        obj.iter_order = iter_order
        return obj

    @classmethod
    def from_base_vectors(cls, *base_vectors, tensors=None, fields=None, **kwargs):
        iter_order = kwargs.pop("iter_order", np.arange(len(base_vectors)))
        if tensors is None:
            tensors = TensorFields.grid(*base_vectors, iter_order=iter_order, **kwargs)
        obj = cls(tensors, base_vectors=base_vectors, iter_order=iter_order)
        if fields:
            obj.fields = fields
        return obj

    @classmethod
    def empty(cls, *base_vectors, **kwargs):
        base_vectors = grid.ensure_complex(*base_vectors)
        bv_lengths = [int(bv[2].imag) for bv in base_vectors]
        tensors = np.empty(shape=(np.prod(bv_lengths), 0))

        return cls.from_base_vectors(*base_vectors, tensors=tensors, **kwargs)

    @classmethod
    def merged(cls, *objects, **kwargs):
        if "base_vectors" not in kwargs:
            base_vectors = None
            for obj in objects:
                if base_vectors is None:
                    base_vectors = obj.base_vectors
                else:
                    if not all(
                        [a == b for a, b in zip(base_vectors, obj.base_vectors)]
                    ):
                        raise NotImplementedError("Non-alligned base vectors")
            kwargs.setdefault("base_vectors", base_vectors)
        merge = super().merged(*objects, **kwargs)
        return merge

    @property
    def rank(self):
        if self.is_empty():
            return 1
        return super().rank

    def is_empty(self):
        return 0 in self.shape

    def explicit(self):
        """
        Build the grid explicitly (e.g. after changing base_vector, iter_order or init with empty)
        """
        kwargs = {attr: getattr(self, attr) for attr in self.__slots__}
        base_vectors = kwargs.pop("base_vectors")
        return self.from_base_vectors(*base_vectors, **kwargs)

    def change_iter_order(self, iter_order):
        bv_lengths = [int(bv[2].imag) for bv in self.base_vectors]
        field_swap_indices = grid.change_iter_order(
            bv_lengths, self.iter_order, iter_order
        )
        for field in self.fields:
            field[:] = field[field_swap_indices]
        self.iter_order = iter_order
        self[:] = self.explicit()
