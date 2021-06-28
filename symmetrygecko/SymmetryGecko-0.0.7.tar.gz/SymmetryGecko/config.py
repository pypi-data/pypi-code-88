FOLDERPATH_INIT = None # folder absolute path of where __init__.py is (set by __init__.py)
FOLDERPATH_LOG = lambda : FOLDERPATH_INIT + "/logs/"

max_requests_per_minute = 50
request_load = 0.7 # % of max requests per minute allowed by coingecko that we'll utilize at most
sleep_time = 60 / max_requests_per_minute * request_load

# coingecko historical interval windows
MAX_DAYS_FOR_5MIN_DATA_INTERVAL = 1
MAX_DAYS_FOR_1HR_DATA_INTERVAL = 90
MAX_DAYS_FOR_1D_DATA_INTERVAL = "max"