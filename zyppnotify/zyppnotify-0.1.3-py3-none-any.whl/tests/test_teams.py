import os
from notify import NotifyTeams
from keyvault import secrets_to_environment
from notify.tests import import_sample_dfs


secrets_to_environment("notify")
teams = NotifyTeams(webhook=os.environ.get("teams_webhook"))


def test_teams_basic_message():
    """
    versturen van een simpel teams bericht
    """

    teams.basic_message(title="Pytest", message="This is a simple message, send with notify")


def test_teams_with_dfs():
    """
    versturen van een uitgebreid rapport over dataframes.
    inclusief buttons.
    """

    dfs = import_sample_dfs()
    teams.basic_message(
        title="Pytest",
        message=(
            "This is an extended message, send with notify.<br>"
            "This message has nice buttons.<br>"
            "And gives information about dataframes."
        ),
        buttons={
            "button 1": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
            "button 2": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
            "button 3": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        },
        dfs=dfs,
    )  # creates a report on the dataframes processed.


def test_teams_with_df():
    """
    versturen van een uitgebreid rapport over dataframes.
    inclusief buttons.
    """

    df = import_sample_dfs().get("Transactions")
    teams.basic_message(
        title="Pytest with 1 dataframe",
        message=("This is an test message, send with notify.<br>"),
        df=df,
    )  # adds the dataframe to the message as a table


if __name__ == "__main__":
    test_teams_with_df()
