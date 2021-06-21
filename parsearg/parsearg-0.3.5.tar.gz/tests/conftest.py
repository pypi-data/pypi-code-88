import pytest 
import argparse
from parsearg.data_structures import (
    Tree,
)
from parsearg.example_trees import (
    a_tree,
    a_dict,
    a_aa_tree,
    a_aa_dict,
)

@pytest.fixture(scope='session')
def get_a_tree():
    return a_tree()

@pytest.fixture(scope='session')
def get_a_aa_tree():
    return a_aa_tree()

@pytest.fixture(scope='session')
def get_a_aa_dict():
    return a_aa_dict()
