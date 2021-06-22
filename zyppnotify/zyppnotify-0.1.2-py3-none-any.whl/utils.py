import os
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
