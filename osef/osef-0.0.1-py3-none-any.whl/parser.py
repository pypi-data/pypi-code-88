"""Functions to read and parse osef files/streams."""
import socket
import sys
import traceback
from collections import namedtuple, deque
from itertools import islice
from struct import Struct, error
from typing import Any, Iterable, Optional, Tuple, BinaryIO, Union, Iterator
from urllib.parse import urlparse

import numpy as np
from osef import types


# -- Public functions --


def open_osef(path: str) -> Union[BinaryIO, socket.socket, None]:
    """Open file path or tcp socket

    :param path: path to osef file or TCP stream if path has form *tcp://hostname:port*
    :return: opened osef file as a binaryIO or a socket (None if file/stream could not be opened)
    """
    parsed = urlparse(path)
    if path == "-":
        return sys.stdin.buffer
    elif parsed.scheme == "tcp":
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        while True:
            try:
                s.connect((parsed.hostname, parsed.port or 11120))
                break
            except ConnectionRefusedError:
                continue
        return s
    else:
        try:
            f = open(path, "rb")
            return f
        except:
            print(f"Cannot open file:{path}\n")
            return None


_Tlv = namedtuple("TLV", "type length value")


def iter_file(opened_file: BinaryIO) -> Iterator[_Tlv]:
    """Iterator function to iterate over each frame in osef file.

    :param opened_file: opened binary file containing tlv frames.
    :return frame_tlv: next tlv frame of the osef file.
    """
    while True:
        try:
            frame_tlv = _read_next_tlv(opened_file)
        except Exception:
            print(
                "Error: cannot read next Tlv from file (malformated Tlv?).\n"
                + f"Details: {traceback.format_exc()}"
                + "\n"
            )
            break
        if frame_tlv is None:
            break
        else:
            yield frame_tlv


def get_tlv_iterator(
    opened_file: BinaryIO, first: int = None, last: int = None
) -> Iterable[_Tlv]:
    """Get an iterator to iterate over each tlv frame in osef file.

    :param opened_file: opened binary file containing tlv frames.
    :param first: iterate only on N first frames of file.
    :param last: iterate only on M last frames of file. Can be used with first to get the range (N-M)..N
    :return: tlv frame iterator
    """
    if first is None and last is None:
        return enumerate(iter_file(opened_file))
    else:
        return deque(islice(enumerate(iter_file(opened_file)), first), last)


_TreeNode = namedtuple("TreeNode", "type children leaf_value")


def build_tree(tlv: _Tlv) -> _TreeNode:
    """Recursive function to get a tree from a raw Tlv frame

    :param tlv: raw tlv frame read from file.
    :return: tree representation of the tlv frame
    """
    # If we know this type is an internal node (not a leaf)
    if tlv.type in types.outsight_types and isinstance(
        types.outsight_types[tlv.type].node_info, types.InternalNodeInfo
    ):
        read = 0
        children = []
        while read < tlv.length:
            sub_tlv, sub_size = _parse_tlv_from_blob(tlv.value, read)
            sub_tree = build_tree(sub_tlv)
            children.append(sub_tree)
            read += sub_size
        return _TreeNode(tlv.type, children, None)
    else:
        return _TreeNode(tlv.type, None, tlv.value)


def unpack_value(value: bytes, leaf_info: types.LeafInfo) -> Any:
    """Unpack a leaf value to a python object (type depends on type of leaf).

    :param value: binary value to be unpacked.
    :param leaf_info: type info for unpacking and conversion to python object.
    :return: python object
    """
    try:
        if leaf_info.leaf_type == types.LeafType.Value:
            pack_format = leaf_info.format_info
            return (Struct(pack_format).unpack(value))[0]

        elif leaf_info.leaf_type == types.LeafType.Array:
            dtype = leaf_info.format_info
            return np.frombuffer(value, dtype=dtype)

        elif leaf_info.leaf_type == types.LeafType.Bytes:
            return value

        elif leaf_info.leaf_type == types.LeafType.StructuredArray:
            dtype = leaf_info.format_info
            array = np.frombuffer(value, dtype=dtype)
            names = array.dtype.names
            if "__todrop" in names:
                names.remove("__todrop")
                array = array[names]
            return array

        elif leaf_info.leaf_type == types.LeafType.Dict:
            pack_format, fields_name = leaf_info.format_info
            array = list(Struct(pack_format).iter_unpack(value))
            return dict(zip(fields_name, array[0]))

        elif leaf_info.leaf_type == types.LeafType.String:
            return value.decode("ascii")[:-1]

        elif leaf_info.leaf_type == types.LeafType.Custom:
            return leaf_info.format_info(value)

        else:  # including LeafType.Unknown
            return value

    except error:
        return value


def parse_to_dict(frame_tree: _TreeNode) -> dict:
    """Parse a whole frame tree to a python dictionary. All values of the tree will be unpacked.

    :param frame_tree: raw tree of a tlv frame.
    :return: dictionary with all values in osef frame.
    """
    type_name, subtree = _parse_raw_to_tuple(frame_tree)
    return {type_name: subtree}


def parse(
    path: str, first: Optional[int] = None, last: Optional[int] = None
) -> Iterator[dict]:
    """Iterator that opens and convert each tlv frame to a dict.

    :param path: path to osef file or TCP stream if path has form *tcp://hostname:port*
    :param first: iterate only on N first frames of file.
    :param last: iterate only on M last frames of file. Can be used with first to get the range (N-M)..N
    :return: next tlv dictionary
    """
    f = open_osef(path)
    if not f:
        raise FileNotFoundError(f"Can't open file/stream from provided path: {path}")
    iterator = get_tlv_iterator(f, first, last)
    for idx, tlv in iterator:
        raw_tree = build_tree(tlv)
        if raw_tree:
            yield parse_to_dict(raw_tree)
    f.close()


# -- Tlv Parsing --

# Structure Format definition (see https://docs.python.org/3/library/struct.html#format-strings):
# Meant to be used as: _STRUCT_FORMAT % length
_STRUCT_FORMAT = "<"  # little endian
_STRUCT_FORMAT += "L"  # unsigned long        (field 'T' ie. 'Type')
_STRUCT_FORMAT += "L"  # unsigned long        (field 'L' ie. 'Length')
_STRUCT_FORMAT += "%ds"  # buffer of fixed size (field 'V' ie. 'Value')


def _align_size(size: int) -> int:
    """Returned aligned size from tlv size"""
    alignment_size = 4
    n = size % alignment_size
    return size if n == 0 else size + alignment_size - n


# Add read method to socket to get same API as file
setattr(socket.socket, "read", lambda self, size=4096: self.recv(size))


def _read_from_file(f: BinaryIO, n: int) -> bytes:
    """Read given number of bytes from readable stream"""
    blob = b""
    while len(blob) < n:
        blob_inc = f.read(n - len(blob))

        # End of file
        if blob_inc is None or len(blob_inc) == 0:
            raise EOFError

        blob += blob_inc

    return blob


def _read_next_tlv(f: BinaryIO) -> Optional[_Tlv]:
    """Read the next TLV from a binary stream (file or socket)"""
    # Read header
    struct = Struct(_STRUCT_FORMAT % 0)
    try:
        blob = _read_from_file(f, struct.size)
    except EOFError:
        return None

    # Parse Type and Length
    read_tlv = _Tlv._make(struct.unpack_from(blob))

    # Now that we know its length we can read the Value
    struct = Struct(_STRUCT_FORMAT % read_tlv.length)
    blob += _read_from_file(f, struct.size - len(blob))
    read_tlv = _Tlv._make(struct.unpack_from(blob))

    return read_tlv


def _parse_tlv_from_blob(blob: bytes, offset=0) -> Tuple[_Tlv, int]:
    """Parse a TLV from a binary blob"""
    # Unpack a first time to get Type and Length
    struct = Struct(_STRUCT_FORMAT % 0)
    read_tlv = _Tlv._make(struct.unpack_from(blob, offset))

    # Then unpack the whole tlv
    struct = Struct(_STRUCT_FORMAT % read_tlv.length)
    read_tlv = _Tlv._make(struct.unpack_from(blob, offset))

    return read_tlv, _align_size(struct.size)


# -- OSEF parsed tree --


def _parse_raw_to_tuple(raw_tree: _TreeNode) -> Tuple[str, Any]:
    """Parse a raw TLV tree, using OSEF types"""
    t, children, leaf_value = raw_tree

    # Get leaf type info
    type_info = types.outsight_type_info(t)

    # For leaves or unknown, return value
    if isinstance(type_info.node_info, types.LeafInfo):
        return type_info.name, unpack_value(leaf_value, type_info.node_info)

    # For non-leaves, add each children to a dictionary
    tree = {}
    zone_list = []
    for child in children:
        child_name, child_tree = _parse_raw_to_tuple(child)
        if type_info.node_info.type == list:
            zone_list.append(child_tree)
            tree = zone_list
        elif type_info.node_info.type == dict:
            tree[child_name] = child_tree
        else:
            raise ValueError("Unsupported internal node type.")
    return type_info.name, tree
