#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# abd.py

from typing import Callable, Dict, Tuple, Union

import functools
from abc import ABC, abstractmethod

__all__ = ['ABD', 'AbstractBaseDecorator', 'BaseDecorator']
_WRAPPER_ASSIGNMENTS = (*functools.WRAPPER_ASSIGNMENTS, '__code__')


class AbstractBaseDecorator(ABC):
    """Abstract class to make decorators or wrappers.
    To create a decorator or a wrapper:
      Inherit this class and add the `invoke` function to the class.
    The decorators accepts arguments & keyword arguments.
    Example usage:
    >>> class Return(AbstractBaseDecorator):
    ...     # decorator that expects the `a` keyword
    ...     #   with a callable as the keyword argument
    ...     def __init__(self, *args, **kwargs):
    ...         # check if an option is given
    ...         if not kwargs:
    ...             raise ValueError('Decorator option expected')
    ...         super(Return, self).__init__(*args, **kwargs)
    ...
    ...     def invoke(self, *args, **kwargs):
    ...         # catch and try to reverse the result
    ...         result = self.decorated_object(*args, **kwargs)
    ...         try: result = result[::-1]
    ...         finally: return result
    ...
    ...     def result(self, *args, **kwargs):
    ...         # add extra functionality to the decorated function
    ...         deco_args, deco_kwargs = self.decorator_options
    ...         res = self.decorated_object(*args, **kwargs)
    ...         return_as = deco_kwargs.get('a', res)
    ...         try: res = return_as(res)
    ...         finally: return res
    ...
    >>> # Create a function with the decorator
    >>> # Give the decorator the expected keyword argument: callable
    >>> @Return(a=list)
    ... def func(as_result):
    ...     return as_result
    ...
    >>> # Call the added function which calls the decorated function
    >>> #   that catches the result and tries to call the given option
    >>> #   which is given to the decorator
    >>> func.result('text')
    ['t', 'e', 'x', 't']
    >>> # Call the decorated function
    >>> # `invoke` catches incoming (keyword arguments)
    >>> #   calls the `decorated_object` and catches the result
    >>> #   than tries reverse the result before returning the result
    >>> func('reversed')
    'desrever'
    >>> # Call the decorated function directly with `decorated_object`
    >>> func.decorated_object('list')
    'list'
    """
    # class attributes
    _deco_args: Tuple = ()
    _deco_kwargs: Dict = {}
    _decorated_obj: Callable = None

    @property
    def decorated_object(self) -> Callable:
        """
        Returns the function that is decorated.
        This should be used/called in AbstractBaseDecorator.invoke
          to change the behavior of the decorated function.
        :return: The decorated/wrapped function
        :rtype: callable
        """
        return self._decorated_obj

    @property
    def decorator_options(self) -> Tuple[Tuple, Dict]:
        """Return the arguments or keyword arguments
        These are given when the creating a new class instance
        :return: The options; (arguments, keyword arguments)
        :rtype: tuple, dict
        """
        return self._deco_args, self._deco_kwargs

    def __repr__(self) -> str:
        """A visual representation that dynamically returns
          <@><class name><(options)>< -> decorated function>
        :return: A string representing the decorator and function
        :rtype: str
        """
        at, func, options = '', '', ''
        class_name = self.__class__.__qualname__
        # join args and kwargs for representation
        args = ', '.join('{0}'.format(repr(arg)) for arg in self._deco_args)
        kwargs = ', '.join('{0}={1}'.format(key, repr(val))
                           for key, val in self._deco_kwargs.items())
        # apply options
        if args or kwargs:
            args = "{0}, ".format(args) if args and kwargs else args
            options = '({0}{1})'.format(args, kwargs)
        if hasattr(self, '__name__'):
            at, func = '@', ' -> {0}'.format(self.__name__)
        # return dynamic representation
        return '{0}{1}{2}{3}'.format(at, class_name, options, func)

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Initialization function of the class.
        The 1st argument is considered to be the
          decorated or wrapped function.
        This function is stored and accessible with `decorated_object`

        The given arguments & keyword arguments are saved.
        These are accessible by `decorator_options`
        New options can be set by `set_decorator_options`

        :param args: The first argument is expected to be the callable.
        And is thus separated from the other arguments.
        Is this not the case, all the arguments are respected.
        :param kwargs: key=`value` pair keyword arguments
        """
        # If 1st element is a callable it will be separated
        function, args = self._pop_callable(*args)

        # always point to the original function
        if isinstance(function, type(self)):
            function = function.decorated_object

        # save or overwrite previous options
        if self._decorated_obj is None:
            self.set_decorator_options(*args, **kwargs)

        # set the function as the decorated object
        if callable(function) and self._decorated_obj is None:
            self._decorate(function)

    def __call__(self, *args: object, **kwargs: object
                 ) -> Union[object, Callable]:
        """This function is invoked
          when the decorated/wrapped function is called.
        Or when an instance of this class gets decorated/wrapped again.

        If the latter is the case,
          the 1st argument is the decorated function.
        Also __init__ will catch the arguments & keyword arguments.

        :param args: All the arguments are passed to `invoke`
        :param kwargs: All the key=value pair keyword arguments
          are passed to `invoke`
        :return: `self` or the result of the decorated/wrapped function
        :rtype: `self` or object
        """
        # If 1st element is a callable it will be separated
        function, args = self._pop_callable(*args)

        # always point to the original function
        if isinstance(function, type(self)):
            function = function.decorated_object

        # set the function as the decorated object
        if callable(function) and self._decorated_obj is None:
            self._decorate(function)
            return self  # don't invoke

        # call invoke where the function is called
        return self.invoke(*args, **kwargs)

    @staticmethod
    def _pop_callable(*args: object) -> Union[Union[Callable, None], Tuple]:
        function = None
        if args and callable(args[0]):
            function, *args = args  # pop function from args
        return function, tuple(args)

    def _decorate(self, function: Callable) -> None:
        """Set the given function as the decorated function."""
        functools.update_wrapper(self, function, _WRAPPER_ASSIGNMENTS)
        self._decorated_obj = function

    def set_decorator_options(self, *args: object, **kwargs: object) -> None:
        """Set or override the options of the decorator."""
        self._deco_args = args
        self._deco_kwargs = kwargs

    @abstractmethod
    def invoke(self, *args: object, **kwargs: object) -> Union[object, None]:
        """When the decorated function is called
          this function is called by __call__.
        This must be overridden by the class that inherit this class.
        """
        return self.decorated_object(*args, **kwargs)


# Monkey patch
ABD = AbstractBaseDecorator


class BaseDecorator(ABD):
    """Most basic decorator
    Example usage:
    >>> class Info(BaseDecorator):
    ...     def code_info(self):
    ...         code = self.decorated_object.__code__
    ...         info = {a: getattr(code, a) for a in dir(code)
    ...                 if not a.startswith('_')}
    ...         return info
    ...     def invoke(self, *args, **kwargs):
    ...         func_name = self.decorated_object.__name__
    ...         print('function: {0} is called'.format(repr(func_name)))
    ...         return bool(args or kwargs)  # return for func
    ...
    >>> @Info
    ... def func(arg, *, kw_only=None):
    ...     pass  # No return
    ...
    >>> info = func.code_info()
    >>> info['co_argcount']
    1
    >>> info['co_kwonlyargcount']
    1
    >>> func()  # expect False, because no argument is given
    function: 'func' is called
    False
    >>> func('some argument')  # expect True, because an argument is given
    function: 'func' is called
    True
    """
    def invoke(self, *args: object, **kwargs: object) -> Union[object, None]:
        """Invoke is called the decorated function is called.
        Can be overwritten when this class is inherited
        """
        return self.decorated_object(*args, **kwargs)


if __name__ == '__main__':
    import doctest
    test_results = doctest.testmod()
    print(test_results)
