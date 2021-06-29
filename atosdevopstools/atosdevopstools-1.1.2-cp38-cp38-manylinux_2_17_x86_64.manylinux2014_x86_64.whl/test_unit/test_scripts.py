import pytest

from atosdevopstools.pylint_wrapper import PylintWrapper


@pytest.mark.parametrize('line, is_error',
                         [
                             ('somefile.py:1:0: C0114: somecode', False),
                             ('somefile.py:1:0: R0114: somecode', False),
                             ('somefile.py:1:0: F0114: somecode', True),
                             ('somefile.py:1:0: W0114: somecode', False),
                             ('somefile.py:1:0: E0114: somecode', True)
                         ])
def test_check_pylint_codes(line, is_error):
    if not is_error:
        PylintWrapper.raise_if_error_or_failure(line)
    else:
        with pytest.raises(ValueError):
            PylintWrapper.raise_if_error_or_failure(line)


@pytest.mark.parametrize('line, qa_value',
                         [
                             ('Your code has been rated at 3.5/10 (previous run: 6.33/10, +0.00)', '3.5'),
                             ('Your code has been rated at 8/10 (previous run: 6.33/10, +0.00)', '8'),
                             ('Your code has been rated at 10.0/10 (previous run: 6.33/10, +0.00)', '10.0'),
                             ('Your code has been rated at -2.5/10 (previous run: 6.33/10, +0.00)', '-2.5'),
                             ('Your code has been rated at 9/10 (previous run: 6.33/10, +0.00)', '9')
                         ])
def test_extract_qa_value(line, qa_value):
    assert PylintWrapper.extract_quality_value(line) == qa_value


def test_pylint_file_not_found():
    with pytest.raises(FileNotFoundError):
        PylintWrapper('some_missing_file.txt')
