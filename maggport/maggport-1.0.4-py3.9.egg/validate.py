import ast
import pathlib

SUPPORTED_EXT = ['.csv', '.json', '.txt']

def validate_extension(out: str) -> str:
    """
    Validates file extension

    Args:
        out (str): Output file

    Return:
        (str): File extension
    """
    file_extension = pathlib.Path(out).suffix

    if file_extension not in SUPPORTED_EXT:
        raise AttributeError('File extension not supported')

    return file_extension.split('.')[-1]


def validate_pipeline(pipeline: str, pipeline_path: str) -> str:
    """
    Validates that a pipeline should be passed to th module

    Args:
        pipeline (List): Pipeline to  run
        pipeline_path (str): Path of pipeline if saved in file

    Return:
        (str): Pipeline to run in mongodb
    """
    if pipeline:
        return pipeline

    if pipeline_path:
        with open(pipeline_path) as file:
            pipeline_text = file.read()

            return ast.literal_eval(pipeline_text)

    raise AttributeError('Expects value in either pipeline or pipeline_path. None given')
