import fnmatch
import re

import numpy as np
import pandas as pd

from seeq import spy
from seeq.sdk import *
from .. import _common
from .. import _config
from .. import _login
from .. import _metadata
from .. import _push
from .. import _search

_reference_types = ['StoredSignal', 'StoredCondition']
_calculated_types = ['CalculatedScalar', 'CalculatedSignal', 'CalculatedCondition']
_data_types = _calculated_types + _reference_types
_supported_input_types = _data_types + ['Asset']
_supported_output_types = _calculated_types + ['Asset']
_dataframe_columns = ['ID', 'Referenced ID', 'Type', 'Path', 'Depth', 'Name', 'Description',
                      'Formula', 'Formula Parameters', 'Cache Enabled']


class Tree:
    _dataframe = pd.DataFrame()
    _workbook = _common.DEFAULT_WORKBOOK_PATH
    _workbook_id = _common.EMPTY_GUID

    quiet = False

    _conditions_api = None
    _formulas_api = None
    _items_api = None
    _scalars_api = None
    _signals_api = None
    _trees_api = None
    _workbooks_api = None

    def __init__(self, data, *, description=None, workbook=None, quiet=False, status=None):
        """
        Utilizes a Python Class-based tree to produce a set of item definitions as
        a metadata DataFrame. Allows users to manipulate the tree using various functions.

        Parameters
        ----------
        data : {pandas.DataFrame, str}
            Defines which element will be inserted at the root.
            If an existing tree already exists in Seeq, the entire tree will be pulled recursively.
            If this tree doesn't already within the scope of the workbook, new tree elements
            will be created (by deep-copy or reference if applicable).
            The following options are allowed:
            1) A name string. If an existing tree with that name (case-insensitive) is found,
                all children will be recursively pulled in.
            2) An ID string of an existing item in Seeq. If that item is in a tree, all
                children will be recursively pulled in.
            3) spy.search results or other custom dataframes. The 'Path' column must be present
                and represent a single tree structure.

        description : str, optional
            The description to set on the root-level asset.

        workbook : str, default 'Data Lab >> Data Lab Analysis'
            The path to a workbook (in the form of 'Folder >> Path >> Workbook Name')
            or an ID that all pushed items will be 'scoped to'. You can
            push to the Corporate folder by using the following pattern:
            '__Corporate__ >> Folder >> Path >> Workbook Name'. A Tree currently
            may not be globally scoped. These items will not be visible/searchable 
            using the data panel in other workbooks.

        quiet : bool, default False
            If True, suppresses progress output. This setting will be used for all
            operations on this Tree.

        status : spy.Status, optional
            If specified, the supplied Status object will be updated as the command
            progresses. It gets filled in with the same information you would see
            in Jupyter in the blue/green/red table below your code while the
            command is executed. The table itself is accessible as a DataFrame via
            the status.df property.
        """
        _common.validate_argument_types([
            (data, 'data', (pd.DataFrame, str)),
            (description, 'description', str),
            (workbook, 'workbook', str),
            (quiet, 'quiet', bool),
            (status, 'status', _common.Status)
        ])
        self.quiet = quiet
        status = _common.Status.validate(status, self.quiet)
        if _login.client:
            self._conditions_api = ConditionsApi(_login.client)
            self._formulas_api = FormulasApi(_login.client)
            self._items_api = ItemsApi(_login.client)
            self._scalars_api = ScalarsApi(_login.client)
            self._signals_api = SignalsApi(_login.client)
            self._trees_api = TreesApi(_login.client)
            self._workbooks_api = WorkbooksApi(_login.client)

        self._workbook = workbook if workbook else _common.DEFAULT_WORKBOOK_PATH
        self._find_workbook_id(status)

        self._dataframe = pd.DataFrame(columns=_dataframe_columns)
        description = description if description else np.nan

        if isinstance(data, pd.DataFrame):
            if len(data) == 0:
                raise ValueError("A tree may not be created from a DataFrame with no rows")
            # TODO CRAB-24288 Allow pulling using a metadata dataframe
            raise NotImplementedError("Creating a SPy Tree from a dataframe is not currently supported")
        elif data and isinstance(data, str):
            existing_node_id = None
            if _common.is_guid(data):
                existing_node_id = data
            else:
                existing_node_id = _find_existing_root_node_id(data, status, self._trees_api, self._workbook_id)

            if existing_node_id:
                self._pull_node_recursively(existing_node_id, status=status, description=description)
            else:
                # Define a brand new root asset
                root_asset_dict = {
                    'Type': 'Asset',
                    'Path': '',
                    'Depth': 1,
                    'Name': data,
                    'Description': description
                }
                self._dataframe = self._dataframe.append(root_asset_dict, ignore_index=True)
                status.update(f"No existing root found. New root '{data}' defined."
                              f"{'' if _login.client else ' If an existing tree was expected, please log in.'}",
                              _common.Status.SUCCESS)
        else:
            raise TypeError("Input 'data' must be a name, Seeq ID, or Metadata dataframe when creating a Tree")
        _validate(self._dataframe)

    def insert(self, children, parent=None, *, friendly_name=None, formula=None, formula_params=None, errors='raise'):
        """
        Insert the specified elements into the tree.

        Parameters
        ----------
        children : {pandas.DataFrame, str, list, Tree}, optional
            Defines which element or elements will be inserted below each parent. If an existing
            node already existed at the level in the tree with that name (case-insensitive),
            it will be updated. If it doesn't already exist, a new node will be created
            (by deep-copy or reference if applicable).
            The following options are allowed:
            1) A basic string or list of strings to create a new asset.
            2) Another SPy Tree.
            3) spy.search results or other custom dataframes.

        parent : {pandas.DataFrame, str, int}, optional
            Defines which element or elements the children will be inserted below.
            If a parent match is not found and non-glob/regex string or path is used,
            the parent (or entire path) will be created too.
            The following options are allowed:
            1) No parent specified will insert directly to the root of the tree.
            2) String name match (case-insensitive equality, globbing, regex, column
                values) will find any existing nodes in the tree that match.
            3) String path match, including partial path matches.
            4) ID. This can either be the actual ID of the tree.push()ed node or the
                ID of the source item.
            5) Number specifying tree level. This will add the children below every
                node at the specified level in the tree (1 being the root node).
            6) spy.search results or other custom dataframe.


        friendly_name : str, optional
            Use this specified name rather than the referenced item's original name.

        formula : str, optional
            The formula for a calculated item. The `formula` and `formula_parameters` are
            used in place of the `children` argument.

        formula_params : dict, optional
            The parameters for a formula.

        errors : {'raise', 'catalog'}, default 'raise'
            If 'raise', any errors encountered will cause an exception. If 'catalog',
            errors will be added to a 'Result' column in the status.df DataFrame.
        """

        if isinstance(children, pd.DataFrame) or isinstance(parent, pd.DataFrame):
            # TODO CRAB-24290 Insert with parents & children defined by dataframes
            # TODO CRAB-24298 Insert using Column Values from a dataframe
            raise NotImplementedError('Inserting using DataFrames is not currently supported.')

        if isinstance(children, Tree):
            # TODO CRAB-24485 Insert a Tree object
            raise NotImplementedError('Inserting a Tree object is not currently supported.')

        if children is None:
            if formula and formula_params:
                # TODO CRAB-24291 Insert calculations
                raise NotImplementedError('Inserting calculations is not currently supported')
            else:
                raise ValueError('Formula and formula parameters must be specified if no children argument is given.')
        else:
            if formula or formula_params:
                raise ValueError('Formula and formula parameters must be None if a children argument is given.')

        _common.validate_argument_types([
            (children, 'children', (pd.DataFrame, Tree, str, list)),
            (parent, 'parent', (pd.DataFrame, str, int)),
            (friendly_name, 'friendly_name', str),
            (formula, 'formula', str),
            (formula_params, 'formula_params', dict),
            (errors, 'errors', str)
        ])
        _common.validate_errors_arg(errors)

        if isinstance(children, str):
            children = [children]
        if isinstance(children, list):
            children = pd.DataFrame({
                'Name': pd.Series(children, dtype='string'),
                'Type': 'Asset'
            })
        elif isinstance(children, Tree):
            children = children._dataframe
        parents_found = pd.Series(data=False, index=children.index)

        insertion_df = pd.DataFrame(columns=_dataframe_columns + ['Result'])
        error_summaries = []
        children_added_count = 0
        children_failed_count = 0
        working_df = self._dataframe if errors == 'catalog' else self._dataframe.copy()

        def _print_error_summaries(summaries, added_count, failed_count):
            print(
                f'Failed to insert {failed_count} items of {added_count + failed_count}'
                f' attempted. See the outputted dataframe for details.')
            print(_format_error_summaries(summaries))

        def _insert_block(insertions, insertion_index):
            nonlocal working_df, insertion_df, error_summaries, children_added_count, children_failed_count
            working_df, new_insertion_df, new_error_summaries, num_success, num_failure = _validate_and_insert(
                working_df, insertions, insertion_index)
            insertion_df = insertion_df.append(new_insertion_df, ignore_index=True)
            error_summaries += new_error_summaries
            children_added_count += num_success
            children_failed_count += num_failure
            if num_failure and errors == 'raise':
                # We will eventually make exceptions more readable using Status objects. This is somewhat of a
                # placeholder
                _print_error_summaries(error_summaries, children_added_count, children_failed_count)
                raise RuntimeError('Error encountered while inserting.')

        def _get_children_to_add(children_df, parent_node, matched=None):
            children_to_add = children_df.copy()
            # TODO CRAB-24290, CRAB-24291: handle pre-existing children paths
            # TODO CRAB-24298: filter children by column names using the match object
            parents_found[:] = True
            children_to_add['Path'] = f"{parent_node['Path']} >> {parent_node['Name']}" if parent_node['Depth'] != 1 \
                else parent_node['Name']
            children_to_add['Depth'] = parent_node['Depth'] + 1
            return children_to_add

        if isinstance(parent, str) and not _common.is_guid(parent):
            pattern = _node_match_string_to_regex(parent)
            for i in range(len(working_df.index)):
                index = children_added_count + i
                node = working_df.iloc[index]
                match = _node_match_using_regex(node, pattern)
                if match:
                    children_to_add = _get_children_to_add(children, node, match)
                    _insert_block(children_to_add, index)

        else:
            for i in range(len(working_df.index)):
                index = children_added_count + i
                node = working_df.iloc[index]
                if _node_match_no_regex(node, parent):
                    children_to_add = _get_children_to_add(children, node)
                    _insert_block(children_to_add, index)

        children_with_no_parents_found = children[~parents_found]
        children_with_no_parents_found['Result'] = 'Ignored: No matching parent found.'
        insertion_df = pd.concat([insertion_df, children_with_no_parents_found], ignore_index=True)

        if children_failed_count and errors == 'catalog':
            _print_error_summaries(error_summaries, children_added_count, children_failed_count)

        if errors == 'raise':
            self._dataframe = working_df

        self.summarize()
        return insertion_df

    def remove(self, elements, *, errors='raise'):
        """
        Remove the specified elements from the tree recursively.

        Parameters
        ----------
        elements : {pandas.DataFrame, str, int}
            Defines which element or elements will be removed.
            1) String name match (case-insensitive equality, globbing, regex, column
                values) will find any existing nodes in the tree that match.
            2) String path match, including partial path matches.
            3) ID. This can either be the actual ID of the tree.push()ed node or the
                ID of the source item.
            4) Number specifying tree level. This will add the children below every
                node at the specified level in the tree (1 being the root node).
            5) spy.search results or other custom dataframe.

        errors : {'raise', 'catalog'}, default 'raise'
            If 'raise', any errors encountered will cause an exception. If 'catalog',
            errors will be added to a 'Result' column in the status.df DataFrame.
        """
        _common.validate_errors_arg(errors)
        # TODO CRAB-24292 Allow removing nodes
        raise NotImplementedError('Removing is not currently supported')

        _validate(self._dataframe)
        return self.summarize()

    def move(self, source, *, destination=None, errors='raise'):
        """
        Move the specified elements (and all children) from one location in
        the tree to another.

        Parameters
        ----------
        source : {pandas.DataFrame, str}
            Defines which element or elements will be removed.
            1) String path match.
            2) ID. This can either be the actual ID of the tree.push()ed node or the
                ID of the source item.
            3) spy.search results or other custom dataframe.
            4) Another SPy Tree.

        destination : {pandas.DataFrame, str}; optional
            Defines which element or elements will be removed.
            1) No destination specified will move the elements to just below
              the root of the tree.
            2) String path match.
            3) ID. This can either be the actual ID of the tree.push()ed node or the
                ID of the source item.
            4) spy.search results or other custom dataframe.
            5) Another SPy Tree (root).

        errors : {'raise', 'catalog'}, default 'raise'
            If 'raise', any errors encountered will cause an exception. If 'catalog',
            errors will be added to a 'Result' column in the status.df DataFrame.
        """
        _common.validate_errors_arg(errors)
        # TODO CRAB-24293 Allow moving nodes
        _validate(self._dataframe)
        raise NotImplementedError('Moving is not currently supported')
        return self.summarize()

    def summarize(self):
        """
        Generate a human-readable summary of the tree.
        """
        # TODO CRAB-24297 Add tree comprehension functions
        return f'This is a tree of height ...'

    def missing_items(self):
        """
        Identify elements that may be missing child elements based on the contents of other sibling nodes.
        """
        missing_items = list()
        # TODO CRAB-24297 Add tree comprehension functions
        raise NotImplementedError('Finding missing items is not currently supported')
        if len(missing_items):
            missing_string = 'The following elements appear to be missing:'
            for missing_entry in missing_items:
                missing_string += f"\n{missing_entry.parent} is missing: {', '.join(missing_entry.children)}"
            return missing_string
        else:
            return 'No items are detected as missing.'

    def push(self, *, errors='raise'):
        """
        Imports the tree into Seeq Server.

        Parameters
        ----------
        errors : {'raise', 'catalog'}, default 'raise'
            If 'raise', any errors encountered will cause an exception. If 'catalog',
            errors will be added to a 'Result' column in the status.df DataFrame.
        """
        _common.validate_errors_arg(errors)
        error_summaries, error_details, num_bad_nodes = _validate(self._dataframe)
        if num_bad_nodes and errors == 'raise':
            raise RuntimeError(_format_error_summaries(error_summaries))

        return _push.push(metadata=self._dataframe, workbook=self._workbook, errors=errors)

    def _find_workbook_id(self, status):
        """
        Set the _workbook_id based on the workbook input. This will enable us to know whether we should set
        the `ID` or `Referenced ID` column when pulling an item.
        """
        if _common.is_guid(self._workbook):
            self._workbook_id = _common.sanitize_guid(self._workbook)
        elif self._workbooks_api:
            search_query, _ = _push.create_analysis_search_query(self._workbook)
            search_df = spy.workbooks.search(search_query,
                                             status=status.create_inner('Find Workbook', quiet=self.quiet))
            self._workbook_id = search_df.iloc[0]['ID'] if len(search_df) > 0 else _common.EMPTY_GUID
        else:
            self._workbook_id = _common.EMPTY_GUID

    def _validate(self):
        error_summaries_properties, error_details_properties = self._validate_properties()
        error_summaries_tree, error_details_tree = self._validate_tree()

        error_string = None
        if error_summaries_properties or error_summaries_tree:
            error_string = f'{len(error_details_properties) + len(error_details_tree)} errors were found in the tree.\n'
            error_string += '\n- '.join(error_summaries_properties + error_summaries_tree)

        error_dataframe = None
        if len(error_details_properties) or len(error_details_tree):
            error_dataframe = pd.concat([error_details_properties, error_details_tree])

        return error_string, error_dataframe

    def _validate_properties(self):
        # TODO CRAB-24294, CRAB-24296 Validate dataframe rows by properties
        return [], pd.DataFrame()

    def _validate_tree(self):
        # TODO CRAB-24295 Validate tree structure
        return [], pd.DataFrame()

    def _pull_node_recursively(self, node_id, status, description=None, path=None):
        """
        Given the ID of an Item, pulls that node and all children recursively and places it into the tree at the
        specified path.
        """
        if not self._items_api or not self._formulas_api:
            raise RuntimeError('Not logged in. Execute spy.login() before calling this function.')
        # Get the requested node itself
        root_node_dict = _pull_node_as_tree_dict(self._items_api, self._formulas_api, self._workbook_id, node_id, path)
        if not root_node_dict:
            return
        is_pulled_tree_from_spy = root_node_dict['ID'] is not np.nan
        root_node_dict['Description'] = _common.none_to_nan(description)
        self._dataframe = self._dataframe.append(root_node_dict, ignore_index=True)

        status.update(f"Recursively pulling {'SPy-created' if is_pulled_tree_from_spy else 'existing'} "
                      f"asset tree with root element '{root_node_dict['Name']}' (ID: {node_id}).",
                      _common.Status.RUNNING)

        # Get all children of the requested asset
        search_results = _search.search(query={'Asset': node_id}, all_properties=True, workbook=self._workbook_id,
                                        status=status.create_inner('Find Children', quiet=self.quiet))
        for index, row in search_results.iterrows():
            child_node_dict = _convert_search_row_to_tree_dict(row, search_results.columns,
                                                               root_node_dict['Name'], is_pulled_tree_from_spy)
            if child_node_dict:
                self._dataframe = self._dataframe.append(child_node_dict, ignore_index=True)
                status.update(f"Pulled {len(self._dataframe)} elements so far.", _common.Status.RUNNING)
        _sort_by_node_path(self._dataframe)

        status.update(f"Recursively pulled {'SPy-created' if is_pulled_tree_from_spy else 'existing'} "
                      f"asset tree with root element '{root_node_dict['Name']}' (ID: {node_id}):"
                      f"\n{self.summarize()}", _common.Status.SUCCESS)

    def _find_workbook_id(self, status):
        """
        Set the _workbook_id based on the workbook input. This will enable us to know whether we should set
        the `ID` or `Referenced ID` column when pulling an item.
        """
        if _common.is_guid(self._workbook):
            self._workbook_id = _common.sanitize_guid(self._workbook)
        elif self._workbooks_api:
            search_query, _ = _push.create_analysis_search_query(self._workbook)
            search_df = spy.workbooks.search(search_query,
                                             status=status.create_inner('Find Workbook', quiet=self.quiet))
            self._workbook_id = search_df.iloc[0]['ID'] if len(search_df) > 0 else _common.EMPTY_GUID
        else:
            self._workbook_id = _common.EMPTY_GUID

    def _pull_node_recursively(self, node_id, status, description=None, path=None):
        """
        Given the ID of an Item, pulls that node and all children recursively and places it into the tree at the
        specified path.
        """
        if not self._items_api or not self._formulas_api:
            raise RuntimeError('Not logged in. Execute spy.login() before calling this function.')
        # Get the requested node itself
        root_node_dict = _pull_node_as_tree_dict(self._items_api, self._formulas_api, self._workbook_id, node_id, path)
        if not root_node_dict:
            return
        is_pulled_tree_from_spy = root_node_dict['ID'] is not np.nan
        root_node_dict['Description'] = _common.none_to_nan(description)
        self._dataframe = self._dataframe.append(root_node_dict, ignore_index=True)

        status.update(f"Recursively pulling {'SPy-created' if is_pulled_tree_from_spy else 'existing'} "
                      f"asset tree with root element '{root_node_dict['Name']}' (ID: {node_id}).",
                      _common.Status.RUNNING)

        # Get all children of the requested asset
        search_results = _search.search(query={'Asset': node_id}, all_properties=True, workbook=self._workbook_id,
                                        status=status.create_inner('Find Children', quiet=self.quiet))

        for index, row in search_results.iterrows():
            child_node_dict = _convert_search_row_to_tree_dict(row, search_results.columns,
                                                               root_node_dict['Name'], is_pulled_tree_from_spy)
            if child_node_dict:
                self._dataframe = self._dataframe.append(child_node_dict, ignore_index=True)
                status.update(f"Pulled {len(self._dataframe)} elements so far.", _common.Status.RUNNING)

        _sort_by_node_path(self._dataframe)

        status.update(f"Recursively pulled {'SPy-created' if is_pulled_tree_from_spy else 'existing'} "
                      f"asset tree with root element '{root_node_dict['Name']}' (ID: {node_id}):"
                      f"\n{self.summarize()}", _common.Status.SUCCESS)


def _sort_by_node_path(df):
    df['Temp Sort Key'] = df.apply(lambda node: _common.path_string_to_list(_get_full_path(node)), axis=1)
    df.sort_values(by='Temp Sort Key', inplace=True, ignore_index=True)
    df.drop('Temp Sort Key', axis=1, inplace=True)


def _validate_and_insert(df, insertions, insertion_index):
    """
    Validate and perform an insertion.

    :param df: The dataframe representing a tree object into which the insertions will be made
    :param insertions: A dataframe of rows to be inserted (without modification) into df
    :param insertion_index: The (numerical) index of df below which the nodes will be inserted
    :return: out_df: The updated dataframe obtained by performing all valid insertions into df
    :return: insertion_df: A copy of `insertions` with a new 'Result' column
    :return: error_summaries: A list of strings summarizing all errors encountered while validating the insertions
    :return: num_success: Integer specifying the number of successful insertions
    :return: num_failure: Integer specifying the number of failed insertions
    """
    error_summaries, error_details, num_success, num_failure = _validate_insertion(df, insertions,
                                                                                   insertion_index)

    out_df = pd.concat([
        df.iloc[:insertion_index + 1],
        insertions[error_details == ''],
        df.iloc[insertion_index + 1:]
    ], ignore_index=True)

    insertion_df = insertions.copy()
    insertion_df['Result'] = error_details

    def _error_to_result(msg):
        if msg == '':
            return 'Success'
        else:
            return 'Failure: ' + msg

    insertion_df['Result'] = insertion_df['Result'].apply(_error_to_result)
    return out_df, insertion_df, error_summaries, num_success, num_failure


def _validate_insertion(df, insertions, insertion_index):
    """
    Validate that a collection of rows to be inserted into a dataframe representing an asset tree will not put that
    tree into a bad state.

    :param df: The dataframe representing the tree that is being operated on
    :param insertions: A dataframe of rows that will be tentatively inserted into df
    :param insertion_index: The index under which to insert
    :return: error_summaries: A list of strings summarizing all errors encountered while validating the insertions
    :return: error_details: A pd.Series object whose index is the same as `insertions` and whose data specifies
    errors specific to the corresponding row in `insertions`
    :return: num_success: Integer specifying the number of insertions that can be performed successfully
    :return: num_failure: Integer specifying the number of insertions that would put the tree in a bad state
    """
    error_summaries_properties, error_details_properties = _validate_properties(insertions)
    error_summaries_tree, error_details_tree = _validate_insertion_tree_structure(df, insertions, insertion_index)

    error_summaries = error_summaries_properties + error_summaries_tree
    error_details = _update_error_msg(error_details_properties, error_details_tree)

    num_failure = len(error_details[error_details != ''].index)
    num_success = len(error_details.index) - num_failure

    return error_summaries, error_details, num_success, num_failure


def _validate_insertion_tree_structure(df, insertions, insertion_index):
    # Check:
    # - That the 'Path' and 'Depth' columns reflect that performing the insertions will maintain a DFS tree traversal
    # order when inserted into df
    # - That no parent node has two children with the same name (so paths are unambiguous)
    # - Will check more when we introduce Calculations and Stored Items, not just bare Assets
    # Assumptions:
    # - df represents a valid asset tree
    # - All nodes in `insertions` are intended to lie below the parent node df.iloc[insertion_index] after being
    # inserted

    num_insertions = len(insertions.index)
    if num_insertions == 0:
        return [], pd.Series()
    ambiguous_names = set()
    error_series = pd.Series('', index=insertions.index, dtype='string')

    insertion_parent = df.iloc[insertion_index]
    insertion_parent_children_names = df[df['Path'] == _get_full_path(insertion_parent)]['Name'].tolist()
    _validate_tree_rec(parent=insertion_parent, node_df=insertions, current_index=0, num_nodes=num_insertions,
                       error_series=error_series, ambiguous_names=ambiguous_names,
                       preexisting_children_names=insertion_parent_children_names,
                       root=True, dead_path_msg='Node\'s parent could not be inserted.')

    error_summaries = _write_error_summaries(insertions, error_series,
                                             'Attempted to insert a node with path "{}" and name "{}":')
    _handle_ambiguous_names(insertions, error_summaries, error_series, ambiguous_names)

    return error_summaries, error_series


def _validate(df):
    """
    Validate that df represents a valid asset tree that can be pushed to Workbench

    CAUTION: Use this function sparingly. We ideally do not want to have to iterate through the entire dataframe each
    time we invoke a method on a Tree object. If at all possible, use this validation function and its
    subfunctions as a template for writing functions that validate specific methods of the Tree class.

    :param df: The dataframe representing the asset tree
    :return: error_summaries: A list of strings summarizing all errors encountered while validating the dataframe
    :return: error_details: A pd.Series object whose index is the same as df and whose data specifies errors specific
    to the corresponding row in df
    :return: num_bad_nodes: Integer specifying the number of invalid nodes found
    """
    error_summaries_properties, error_details_properties = _validate_properties(df)
    error_summaries_tree, error_details_tree = _validate_tree_structure(df)

    error_summaries = error_summaries_properties + error_summaries_tree
    error_details = _update_error_msg(error_details_properties, error_details_tree)

    num_bad_nodes = len(error_details[error_details != ''].index)

    return error_summaries, error_details, num_bad_nodes


def _validate_tree_structure(df):
    # Check:
    # - That the 'Path' and 'Depth' columns reflect that the order of the nodes in df specify a DFS tree traversal order
    # - That no parent node has two children with the same name (so paths are unambiguous)
    # - Will check more when we introduce Calculations and Stored Items, not just bare Assets
    # Assumptions:
    # - None currently

    size = len(df.index)
    if size == 0:
        return ['Tree must be non-empty.'], pd.Series()
    ambiguous_names = set()
    error_series = pd.Series('', index=df.index, dtype='string')

    root_node = df.iloc[0]
    if not _is_valid_root_path(root_node['Path']):
        error_series.iloc[0] = f'The root of the tree has the following malformed path: "{root_node["Path"]}".'
        dead_tree = True
    else:
        dead_tree = False

    _validate_tree_rec(parent=root_node, node_df=df, current_index=1, num_nodes=size, error_series=error_series,
                       ambiguous_names=ambiguous_names, dead_path=dead_tree, root=True)

    error_summaries = _write_error_summaries(df, error_series,
                                             'Invalid node with path "{}" and name "{}":')
    _handle_ambiguous_names(df, error_summaries, error_series, ambiguous_names)

    return error_summaries, error_series


def _validate_tree_rec(parent, node_df, current_index, num_nodes, error_series, ambiguous_names,
                       preexisting_children_names=None, dead_path=False, root=False,
                       dead_path_msg='Node\'s parent is invalid.'):
    if preexisting_children_names is None:
        preexisting_children_names = []
    while current_index < num_nodes and (node_df.iloc[current_index]['Depth'] > parent['Depth'] or root):
        child = node_df.iloc[current_index]
        if dead_path:
            error_message = dead_path_msg
        else:
            error_message = _validate_parent_child_relationship(parent, child)
        error_series[current_index] = _update_error_msg(error_series[current_index], error_message)
        if child['Name'] in preexisting_children_names:
            ambiguous_names.add((child['Path'], child['Name']))
        else:
            preexisting_children_names.append(child['Name'])
        current_index = _validate_tree_rec(child, node_df, current_index + 1, num_nodes, error_series,
                                           ambiguous_names,
                                           dead_path=dead_path or error_message,
                                           root=False,
                                           dead_path_msg=dead_path_msg)
    return current_index


def _write_error_summaries(data, error_series, summary_header_format):
    error_headers = pd.Series({
        i: summary_header_format.format(data.loc[i]['Path'], data.loc[i]['Name'])
        if error_series[i] != '' else '' for i in data.index
    }, dtype='string', index=data.index)
    full_errors = _update_error_msg(error_headers, error_series)
    return full_errors[full_errors != ''].tolist()


def _handle_ambiguous_names(data, error_summaries, error_series, ambiguous_names):
    for path, name in ambiguous_names:
        error_message = f'Tree cannot have multiple nodes with path "{path}" and name "{name}".'
        error_summaries.append(error_message)
        bad_indices = (data['Path'] == path) & (data['Name'] == name)
        error_series[bad_indices] = _update_error_msg(error_series[bad_indices], error_message)


def _validate_parent_child_relationship(parent, child):
    if child['Path'] != _get_full_path(parent):
        return f'Node\'s parent has mismatching path. Full path of invalid parent: "{_get_full_path(parent)}".'
    elif child['Depth'] != parent['Depth'] + 1:
        return f'Node\'s depth must be one more than the depth of its parent. Node depth: ' \
               f'{child["Depth"]}. Depth of parent: {parent["Depth"]}.'
    else:
        return None


def _validate_properties(df):
    # TODO CRAB-24294, CRAB-24296 Validate dataframe rows by properties
    return [], pd.Series('', dtype='string', index=df.index)


def _update_error_msg(old_msg, new_msg):
    if new_msg is None or isinstance(new_msg, str) and new_msg == '':
        return old_msg
    out = old_msg + ' ' + new_msg
    if isinstance(out, pd.Series):
        return out.str.strip()
    else:
        return out.strip()


def _format_error_summaries(error_summaries):
    if len(error_summaries) == 0:
        return None
    else:
        return '- ' + '\n- '.join(error_summaries)


def _get_full_path(node):
    if node['Depth'] == 1:
        return node['Name']
    else:
        return f"{node['Path']} >> {node['Name']}"


def _is_valid_root_path(path):
    try:
        if np.isnan(path):
            return True
    except TypeError:
        return path is None or path == ''


def _node_match_string_to_regex(pattern):
    """
    :param pattern: String name match (case-insensitive equality, globbing, regex, column values)
                    or string path match (full or partial; case-insensitive equality, globbing, or regex)
    :return: A regular expression that matches correctly on f"{node['Path']} >> {node['Name']}"
    """
    # TODO: CRAB-24298 incorporate column values into this regex match
    # This will require using groups to sort of invert the column value matching -- this will be a little
    # difficult to logic through, but will make it so we don't have to iterate through self._dataframe more
    # than once during an insert
    patterns = _common.path_string_to_list(pattern)
    return [_exact_or_glob_or_regex(p) for p in patterns]


def _exact_or_glob_or_regex(pat):
    try:
        re.compile(pat)
        return re.compile('(?i)' + '(' + ')|('.join([re.escape(pat), fnmatch.translate(pat), pat]) + ')')
    except re.error:
        return re.compile('(?i)' + '(' + ')|('.join([re.escape(pat), fnmatch.translate(pat)]) + ')')


def _node_match_using_regex(node, pattern_list):
    path_list = _common.path_string_to_list(_get_full_path(node))
    offset = len(path_list) - len(pattern_list)
    if offset < 0:
        return None
    out = []
    for i in range(len(pattern_list)):
        match = pattern_list[i].fullmatch(path_list[offset + i])
        if match is None:
            return None
        out.append(match)
    return out


def _node_match_no_regex(node, pattern):
    if pattern is None:
        return node['Depth'] == 1
    if isinstance(pattern, int):
        return node['Depth'] == pattern
    if isinstance(pattern, pd.DataFrame):
        # TODO CRAB-24290 Insert with parents & children defined by dataframes
        return False
    if isinstance(pattern, str):
        if isinstance(node['ID'], str) and pattern.upper() == node['ID'].upper():
            return True
        if isinstance(node['Referenced ID'], str) and pattern.upper() == node['Referenced ID'].upper():
            return True
    return False


def _find_existing_root_node_id(name, status, trees_api=None, workbook_id=None):
    """
    Finds the Seeq ID of a case-insensitive name match of existing root nodes.
    """
    if not trees_api:
        # User is not logged in or this is a unit test. We must create a new tree.
        return None
    name_pattern = re.compile('(?i)^' + re.escape(name) + '$')
    matching_root_nodes = list()

    offset = 0
    limit = _config.options.search_page_size
    kwargs = dict()
    # Can't use get_tree_root_nodes()'s `properties` filter for scoped_to because the endpoint is case-sensitive and
    # we want both global and scoped nodes.
    if workbook_id and workbook_id is not _common.EMPTY_GUID:
        kwargs['scoped_to'] = workbook_id

    status.update('Finding best root.', _common.Status.RUNNING)
    keep_going = True
    while keep_going:
        kwargs['offset'] = offset
        kwargs['limit'] = limit
        root_nodes = trees_api.get_tree_root_nodes(**kwargs)  # type: AssetTreeOutputV1
        for root_node in root_nodes.children:  # type: TreeItemOutputV1
            if name_pattern.match(root_node.name):
                # A root node matching the name was already found. Choose a best_root_node based on this priority:
                # Workbook-scoped SPy assets > workbook-scoped assets > global SPy assets > global assets
                has_scope = hasattr(root_node, 'scoped_to') and _common.is_guid(root_node.scoped_to)
                workbook_scoped_score = 2 if has_scope else 0
                spy_created_score = 0
                if hasattr(root_node, 'properties'):
                    for prop in root_node.properties:  # type: PropertyOutputV1
                        if prop.name == 'Datasource Class' and prop.value == 'Seeq Data Lab':
                            spy_created_score = 1
                            break
                matching_root_nodes.append({'id': root_node.id, 'score': workbook_scoped_score + spy_created_score})

        status.update(f'Finding best root. {len(matching_root_nodes)} matches out of {offset + limit} roots requested.',
                      _common.Status.RUNNING)
        keep_going = root_nodes.next is not None
        offset = offset + limit
    if len(matching_root_nodes) == 0:
        status.update(f"No existing root items were found matching '{name}'.", _common.Status.RUNNING)
        return None
    best_score = max([n['score'] for n in matching_root_nodes])
    best_root_nodes = list(filter(lambda n: n['score'] == best_score, matching_root_nodes))
    if len(best_root_nodes) > 1:
        raise ValueError(
            f"More than one existing tree was found with name '{name}'. Please use an ID to prevent ambiguities.")
    best_id = best_root_nodes[0]['id']
    if len(matching_root_nodes) > 1:
        status.update(f"{len(matching_root_nodes)} root items were found matching '{name}'. Selecting {best_id}.",
                      _common.Status.RUNNING)
    return best_id


def _add_tree_property(properties, key, value):
    """
    If the property is one which is used by SPy Trees, adds the key+value pair to the dict.
    """
    if key in _dataframe_columns:
        value = _common.none_to_nan(value)
        if isinstance(value, str) and key in ['Cache Enabled', 'Archived', 'Enabled', 'Unsearchable']:
            # Ensure that these are booleans. Otherwise Seeq Server will silently ignore them.
            value = (value.lower() == 'true')
        properties[key] = value
    return properties


def _pull_node_as_tree_dict(items_api, formulas_api, workbook_id, node_id, path=None):
    """
    Given the ID of an Item, pulls that node and places it into the tree at the specified path.
    """
    if not items_api or not formulas_api:
        raise RuntimeError('Not logged in. Execute spy.login() before calling this function.')

    node = items_api.get_item_and_all_properties(id=node_id)  # type: ItemOutputV1
    node_dict = dict()

    # Extract only the properties we use
    node_dict['Name'] = node.name
    node_dict['Type'] = node.type
    node_dict['ID'] = node.id  # If this should be a copy, it'll be converted to 'Referenced ID' later
    for prop in node.properties:  # type: PropertyOutputV1
        _add_tree_property(node_dict, prop.name, prop.value)

    # Figure out the path-related columns
    node_dict['Path'] = path if path else ''
    if node_dict['Path'] is '':
        node_dict['Depth'] = 1
    else:
        node_dict['Depth'] = node_dict['Path'].count('>>') + 2

    # If this is a referenced item, push() should make a copy instead of updating the original
    is_pulled_node_from_spy = node.scoped_to and node.scoped_to.lower() == workbook_id.lower()

    if node.type in _data_types and not is_pulled_node_from_spy:
        # Data items will be made into Reference Formulas (unless this already was a SPy-made Tree)
        _metadata._build_reference(node_dict)
    elif node.type in _calculated_types:
        # Calculated items from an existing SPy Tree will be pulled in as direct Formulas.
        formula_output = formulas_api.get_item(id=node.id)  # type: FormulaItemOutputV1
        node_dict['Formula Parameters'] = [
            '%s=%s' % (p.name, p.item.id if p.item else p.formula) for p in formula_output.parameters
        ]
    elif node.type not in _supported_input_types:
        # TODO CRAB-24637: Allow Threshold Metrics to be pulled in too.
        return None
    if not is_pulled_node_from_spy:
        node_dict['ID'] = np.nan
        node_dict['Referenced ID'] = node.id
    return node_dict


def _convert_search_row_to_tree_dict(row, search_result_columns, parent_node_name, is_pulled_tree_from_spy):
    """
    Converts a row from search() to a dict compatible with the Tree data.
    """
    # Extract only the properties we use
    node_dict = dict()

    for column in search_result_columns:
        _add_tree_property(node_dict, column, row[column])
    if node_dict['Type'] and node_dict['Type'] not in _supported_input_types:
        # TODO CRAB-24637: Allow Threshold Metrics to be pulled in too.
        return None

    # Figure out the path-related columns
    if not isinstance(row['Path'], str):
        row['Path'] = None
    if not isinstance(row['Asset'], str):
        row['Asset'] = None
    path = ''
    if row['Path'] and row['Asset']:
        path = ' >> '.join([row['Path'], row['Asset']])
    elif row['Asset']:
        path = row['Asset']
    if (parent_node_name + ' >> ') in path:
        path = parent_node_name + ' >> ' + path.split(parent_node_name + ' >> ', 1)[1]
    elif path.endswith(parent_node_name):
        path = parent_node_name
    node_dict['Path'] = path
    node_dict['Depth'] = node_dict['Path'].count('>>') + 2
    node_dict['ID'] = row['ID']

    if is_pulled_tree_from_spy:
        node_dict['ID'] = row['ID']
    else:
        # If we are pulling a tree that was not made by SPy, push() should make a copy instead of updating the original
        if node_dict['Type'] in _data_types:
            _metadata._build_reference(node_dict)
        elif node_dict['Type'] not in _supported_input_types:
            # TODO CRAB-24637: Allow Threshold Metrics to be pulled in too.
            return None
        node_dict['ID'] = np.nan
        node_dict['Referenced ID'] = row['ID']
    return node_dict
