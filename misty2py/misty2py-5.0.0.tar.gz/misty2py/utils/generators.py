"""This module contains generator functions."""
import random
import string


def get_random_string(n: int) -> str:
    """Constructs an `n` characters long random string containing ASCII letters and digits.

    Args:
        n (int): The required length of the string.

    Returns:
        str: The random string.
    """

    assert n > 0, "Required string length must be a positive integer."

    return "".join(
        random.SystemRandom().choice(string.ascii_letters + string.digits)
        for _ in range(n)
    )
