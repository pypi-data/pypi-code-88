# Copyright (c) 2021 spookiej.
#
# This is a python library that takes an input for the number of shards
# and returns the shard range required by Vitess.
#

'''
Example usage:
>>> from vitess_helpers import shard_ranges
>>> shard_ranges(3)
['-55', '55-aa', 'aa-']
'''

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

def range_formatter(range_start, range_end, shard_max, hex_format):
    start_hex = ""
    end_hex = ""

    if range_start != 0:
        start_hex = hex_format % range_start

    if range_end != shard_max:
        end_hex = hex_format % range_end

    range_hex = "%s-%s" % (start_hex, end_hex)

    return range_hex


def shard_ranges(shards):
    if type(shards) != int:
        raise ValueError("shard_ranges expects an input of type 'int' but got '%s'" % type(shards).__name__)

    if shards <= 0:
        raise ValueError("number of shards must be greater than zero")

    elif shards > 65536:
        raise ValueError("number of shards must be less than 65536")

    elif shards <= 256:
        hex_format = "%02x"
        max_shards = 256

    elif shards <= 65536:
        hex_format = "%04x"
        max_shards = 65536

    range_start = 0
    size = max_shards / shards
    shard_names = []

    for i in range(1, shards + 1):
        range_end = int((i * size))
        shard_names.append(range_formatter(range_start, range_end, max_shards, hex_format))
        range_start = range_end

    return shard_names
