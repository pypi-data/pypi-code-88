"""
Module with miscellaneous functions. For example myproperty, which is decarator for creating
simplified properties or json_to_py that can convert json string to correct python types or
str_to_infer_type that will convert string to correct type.
"""
import builtins
from typing import Callable

import mylogging


_JUPYTER = 1 if hasattr(builtins, "__IPYTHON__") else 0


def myproperty(types=None, options=None, setter=None):
    """Function that is used as decorator on the sam place where @property is usually used.
    Because of this function, you can use docstrings for your variable, you don't need to
    define setter and initialize _variable. Syntax is very compact...

    Type hints in IDE works (not defined dynamically) and also it is possible to restrict
    types and possible options that setter can set.

    Examples:

        >>> class Myclass:
        ...    @myproperty(int)  # Use tuple like (str, int, bool) if more classes.
        ...    def var(self) -> int:  # This is for type hints in IDE.
        ...        '''This is docstrings (also visible in IDE, because not defined dynamically).'''
        ...        return 123  # This is initial value that can be edited.
        ...
        >>> myobj = Myclass()
        >>> myobj.var
        123
        >>> myobj.var = 666
        >>> myobj.var
        666
        >>> myobj.var = "String is problem"
        Traceback (most recent call last):
        ...
        TypeError: Allowed types for variable var are <class 'int'>, but you try to set an <class 'str'>

        You can also use options checker. If there are only few values, that variable can has.

        >>> class Myclass:
        ...     @myproperty(int, [1, 2, 3])
        ...     def var(self) -> int:
        ...         pass  # This means that value will not be set on init
        ...
        >>> myobj = Myclass()
        >>> myobj.var = 2
        >>> myobj.var
        2
        >>> myobj.var = 4
        Traceback (most recent call last):
        ...
        KeyError: 'New value 4 for variable var is not in allowed options [1, 2, 3].'

        You can also define setter via lambda function, but only very simple, if more logic,
        it's better to use normal property and add type checking manually.

        It's lazy evaluated on first getter or setter. If you want to run setter on object initialization,
        return pass and set in __init__.

        Use name with underscore as prefix and use setattr.

        >>> class Myclass:
        ...     def __init__(self):
        ...         self.with_setter_on_init = 333
        ...
        ...         # If want set value, but don't want run setter, use
        ...         # self._with_setter_on_init = 333
        ...
        ...     @myproperty(
        ...         int,
        ...         setter=lambda self, new: (
        ...             print("I'm listener, i can call any function on change."),
        ...             print("I'm lazy, i will be called after first get or set..."),
        ...             setattr(self, "_with_setter", new + 1),
        ...         ),
        ...     )
        ...     def with_setter(self) -> int:
        ...         '''Also docstrings'''
        ...         return 1
        ...
        ...     @myproperty(
        ...         int,
        ...         setter=lambda self, new: (
        ...             print("I'm called when object created (with __init__)."),
        ...             setattr(self, "_with_setter_on_init", new * 2),
        ...         ),
        ...     )
        ...     def with_setter_on_init(self) -> int:
        ...         '''Also docstrings'''
        ...         pass
        ...
        >>> myclass = Myclass()
        I'm called when object created (with __init__).
        >>> myclass.with_setter
        I'm listener, i can call any function on change.
        I'm lazy, i will be called after first get or set...
        >>> myclass.with_setter
        2
        >>> myclass.with_setter = 665
        I'm listener, i can call any function on change.
        I'm lazy, i will be called after first get...
        >>> myclass.with_setter
        666

    Note:
        If you set class variable itself, not on an object, you will remove all property and replace
        it with just a value.
    """

    if isinstance(types, list):
        types = tuple(types)

    def decorator(f):

        field = "_" + f.__name__

        if setter is None:
            # This is default setter if not configured
            def setter_function(self, new):
                setattr(self, field, new)

        else:
            setter_function = setter

        if types:
            setter_function = type_checker_wrapper(setter_function, types, f.__name__)

        if options:
            setter_function = options_checker_wrapper(setter_function, options, f.__name__)

        def getter(self):
            # If there is no value yet, set it
            try:
                getattr(self, field)
            except AttributeError:

                # Just syntax check if there is self in function
                try:
                    setter_function(self, f(self))
                except TypeError:
                    raise SyntaxError(f"In function in @mydecorator on value {f.__name__} is no self")

            return getattr(self, field)

        return property(getter, setter_function, None, f.__doc__)

    return annotationoverload(decorator)


def annotationoverload(f) -> Callable:
    """Only reason is to has correct type hits for myproperty. Kind of monkey patch. Definition on decorator is
    not possible dynamically and this remove need for decorators for every type."""
    return f


def type_checker_wrapper(f, types, name) -> Callable:
    def inner(inst, new):
        if types and not isinstance(new, types):
            raise TypeError(
                f"Allowed types for variable {name} are {types}, but you try to set an {type(new)}"
            )
        f(inst, new)

    return inner


def options_checker_wrapper(f, options, name) -> Callable:
    def inner(inst, new):
        if new not in options:
            raise KeyError(f"New value {new} for variable {name} is not in allowed options {options}.")
        f(inst, new)

    return inner


def type_and_option_check(value, variable="Not defined", types=None, options=None):
    if isinstance(types, list):
        types = tuple(types)

    if types and not isinstance(value, types):
        raise TypeError(
            mylogging.return_str(
                f"Allowed types for variable {variable} are {types}, but you try to set an {type(value)}"
            )
        )

    if options and value not in options:
        raise KeyError(
            mylogging.return_str(
                f"New value {value} for variable {variable} is not in allowed options {options}."
            )
        )


def str_to_infer_type(string_var):
    import ast

    evaluated = string_var
    try:
        evaluated = ast.literal_eval(evaluated)
    except Exception:
        pass
    return evaluated


def json_to_py(json, replace_comma_decimal=True, convert_decimal=False):
    """Take json and eval it from strings.
    If string to string, if float to float, if object then to dict.

    When to use? - If sending object as parameter in function.

    Args:
        json (dict): JSON with various formats as string.
        replace_comma_decimal (bool): Some countries use comma as decimal separator (e.g. 12,3).
            If True, comma replaced with dot (if not converted to number string remain untouched)
        convert_decimal (bool): Some countries has ',' decimal, then conversion would fail.
            If True, convert ',' to '.' in strings. Only if there are no brackets (list, dict...).
            For example '2,6' convert to 2.6.

    Returns:
        dict: Python dictionary with correct types.
    """

    import ast

    evaluated = json.copy()

    for i, j in json.items():

        if replace_comma_decimal and isinstance(j, str) and "(" not in j and "[" not in j and "{" not in j:
            j = j.replace(",", ".")

        try:
            evaluated[i] = ast.literal_eval(j)
        except Exception:
            pass

    return evaluated
