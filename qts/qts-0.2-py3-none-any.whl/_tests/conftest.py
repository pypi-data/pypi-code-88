import typing

# TODO: https://github.com/pytest-dev/pytest/issues/7469
import _pytest.fixtures
import pytest

import qts
import qts._tests


if typing.TYPE_CHECKING:
    from qts import QtCore


pytest_plugins = "pytester"


@pytest.fixture(autouse=True, name="setup_qts", scope="session")
def setup_qts_fixture() -> None:
    # TODO: don't just hardcode this
    pass


@pytest.fixture(autouse=True, name="qt_application", scope="session")
def qt_application_fixture(setup_qts: None) -> "QtCore.QCoreApplication":
    from qts import QtCore

    qt_application = QtCore.QCoreApplication([])

    return qt_application


@pytest.fixture(name="wrapper", scope="session")
def wrapper_fixture(setup_qts: None) -> qts.Wrapper:
    assert qts.wrapper is not None
    return qts.wrapper


@pytest.fixture(
    name="any_wrapper",
    scope="session",
    params=qts.supported_wrappers,
    ids=[wrapper.name for wrapper in qts.supported_wrappers],
)
def any_wrapper_fixture(
    request: _pytest.fixtures.SubRequest,
    setup_qts: None,
) -> qts.Wrapper:
    # this is coming from qts.Wrappers so it will generally be a wrapper
    return request.param  # type: ignore[no-any-return]


available_wrapper = qts.available_wrapper()
qts.set_wrapper(available_wrapper)

other_wrappers = [
    wrapper for wrapper in qts.supported_wrappers if wrapper != available_wrapper
]


# @pytest.fixture(
#     name="other_wrapper",
#     scope="session",
#     params=other_wrappers,
#     ids=[wrapper.name for wrapper in other_wrappers],
# )
# def other_wrapper_fixture(request: pytest.FixtureRequest, setup_qts):
#     return request.param


@pytest.fixture(
    name="qt_module",
    params=qts._tests.qt_modules,
    ids=[module.name for module in qts._tests.qt_modules],
)
def qt_module_fixture(request: _pytest.fixtures.SubRequest) -> qts._tests.QtModule:
    return request.param  # type: ignore[no-any-return]
