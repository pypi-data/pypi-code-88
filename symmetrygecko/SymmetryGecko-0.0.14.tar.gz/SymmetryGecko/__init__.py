""" call one of the api_calls functions that are imported """

import os
from . import config
config.FOLDERPATH_INIT = os.path.dirname( os.path.abspath(__file__) )

# ----------------------------------------------------------------------
from .src.api_calls import get_market_data, get_complete_data, get_historical_data
# ----------------------------------------------------------------------

if __name__ == "__main__":
    pass