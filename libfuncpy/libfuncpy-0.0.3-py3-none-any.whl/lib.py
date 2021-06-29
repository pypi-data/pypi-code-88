from contextlib import contextmanager
from functools import partial, reduce
from operator import (
    lt, le, eq, ne, ge, gt,
    add, sub, truediv, floordiv, mul, matmul, mod, pow, neg, pos,
    contains, concat,
    and_, or_, xor, not_, truth,
    invert, lshift, rshift,
    is_, is_not,
    setitem, getitem, delitem,
    iadd,
    )  # noqa: F401


def vartial(func, *args, **keywords):
    def newfunc(value, *fargs, **fkeywords):
        #newkeywords = {**keywords, **fkeywords}
        newkeywords = keywords.copy()
        newkeywords.update(fkeywords)
        return func(value, *args, *fargs, **newkeywords)
    newfunc.func = func
    newfunc.args = args
    newfunc.keywords = keywords
    return newfunc


def give(value):
    def newfunc(*ignore, **everything):
        return value
    newfunc.value = value
    return newfunc


# predefined set ups
true = give(True)
false = give(False)
none = give(None)


def pass_(value):
    return value


def f1f2(f1, f2, *a, **k):
    return f1(f2(*a, **k))


def f2f1(f1, f2, *a, **k):
    return f2(f1(*a, **k))


def ternary_operator(iflogic, assertion, elselogic):
    """Ternary operator logic."""
    return iflogic() if assertion() else elselogic()


def ternary_operator_x(x, iflogic, assertion, elselogic):
    """Ternary operator logic."""
    return iflogic(x) if assertion(x) else elselogic(x)


def make_iterable(value):
    """
    Transform into an iterable.

    Transforms a given `value` into an iterable if it is not.
    Else, return the value itself.

    Example
    =======
    >>> make_iterable(1)
    [1]

    >>> make_iterable([1])
    [1]
    """
    try:
        iter(value)
    except TypeError:
        return [value]
    else:
        return value


def reduce_helper(value, f, *a, **k):
    return f(value, *a, **k)


def chainf(init, *funcs):
    return reduce(reduce_helper, funcs, init)


def chainfs(*funcs):
    def execute(value):
        return chainf(value, *funcs)
    return execute


def if_elif_else(value, condition_function_pair):
    for condition, func in condition_function_pair:
        if condition(value):
            return func(value)


def whileloop(cond, func, do_stopiteration=none, do_exhaust=none):
    # the "problem" here is that you have to save state
    while cond():
        try:
            func()
        except StopIteration:
            do_stopiteration()
            return
    do_exhaust()
    return


def consume(gen):
    for _ in gen:
        pass


def flatlist(list_):
    """
    Flat a list recursively.

    This is a generator.
    """
    # escape strings which would yield infinite recursion
    if isinstance(list_, str):
        yield list_
    else:
        try:
            for sublist in list_:
                yield from flatlist(sublist)
        except TypeError:  # sublist is not iterable
            yield sublist


def raise_(exception, *ignore, **everything):
    raise exception


@contextmanager
def context_engine(
        func,
        exceptions,
        doerror,
        doelse,
        dofinally,
        *args,
        **kwargs):
    try:
        result = func(*args, **kwargs)

    except (exceptions) as err:
        doerror(err)

    else:
        yield result
        doelse(*args, **kwargs)

    finally:
        dofinally(result)


# If Then Else
ITE = ternary_operator
ITEX = ternary_operator_x

# conditionals
is_none = partial(is_, None)
is_not_none = partial(is_not, None)
