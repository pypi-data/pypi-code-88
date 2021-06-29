import importlib.util
import os
import typing

import attr

import qts


@attr.frozen
class Wrapper:
    """A representation of a specific wrapper that can be used to access a specific
    version of Qt.
    """

    family: str
    """The wrapper family.  ``"PyQt"`` or ``"PySide"``."""
    name: str
    """The name of the specific wrapper, including the version number.  Such as ``"PySide6"``."""
    major_version: int
    """The major version of the wrapped Qt library.  Such as ``6``."""
    module_name: str
    """The name used to import the module.  Such as ``"PySide6"``."""


pyqt_5_wrapper = Wrapper(
    family="PyQt", name="PyQt5", major_version=5, module_name="PyQt5"
)
"""The PyQt/Qt5 wrapper object."""
pyqt_6_wrapper = Wrapper(
    family="PyQt", name="PyQt6", major_version=6, module_name="PyQt6"
)
"""The PyQt/Qt6 wrapper object."""
pyside_5_wrapper = Wrapper(
    family="PySide", name="PySide2", major_version=5, module_name="PySide2"
)
"""The PySide/Qt5 wrapper object."""
pyside_6_wrapper = Wrapper(
    family="PySide", name="PySide6", major_version=6, module_name="PySide6"
)
"""The PySide/Qt6 wrapper object."""
supported_wrappers = [
    pyside_6_wrapper,
    pyqt_6_wrapper,
    pyside_5_wrapper,
    pyqt_5_wrapper,
]
"""A list of all the supported wrapper objects."""


_wrappers_by_name = {wrapper.name.casefold(): wrapper for wrapper in supported_wrappers}


def set_wrapper(wrapper: Wrapper) -> None:
    """Set the wrapper you want to back the Qt modules accessed through qts.

    :raises qts.WrapperAlreadySelectedError: When called and a wrapper has already
        been set.
    :raises qts.InvalidWrapperError: When called with an invalid wrapper.
    """

    # This could accept the new wrapper if it matches the existing selection, but this
    # seems like it would mostly just encourage coding that hazards setting to a
    # different wrapper in some other case.  May as well complain early so that
    # developers get early warning and can adjust their design.

    if qts.wrapper is not None:
        raise qts.WrapperAlreadySelectedError(
            existing_wrapper=qts.wrapper,
            requested_wrapper=wrapper,
        )

    if wrapper not in supported_wrappers:
        raise qts.InvalidWrapperError(wrapper=wrapper)

    qts.wrapper = wrapper

    qts.is_pyqt_5_wrapper = wrapper == pyqt_5_wrapper
    qts.is_pyqt_6_wrapper = wrapper == pyqt_6_wrapper
    qts.is_pyside_5_wrapper = wrapper == pyside_5_wrapper
    qts.is_pyside_6_wrapper = wrapper == pyside_6_wrapper


def autoset_wrapper() -> None:
    """Automatically choose and set the wrapper used to back the Qt modules accessed
    through qts.  If the environment variable ``QTS_WRAPPER`` is set to a name of a
    supported wrapper then that wrapper will be used.  The lookup is case insensitive.

    :raises qts.InvalidWrapperError: When an unsupported wrapper name is specified in
        the ``QTS_WRAPPER`` environment variable.
    """
    environment_wrapper_name = os.environ.get("QTS_WRAPPER")

    if environment_wrapper_name is not None:
        environment_wrapper = _wrappers_by_name.get(environment_wrapper_name.casefold())

        if environment_wrapper is None:
            raise qts.InvalidWrapperError(wrapper=environment_wrapper)
        else:
            set_wrapper(wrapper=environment_wrapper)
            return

    set_wrapper(wrapper=an_available_wrapper())


def available_wrappers(
    wrappers: typing.Optional[typing.Iterable[Wrapper]] = None,
) -> typing.Sequence[Wrapper]:
    """Get a sequence of the wrappers that are available for use.  If ``wrappers`` is
    passed, only wrappers that are both available and in the passed iterable will be
    returned.

    :returns: The wrappers that are installed and available for use.
    """

    if wrappers is None:
        wrappers = supported_wrappers

    available = [
        wrapper for wrapper in wrappers if importlib.util.find_spec(wrapper.module_name)
    ]
    return available


def available_wrapper(
    wrappers: typing.Optional[typing.Iterable[Wrapper]] = None,
) -> Wrapper:
    """Get the available wrapper when there is only one.

    :return: The wrapper object for the single available wrapper.

    :raises qts.NoWrapperAvailableError: When no wrappers are available.
    :raises qts.MultipleWrappersAvailableError: If more than one wrapper is available.
    """
    if wrappers is None:
        wrappers = supported_wrappers

    all_available = available_wrappers(wrappers=wrappers)

    if len(all_available) == 0:
        raise qts.NoWrapperAvailableError(wrappers=wrappers)
    elif len(all_available) > 1:
        raise qts.MultipleWrappersAvailableError(searched=wrappers, found=all_available)

    [the_one] = all_available
    return the_one


def an_available_wrapper(
    wrappers: typing.Optional[typing.Iterable[Wrapper]] = None,
) -> Wrapper:
    """Get an available wrapper when there is one or more available.

    :param wrappers: The wrappers to consider.  All if not specified.

    :return: The wrapper object for the single available wrapper.

    :raises qts.NoWrapperAvailableError: When no wrappers are available.
    """
    if wrappers is None:
        wrappers = supported_wrappers

    all_available = available_wrappers(wrappers=wrappers)

    for wrapper in wrappers:
        if wrapper in all_available:
            return wrapper

    raise qts.NoWrapperAvailableError(wrappers=wrappers)


def wrapper_by_name(name: str) -> Wrapper:
    """Get a wrapper object by its name.  The name is checked case insensitively.

    :returns: The wrapper that goes by the passed name.
    """
    return _wrappers_by_name[name.casefold()]
