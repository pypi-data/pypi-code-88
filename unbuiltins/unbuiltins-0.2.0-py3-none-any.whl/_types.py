from typing import Iterable, Protocol, TypeVar

_KT = TypeVar("_KT")
_KT_co = TypeVar("_KT_co", covariant=True)
_KT_contra = TypeVar("_KT_contra", contravariant=True)
_VT = TypeVar("_VT")
_VT_co = TypeVar("_VT_co", covariant=True)
_T_co = TypeVar("_T_co", covariant=True)
_T_contra = TypeVar("_T_contra", contravariant=True)


class SupportsKeysAndGetItem(Protocol[_KT, _VT_co]):
    # shamelessly stolen from
    # https://github.com/python/typeshed/blob/master/stdlib/2and3/_typeshed/__init__.pyi#L39
    def keys(self) -> Iterable[_KT]:
        ...  # pragma: no cover

    def __getitem__(self, __k: _KT) -> _VT_co:
        ...  # pragma: no cover
