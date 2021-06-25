"""
A Plugin to split tests into equally sized groups
"""
import pytest


def pytest_addoption(parser, pluginmanager):
    parser.addoption("--divide", type=str, metavar="M/N",
                     default=None,
                     help="Split tests into groups of N tests and execute the Mth group")


def pytest_collection_modifyitems(session, config, items):
    divide = config.option.divide
    if divide is not None:
        assert "/" in divide, "--divide must be M/N"

        try:
            m, n = divide.split("/", 1)
            m = int(m)
            n = int(n)

            assert n > 0, f"N must be positive"
            assert m > 0, f"M must be positive"
            assert m <= n, f"M must be <= than M for --divide M/N"

            new_items = []
            for i in range(len(items)):
                if (i % n) == (m - 1):
                    new_items.append(items[i])
            items.clear()
            items.extend(new_items)
        except ValueError:
            assert False, f"{divide} is not valid for --divide"




