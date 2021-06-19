import pytest
import os
from parglare import Grammar

this_folder = os.path.dirname(__file__)


@pytest.mark.skip
def test_import_complex():
    g = Grammar.from_file(os.path.join(this_folder, 'A.pg'))
    assert g
