import os

import pandas as pd

from notify.exceptions import EnvironmentVariablesError


def check_environment_variables(required_variables: list):
    """
    Parameters
    ----------
    required_variables: list
        list of required variables that need to be present in environment variables.

    Returns
    -------

    """
    # Test if environment variables are set.

    values = [os.environ.get(x) for x in required_variables]

    if not all(values):
        raise EnvironmentVariablesError(
            f"One of the environment variables {', '.join(required_variables)} is not set"
        )


def dataframe_to_html(df: pd.DataFrame) -> str:
    """

    Parameters
    ----------
    df

    Returns
    -------

    """

    html_table = df.to_html(index=False, classes="styled-table", justify="center")

    pretty_html_table = (
        """
        <head>
            <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
            <title>Dataframe report</title>
            <style type="text/css" media="screen">
                h1 {
                    background-color: #a8a8a8;
                    display: flex;
                    flex-direction: column;
                    justify-content: center;
                    text-align: center;
                }

                .styled-table {
                    border-collapse: collapse;
                    margin: 25px 0;
                    font-size: 0.9em;
                    font-family: sans-serif;
                    min-width: 400px;
                    box-shadow: 0 0 20px rgba(0, 0, 0, 0.15);
                }

                .styled-table thead tr {
                    background-color: #009879;
                    color: #ffffff;
                    text-align: left;
                }

                .styled-table th,
                .styled-table td {
                    padding: 12px 15px;
                }

                .styled-table tbody tr {
                    border-bottom: thin solid #dddddd;
                }

                .styled-table tbody tr:nth-of-type(even) {
                    background-color: #f3f3f3;
                }

                .styled-table tbody tr.active-row {
                    font-weight: bold;
                    color: #009879;
                }

                .styled-table tbody tr:last-of-type {
                    border-bottom: 2px solid #009879;
                }
            </style>
        </head>
        <body>"""
        + html_table
        + "</body>"
    )

    return pretty_html_table
