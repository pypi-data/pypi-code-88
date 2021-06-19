"""
    livetube - A API for youtube streaming
    作者: Sam
    创建日期: 2021/04/04 03:41
    文件:    cipher.py
    文件描述: Signature decipher
"""

import re
from itertools import chain
from typing import Any
from typing import Callable
from typing import Dict
from typing import List
from typing import Optional
from typing import Tuple

from .regex import regex_search
from .exceptions import RegexMatchError


class Cipher:
    def __init__(self, js: str):
        self.transform_plan: List[str] = get_transform_plan(js)
        var_regex = re.compile(r"^\w+\W")
        var_match = var_regex.search(self.transform_plan[0])
        if not var_match:
            raise RegexMatchError(
                caller="Cipher init", pattern=var_regex.pattern
            )
        var = var_match.group(0)[:-1]
        self.transform_map = get_transform_map(js, var)
        self.js_func_patterns = [
            r"\w+\.(\w+)\(\w,(\d+)\)",
            r"\w+\[(\"\w+\")\]\(\w,(\d+)\)"
        ]

    def get_signature(self, ciphered_signature: str) -> str:
        """Decipher the signature.
        Taking the ciphered signature, applies the transform functions.
        :param str ciphered_signature:
            The ciphered signature sent in the ``player_config``.
        :rtype: str
        :returns:
           Decrypted signature required to download the media content.
        """
        signature = list(ciphered_signature)

        for js_func in self.transform_plan:
            name, argument = self.parse_function(js_func)  # type: ignore
            signature = self.transform_map[name](signature, argument)
        return "".join(signature)

    def parse_function(self, js_func: str) -> Tuple[str, int]:
        """Parse the Javascript transform function.
        Break a JavaScript transform function down into a two element ``tuple``
        containing the function name and some integer-based argument.
        :param str js_func:
            The JavaScript version of the transform function.
        :rtype: tuple
        :returns:
            two element tuple containing the function name and an argument.
        **Example**:
        parse_function('DE.AJ(a,15)')
        ('AJ', 15)
        """
        for pattern in self.js_func_patterns:
            regex = re.compile(pattern)
            parse_match = regex.search(js_func)
            if parse_match:
                fn_name, fn_arg = parse_match.groups()
                return fn_name, int(fn_arg)

        raise RegexMatchError(
            caller="parse_function", pattern="js_func_patterns"
        )


def get_initial_function_name(js: str) -> str:
    """Extract the name of the function responsible for computing the signature.
    :param str js:
        The contents of the base.js asset file.
    :rtype: str
    :returns:
       Function name from regex match
    """

    function_patterns = [
        r"\b[cs]\s*&&\s*[adf]\.set\([^,]+\s*,\s*encodeURIComponent\s*\(\s*(?P<sig>[a-zA-Z0-9$]+)\(",
        r"\b[a-zA-Z0-9]+\s*&&\s*[a-zA-Z0-9]+\.set\([^,]+\s*,\s*encodeURIComponent\s*\(\s*(?P<sig>[a-zA-Z0-9$]+)\(",
        # noqa: E501
        r'(?:\b|[^a-zA-Z0-9$])(?P<sig>[a-zA-Z0-9$]{2})\s*=\s*function\(\s*a\s*\)\s*{\s*a\s*=\s*a\.split\(\s*""\s*\)',
        # noqa: E501
        r'(?P<sig>[a-zA-Z0-9$]+)\s*=\s*function\(\s*a\s*\)\s*{\s*a\s*=\s*a\.split\(\s*""\s*\)',  # noqa: E501
        r'(["\'])signature\1\s*,\s*(?P<sig>[a-zA-Z0-9$]+)\(',
        r"\.sig\|\|(?P<sig>[a-zA-Z0-9$]+)\(",
        r"yt\.akamaized\.net/\)\s*\|\|\s*.*?\s*[cs]\s*&&\s*[adf]\.set"
        r"\([^,]+\s*,\s*(?:encodeURIComponent\s*\()?\s*(?P<sig>[a-zA-Z0-9$]+)\(",
        # noqa: E501
        r"\b[cs]\s*&&\s*[adf]\.set\([^,]+\s*,\s*(?P<sig>[a-zA-Z0-9$]+)\(",  # noqa: E501
        r"\b[a-zA-Z0-9]+\s*&&\s*[a-zA-Z0-9]+\.set\([^,]+\s*,\s*(?P<sig>[a-zA-Z0-9$]+)\(",  # noqa: E501
        r"\bc\s*&&\s*a\.set\([^,]+\s*,\s*\([^)]*\)\s*\(\s*(?P<sig>[a-zA-Z0-9$]+)\(",  # noqa: E501
        r"\bc\s*&&\s*[a-zA-Z0-9]+\.set\([^,]+\s*,\s*\([^)]*\)\s*\(\s*(?P<sig>[a-zA-Z0-9$]+)\(",  # noqa: E501
        r"\bc\s*&&\s*[a-zA-Z0-9]+\.set\([^,]+\s*,\s*\([^)]*\)\s*\(\s*(?P<sig>[a-zA-Z0-9$]+)\(",  # noqa: E501
    ]
    for pattern in function_patterns:
        regex = re.compile(pattern)
        function_match = regex.search(js)
        if function_match:
            return function_match.group(1)

    raise RegexMatchError(
        caller="get_initial_function_name", pattern="multiple"
    )


def get_transform_plan(js: str) -> List[str]:
    """Extract the "transform plan".
    The "transform plan" is the functions that the ciphered signature is
    cycled through to obtain the actual signature.
    :param str js:
        The contents of the base.js asset file.
    **Example**:
    ['DE.AJ(a,15)',
    'DE.VR(a,3)',
    'DE.AJ(a,51)',
    'DE.VR(a,3)',
    'DE.kT(a,51)',
    'DE.kT(a,8)',
    'DE.VR(a,3)',
    'DE.kT(a,21)']
    """
    name = re.escape(get_initial_function_name(js))
    pattern = r"%s=function\(\w\){[a-z=\.\(\"\)]*;(.*);(?:.+)}" % name
    return regex_search(pattern, js, group=1).split(";")


def get_transform_object(js: str, var: str) -> List[str]:
    """Extract the "transform object".
    The "transform object" contains the function definitions referenced in the
    "transform plan". The ``var`` argument is the obfuscated variable name
    which contains these functions, for example, given the function call
    ``DE.AJ(a,15)`` returned by the transform plan, "DE" would be the var.
    :param str js:
        The contents of the base.js asset file.
    :param str var:
        The obfuscated variable name that stores an object with all functions
        that descrambles the signature.
    **Example**:
    >>> get_transform_object(js, 'DE')
    ['AJ:function(a){a.reverse()}',
    'VR:function(a,b){a.splice(0,b)}',
    'kT:function(a,b){var c=a[0];a[0]=a[b%a.length];a[b]=c}']
    """
    pattern = r"var %s={(.*?)};" % re.escape(var)
    regex = re.compile(pattern, flags=re.DOTALL)
    transform_match = regex.search(js)
    if not transform_match:
        raise RegexMatchError(caller="get_transform_object", pattern=pattern)

    return transform_match.group(1).replace("\n", " ").split(", ")


def get_transform_map(js: str, var: str) -> Dict:
    """Build a transform function lookup.
    Build a lookup table of obfuscated JavaScript function names to the
    Python equivalents.
    :param str js:
        The contents of the base.js asset file.
    :param str var:
        The obfuscated variable name that stores an object with all functions
        that descrambles the signature.
    """
    transform_object = get_transform_object(js, var)
    mapper = {}
    for obj in transform_object:
        # AJ:function(a){a.reverse()} => AJ, function(a){a.reverse()}
        name, function = obj.split(":", 1)
        fn = map_functions(function)
        mapper[name] = fn
    return mapper


def reverse(arr: List, _: Optional[Any]):
    """Reverse elements in a list.
    This function is equivalent to:
    .. code-block:: javascript
       function(a, b) { a.reverse() }
    This method takes an unused ``b`` variable as their transform functions
    universally sent two arguments.
    **Example**:
    >>> reverse([1, 2, 3, 4])
    [4, 3, 2, 1]
    """
    return arr[::-1]


def splice(arr: List, b: int):
    """Add/remove items to/from a list.
    This function is equivalent to:
    .. code-block:: javascript
       function(a, b) { a.splice(0, b) }
    **Example**:
    >>> splice([1, 2, 3, 4], 2)
    [1, 2]
    """
    return arr[b:]


def swap(arr: List, b: int):
    """Swap positions at b modulus the list length.
    This function is equivalent to:
    .. code-block:: javascript
       function(a, b) { var c=a[0];a[0]=a[b%a.length];a[b]=c }
    **Example**:
    >>> swap([1, 2, 3, 4], 2)
    [3, 2, 1, 4]
    """
    r = b % len(arr)
    return list(chain([arr[r]], arr[1:r], [arr[0]], arr[r + 1:]))


def map_functions(js_func: str) -> Callable:
    """For a given JavaScript transform function, return the Python equivalent.
    :param str js_func:
        The JavaScript version of the transform function.
    """
    mapper = (
        # function(a){a.reverse()}
        (r"{\w\.reverse\(\)}", reverse),
        # function(a,b){a.splice(0,b)}
        (r"{\w\.splice\(0,\w\)}", splice),
        # function(a,b){var c=a[0];a[0]=a[b%a.length];a[b]=c}
        (r"{var\s\w=\w\[0\];\w\[0\]=\w\[\w\%\w.length\];\w\[\w\]=\w}", swap),
        # function(a,b){var c=a[0];a[0]=a[b%a.length];a[b%a.length]=c}
        (
            r"{var\s\w=\w\[0\];\w\[0\]=\w\[\w\%\w.length\];\w\[\w\%\w.length\]=\w}",
            swap,
        ),
    )

    for pattern, fn in mapper:
        pattern = re.compile(pattern)
        if pattern.search(js_func):
            return fn
    raise RegexMatchError(caller="map_functions", pattern="multiple")
