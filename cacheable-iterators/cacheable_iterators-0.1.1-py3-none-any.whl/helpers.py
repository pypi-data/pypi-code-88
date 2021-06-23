from functools import wraps
from typing import *

F = TypeVar('F', bound=Callable)

try:
    from functools import cache as simple_cache
except ImportError:
    def _cache_key(args: Tuple[Any, ...], kwargs: Dict[str, Any]) -> Tuple[Tuple[Any, ...], Tuple[Tuple[str, Any], ...]]:
        # noinspection PyTypeChecker
        return args, tuple(kwargs.items())
    
    def simple_cache(func: F) -> F:
        """
        Same as `functools.cache`.
        Decorates a function with the cache of infinite amount.
        
        Args:
            func: A function to decorate
        
        Returns:
            Returns the decorated function
        """
        
        # print(f"Decorator: simple_cache({func})")
        
        setattr(func, '_cache', dict())
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            _cache = getattr(func, '_cache')
            _key = _cache_key(args, kwargs)
            if (_key in _cache):
                return _cache[_key]
            else:
                result = func(*args, **kwargs)
                _cache[_key] = result
                return result
        
        return wrapper

def smart_decorator(decorator: Callable[[F], F]) -> Callable[[F], F]:
    """
    Makes a parameterized decorator smarter.
    When called with no parenthesis, it treats all arguments as having default value.
    Does not work the reversed way.
    
    Examples:
        ```python
        @smart_decorator
        def deco(x=5):
            def decorator(func):
                print(f"Called for {func.__name__} with x={x}")
                return func
            return decorator
        
        # All of the following will work properly
        @deco()
        def x(): pass
        # Called for x with x=5
        
        @deco # Looks shorter and prettier!
        def y(): pass
        # Called for y with x=5
        
        @deco(x=6)
        def z(): pass
        # Called for z with x=6
        
        ```
    
    Args:
        decorator: A decorator which should become smarter.
    
    Returns:
        Returns the new decorator which is smarter version of the existing one.
    """
    
    @wraps(decorator)
    def wrapper(*args, **kwargs):
        if (not kwargs and len(args) == 1 and callable(args[0])):
            func, *args = args
            return decorator(*args, **kwargs)(func)
        
        return decorator(*args, **kwargs)
    
    return wrapper


__all__ = \
[
    'simple_cache',
    'smart_decorator',
]
