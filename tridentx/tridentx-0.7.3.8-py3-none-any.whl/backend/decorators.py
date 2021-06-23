import warnings
from requests.exceptions import HTTPError

def trident_export(*api_names, **kwargs):
    def Decorator(func_or_class):
        func_or_class._TRIDENT_API = api_names
        return func_or_class
    return Decorator


def deprecated(version, substitute):
    """deprecated warning
    Args:
        version (str): version that the operator or function is deprecated.
        substitute (str): the substitute name for deprecated operator or function.
    """

    def decorate(func):
        def wrapper(*args, **kwargs):
            cls = getattr(args[0], "__class__", None) if args else None
            name = cls.__name__ if cls else func.__name__
            print(f"WARNING: '{func.__name__}' is deprecated from version {version} and will be removed in a future version, "
                  f"use '{substitute}' instead.")
            ret = func(*args, **kwargs)
            return ret

        return wrapper

    return decorate

def skip_http_error(statuses):
    """
    A decorator to wrap with try..except to swallow
    specific HTTP errors.
    @skip_http_error((404, 503))
    def fetch():
        ...
    """

    assert isinstance(statuses, tuple)

    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except HTTPError as e:
                status_code = e.response.status_code
                if status_code in statuses:
                    warnings.warn(str(e))
                else:
                    raise
        return wrapper
    return decorator