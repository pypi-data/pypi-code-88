import typing_extensions

import qts


class ExecProtocol(typing_extensions.Protocol):
    """A protocol that requires the presence of either ``.exec()`` or ``.exec_()`` if
    the selected wrapper requires the trailing ``_``.
    """

    # TODO: note that this will likely not be valid at runtime since i would not
    #       expect the wrapper to be set prior to importing this

    if qts._building_docs or qts.is_pyside_5_wrapper:

        def exec_(self) -> int:
            """Used only in cases where the trailing ``_`` is required."""
            pass

    if (
        qts._building_docs
        or qts.is_pyside_6_wrapper
        or qts.pyqt_5_wrapper
        or qts.pyqt_6_wrapper
    ):

        def exec(self) -> int:
            """Used in all cases where the trailing ``_`` is not required"""
            pass


def exec(execable: "ExecProtocol") -> int:
    """Call the proper execute method on the passed object.  Either ``.exec()`` or
    ``.exec_()`` is chosen based on the configured wrapper.  ``.exec_()`` exists as an
    artifact from supporting Python 2 where ``exec`` was a keyword.
    """
    if qts.is_pyside_5_wrapper:
        return execable.exec_()

    return execable.exec()
