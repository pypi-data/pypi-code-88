""" Test module. Auto pytest that can be started in IDE or with::

    python -m pytest

in terminal in tests folder.
"""
#%%

import sys
from pathlib import Path
import inspect
import os
import warnings
from io import StringIO


tests_path = Path(os.path.abspath(inspect.getframeinfo(inspect.currentframe()).filename)).parent
root_path = tests_path.parent

for i in [tests_path, root_path]:
    if i.as_posix() not in sys.path:
        sys.path.insert(0, i.as_posix())

from help_file import info_outside, warn_outside, traceback_outside, warn_to_be_filtered
import mylogging


def get_stdout_and_stderr(func, args=[], kwargs={}):

    old_stdout = sys.stdout
    old_stderr = sys.stderr
    my_stdout = StringIO()
    my_stderr = StringIO()
    sys.stdout = my_stdout
    sys.stderr = my_stderr

    # mylogging._logger.stderr.mode = "a+"
    func(*args, **kwargs)

    # mylogging._logger.stderr

    output = my_stdout.getvalue() + my_stderr.getvalue() + mylogging._logger._stream.getvalue()

    mylogging._logger._stream.truncate(0)

    my_stdout.close()
    my_stderr.close()

    sys.stdout = old_stdout
    sys.stderr = old_stderr

    return output


def test_return_str():
    def raise_formatted():
        try:
            raise Exception(mylogging.return_str("asdas", caption="User"))
        except Exception:
            pass


def test_logs():

    mylogging.config.LEVEL = "DEBUG"
    mylogging.config.FILTER = "always"
    mylogging.config.OUTPUT = "delete.log"

    errors = []

    def check_log():
        with open("delete.log", "r") as log:
            log_content = log.read()
        # Clear content before next run
        open("delete.log", "w").close()

        if log_content:
            return True
        else:
            return False

    mylogging.info(
        "Hessian matrix copmputation failed for example",
        caption="RuntimeError on model x",
    )

    if not check_log():
        errors.append("Info not created")

    mylogging.warn(
        "Hessian matrix copmputation failed for example",
        caption="RuntimeError on model x",
    )
    mylogging.warn("Second")

    if not check_log():
        errors.append("Warning not created")

    try:
        print(10 / 0)

    except Exception:
        mylogging.traceback("Maybe try to use something different than 0")

    if not check_log():
        errors.append("Traceback not created")

    for i in [info_outside, warn_outside, traceback_outside]:
        i("Message")
        if not check_log():
            errors.append("Outside function not working")


def test_warnings_filter():

    mylogging.config.OUTPUT = "console"
    mylogging.config.LEVEL = "INFO"
    mylogging.config._console_log_or_warn = "log"

    mylogging._logger._stream = StringIO()
    mylogging._logger.mylogger.get_handler()

    errors = []

    ################
    ### Debug = 0 - show not
    ################
    mylogging.config.FILTER = "ignore"

    if get_stdout_and_stderr(mylogging.warn, ["Asdasd"]):
        errors.append("Debug 0. Printed, but should not.")

    try:
        print(10 / 0)

    except Exception:
        if get_stdout_and_stderr(mylogging.traceback, ["Maybe try to use something different than 0"]):
            errors.append("Debug = 0 - traceback. Printed, but should not.")

    ################
    ### Debug = 1 - show once
    ################
    mylogging.config.FILTER = "once"

    if not get_stdout_and_stderr(mylogging.info, ["Hello unique"]):
        errors.append("Debug 1. Not printed, but should.")
    if get_stdout_and_stderr(mylogging.info, ["Hello unique"]):
        errors.append("Debug 1. Printed, but should not.")

    ################
    ### Debug = 2 - show always
    ################

    mylogging.config.FILTER = "always"

    if not get_stdout_and_stderr(mylogging.warn, ["Asdasd"]):
        errors.append("Debug 2. Not printed, but should.")
    if not get_stdout_and_stderr(mylogging.warn, ["Asdasd"]):
        errors.append("Debug 2. Not printed, but should.")

    # Test outer file
    mylogging.config.FILTER = "once"

    if not get_stdout_and_stderr(info_outside, ["Info outside"]):
        errors.append("Outside info not working")

    mylogging.config._console_log_or_warn = "warn"

    with warnings.catch_warnings(record=True) as w5:

        warn_outside("Warn outside")
        traceback_outside("Traceback outside")

        if len(w5) != 2:
            errors.append("Warn from other file not working")

    assert not errors


def test_blacklist():
    mylogging.config.OUTPUT = "Console"
    mylogging.config.LEVEL = "INFO"
    mylogging.config._console_log_or_warn = "warn"

    errors = []

    # with
    mylogging.warn("Test blacklist one")

    errors.append("Not stopped on runtime warning.")

    mylogging.config.BLACKLIST
    mylogging.warn("Test blacklist two")


def test_outer_filters():

    errors = []

    mylogging.config.FILTER = "always"
    warnings.filterwarnings("always")

    ignored_warnings = ["mean of empty slice"]

    # Sometimes only message does not work, then ignore it with class and warning type
    ignored_warnings_class_type = [
        ("TestError", FutureWarning),
    ]

    with warnings.catch_warnings(record=True) as fo:
        mylogging.outer_warnings_filter(ignored_warnings, ignored_warnings_class_type)
        warn_to_be_filtered()

    if fo:
        errors.append("Doesn't filter.")

    with warnings.catch_warnings(record=True) as fo2:
        warn_to_be_filtered()

    if not fo2:
        errors.append("Filter but should not.")

    mylogging.outer_warnings_filter(ignored_warnings, ignored_warnings_class_type)

    with warnings.catch_warnings(record=True) as w6:
        warn_to_be_filtered()

        if w6:
            errors.append("Doesn't filter.")

    mylogging.reset_outer_warnings_filter()

    with warnings.catch_warnings(record=True) as w7:
        warn_to_be_filtered()

    if not w7:
        errors.append("Doesn't filter.")

    assert not errors


def test_warnings_levels():

    errors = []

    # Logging to file is already tested, because level filtering occur before division console or file
    mylogging.config.FILTER = "always"

    all_levels_print_functions = [
        mylogging.debug,
        mylogging.info,
    ]

    all_levels_warnings_functions = [
        mylogging.warn,
        mylogging.error,
        mylogging.critical,
    ]

    message_number_should_pass = 1

    for i in ["CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG"]:

        mylogging.config.LEVEL = i

        with warnings.catch_warnings(record=True) as wl:
            for i in all_levels_warnings_functions:
                i("Message")

        for j in all_levels_print_functions:
            if get_stdout_and_stderr(j, ["Message"]):
                wl.append("Message")

    if not len(wl) != message_number_should_pass:
        errors.append("DEBUG level not correct.")

        message_number_should_pass = message_number_should_pass + 1

    with warnings.catch_warnings(record=True) as wl2:
        mylogging.fatal("This is fatal.")

    if not len(wl2) != message_number_should_pass:
        errors.append("Fatal not working")


# def test_settings():
#     # TODO
#     # Test color and debug
#     pass


def test_readme_configs():
    import mylogging

    mylogging.config.COLOR = 0  # Turn off colorization on all functions to get rid of weird symbols

    mylogging.info("Not color")


if __name__ == "__main__":
    # test_return_str()
    # test_warnings_filter()
    # test_outer_filters()
    # test_warnings_levels()

    pass
