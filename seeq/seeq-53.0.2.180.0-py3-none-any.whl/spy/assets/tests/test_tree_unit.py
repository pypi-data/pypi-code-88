import pytest

import pandas as pd
import numpy as np

from seeq import spy


def _tree_from_nested_dict(d):
    if len(d) != 1:
        raise ValueError('Cannot have more than one root.')

    root_name, root_branches = [(k, v) for k, v in d.items()][0]
    tree = spy.assets.Tree(root_name)

    def _add_branches(parent_name, branches_dict):
        for branch_name, sub_branches in branches_dict.items():
            tree.insert(branch_name, parent_name)
            _add_branches(branch_name, sub_branches)

    _add_branches(root_name, root_branches)
    return tree


def _build_dataframe_from_path_name_depth_triples(data, *, index=None):
    if index is None:
        index = range(len(data))
    return pd.DataFrame([{
        'ID': np.nan,
        'Referenced ID': np.nan,
        'Type': 'Asset',
        'Path': path,
        'Depth': depth,
        'Name': name,
        'Description': np.nan,
        'Formula': np.nan,
        'Formula Parameters': np.nan,
        'Cache Enabled': np.nan
    } for path, name, depth in data
    ], index=index)


@pytest.mark.unit
def test_constructor_invalid():
    # Basic property validation
    with pytest.raises(TypeError, match="Argument 'data' should be type DataFrame or str, but is type int"):
        spy.assets.Tree(0)
    with pytest.raises(TypeError, match="'data' must be a name, Seeq ID, or Metadata dataframe"):
        spy.assets.Tree(data='')
    with pytest.raises(ValueError, match="DataFrame with no rows"):
        spy.assets.Tree(pd.DataFrame(columns=['Name']))
    with pytest.raises(TypeError, match="Argument 'description' should be type str"):
        spy.assets.Tree('name', description=0)
    with pytest.raises(TypeError, match="Argument 'workbook' should be type str"):
        spy.assets.Tree('name', workbook=0)

    with pytest.raises(RuntimeError, match="Not logged in"):
        spy.assets.Tree('8DEECF16-A500-4231-939D-6C24DD123A30')


@pytest.mark.unit
def test_constructor_name():
    # Valid constructor for a new root asset with all other properties default
    name = 'test name'
    expected = pd.DataFrame({
        'ID': np.nan,
        'Referenced ID': np.nan,
        'Type': 'Asset',
        'Path': '',
        'Depth': 1,
        'Name': name,
        'Description': np.nan,
        'Formula': np.nan,
        'Formula Parameters': np.nan,
        'Cache Enabled': np.nan
    }, index=[0])
    test_tree = spy.assets.Tree(name)
    assert test_tree._dataframe.columns.equals(expected.columns)
    assert test_tree._dataframe.iloc[0].equals(expected.iloc[0])
    assert test_tree._workbook == spy._common.DEFAULT_WORKBOOK_PATH

    # Valid constructor for a new root asset with all other properties assigned to non-defaults
    description = 'test description'
    workbook = 'test workbook'
    expected = pd.DataFrame({
        'ID': np.nan,
        'Referenced ID': np.nan,
        'Type': 'Asset',
        'Path': '',
        'Depth': 1,
        'Name': name,
        'Description': description,
        'Formula': np.nan,
        'Formula Parameters': np.nan,
        'Cache Enabled': np.nan
    }, index=[0])
    test_tree = spy.assets.Tree(name, description=description, workbook=workbook)
    assert test_tree._dataframe.columns.equals(expected.columns)
    assert test_tree._dataframe.iloc[0].equals(expected.iloc[0])
    assert test_tree._workbook == workbook


@pytest.mark.unit
def test_insert_by_name():
    tree_dict = {
        'Root Asset': {
            'L Asset': {
                'LL Asset': {},
                'LR Asset': {}
            },
            'R Asset': {}
        }
    }
    test_tree = _tree_from_nested_dict(tree_dict)
    expected = _build_dataframe_from_path_name_depth_triples([
        ('', 'Root Asset', 1),
        ('Root Asset', 'R Asset', 2),
        ('Root Asset', 'L Asset', 2),
        ('Root Asset >> L Asset', 'LR Asset', 3),
        ('Root Asset >> L Asset', 'LL Asset', 3)
    ], index=range(5))
    assert test_tree._dataframe.shape[0] == 5
    for i in range(5):
        assert test_tree._dataframe.iloc[i].equals(expected.iloc[i])


@pytest.mark.unit
def test_insert_by_name_list():
    tree_dict = {
        'Root Asset': {
            'Location A': {},
            'Location B': {}
        }
    }
    test_tree = _tree_from_nested_dict(tree_dict)
    test_tree.insert([f'Equipment {n}' for n in range(1, 4)], parent='Location A')
    expected = _build_dataframe_from_path_name_depth_triples([
        ('', 'Root Asset', 1),
        ('Root Asset', 'Location B', 2),
        ('Root Asset', 'Location A', 2),
        ('Root Asset >> Location A', 'Equipment 1', 3),
        ('Root Asset >> Location A', 'Equipment 2', 3),
        ('Root Asset >> Location A', 'Equipment 3', 3)
    ])
    assert test_tree._dataframe.shape[0] == 6
    for i in range(6):
        assert test_tree._dataframe.iloc[i].equals(expected.iloc[i])


@pytest.mark.unit
def test_insert_at_depth():
    tree_dict = {
        'Root Asset': {
            'Location A': {},
            'Location B': {}
        }
    }
    test_tree = _tree_from_nested_dict(tree_dict)
    test_tree.insert([f'Equipment {n}' for n in range(1, 4)], parent=2)
    expected = _build_dataframe_from_path_name_depth_triples([
        ('', 'Root Asset', 1),
        ('Root Asset', 'Location B', 2),
        ('Root Asset >> Location B', 'Equipment 1', 3),
        ('Root Asset >> Location B', 'Equipment 2', 3),
        ('Root Asset >> Location B', 'Equipment 3', 3),
        ('Root Asset', 'Location A', 2),
        ('Root Asset >> Location A', 'Equipment 1', 3),
        ('Root Asset >> Location A', 'Equipment 2', 3),
        ('Root Asset >> Location A', 'Equipment 3', 3)
    ])
    assert test_tree._dataframe.shape[0] == 9
    for i in range(9):
        assert test_tree._dataframe.iloc[i].equals(expected.iloc[i])


@pytest.mark.unit
def test_insert_at_path():
    tree_dict = {
        'Root Asset': {
            'Factory': {
                'Location A': {},
                'Location B': {}
            }
        }
    }
    test_tree = _tree_from_nested_dict(tree_dict)
    # Test partial path match with regex
    test_tree.insert('Equipment 1', parent='Factory >> Location [A-Z]')
    # Test full path match with case insensitivity
    test_tree.insert('Equipment 2', parent='rOoT aSsEt >> FaCtOrY >> lOcAtIoN b')
    expected = _build_dataframe_from_path_name_depth_triples([
        ('', 'Root Asset', 1),
        ('Root Asset', 'Factory', 2),
        ('Root Asset >> Factory', 'Location B', 3),
        ('Root Asset >> Factory >> Location B', 'Equipment 2', 4),
        ('Root Asset >> Factory >> Location B', 'Equipment 1', 4),
        ('Root Asset >> Factory', 'Location A', 3),
        ('Root Asset >> Factory >> Location A', 'Equipment 1', 4),
    ])
    assert test_tree._dataframe.shape[0] == 7
    for i in range(7):
        assert test_tree._dataframe.iloc[i].equals(expected.iloc[i])


@pytest.mark.unit
def test_insert_at_root():
    tree_dict = {
        'Root Asset': {
            'Location A': {},
            'Location B': {}
        }
    }
    test_tree = _tree_from_nested_dict(tree_dict)
    test_tree.insert('Location C')
    expected = _build_dataframe_from_path_name_depth_triples([
        ('', 'Root Asset', 1),
        ('Root Asset', 'Location C', 2),
        ('Root Asset', 'Location B', 2),
        ('Root Asset', 'Location A', 2)
    ])
    assert test_tree._dataframe.shape[0] == 4
    for i in range(4):
        assert test_tree._dataframe.iloc[i].equals(expected.iloc[i])


@pytest.mark.unit
def test_insert_at_regex():
    tree_dict = {
        'Root Asset': {
            'Factory': {
                'Location Z': {}
            },
            'Area 51': {}
        }
    }
    test_tree = _tree_from_nested_dict(tree_dict)
    test_tree.insert('Equipment 1', parent='Area [1-9][0-9]*|Location [A-Z]+')
    expected = _build_dataframe_from_path_name_depth_triples([
        ('', 'Root Asset', 1),
        ('Root Asset', 'Area 51', 2),
        ('Root Asset >> Area 51', 'Equipment 1', 3),
        ('Root Asset', 'Factory', 2),
        ('Root Asset >> Factory', 'Location Z', 3),
        ('Root Asset >> Factory >> Location Z', 'Equipment 1', 4)
    ])
    assert test_tree._dataframe.shape[0] == 6
    for i in range(6):
        assert test_tree._dataframe.iloc[i].equals(expected.iloc[i])


@pytest.mark.unit
def test_insert_at_glob():
    tree_dict = {
        'Root Asset': {
            'Location A': {},
            'Location 1': {}
        }
    }
    test_tree = _tree_from_nested_dict(tree_dict)
    test_tree.insert('Equipment 1', parent='Location ?')
    expected = _build_dataframe_from_path_name_depth_triples([
        ('', 'Root Asset', 1),
        ('Root Asset', 'Location 1', 2),
        ('Root Asset >> Location 1', 'Equipment 1', 3),
        ('Root Asset', 'Location A', 2),
        ('Root Asset >> Location A', 'Equipment 1', 3)
    ])
    assert test_tree._dataframe.shape[0] == 5
    for i in range(5):
        assert test_tree._dataframe.iloc[i].equals(expected.iloc[i])


@pytest.mark.unit
def test_insert_preexisting_node():
    tree_dict = {
        'Root': {
            'Location A': {}
        }
    }
    tree = _tree_from_nested_dict(tree_dict)
    with pytest.raises(RuntimeError, match="Error encountered while inserting."):
        tree.insert('Location A')
    insertion_df = tree.insert('Location A', errors='catalog')
    assert 'Failure' in insertion_df.iloc[0]['Result']
    assert 'Tree cannot have multiple nodes with path "Root" and name "Location A"' in insertion_df.iloc[0]['Result']


@pytest.mark.unit
def test_insert_same_node_twice():
    tree_dict = {
        'Root': {}
    }
    tree = _tree_from_nested_dict(tree_dict)
    with pytest.raises(RuntimeError, match="Error encountered while inserting."):
        tree.insert(['Location A', 'Location A'])
    insertion_df = tree.insert(['Location A', 'Location A'], errors='catalog')
    assert 'Tree cannot have multiple nodes with path "Root" and name "Location A"' in insertion_df.iloc[0]['Result']
    assert 'Tree cannot have multiple nodes with path "Root" and name "Location A"' in insertion_df.iloc[1]['Result']


@pytest.mark.unit
def test_validate_insert_bad_depth():
    tree_dict = {
        'Root': {}
    }
    tree = _tree_from_nested_dict(tree_dict)
    insertions = _build_dataframe_from_path_name_depth_triples([
        ('Root', 'Location A', 2),
        ('Root', 'Location B', 1)
    ])
    out_df, insertion_df, error_summaries, num_success, num_failure = spy.assets._tree._validate_and_insert(
        tree._dataframe, insertions, 0)
    assert num_success == 1 and num_failure == 1
    assert len(out_df.index) == 2
    assert len(error_summaries) == 1
    assert 'Node\'s depth must be one more than the depth of its parent.' in error_summaries[0]
    assert 'Failure' in insertion_df.iloc[1]['Result']


@pytest.mark.unit
def test_validate_insert_bad_path():
    tree_dict = {
        'Root': {}
    }
    tree = _tree_from_nested_dict(tree_dict)
    insertions = _build_dataframe_from_path_name_depth_triples([
        ('Root', 'Location A', 2),
        ('Root >> Locat--TYPO--ion A', 'Equipment 1', 3),
        ('Root >> Location A', 'Equipment 2', 3),
    ])
    out_df, insertion_df, error_summaries, num_success, num_failure = spy.assets._tree._validate_and_insert(
        tree._dataframe, insertions, 0)
    assert num_success == 2 and num_failure == 1
    assert len(out_df.index) == 3
    assert len(error_summaries) == 1
    assert 'Node\'s parent has mismatching path.' in error_summaries[0]
    assert 'Failure' in insertion_df.iloc[1]['Result']


@pytest.mark.unit
def test_validate_insert_bad_parent():
    tree_dict = {
        'Root': {}
    }
    tree = _tree_from_nested_dict(tree_dict)
    insertions = _build_dataframe_from_path_name_depth_triples([
        ('', 'Location A', 2),
        ('Root >> Location A', 'Equipment 1', 3),
        ('Root', 'Location B', 2),
    ])
    out_df, insertion_df, error_summaries, num_success, num_failure = spy.assets._tree._validate_and_insert(
        tree._dataframe, insertions, 0)
    assert num_success == 1 and num_failure == 2
    assert len(out_df.index) == 2
    assert len(error_summaries) == 2
    assert 'Node\'s parent has mismatching path.' in error_summaries[0]
    assert 'Node\'s parent could not be inserted.' in error_summaries[1]
    assert 'Failure' in insertion_df.iloc[0]['Result'] and 'Failure' in insertion_df.iloc[1]['Result']
    assert 'Success' in insertion_df.iloc[2]['Result']


@pytest.mark.unit
def test_validate_duplicate_nodes():
    tree = spy.assets.Tree('Root')
    tree._dataframe = _build_dataframe_from_path_name_depth_triples([
        ('', 'Root', 1),
        ('Root', 'Location A', 2),
        ('Root >> Location A', 'Equipment 1', 3),
        ('Root >> Location A', 'Equipment 1', 3),
        ('Root', 'Location B', 2)
    ])
    error_summaries, error_details, num_bad_nodes = spy.assets._tree._validate(tree._dataframe)
    assert num_bad_nodes == 2
    assert len(error_summaries) == 1
    error_msg = 'Tree cannot have multiple nodes with path "Root >> Location A" and name "Equipment 1"'
    assert error_msg in error_summaries[0]
    assert error_msg in error_details[2]
    assert error_msg in error_details[3]


@pytest.mark.unit
def test_validate_bad_depth():
    tree = spy.assets.Tree('Root')
    tree._dataframe = _build_dataframe_from_path_name_depth_triples([
        ('', 'Root', 1),
        ('Root', 'Location A', 2),
        ('Root >> Location A', 'Equipment 1', 3),
        ('Root >> Location A', 'Equipment 2', 1),
    ])
    # This will actually throw a bad path error because _validate() checks nodes recursively by depth instead of path
    error_summaries, error_details, num_bad_nodes = spy.assets._tree._validate(tree._dataframe)
    print(error_summaries)
    assert num_bad_nodes == 1
    assert len(error_summaries) == 1
    error_msg = 'Node\'s parent has mismatching path.'
    assert error_msg in error_summaries[0]
    assert error_msg in error_details[3]

    tree = spy.assets.Tree('Root')
    tree._dataframe = _build_dataframe_from_path_name_depth_triples([
        ('', 'Root', 1),
        ('Root', 'Location A', 3)
    ])
    error_summaries, error_details, num_bad_nodes = spy.assets._tree._validate(tree._dataframe)
    assert num_bad_nodes == 1
    assert len(error_summaries) == 1
    error_msg = 'Node\'s depth must be one more than the depth of its parent.'
    assert error_msg in error_summaries[0]
    assert error_msg in error_details[1]


@pytest.mark.unit
def test_validate_bad_path():
    tree = spy.assets.Tree('Root')
    tree._dataframe = _build_dataframe_from_path_name_depth_triples([
        ('', 'Root', 1),
        ('Root', 'Location A', 2),
        ('Root >> Locat--TYPO--ion A', 'Equipment 1', 3),
        ('Root >> Location A', 'Equipment 2', 3),
    ])
    error_summaries, error_details, num_bad_nodes = spy.assets._tree._validate(tree._dataframe)
    assert num_bad_nodes == 1
    assert len(error_summaries) == 1
    error_msg = 'Node\'s parent has mismatching path.'
    assert error_msg in error_summaries[0]
    assert error_msg in error_details[2]


@pytest.mark.unit
def test_validate_insert_bad_parent():
    tree = spy.assets.Tree('Root')
    tree._dataframe = _build_dataframe_from_path_name_depth_triples([
        ('', 'Root', 1),
        ('', 'Location A', 2),
        ('Root >> Location A', 'Equipment 1', 3),
        ('Root', 'Location B', 2),
    ])
    error_summaries, error_details, num_bad_nodes = spy.assets._tree._validate(tree._dataframe)
    assert num_bad_nodes == 2
    assert len(error_summaries) == 2
    assert 'Node\'s parent has mismatching path.' in error_summaries[0]
    assert 'Node\'s parent has mismatching path.' in error_details[1]
    assert 'Node\'s parent is invalid.' in error_summaries[1]
    assert 'Node\'s parent is invalid.' in error_details[2]


@pytest.mark.unit
def test_insert_no_parent_match():
    tree = spy.assets.Tree('Root')
    bad_depth_df = tree.insert(children=['Child 1', 'Child 2'], parent=3)
    bad_name_df = tree.insert(children=['Child 1', 'Child 2'], parent='asdf')
    assert len(bad_depth_df.index) == 2
    assert len(bad_name_df.index) == 2
    assert (bad_depth_df['Result'] == 'Ignored: No matching parent found.').all()
    assert (bad_name_df['Result'] == 'Ignored: No matching parent found.').all()
