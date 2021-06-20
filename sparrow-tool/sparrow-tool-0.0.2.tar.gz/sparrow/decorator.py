from functools import wraps, partial
import logging
import time


def test_time(times=10):
    # if func is None:
    #     return partial(time_it, times=times)
    def decorate(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            n = times
            for i in range(n):
                func(*args, **kwargs)
            end = time.time()
            average_cost_time = (end-start)/n
            print(f"Run 10 times, the average time is {average_cost_time} seconds.")
            return func(*args, **kwargs)
        return wrapper
    return decorate


def logged(level, name=None, message=None):
    """
    Add logging to a function. level is the logging
    level, name is the logger name, and message is the
    log message. If name and message aren't specified,
    they default to the function's module and name.
    """
    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)
        return wrapper
    return decorate


if __name__ == "__main__":
    # Example use
    @logged(logging.DEBUG)
    def add(x, y):
        return x + y


    @logged(logging.CRITICAL, 'example')
    def spam():
        print('Spam!')


    @test_time(1)
    def function(n):
        s = -1
        for i in range(n):
            s += i
        return s

    print(function(100000))