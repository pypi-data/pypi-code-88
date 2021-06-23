import inspect


def find_attributes(Class: type) -> list[str]:
    attributes = [m[0] for m in inspect.getmembers(
        Class, lambda a: not callable(a))]
    attributes = filter(lambda a: a.startswith(
        f"_{Class.__name__}") and not a.endswith("__"), attributes)
    return list(attributes)
