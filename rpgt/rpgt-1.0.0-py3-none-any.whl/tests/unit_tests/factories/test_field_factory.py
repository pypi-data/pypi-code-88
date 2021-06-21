"""
Field factory test file
"""
import argparse

from rpgt.src.factories.field_factory import get_field


def test_factory() -> None:
    """
    Tests the ML setup
    :return: whether the assertion failed or not
    """
    parser = argparse.ArgumentParser(
        description="Generator to automatically set up your new project!"
    )
    args, _ = parser.parse_known_args()

    get_field("RL", args, "")
