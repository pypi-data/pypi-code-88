"""See top level package docstring for documentation"""


def dispatch():
    """
    Return a function that can dispatch between monist and other option

    .. code-block:: python

      dispatch = eval(monist.dispatch())

    """
    return 'lambda x, y: getattr(monist, x) if hasattr(monist, x) else y'
