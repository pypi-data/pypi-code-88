from mitosheet.steps.import_steps.raw_python_import import RAW_PYTHON_IMPORT_STEP_TYPE
from mitosheet.steps.import_steps.simple_import import SIMPLE_IMPORT_STEP_TYPE
from mitosheet.save_utils import read_analysis

def get_import_summary(event):
    """
    Handle import summary is a route that, given the name of an analysis, will
    return the parameters to import steps over the course of the analysis. 

    The data we return is in the format:
    {
        "1": {
            "file_names": ["file123.csv"]
        }, 
        "3": {
            "python_code": "import pandas as ...",
            "new_df_names": ["df1"]
        }
    }
    which is a mapping from raw import steps to the files that they import.
    """
    analysis_name = event['analysis_name']
    # NOTE: we don't upgrade, as this happens when you actually choose to replay an analysis
    analysis = read_analysis(analysis_name)

    imports_only = dict()
    if analysis is not None:
        for step_idx, step in analysis['steps'].items():
            if step['step_type'] == SIMPLE_IMPORT_STEP_TYPE:
                imports_only[step_idx] = dict()
                imports_only[step_idx]['step_type'] = SIMPLE_IMPORT_STEP_TYPE
                imports_only[step_idx]['file_names'] = step['file_names']
            elif step['step_type'] == RAW_PYTHON_IMPORT_STEP_TYPE:
                imports_only[step_idx] = dict()
                imports_only[step_idx]['step_type'] = RAW_PYTHON_IMPORT_STEP_TYPE
                imports_only[step_idx]['python_code'] = step['python_code']
                imports_only[step_idx]['new_df_names'] = step['new_df_names']

    return imports_only