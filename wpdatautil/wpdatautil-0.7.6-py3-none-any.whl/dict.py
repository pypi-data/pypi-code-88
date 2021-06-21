"""dict utilities."""
import textwrap
from typing import Dict, List, Optional


def dict_repr(data: dict) -> str:
    """Return a humanized string with canonical values from the items in the given dictionary."""
    return ", ".join(f"{k}={v!r}" for k, v in data.items())


def dict_str(data: dict) -> str:
    """Return a humanized string from the items in the given dictionary."""
    return ", ".join(f"{k}={v}" for k, v in data.items())


def sql_column_selections(inputs: List[str], transformations: Dict[str, Optional[str]]) -> Dict[str, str]:
    """Return a mapping of SQL SELECT clauses given the input columns after applying the given transformations.

    Example: column_selections(['c1', 'c2', 'c3'], transformations=['c2': None, 'c3': '{col} * 2']) -> {'c1': 'c1', 'c3': 'c3 * 2'}

    :param inputs: Input column names.
    :param transformations: Applicable transformations. If an input column is to be transformed, its name is the key and its value is the transformation.
                            In the value, {col} is replaced with the input column name.
    If the value is None, the column is skipped.
    """
    for column_name in transformations:
        assert column_name in inputs, {"column_name": column_name, "inputs": inputs, "transformations": transformations}

    selections = {}
    for column_name in inputs:
        if column_name in transformations:
            transformed_column = transformations[column_name]
            if transformed_column is None:
                continue  # Skip column.
            transformed_column = transformed_column.format(col=column_name)
            selections[column_name] = transformed_column
        else:
            selections[column_name] = column_name

    return selections


def sql_column_selections_str(inputs: Dict[str, str]) -> str:
    """Return a string representation of a mapping of SQL SELECT clauses.

    Example: {'c1': 'c1', 'c2': 'c2 * 2'} -> 'c1, c2 * 2 AS c2'
    """
    selections = ", ".join(k if k == v else f"\n{v} AS {k}" for k, v in inputs.items())
    if "\n" in selections:
        selections = "\n" + textwrap.indent(selections, prefix=" " * 4 * 4)
    return selections
