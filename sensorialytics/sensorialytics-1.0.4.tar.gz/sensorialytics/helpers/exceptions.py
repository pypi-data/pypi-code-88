#  exceptions.py
#  Project: sensorialytics
#  Copyright (c) 2021 Sensoria Health Inc.
#  All rights reserved


class FitError(Exception):
    def __init__(self, *args):
        super().__init__(*args)


class MaximumDepthError(Exception):
    def __init__(self, *args):
        super().__init__(*args)
