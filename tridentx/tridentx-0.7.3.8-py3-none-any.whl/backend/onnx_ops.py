import numbers

import numpy as np
import onnx
from onnx import shape_inference, OperatorSetIdProto, AttributeProto, TensorProto,ModelProto
from onnx import helper, numpy_helper,onnx_pb, defs, numpy_helper, __version__

from onnx import optimizer
from trident.backend.common import unpack_singleton,make_sure
__all__ = ['Tensor','find_opset','make_name','port_name','is_onnx_domain','are_shapes_equal','are_shapes_compatible']

Tensor=TensorProto

TRIDENT_PACKAGE_NAME = __name__.split('.')[0]

# Built-in supported domains
ONNX_DOMAIN = ""
AI_ONNX_ML_DOMAIN = "ai.onnx.ml"
MICROSOFT_DOMAIN = "com.microsoft"
CONTRIB_OPS_DOMAIN = "ai.onnx.contrib"

# Default opset version for onnx domain
PREFERRED_OPSET = 9

# Default opset for custom ops
TRIDENT_OPSET = helper.make_opsetid("ai.onnx.converters.trident", 1)

# Target for the generated onnx graph. It possible targets:
# onnx-1.1 = onnx at v1.1 (winml in rs4 is based on this)
# caffe2 = include some workarounds for caffe2 and winml
TARGET_RS4 = "rs4"
TARGET_RS5 = "rs5"
TARGET_RS6 = "rs6"
TARGET_CAFFE2 = "caffe2"
POSSIBLE_TARGETS = [TARGET_RS4, TARGET_RS5, TARGET_RS6, TARGET_CAFFE2]
DEFAULT_TARGET = []

NCHW_TO_NHWC = [0, 2, 3, 1]
NHWC_TO_NCHW = [0, 3, 1, 2]
HWCN_TO_NCHW = [3, 2, 0, 1]
NCHW_TO_HWCN = [2, 3, 1, 0]



# Mapping opset to IR version.
# Note: opset 7 and opset 8 came out with IR3 but we need IR4 because of PlaceholderWithDefault
OPSET_TO_IR_VERSION = {
    1: 3, 2: 3, 3: 3, 4: 3, 5: 3, 6: 3, 7: 4, 8: 4, 9: 4, 10: 5, 11: 6, 12: 7, 13: 7
}

ONNX_TO_NUMPY_DTYPE = {
    onnx_pb.TensorProto.FLOAT: np.float32,
    onnx_pb.TensorProto.FLOAT16: np.float16,
    onnx_pb.TensorProto.DOUBLE: np.float64,
    onnx_pb.TensorProto.INT32: np.int32,
    onnx_pb.TensorProto.INT16: np.int16,
    onnx_pb.TensorProto.INT8: np.int8,
    onnx_pb.TensorProto.UINT8: np.uint8,
    onnx_pb.TensorProto.UINT16: np.uint16,
    onnx_pb.TensorProto.INT64: np.int64,
    onnx_pb.TensorProto.UINT64: np.uint64,
    onnx_pb.TensorProto.BOOL: np.bool,
    onnx_pb.TensorProto.COMPLEX64: np.complex64,
    onnx_pb.TensorProto.COMPLEX128: np.complex128,
    onnx_pb.TensorProto.STRING: np.object,
}

#
#  onnx dtype names
#
ONNX_DTYPE_NAMES = {
    onnx_pb.TensorProto.FLOAT: "float",
    onnx_pb.TensorProto.FLOAT16: "float16",
    onnx_pb.TensorProto.DOUBLE: "double",
    onnx_pb.TensorProto.INT32: "int32",
    onnx_pb.TensorProto.INT16: "int16",
    onnx_pb.TensorProto.INT8: "int8",
    onnx_pb.TensorProto.UINT8: "uint8",
    onnx_pb.TensorProto.UINT16: "uint16",
    onnx_pb.TensorProto.INT64: "int64",
    onnx_pb.TensorProto.STRING: "string",
    onnx_pb.TensorProto.BOOL: "bool",
    onnx_pb.TensorProto.COMPLEX64: "complex64",
    onnx_pb.TensorProto.COMPLEX128: "complex128"
}


ONNX_UNKNOWN_DIMENSION = -1
ONNX_EMPTY_INPUT = ""

# index for internally generated names
INTERNAL_NAME = 1

# Fake onnx op type which is used for Graph input.
GRAPH_INPUT_TYPE = "NON_EXISTENT_ONNX_TYPE"

def make_name(name):
    """Make op name for inserted ops."""
    global INTERNAL_NAME
    INTERNAL_NAME += 1
    return "{}__{}".format(name, INTERNAL_NAME)

def port_name(name, nr=0):
    """Map node output number to name."""
    return name + ":" + str(nr)


def is_unknown_dimension(dim):
    """  Return true if dim is not a positive integer value. """
    if dim is None or not isinstance(dim, int):
        return True
    return dim <= 0

def merge_shapes(shape1, shape2):
    """
    Merge 2 shapes, return merged shape, choose more specific dimension value from either side.
    Raise exception for mismatch.
    """
    if shape1 is None:
        return shape2
    if shape2 is None:
        return shape1

    make_sure(isinstance(shape1,(tuple,list)), "invalid type for shape1")
    make_sure(isinstance(shape2,(tuple,list)), "invalid type for shape2")
    make_sure(len(shape1) == len(shape2), "shapes rank mismatch: shape1=%s, shape2=%s", shape1, shape2)

    merged = []
    for d1, d2 in zip(shape1, shape2):
        d = d1
        if is_unknown_dimension(d1):
            d = d2
        elif not is_unknown_dimension(d2):
            make_sure(d1 == d2, "shapes dimension mismatch: shape1=%s, shape2=%s", shape1, shape2)
        merged.append(d)
    return merged

def are_shapes_compatible(src, dest):
    """
    Returns True iff src is compatible with dest.
    None is compatible with all shapes, different ranks are not considered as compatible
    """
    try:
        merge_shapes(src, dest)
        return True
    except:  # pylint: disable=bare-except
        return False


def are_shapes_equal(src, dest):
    """ Check whether 2 shapes are equal. """
    if src is None:
        return dest is None
    if dest is None:
        return src is None

    make_sure(isinstance(src,(tuple,list)), "invalid type for src")
    make_sure(isinstance(dest,(tuple,list)), "invalid type for dest")

    if len(src) != len(dest):
        return False
    return all(i == j for i, j in zip(src, dest))

def map_numpy_to_onnx_dtype(np_dtype):
    for onnx_dtype, numpy_dtype in ONNX_TO_NUMPY_DTYPE.items():
        if numpy_dtype == np_dtype:
            return onnx_dtype
    raise ValueError("unsupported numpy dtype '%s' for mapping to onnx" % np_dtype)


def map_onnx_to_numpy_type(onnx_type):
    return ONNX_TO_NUMPY_DTYPE[onnx_type]


def node_name(name):
    """Get node name without io#."""
    pos = name.find(":")
    if pos >= 0:
        return name[:pos]
    return name

def find_opset(opset):
    """Find opset."""
    if opset is None or opset == 0:
        opset = defs.onnx_opset_version()
        if opset > PREFERRED_OPSET:
            # if we use a newer onnx opset than most runtimes support, default to the one most supported
            opset = PREFERRED_OPSET
    return opset

def is_onnx_domain(domain):
    if domain is None or domain == "":
        return True
    return False


def to_numpy(*x) -> np.ndarray:
    """Convert whatever to numpy array

    Args:
        x (List, tuple, tensor or numpy array): whatever you want to convert to numpy ndarray.

    Returns:
        a numpy ndarray

    Examples:
        >>> to_numpy(5)
        array([5])
        >>> to_numpy([1,2,3])
        array([1, 2, 3])
        >>> to_numpy((2,4),(1,3))
        array([[2, 4],
           [1, 3]])

    """
    x = unpack_singleton(x)
    if isinstance(x, np.ndarray):
        return x
    elif x is None:
        return None
    elif isinstance(x, Tensor):
        return numpy_helper.to_array(x)
    elif isinstance(x, list):
        return np.asarray(x)
    elif isinstance(x, tuple):
        return np.asarray(list(x))
    elif isinstance(x,numbers.Number):
        return np.asarray([x])
    else:
        raise ValueError("Unsupported type")


def to_tensor(x, dtype=None,device=None, requires_grad=None) -> Tensor:
    """ Convert input  to a tensor as possible

    Args:
        x: An object to be converted (ex.numpy array, list, tensors).
        dtype (str or torch.dtype):
        device (str or torch.device):
        requires_grad (None or bool): whether need grade

    Returns:
        A tensor.

    Examples:
        >>> to_tensor(2)
        tensor(2, dtype=torch.int32)
        >>> to_tensor([1.0,2.0,3.0],requires_grad=True)
        tensor([1., 2., 3.], requires_grad=True)
        >>> to_tensor([1.0,2.0,3.0],requires_grad=False)
        tensor([1., 2., 3.])
        >>> to_tensor([1.0,2.0,3.0])
        tensor([1., 2., 3.])
        >>> to_tensor((1.0,2.0,3.0))
        tensor([1., 2., 3.])
        >>> to_tensor(np.arange(0,5))
        tensor([0, 1, 2, 3, 4])

    """

    if isinstance(x, Tensor):
        return x
    else:
        if isinstance(x, int):
            return numpy_helper.from_array(np.array([x],dtype=np.int64))
        elif isinstance(x, float):
            return numpy_helper.from_array(np.array([x],dtype=np.float32))
        elif isinstance(x, (list, tuple)):
            if all([isinstance(item,numbers.Integral) for item in x]):
                return numpy_helper.from_array(np.array(x,dtype=np.int64))
            else:
                return numpy_helper.from_array(np.array([x], dtype=np.float32))
        elif isinstance(x, np.ndarray):
            x = numpy_helper.from_array(x)
            return x
        else:
            return x
