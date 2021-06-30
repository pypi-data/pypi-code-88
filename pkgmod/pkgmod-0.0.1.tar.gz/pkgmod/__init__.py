"""Get module names from installed package names and back."""
import functools
import pkg_resources
import sys
import zipfile
import isort


def get_package_name(module):
    """Return package name for this module."""
    # split the module into parts, so we can iterate back and find the top
    # level module name
    module_parts = module.split(".")

    if module in sys.builtin_module_names:
        return module, True

    if module_parts[0] in sys.builtin_module_names or isort.place_module(module_parts[0]) == "STDLIB":
        return module_parts[0], True

    for i in range(len(module_parts), 0, -1):
        modname = ".".join(module_parts[:i])
        if modname in sys.builtin_module_names or isort.place_module(modname) == "STDLIB":
            return modname, True

    # loop through the installed packages
    for pkg in pkg_resources.working_set:
        # loop through the modules provided by this package
        for pkg_module in get_module_names(pkg.project_name):
            # iterate on the module parts until it matches with one of the
            # package's modules
            for i in range(len(module_parts), 0, -1):
                modname = ".".join(module_parts[:i])
                if modname == pkg_module:
                    return pkg.project_name, False


@functools.lru_cache(maxsize=1024**2)
def get_module_names(pkg):
    """Return module names for this package."""
    metadata_dir = pkg_resources.get_distribution(pkg).egg_info
    try:
        return [
            x.rstrip()
            for x in open("%s/%s" % (metadata_dir, "top_level.txt")).readlines()
        ]
    except FileNotFoundError:
        # if we couldn't get the list of modules, return the package name,
        # hopefully that'll be enough...
        return [pkg]
    except NotADirectoryError:
        # it's an egg, read top_level.txt from that
        eggpath = "/".join(metadata_dir.split("/")[:-1])
        zipf = zipfile.ZipFile(eggpath, "r")
        f = zipf.open("EGG-INFO/top_level.txt", "r")
        return [x.rstrip() for x in f.readlines()]


__version__ = "0.0.1"
