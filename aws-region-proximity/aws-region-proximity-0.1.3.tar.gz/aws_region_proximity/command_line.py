from . import regions
from .__version__ import __version__

import argparse
import json


def get_closest_regions(*regions_available):
    """
    Output a JSON dictionary where the key is an AWS region's code (i.e. us-east-1, eu-central-1, etc.), and the
    value is a list of all regions sorted by geographic proximity (for us-east-1, the list will be
    [us-east-1, us-east-2, ca-central-1, us-west-2, ...]

    You may optionally provide a list of regions. The return dictionary will always have one key for EVERY region, but
    the list of closest regions will be limited to those that you provide as arguments.

    :param regions_available: an optional list of regions to limit the output to
    :type regions_available: str
    :return: a dictionary where the keys are AWS region code names and the values are the list of all other regions in
             order of geographic proximity
    :rtype: dict[str, list[str]]
    """
    closest_regions = {}

    for region in regions:
        key = region.code
        value = [r.code for r in region.closest_regions if (not regions_available) or r.code in regions_available]
        closest_regions[key] = value

    return closest_regions


def cli():
    """
    Entrypoint for use in setup.py to make a console script named `aws-regions`

    :return: Prints the resulting dictionary from `get_closest_regions` to stdout
    """
    parser = argparse.ArgumentParser("aws-regions",
                                     description="Generate a JSON map of regions with a list of all the other regions "
                                                 "ordered by their geographic proximity.")
    parser.add_argument("regions", nargs="*",
                        help="Optionally limit the list of closest regions to the ones specified on the command line.")
    parser.add_argument("-v", "--version", action="store_true",
                        help="Prints the version (v%s) and exits." % __version__)
    args = parser.parse_args()
    if args.version:
        print("aws-region-proximity v%s" % __version__)
        exit(0)
    closest_regions = get_closest_regions(*args.regions)
    print(json.dumps(closest_regions, indent=4))
