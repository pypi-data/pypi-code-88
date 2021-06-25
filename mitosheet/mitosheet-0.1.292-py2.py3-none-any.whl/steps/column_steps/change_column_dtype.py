#!/usr/bin/env python
# coding: utf-8

# Copyright (c) Mito.
# Distributed under the terms of the Modified BSD License.

"""
A step that allows changing the dtype of a column to a different
dtype.

Currently, supports: 'bool', 'int', 'float', 'str', 'datetime', 'timedelta'
"""
from mitosheet.mito_analytics import log
from mitosheet.errors import make_invalid_column_type_change_error
from mitosheet.sheet_functions.types.to_number_series import to_number_series
from mitosheet.sheet_functions.types.to_boolean_series import to_boolean_series
from mitosheet.sheet_functions.types.utils import (
    get_datetime_format, get_mito_type, is_bool_dtype, is_float_dtype, is_int_dtype,
    is_string_dtype, is_datetime_dtype, is_timedelta_dtype
) 
import pandas as pd
from mitosheet.utils import create_new_step

CHANGE_COLUMN_DTYPE_DISPLAY_NAME = 'Change column dtype'

CHANGE_COLUMN_DTYPE_EVENT = 'change_column_dtype_edit'
CHANGE_COLUMN_DTYPE_STEP_TYPE = 'change_column_dtype'


CHANGE_COLUMN_DTYPE_PARAMS = [
    'sheet_index',
    'column_header',
    'old_dtype', # saturated
    'new_dtype',
]

def saturate_change_column_dtype(
        curr_step,
        event
    ):
    """
    Fills in the old_dtype variable!
    """
    event['old_dtype'] = str(curr_step['dfs'][event['sheet_index']][event['column_header']].dtype)


def execute_change_column_dtype(
        curr_step,
        sheet_index,
        column_header,
        old_dtype,
        new_dtype
    ):
    """
    Executes the dtype change on the specific column
    """
    # Create a new step
    new_step = create_new_step(curr_step, CHANGE_COLUMN_DTYPE_STEP_TYPE)
    
    column: pd.Series = new_step['dfs'][sheet_index][column_header]
    new_column = column

    # How we handle the type conversion depends on what type it is
    try:
        if is_bool_dtype(old_dtype):
            if is_bool_dtype(new_dtype):
                pass
            elif is_int_dtype(new_dtype):
                new_column = new_column.astype('int')
            elif is_float_dtype(new_dtype):
                new_column = column.astype('float')
            elif is_string_dtype(new_dtype):
                new_column = column.astype('str')
            elif is_datetime_dtype(new_dtype):
                raise make_invalid_column_type_change_error(
                    column_header,
                    old_dtype,
                    new_dtype
                )
            elif is_timedelta_dtype(new_dtype):
                raise make_invalid_column_type_change_error(
                    column_header,
                    old_dtype,
                    new_dtype
                )
        if is_int_dtype(old_dtype):
            if is_bool_dtype(new_dtype):
                new_column = column.astype('bool')
            elif is_int_dtype(new_dtype):
                pass
            elif is_float_dtype(new_dtype):
                new_column = column.astype('float')
            elif is_string_dtype(new_dtype):
                new_column = column.astype('str')
            elif is_datetime_dtype(new_dtype):
                new_column = pd.to_datetime(
                    column, 
                    unit='s',
                    errors='coerce'
                )
            elif is_timedelta_dtype(new_dtype):
                new_column = pd.to_timedelta(
                    column, 
                    unit='s',
                    errors='coerce'
                )
        elif is_float_dtype(old_dtype):
            if is_bool_dtype(new_dtype):
                new_column = column.astype('bool')
            elif is_int_dtype(new_dtype):
                new_column = column.astype('int')
            elif is_float_dtype(new_dtype):
                pass
            elif is_string_dtype(new_dtype):
                new_column = column.astype('str')
            elif is_datetime_dtype(new_dtype):
                new_column = pd.to_datetime(
                    column, 
                    unit='s',
                    errors='coerce'
                )
            elif is_timedelta_dtype(new_dtype):
                new_column = pd.to_timedelta(
                    column, 
                    unit='s',
                    errors='coerce'
                )
        elif is_string_dtype(old_dtype):
            if is_bool_dtype(new_dtype):
                new_column = to_boolean_series(new_column)
            elif is_int_dtype(new_dtype):
                new_column = to_number_series(column).astype('int')
            elif is_float_dtype(new_dtype):
                new_column = to_number_series(column)
            elif is_string_dtype(new_dtype):
                pass
            elif is_datetime_dtype(new_dtype):
                # Guess the datetime format to the best of Pandas abilities
                datetime_format = get_datetime_format(column)
                # If it's None, then infer_datetime_format is enough to figure it out
                if datetime_format is not None:
                    # Save the datetime format in the string so that we have an easier
                    # time transpiling it in the future
                    new_step['datetime_format'] = datetime_format
                    new_column = pd.to_datetime(
                        column,
                        format=datetime_format,
                        errors='coerce'
                    )
                else:
                    new_column = pd.to_datetime(
                        column,
                        infer_datetime_format=True,
                        errors='coerce'
                    )
            elif is_timedelta_dtype(new_dtype):
                new_column = pd.to_timedelta(
                    column,
                    errors='coerce'
                )
        elif is_datetime_dtype(old_dtype):
            if is_bool_dtype(new_dtype):
                new_column = ~column.isnull()
            elif is_int_dtype(new_dtype):
                new_column = column.astype('int') / 10**9
            elif is_float_dtype(new_dtype):
                # For some reason, we have to do all the conversions at once
                new_column = column.astype('int').astype('float') / 10**9
            elif is_string_dtype(new_dtype):
                # NOTE: this is the same conversion that we send to the frontend
                new_column = column.dt.strftime('%Y-%m-%d %X')
            elif is_datetime_dtype(new_dtype):
                pass
            elif is_timedelta_dtype(new_dtype):
                raise make_invalid_column_type_change_error(
                    column_header,
                    old_dtype,
                    new_dtype
                )
        elif is_timedelta_dtype(old_dtype):
            if is_bool_dtype(new_dtype):
                new_column = ~column.isnull()
            elif is_int_dtype(new_dtype):
                new_column = column.dt.total_seconds().astype('int')
            elif is_float_dtype(new_dtype):
                new_column = column.dt.total_seconds()
            elif is_string_dtype(new_dtype):
                new_column = column.astype('str')
            elif is_datetime_dtype(new_dtype):
                raise make_invalid_column_type_change_error(
                    column_header,
                    old_dtype,
                    new_dtype
                )
            elif is_timedelta_dtype(new_dtype):
                pass

        # We update the column, as well as the type of the column
        new_step['dfs'][sheet_index][column_header] = new_column
        new_step['column_type'][sheet_index][column_header] = get_mito_type(new_column)
        
        # We check if there are formula columns that rely on this type, and log if
        # so, so that know if this is an issue folks run into
        if len(new_step['column_evaluation_graph'][sheet_index][column_header]) > 0:
            log(
                'change_column_dtype_column_has_dependents',
                {
                    'column_header': column_header
                }
            )

        return new_step
    except:
        raise make_invalid_column_type_change_error(
            column_header,
            old_dtype,
            new_dtype
        )
        


def transpile_change_column_dtype(
        step,
        sheet_index,
        column_header,
        old_dtype,
        new_dtype
    ):
    """
    Transpiles the dtype change on the specific column
    """
    df_name = step['df_names'][sheet_index]

    conversion_code = f'{df_name}[\'{column_header}\']'
    if is_bool_dtype(old_dtype):
        if is_bool_dtype(new_dtype):
            pass
        elif is_int_dtype(new_dtype):
            conversion_code = f'{df_name}[\'{column_header}\'].astype(\'int\')'
        elif is_float_dtype(new_dtype):
            conversion_code = f'{df_name}[\'{column_header}\'].astype(\'float\')'
        elif is_string_dtype(new_dtype):
            conversion_code = f'{df_name}[\'{column_header}\'].astype(\'str\')'
        elif is_datetime_dtype(new_dtype):
            raise make_invalid_column_type_change_error(
                column_header,
                old_dtype,
                new_dtype
            )
        elif is_timedelta_dtype(new_dtype):
            raise make_invalid_column_type_change_error(
                column_header,
                old_dtype,
                new_dtype
            )
    elif is_int_dtype(old_dtype):
        if is_bool_dtype(new_dtype):
            conversion_code = f'{df_name}[\'{column_header}\'].astype(\'bool\')'
        elif is_int_dtype(new_dtype):
            pass
        elif is_float_dtype(new_dtype):
            conversion_code = f'{df_name}[\'{column_header}\'].astype(\'float\')'
        elif is_string_dtype(new_dtype):
            conversion_code = f'{df_name}[\'{column_header}\'].astype(\'str\')'
        elif is_datetime_dtype(new_dtype):
            conversion_code = f'pd.to_datetime({df_name}[\'{column_header}\'], unit=\'s\', errors=\'coerce\')'
        elif is_timedelta_dtype(new_dtype):
            conversion_code = f'pd.to_timedelta({df_name}[\'{column_header}\'], unit=\'s\', errors=\'coerce\')'
    elif is_float_dtype(old_dtype):
        if is_bool_dtype(new_dtype):
            conversion_code = f'{df_name}[\'{column_header}\'].astype(\'bool\')'
        elif is_int_dtype(new_dtype):
            conversion_code = f'{df_name}[\'{column_header}\'].astype(\'int\')'
        elif is_float_dtype(new_dtype):
            pass
        elif is_string_dtype(new_dtype):
            conversion_code = f'{df_name}[\'{column_header}\'].astype(\'str\')'
        elif is_datetime_dtype(new_dtype):
            conversion_code = f'pd.to_datetime({df_name}[\'{column_header}\'], unit=\'s\', errors=\'coerce\')'
        elif is_timedelta_dtype(new_dtype):
            conversion_code = f'pd.to_timedelta({df_name}[\'{column_header}\'], unit=\'s\', errors=\'coerce\')'
    elif is_string_dtype(old_dtype):
        if is_bool_dtype(new_dtype):
            conversion_code = f'to_boolean_series({df_name}[\'{column_header}\'])'
        elif is_int_dtype(new_dtype):
            conversion_code = f'to_number_series({df_name}[\'{column_header}\']).astype(\'int\')'
        elif is_float_dtype(new_dtype):
            conversion_code = f'to_number_series({df_name}[\'{column_header}\'])'
        elif is_string_dtype(new_dtype):
            pass
        elif is_datetime_dtype(new_dtype):
            # Guess the datetime format to the best of Pandas abilities
            if 'datetime_format' in step:
                conversion_code = f'pd.to_datetime({df_name}[\'{column_header}\'], format=\'{step["datetime_format"]}\', errors=\'coerce\')'
            else:
                conversion_code = f'pd.to_datetime({df_name}[\'{column_header}\'], infer_datetime_format=True, errors=\'coerce\')'
        elif is_timedelta_dtype(new_dtype):
            conversion_code = f'pd.to_timedelta({df_name}[\'{column_header}\'], errors=\'coerce\')'
    elif is_datetime_dtype(old_dtype):
        if is_bool_dtype(new_dtype):
            conversion_code = f'~{df_name}[\'{column_header}\'].isnull()'
        elif is_int_dtype(new_dtype):
            conversion_code = f'{df_name}[\'{column_header}\'].astype(\'int\') / 10**9'
        elif is_float_dtype(new_dtype):
            conversion_code = f'{df_name}[\'{column_header}\'].astype(\'int\').astype(\'float\') / 10**9'
        elif is_string_dtype(new_dtype):
            conversion_code = f'{df_name}[\'{column_header}\'].dt.strftime(\'%Y-%m-%d %X\')'
        elif is_datetime_dtype(new_dtype):
            pass
        elif is_timedelta_dtype(new_dtype):
            raise make_invalid_column_type_change_error(
                column_header,
                old_dtype,
                new_dtype
            )
    elif is_timedelta_dtype(old_dtype):
        if is_bool_dtype(new_dtype):
            conversion_code = f'~{df_name}[\'{column_header}\'].isnull()'
        elif is_int_dtype(new_dtype):
            conversion_code = f'{df_name}[\'{column_header}\'].dt.total_seconds().astype(\'int\')'
        elif is_float_dtype(new_dtype):
            conversion_code = f'{df_name}[\'{column_header}\'].dt.total_seconds()'
        elif is_string_dtype(new_dtype):
            conversion_code = f'{df_name}[\'{column_header}\'].astype(\'str\')'
        elif is_datetime_dtype(new_dtype):
            raise make_invalid_column_type_change_error(
                column_header,
                old_dtype,
                new_dtype
            )
        elif is_timedelta_dtype(new_dtype):
            pass

    return [f'{df_name}[\'{column_header}\'] = {conversion_code}']


def describe_change_column_dtype(
        sheet_index,
        column_header,
        old_dtype,
        new_dtype,
        df_names=None
    ):
    """
    Describes the changing of the column dtype
    """
    return f'Changed {column_header} from {old_dtype} to {new_dtype}'


CHANGE_COLUMN_DTYPE_STEP = {
    'step_version': 1,
    'step_display_name': CHANGE_COLUMN_DTYPE_DISPLAY_NAME,
    'event_type': CHANGE_COLUMN_DTYPE_EVENT,
    'step_type': CHANGE_COLUMN_DTYPE_STEP_TYPE,
    'params': CHANGE_COLUMN_DTYPE_PARAMS,
    'saturate': saturate_change_column_dtype,
    'execute': execute_change_column_dtype,
    'transpile': transpile_change_column_dtype,
    'describe': describe_change_column_dtype
}