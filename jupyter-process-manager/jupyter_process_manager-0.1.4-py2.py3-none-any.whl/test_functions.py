"""Module with functions to test this package"""
import warnings
from time import sleep
import logging


def test_func(int_seconds=3):
    """Test function 1"""
    if int_seconds == 15:
        raise ValueError("hihi")
    if int_seconds == 20:
        warnings.warn("Warning...........Message", DeprecationWarning)
        logging.warning("Logging is here")

    for int_num in range(int_seconds):
        print(int_num)
        sleep(1)


def test_func2(int_num=1):
    """Test function 2"""
    with open("./%d.txt" % int_num, "w") as file_handler:
        file_handler.write("hihi")
