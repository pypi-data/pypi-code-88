#!/usr/bin/env python
# coding: utf-8

# Copyright (c) Mito.
# Distributed under the terms of the Modified BSD License.

"""
Exports the transpile function, which takes the backend widget
container and generates transpiled Python code.
"""

from mitosheet.preprocessing import PREPROCESS_STEPS
from mitosheet.steps import STEP_TYPE_TO_STEP


IN_PREVIOUS_STEP_COMMENT = '# You\'re viewing a previous step. Click fast forward in the Mitosheet above to see the full analysis.'

def transpile(widget_state_container, add_comments=True):
    """
    Transpiles the code from the current steps in the widget_state_container, 
    displaying up to the checked out step.

    If add_comments, then adds descriptive comments using the step 
    describe functions. 
    """

    code = []

    # First, we transpile all the preprocessing steps
    for PREPROCESS_STEP in PREPROCESS_STEPS:
        preprocess_code = PREPROCESS_STEP['transpile'](widget_state_container)
        if len(preprocess_code) > 0:
            code.extend(preprocess_code)

    # We only transpile up to the currently checked out step
    for step_index, step in enumerate(widget_state_container.steps[:widget_state_container.curr_step_idx + 1]):

        # The total code for this step
        step_code = []

        # The object that contains all the functions for the step
        step_object = STEP_TYPE_TO_STEP[step['step_type']]

        params = {key: value for key, value in step.items() if key in step_object['params']}

        # NOTE: we add a comment if add_comment is True, but we do not add a comment
        # to the initalize step (as it says nothing)
        if add_comments and step_index > 0:
            step_code.append(
                '# ' + step_object['describe'](
                    **params,
                    df_names=step['df_names']
                )
            )
        
        transpiled_code = step_object['transpile'](
            step,
            **params
        )
        
        # Make sure we don't add comments for steps with no code
        if len(transpiled_code) > 0:

            step_code.extend(
                transpiled_code
            )
            
            code.extend(step_code)

    # If we have a historical step checked out, then we add a comment letting
    # the user know this is the case
    if widget_state_container.curr_step_idx != len(widget_state_container.steps) - 1:
        code.append(IN_PREVIOUS_STEP_COMMENT)

    return {
        'imports': f'from mitosheet import *',
        'code': code
    }