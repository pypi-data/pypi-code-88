import pytest
import pandas as pd
import numpy as np

from seeq import spy
from seeq.sdk import *
from seeq.spy.assets import Tree

from ... import _common
from ...tests import test_common


def setup_module():
    test_common.login()


start_cleanup_names = {'test_tree_system'}
end_cleanup_ids = set()


@pytest.mark.system
def test_create_new_tree_then_repull_and_edit():
    tree = Tree('test_tree_system')
    tree.insert(['Cooling Tower 1', 'Cooling Tower 2'])
    tree.insert(children=['Area A', 'Area B', 'Area C'], parent='Cooling Tower 1')
    tree.insert(children=['Area E', 'Area F', 'Area G', 'Area H'], parent='Cooling Tower 2')
    tree.insert(children=['Temperature', 'Optimizer', 'Compressor'], parent=3)

    tower1_areas = ['Area A', 'Area B', 'Area C']
    tower2_areas = ['Area E', 'Area F', 'Area G', 'Area H']
    leaves = ['Temperature', 'Optimizer', 'Compressor']

    expected = list()
    expected.append({
        'Name': 'test_tree_system',
        'Path': '',
        'Type': 'Asset'
    })
    expected.append({
        'Name': 'Cooling Tower 1',
        'Path': 'test_tree_system',
        'Type': 'Asset'
    })
    expected.append({
        'Name': 'Cooling Tower 2',
        'Path': 'test_tree_system',
        'Type': 'Asset'
    })
    for area in tower1_areas:
        expected.append({
            'Name': area,
            'Path': 'test_tree_system >> Cooling Tower 1',
            'Type': 'Asset'
        })
        for leaf in leaves:
            expected.append({
                'Name': leaf,
                'Path': f'test_tree_system >> Cooling Tower 1 >> {area}',
                'Type': 'Asset'
            })
    for area in tower2_areas:
        expected.append({
            'Name': area,
            'Path': 'test_tree_system >> Cooling Tower 2',
            'Type': 'Asset'
        })
        for leaf in leaves:
            expected.append({
                'Name': leaf,
                'Path': f'test_tree_system >> Cooling Tower 2 >> {area}',
                'Type': 'Asset'
            })
    assert_tree_equals_expected(tree, expected)

    tree.push()
    search_results_df = spy.search({
        'Path': 'test_tree_system'
    })
    expected.pop(0)  # Since we're searching using Path, the root node won't be retrieved.
    assert_search_results_equals_expected(search_results_df, expected)
    add_all_pushed_ids_to_cleanup(search_results_df)

    # Pull in the previously-created test_tree_system by name
    tree = Tree('test_tree_system')
    add_all_pushed_ids_to_cleanup(tree._dataframe)
    original_root_id, original_root_referenced_id = get_root_node_ids(tree)
    assert _common.is_guid(original_root_id), \
        f'Pulled root ID should be a GUID: {original_root_id}'
    assert str(original_root_referenced_id) == str(np.nan), \
        f'Pulled root Reference ID should be {np.nan}: {original_root_referenced_id}'

    expected_existing_items = 1 + 2 + 3 + 4 + (3 * 3) + (4 * 3)
    assert len(tree._dataframe) == expected_existing_items, \
        f'Pulled tree items do not match count: Real={len(tree._dataframe)}, Expected={expected_existing_items}'
    expected_nodes = create_expected_list_from_tree(tree)

    # Add a single node
    tree.insert(children='Area I', parent='Cooling Tower 2')
    expected_nodes.append({
        'Name': 'Area I',
        'Path': 'test_tree_system >> Cooling Tower 2',
        'Type': 'Asset'
    })
    expected_existing_items += 1
    assert_tree_equals_expected(tree, expected_nodes)
    tree.push()

    # Pull it again, but by ID
    tree2 = Tree(original_root_id)
    add_all_pushed_ids_to_cleanup(tree2._dataframe)
    assert len(tree2._dataframe) == expected_existing_items, \
        f'Edited tree items do not match count: Real={len(tree2._dataframe)}, Expected={expected_existing_items}'
    updated_root_id, updated_root_referenced_id = get_root_node_ids(tree2)
    assert original_root_id == updated_root_id, \
        f'Pulled root ID should be the same as before: Original={original_root_id}, Updated={updated_root_id}'
    assert str(original_root_referenced_id) == str(np.nan), \
        f'Pulled root Reference ID should be the same as before: ' \
        f'Original={original_root_referenced_id}, Updated={updated_root_referenced_id}'
    assert_tree_equals_expected(tree2, expected_nodes)


def assert_tree_equals_expected(tree, expected_nodes):
    pd.set_option('display.max_columns', None)  # Print all columns if something errors
    tree_dataframe = tree._dataframe
    for expected_node in expected_nodes:
        node_df = tree_dataframe[
            (tree_dataframe['Name'] == expected_node['Name']) &
            (tree_dataframe['Path'] == expected_node['Path']) &
            (tree_dataframe['Type'] == expected_node['Type'])]

        assert len(node_df) == 1, \
            f"Expected item ({expected_node['Name']}, {expected_node['Path']},  {expected_node['Type']})" \
            f"\n was not found in Dataframe" \
            f"\n{tree_dataframe}"
    assert len(tree_dataframe) == len(expected_nodes), \
        f'Tree items do not match count: Real={len(tree_dataframe)}, Expected={len(expected_nodes)}'


def assert_search_results_equals_expected(search_results_df, expected_nodes):
    pd.set_option('display.max_columns', None)  # Print all columns if something errors

    for expected_node in expected_nodes:
        asset = np.nan
        # Extract the parent asset from that path
        if expected_node['Path'].count('>>') > 0:
            asset = expected_node['Path'].rpartition(' >> ')[2]
        elif expected_node['Path'] is not '':
            asset = expected_node['Path']

        node_df = search_results_df[
            (search_results_df['Name'] == expected_node['Name']) &
            (search_results_df['Asset'] == asset) &
            (search_results_df['Type'] == expected_node['Type'])]

        assert len(node_df) == 1, \
            f"Expected item ({expected_node['Name']}, {asset}, {expected_node['Type']})" \
            f"\n was not found in Dataframe" \
            f"\n{search_results_df}"
    assert len(search_results_df) == len(expected_nodes), \
        f'Search result items do not match count: Real={len(search_results_df)}, Expected={len(expected_nodes)}'


def create_expected_list_from_tree(tree):
    # Create a list of node dicts from an existing tree.
    tree_dataframe = tree._dataframe
    expected = list()
    for index, row in tree_dataframe.iterrows():
        expected.append({
            'Name': row['Name'],
            'Path': row['Path'],
            'Type': row['Type']
        })
    return expected


def get_root_node_ids(tree):
    # Get the ID and Reference ID from the tree's root
    tree_dataframe = tree._dataframe
    root_df = tree_dataframe[(tree_dataframe['Path'] == '')]
    assert len(root_df) == 1, \
        f"Exactly one root node was not found in Dataframe: \n{tree_dataframe}"
    id = root_df['ID'].values[0]
    referenced_id = root_df['Referenced ID'].values[0]
    return id, referenced_id


def add_all_pushed_ids_to_cleanup(dataframe):
    # Get all IDs from the tree and add it to the set of cleanup_ids.
    for index, row in dataframe.iterrows():
        end_cleanup_ids.add(row['ID'])


@pytest.fixture(scope='module', autouse=True)
def setup_and_teardown():
    items_api = ItemsApi(test_common.get_client())
    # Setup: Make sure any previously-created versions of these trees are not present when beginning the test
    for cleanup_name in start_cleanup_names:
        cleanup_df = spy.search(query={'Name': cleanup_name})
        for index, cleanup_row in cleanup_df.iterrows():
            items_api.archive_item(id=cleanup_row['ID'])
    yield None
    # Teardown: Trash any items that we created
    for cleanup_id in end_cleanup_ids:
        items_api.archive_item(id=cleanup_id)
