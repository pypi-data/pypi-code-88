import pytest

import qts


def test_version_is_a_string() -> None:
    assert isinstance(qts.__version__, str)


def test_importing_does_not_import_qt(
    pytester: pytest.Pytester,
    any_wrapper: qts.Wrapper,
) -> None:
    content = f"""
    import sys

    import qts


    def test():
        assert {any_wrapper.module_name!r} not in sys.modules
    """
    pytester.makepyfile(content)
    run_result = pytester.runpytest_subprocess()
    run_result.assert_outcomes(passed=1)
