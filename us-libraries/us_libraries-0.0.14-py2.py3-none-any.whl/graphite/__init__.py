import time
from functools import wraps
from typing import Any

from us_libraries.graphite.statsclients import StatsClientHelper

statsclients = StatsClientHelper()


def client_timing(func: Any) -> Any:
    """Thread-safe timing function decorator."""
    @wraps(func)
    def _wrapped(*args: Any, **kwargs: Any) -> Any:
        obj = args[0]
        start_time = time.time()
        timing_metric = "{}.{}.{}.{}".format("client", obj.__class__.__name__, func.__name__, "timing")
        success_metric = "{}.{}.{}.{}".format("client", obj.__class__.__name__, func.__name__, "success")
        failure_metric = "{}.{}.{}.{}".format("client", obj.__class__.__name__, func.__name__, "failure")
        try:
            return_value = func(*args, **kwargs)
            statsclients.incr(success_metric)
        except Exception:
            statsclients.incr(failure_metric)
            raise
        finally:
            elapsed_time_ms = int(round(1000 * (time.time() - start_time)))
            statsclients.timing(timing_metric, elapsed_time_ms)
        return return_value
    return _wrapped


def flask_handler_timing(func: Any) -> Any:
    """Thread-safe timing function decorator."""
    @wraps(func)
    def _wrapped(*args: Any, **kwargs: Any) -> Any:
        start_time = time.time()
        timing_metric = "{}.{}.{}".format("handler", func.__name__, "timing")
        success_metric = "{}.{}.{}".format("handler", func.__name__, "success")
        failure_metric = "{}.{}.{}".format("handler", func.__name__, "failure")
        try:
            return_value = func(*args, **kwargs)
            statsclients.incr(success_metric)
        except Exception:
            statsclients.incr(failure_metric)
            raise
        finally:
            elapsed_time_ms = int(round(1000 * (time.time() - start_time)))
            statsclients.timing(timing_metric, elapsed_time_ms)
        return return_value
    return _wrapped


def pyramid_handler_timing(handler: Any, registry: Any) -> Any:
    """Thread-safe timing function decorator."""
    @wraps(handler, registry)
    def _wrapped(request: Any) -> Any:
        start_time = time.time()
        path = str(request.path).replace('/', '', 1)
        path = path.replace('/', '_')
        timing_metric = "{}.{}.{}".format("handler", path, "timing")
        success_metric = "{}.{}.{}".format("handler", path, "success")
        failure_metric = "{}.{}.{}".format("handler", path, "failure")
        try:
            return_value = handler(request)
            statsclients.incr(success_metric)
        except Exception:
            statsclients.incr(failure_metric)
            raise
        finally:
            elapsed_time_ms = int(round(1000 * (time.time() - start_time)))
            statsclients.timing(timing_metric, elapsed_time_ms)
        return return_value
    return _wrapped


def method_metric(func: Any) -> Any:
    """Thread-safe timing function decorator."""
    @wraps(func)
    def _wrapped(*args: Any, **kwargs: Any) -> Any:
        obj = args[0]
        success_metric = "{}.{}.{}".format(obj.__class__.__name__, func.__name__, "success")
        failure_metric = "{}.{}.{}".format(obj.__class__.__name__, func.__name__, "failure")
        try:
            return_value = func(*args, **kwargs)
            statsclients.incr(success_metric)
        except Exception:
            statsclients.incr(failure_metric)
            raise
        return return_value
    return _wrapped
