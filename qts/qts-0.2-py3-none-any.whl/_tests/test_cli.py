import os
import pathlib
import subprocess
import sys
import sysconfig
import typing

# TODO: https://github.com/pytest-dev/pytest/issues/7469
import _pytest.fixtures
import pytest

import qts


script_path = pathlib.Path(typing.cast(str, sysconfig.get_path("scripts")), "qts")


# https://github.com/altendky/ssst/blob/1e23bf26a47b48d714ae643f5d8af95394172464/src/ssst/_tests/test_cli.py#L74-L109
@pytest.fixture(
    name="launch_command",
    params=["script", "-m"],  # or "frozen"
)
def launch_command_fixture(
    request: _pytest.fixtures.SubRequest,
    # frozen_executable: typing.Optional[pathlib.Path],
) -> typing.List[str]:
    """This launch command fixture will return a list of strings that can be used as
    a subprocess command to launch the base SSST program.  There are three possible
    modes.
    - myvenv/bin/ssst
    - myvenv/bin/python -m ssst
    - dist/myfrozenssst
    If --frozen-executable has been specified then the first two will be skipped.
    Otherwise, the frozen executable mode will be skipped.
    """

    if request.param == "script":
        # if frozen_executable is not None:
        #     pytest.skip("Frozen executable specified, skipping non-frozen tests")

        path = script_path

        return [os.fspath(path)]
    elif request.param == "-m":
        # if frozen_executable is not None:
        #     pytest.skip("Frozen executable specified, skipping non-frozen tests")

        return [sys.executable, "-m", "qts"]
    # elif request.param == "frozen":
    #     pytest.skip("No frozen target yet")
    #     if frozen_executable is None:
    #         pytest.skip("Frozen executable not specified, pass via --frozen-executable")
    #
    #     return [os.fspath(frozen_executable)]

    raise qts.InternalError("Unhandled parametrization")  # pragma: no cover


@pytest.mark.parametrize(
    argnames=["delimiter_argument", "delimiter_result"],
    argvalues=[[None, "\n"], ["\n", "\n"], [" ", " "]],
)
@pytest.mark.parametrize(
    argnames=["argument", "expected_result"],
    argvalues=[
        [
            None,
            [
                f"--always-{'true' if qts.is_pyqt_5_wrapper else 'false'}=is_pyqt_5_wrapper",
                f"--always-{'true' if qts.is_pyqt_6_wrapper else 'false'}=is_pyqt_6_wrapper",
                f"--always-{'true' if qts.is_pyside_5_wrapper else 'false'}=is_pyside_5_wrapper",
                f"--always-{'true' if qts.is_pyside_6_wrapper else 'false'}=is_pyside_6_wrapper",
            ],
        ],
        [
            "pyqt5",
            [
                "--always-true=is_pyqt_5_wrapper",
                "--always-false=is_pyqt_6_wrapper",
                "--always-false=is_pyside_5_wrapper",
                "--always-false=is_pyside_6_wrapper",
            ],
        ],
        [
            "pyqt6",
            [
                "--always-false=is_pyqt_5_wrapper",
                "--always-true=is_pyqt_6_wrapper",
                "--always-false=is_pyside_5_wrapper",
                "--always-false=is_pyside_6_wrapper",
            ],
        ],
        [
            "pyside2",
            [
                "--always-false=is_pyqt_5_wrapper",
                "--always-false=is_pyqt_6_wrapper",
                "--always-true=is_pyside_5_wrapper",
                "--always-false=is_pyside_6_wrapper",
            ],
        ],
        [
            "pyside6",
            [
                "--always-false=is_pyqt_5_wrapper",
                "--always-false=is_pyqt_6_wrapper",
                "--always-false=is_pyside_5_wrapper",
                "--always-true=is_pyside_6_wrapper",
            ],
        ],
    ],
)
def test_(
    launch_command: typing.List[str],
    argument: typing.Optional[str],
    expected_result: typing.List[str],
    delimiter_argument: typing.Optional[str],
    delimiter_result: str,
) -> None:
    args = [*launch_command, "mypy", "args"]
    if argument is not None:
        args.extend(["--wrapper", argument])
    if delimiter_argument is not None:
        args.extend(["--delimiter", delimiter_argument])
    completed_process = subprocess.run(
        args=args,
        check=True,
        encoding="utf-8",
        stdout=subprocess.PIPE,
    )
    assert completed_process.returncode == 0

    results = completed_process.stdout.strip().split(delimiter_result)

    assert results == expected_result
