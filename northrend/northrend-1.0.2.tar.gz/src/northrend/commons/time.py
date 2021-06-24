import time
from functools import wraps


def log_time(get_time=False, printer=print):
    def _log_time(method):
        @wraps(method)
        def timed(*args, **kw):
            ts = time.time()
            result = method(*args, **kw)
            te = time.time()
            walltime = te - ts
            printer("{} runtime: {:.0f}s".format(method.__name__, (te - ts)))
            if get_time:
                return result, walltime
            else:
                return result

        return timed

    return _log_time
