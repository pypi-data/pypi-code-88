import numpy as np

def retry(n):
    def decorator_wrapper(function):
        def wrapper(*args, **kwargs):
            for it in range(n):
                try:
                    result = function(*args, **kwargs)

                    return result
                except:
                    continue
            return result

        return wrapper

    return decorator_wrapper


def fail_with_prob(p):
    def decorator_wrapper(function):
        def wrapper(*args, **kwargs):
            assert np.random.choice(np.linspace(0, 1, 1001)) > p
            return function(*args, **kwargs)

        return wrapper

    return decorator_wrapper