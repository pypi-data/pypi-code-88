import ctypes as C
import ctypes.util
from enum import IntEnum, IntFlag
from typing import Any, ByteString, Callable, Generic, Optional, Sequence, TypeVar, TYPE_CHECKING
from dataclasses import dataclass

_libc_name = C.util.find_library('c')
if _libc_name is None:
    raise Exception
else:
    _libc = C.cdll.LoadLibrary(_libc_name)

if TYPE_CHECKING:
    Pointer = C.pointer
else:
    class _Pointer:
        def __getitem__(self, k):
            return None
    Pointer = _Pointer()

_Match_event_handler = C.CFUNCTYPE(C.c_int,
    C.c_uint,
    C.c_ulonglong,
    C.c_ulonglong,
    C.c_uint,
    C.c_void_p,
)

T = TypeVar('T')
class ManagedPtr(Generic[T]):
    def __init__(self, obj: T, free=_libc.free) -> None:
        self._object = obj
        self._free = free

    def __del__(self):
        if self._object is not None:
            self._free(C.byref(self._object))
            self._object = None

    def consume(self) -> T:
        if self._object is None:
            raise ValueError
        try:
            return self._object
        finally:
            self._object = None

    @property
    def contents(self) -> T:
        if self._object is None:
            raise ValueError
        return self._object

    @property
    def _as_parameter_(self):
        if self._object is None:
            raise ValueError
        return C.byref(self._object)

class HsError(IntEnum):
    SUCCESS = 0
    INVALID = -1
    NOMEM = -2
    SCAN_TERMINATED = -3
    COMPILER_ERROR = -4
    DB_VERSION_ERROR = -5
    DB_PLATFORM_ERROR = -6
    DB_MODE_ERROR = -7
    BAD_ALIGN = -8
    BAD_ALLOC = -9
    SCRATCH_IN_USE = -10
    ARCH_ERROR = -11
    INSUFFICIENT_SPACE = -12
    UNKNOWN_ERROR = -13

class HsExtFlag(IntFlag):
    MIN_OFFSET = 1
    MAX_OFFSET = 2
    MIN_LENGHT = 4
    EDIT_DISTANCE = 8
    HAMMING_DISTANCE = 16

class HsFlag(IntFlag):
    CASELESS = 1
    DOTALL = 2
    MULTILINE = 4
    SINGLEMATCH = 8
    ALLOWEMPTY = 16
    UTF8 = 32
    UCP = 64
    PREFILTER = 128
    SOM_LEFTMOST = 256
    COMBINATION = 512
    QUIET = 1024

class HsMode(IntFlag):
    BLOCK = 1
    NOSTREAM = BLOCK
    STREAM = 2
    VECTORED = 4
    SOM_HORIZON_LARGE = 1 << 24
    SOM_HORIZON_MEDIUM = 1 << 25
    SOM_HORIZON_SMALL = 1 << 26

class HsCpuFeatures(IntFlag):
    AVX2 = 1 << 2
    AVX512 = 1 << 3
    AVX512VBMI = 1 << 4

class HsTune(IntEnum):
    GENERIC = 0
    SNB = 1
    IVB = 2
    HSW = 3
    SLM = 4
    BDW = 5
    SKL = 6
    SKX = 7
    GLM = 8
    ICL = 9
    ICX = 10

@dataclass(frozen=True)
class HsPlatformInfo:
    tune: HsTune = HsTune.GENERIC
    cpu_features: int = 0

    def __post_init__(self):
        object.__setattr__(self, '_as_parameter_', C.byref(hs_platform_info(tune=self.tune, cpu_features=self.cpu_features)))

@dataclass(frozen=True)
class HsExprExt:
    min_offset: Optional[int] = None
    max_offset: Optional[int] = None
    min_length: Optional[int] = None
    edit_distance: Optional[int] = None
    hamming_distance: Optional[int] = None

    def __post_init__(self):
        obj = hs_expr_ext()
        if self.min_offset is not None:
            obj.min_offset = self.min_offset
            obj.flags |= HsExtFlag.MIN_OFFSET
        if self.min_offset is not None:
            obj.min_offset = self.min_offset
            obj.flags |= HsExtFlag.MIN_OFFSET
        if self.min_offset is not None:
            obj.min_offset = self.min_offset
            obj.flags |= HsExtFlag.MIN_OFFSET
        if self.min_offset is not None:
            obj.min_offset = self.min_offset
            obj.flags |= HsExtFlag.MIN_OFFSET
        if self.min_offset is not None:
            obj.min_offset = self.min_offset
            obj.flags |= HsExtFlag.MIN_OFFSET
        object.__setattr__(self, '_as_parameter_', obj)

class hs_compile_error(C.Structure):
    _fields_ = [
        ('message', C.c_char_p),
        ('expression', C.c_int),
    ]

class hs_platform_info(C.Structure):
    _fields_ = [
        ('tune', C.c_uint),
        ('cpu_features', C.c_ulonglong),
        ('reserved1', C.c_ulonglong),
        ('reserved2', C.c_ulonglong),
    ]

class hs_expr_info(C.Structure):
    _fields_ = [
        ('min_width', C.c_uint),
        ('max_width', C.c_uint),
        ('unordered_matches', C.c_byte),
        ('matches_at_eod', C.c_byte),
        ('matches_only_at_eod', C.c_byte),
    ]

class hs_expr_ext(C.Structure):
    _fields_ = [
        ('flags', C.c_ulonglong),
        ('min_offset', C.c_ulonglong),
        ('max_offset', C.c_ulonglong),
        ('min_length', C.c_ulonglong),
        ('edit_distance', C.c_uint),
        ('hamming_distance', C.c_uint),
    ]

class hs_database(C.Structure):
    pass

class hs_stream(C.Structure):
    pass

class hs_scratch(C.Structure):
    pass

class HyperscanError(Exception):
    def __init__(self, code: HsError, error: Optional[hs_compile_error] = None):
        self.code = code
        if error is not None:
            self.message = error.message.decode()
            self.expression = error.expression
        else:
            self.message = None
            self.expression = -1

    def __str__(self):
        if self.message is not None:
            return f"{self.code.name}: {self.message}"
        else:
            return self.code.name

class HsApi:
    def __init__(self, sofile):
        hs = self._hs = C.cdll.LoadLibrary(sofile)

        self.hs_compile: Callable[
            [
                str,
                int,
                int,
                C.POINTER[hs_platform_info],
                C.POINTER[C.POINTER[hs_database]],
                C.POINTER[C.POINTER[hs_compile_error]],
            ],
            HsError
        ]
        self.hs_compile = hs.hs_compile
        self.hs_compile.argtypes = [
            C.c_char_p,
            C.c_uint,
            C.c_uint,
            C.POINTER(hs_platform_info),
            C.POINTER(C.POINTER(hs_database)),
            C.POINTER(C.POINTER(hs_compile_error))
        ]
        self.hs_compile.restype = HsError

        self.hs_compile_multi = hs.hs_compile_multi
        self.hs_compile_multi.argtypes = [
            C.POINTER(C.c_char_p),
            C.POINTER(C.c_uint),
            C.POINTER(C.c_uint),
            C.c_uint,
            C.c_uint,
            C.POINTER(hs_platform_info),
            C.POINTER(C.POINTER(hs_database)),
            C.POINTER(C.POINTER(hs_compile_error)),
        ]
        self.hs_compile_multi.restype = HsError

        self.hs_compile_ext_multi = hs.hs_compile_ext_multi
        self.hs_compile_ext_multi.argtypes = [
            C.POINTER(C.c_char_p),
            C.POINTER(C.c_uint),
            C.POINTER(C.c_uint),
            C.POINTER(C.POINTER(hs_expr_ext)),
            C.c_uint,
            C.c_uint,
            C.POINTER(hs_platform_info),
            C.POINTER(C.POINTER(hs_database)),
            C.POINTER(C.POINTER(hs_compile_error)),
        ]
        self.hs_compile_ext_multi.restype = HsError

        self.hs_compile_lit = hs.hs_compile_lit
        self.hs_compile_lit.argtypes = [
            C.c_char_p,
            C.c_uint,
            C.c_uint,
            C.POINTER(hs_platform_info),
            C.POINTER(C.POINTER(hs_database)),
            C.POINTER(C.POINTER(hs_compile_error))
        ]
        self.hs_compile_lit.restype = HsError

        self.hs_compile_lit_multi = hs.hs_compile_lit_multi
        self.hs_compile_lit_multi.argtypes = [
            C.POINTER(C.c_char_p),
            C.POINTER(C.c_uint),
            C.POINTER(C.c_uint),
            C.c_uint,
            C.c_uint,
            C.POINTER(hs_platform_info),
            C.POINTER(C.POINTER(hs_database)),
            C.POINTER(C.POINTER(hs_compile_error)),
        ]
        self.hs_compile_lit_multi.restype = HsError

        self.hs_free_compile_error = hs.hs_free_compile_error
        self.hs_free_compile_error.argtypes = [C.POINTER(hs_compile_error)]
        self.hs_free_compile_error.restype = HsError

        self.hs_expression_info = hs.hs_expression_info
        self.hs_expression_info.argtypes = [
            C.c_char_p,
            C.c_uint,
            C.POINTER(C.POINTER(hs_expr_info)),
            C.POINTER(C.POINTER(hs_compile_error)),
        ]
        self.hs_expression_info.restype = HsError

        self.hs_expression_ext_info = hs.hs_expression_ext_info
        self.hs_expression_ext_info.argtypes = [
            C.c_char_p,
            C.c_uint,
            C.POINTER(hs_expr_ext),
            C.POINTER(C.POINTER(hs_expr_info)),
            C.POINTER(C.POINTER(hs_compile_error)),
        ]
        self.hs_expression_ext_info.restype = HsError

        self.hs_free_database = hs.hs_free_database
        self.hs_free_database.argtypes = [C.POINTER(hs_database)]
        self.hs_free_database.restype = HsError

        self.hs_serialize_database = hs.hs_serialize_database
        self.hs_serialize_database.argtypes = [
            C.POINTER(hs_database),
            C.POINTER(C.POINTER(C.c_char)),
            C.POINTER(C.c_size_t),
        ]
        self.hs_serialize_database.restype = HsError

        self.hs_deserialize_database = hs.hs_deserialize_database
        self.hs_deserialize_database.argtypes = [
            C.POINTER(C.c_char),
            C.c_size_t,
            C.POINTER(C.POINTER(hs_database)),
        ]
        self.hs_deserialize_database.restype = HsError

        self.hs_database_info = hs.hs_database_info
        self.hs_database_info.argtypes = [C.POINTER(hs_database), C.POINTER(C.c_char_p)]
        self.hs_database_info.restype = HsError

        self.hs_serialized_database_info = hs.hs_serialized_database_info
        self.hs_serialized_database_info.argtypes = [C.POINTER(C.c_char), C.c_size_t, C.POINTER(C.c_char_p)]
        self.hs_serialized_database_info.restype = HsError

        self.hs_alloc_scratch = hs.hs_alloc_scratch
        self.hs_alloc_scratch.argtypes = [C.POINTER(hs_database), C.POINTER(C.POINTER(hs_scratch))]
        self.hs_alloc_scratch.restype = HsError

        self.hs_free_scratch = hs.hs_free_scratch
        self.hs_free_scratch.argtypes = [C.POINTER(hs_scratch)]
        self.hs_free_scratch.restype = HsError

        self.hs_scan = hs.hs_scan
        self.hs_scan.argtypes = [
            C.POINTER(hs_database),
            C.POINTER(C.c_char),
            C.c_uint,
            C.c_uint,
            C.POINTER(hs_scratch),
            _Match_event_handler,
            C.c_void_p,
        ]
        self.hs_scan.restype = HsError


    def _check_error(self, code: HsError, error: Optional[Pointer[hs_compile_error]] = None) -> None:
        if code == HsError.SUCCESS:
            return
        if error is not None:
            exc = HyperscanError(code, error.contents)
            self.hs_free_compile_error(error)
        else:
            exc = HyperscanError(code)
        raise exc

    def compile(
            self,
            expression: ByteString,
            flags: int,
            mode: int,
            platform: HsPlatformInfo,
    ) -> ManagedPtr[hs_database]:
        db_ptr = C.POINTER(hs_database)()
        err_ptr = C.POINTER(hs_compile_error)()
        error = self.hs_compile(expression, flags, mode, platform, C.byref(db_ptr), C.byref(err_ptr))
        self._check_error(error, err_ptr)
        return ManagedPtr(db_ptr.contents, free=self.hs_free_database)

    def compile_multi(
            self,
            expressions: Sequence[ByteString],
            flags: Sequence[int],
            ids: Sequence[int],
            mode: int,
            platform: HsPlatformInfo,
    ) -> ManagedPtr[hs_database]:
        if not (len(expressions) == len(flags) == len(ids)):
            raise ValueError("expressions, flags and ids must have equal length")
        db_ptr = C.POINTER(hs_database)()
        err_ptr = C.POINTER(hs_compile_error)()
        expressions_ary = (C.c_char_p * len(expressions))(*expressions)
        flags_ary = (C.c_uint * len(flags))(*flags)
        ids_ary = (C.c_uint * len(ids))(*ids)
        error = self.hs_compile_multi(expressions_ary, flags_ary, ids_ary, len(ids), mode, platform, C.byref(db_ptr), C.byref(err_ptr))
        self._check_error(error, err_ptr)
        return ManagedPtr(db_ptr.contents, free=self.hs_free_database)

    def compile_ext_multi(
            self,
            expressions: Sequence[ByteString],
            flags: Sequence[int],
            ids: Sequence[int],
            exts: Sequence[HsExprExt],
            mode: int,
            platform: HsPlatformInfo,
    ) -> ManagedPtr[hs_database]:
        if not (len(expressions) == len(flags) == len(ids) == len(exts)):
            raise ValueError("expressions, flags, ids and exts must have equal length")
        db_ptr = C.POINTER(hs_database)()
        err_ptr = C.POINTER(hs_compile_error)()
        expressions_ary = (C.c_char_p * len(expressions))(*expressions)
        flags_ary = (C.c_uint * len(flags))(*flags)
        ids_ary = (C.c_uint * len(ids))(*ids)
        exts_ary = (C.POINTER(hs_expr_ext) * len(exts))(*(C.pointer(item._as_parameter_) if item is not None else None for item in exts))
        error = self.hs_compile_ext_multi(expressions_ary, flags_ary, ids_ary, exts_ary, len(ids), mode, platform, C.byref(db_ptr), C.byref(err_ptr))
        self._check_error(error, err_ptr)
        return ManagedPtr(db_ptr.contents, free=self.hs_free_database)

    def serialize_database(
            self,
            database: ManagedPtr[hs_database],
    ) -> bytearray:
        data_ptr = C.POINTER(C.c_char)()
        length = C.c_size_t()
        error = self.hs_serialize_database(database, C.byref(data_ptr), C.byref(length))
        self._check_error(error)
        array = C.cast(data_ptr, C.POINTER(C.c_char * length.value))
        return bytearray(array.contents)

    def deserialize_database(
            self,
            data: ByteString,
    ) -> ManagedPtr[hs_database]:
        if not isinstance(data, bytearray):
            data = bytearray(data)
        db_ptr = C.POINTER(hs_database)()
        c_data = C.c_char.from_buffer(data)
        error = self.hs_deserialize_database(C.byref(c_data), len(data), C.byref(db_ptr))
        self._check_error(error)
        return ManagedPtr(db_ptr.contents)

    def database_info(
            self,
            database: ManagedPtr[hs_database],
    ) -> str:
        str_ptr = C.c_char_p()
        error = self.hs_database_info(database, C.byref(str_ptr))
        self._check_error(error)
        str_value = str_ptr.value.decode()
        _libc.free(str_ptr)
        return str_value

    def serialized_database_info(
            self,
            data: ByteString,
    ) -> str:
        if not isinstance(data, bytearray):
            data = bytearray(data)
        str_ptr = C.c_char_p()
        c_data = C.c_char.from_buffer(data)
        error = self.hs_serialized_database_info(C.byref(c_data), len(data), C.byref(str_ptr))
        self._check_error(error)
        str_value = str_ptr.value.decode()
        _libc.free(str_ptr)
        return str_value

    def alloc_scratch(
            self,
            database: ManagedPtr[hs_database],
            scratch: Optional[ManagedPtr[hs_scratch]] = None,
    ) -> ManagedPtr[hs_scratch]:
        if scratch is not None:
            scratch_ptr = C.POINTER(hs_scratch)(scratch.contents)
        else:
            scratch_ptr = C.POINTER(hs_scratch)()
        error = self.hs_alloc_scratch(database, C.byref(scratch_ptr))
        self._check_error(error)
        if scratch is not None:
            scratch.consume()
        return ManagedPtr(scratch_ptr.contents, free=self.hs_free_scratch)

    def scan(
            self,
            database: ManagedPtr[hs_database],
            scratch: ManagedPtr[hs_scratch],
            data: ByteString,
            match_event_handler: Optional[Callable[[int, int, int, int, object], int]],
    ) -> HsError:
        if not isinstance(data, bytearray):
            data = bytearray(data)
        c_data = C.c_char.from_buffer(data)
        if match_event_handler is not None:
            callback = _Match_event_handler(match_event_handler)
        else:
            callback = None
        error = self.hs_scan(database, C.byref(c_data), len(data), 0, scratch, callback, None)
        if error not in (HsError.SUCCESS, HsError.SCAN_TERMINATED):
            self._check_error(error)
        return error

_libhs_name = C.util.find_library('hs')
if _libhs_name is not None:
    HS = HsApi(_libhs_name)


if __name__ == '__main__':
    pi = HsPlatformInfo()
    ext = HsExprExt()
    hs = HsApi('libhs.so.5')
    db = hs.compile('abc', 0, HsMode.BLOCK, pi)
    scratch = hs.alloc_scratch(db)
    hs.scan(db, scratch, b'abc', lambda *a: (print(a), 0)[1])
    ser = hs.serialize_database(db)
    print(hs.serialized_database_info(ser))
    db_ = hs.deserialize_database(ser)
    print(hs.database_info(db_))
    hs.compile('abc', 0, HsMode.BLOCK, pi)
    hs.compile_multi(['abc'], [0], [123], HsMode.BLOCK, pi)
    hs.compile_ext_multi(['abc'], [0], [123], [ext], HsMode.BLOCK, pi)
