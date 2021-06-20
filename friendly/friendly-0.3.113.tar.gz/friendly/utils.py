"""utils.py

A few useful objects which do not naturally fit anywhere else.
"""
import ast
import difflib
import uuid

import pure_eval
from . import debug_helper
from .my_gettext import no_information, internal_error
from .path_info import path_utils


class RuntimeMessageParser:
    """Used to collect message parsers and cycle through them in
    an attempt at finding the cause of an exception.
    """

    def __init__(self):
        self.parsers = []
        self.current_parser = None

    def add(self, func):
        """Use as a decorator to add a message parser"""
        self.parsers.append(func)

    def get_cause(self, value, frame, tb_data):
        """Called from info_specific.py"""
        message = str(value)
        try:
            return self._get_cause(message, frame, tb_data)
        except Exception as e:  # noqa # pragma: no cover
            debug_helper.log(f"Problem with {self.current_parser.__name__}")
            debug_helper.log(f"in module {path_utils.shorten_path(__file__)}")
            return {"cause": internal_error(), "suggest": internal_error()}

    def _get_cause(self, message, frame, tb_data):
        """Cycle through the parsers, looking for one that can find a cause."""
        for self.current_parser in self.parsers:
            # This could be simpler if we could use the walrus operator
            cause = self.current_parser(message, frame, tb_data)
            if cause:
                return cause
        return {"cause": no_information()}


def unique_variable_name():
    """Creates a unique variable name. Useful when attempting to introduce
    a new token to see if it can fix specific cases of SyntaxError."""
    name = uuid.uuid4()
    return "_%s" % name.hex


def eval_expr(expr, frame):
    """Attempts to evaluate the expression 'expr' in a frame.
    Note that 'expr' might be a string containing leading spaces which need
    to be removed prior to being evaluated.

    This can raise some exceptions which are meant to be caught by the
    calling function.
    """
    node = ast.parse(expr.strip()).body[0].value
    evaluator = pure_eval.Evaluator.from_frame(frame)
    return evaluator[node]  # can raise an exception


def get_similar_words(word_with_typo, words):
    """Returns a list of similar words.

    The parameters we chose are based on experimenting with
    different values of the cutoff parameter for the difflib function
    get_close_matches.

    Suppose we have the following words:
    ['cos', 'cosh', 'acos', 'acosh']
    If we use a cutoff of 0.66, and ask for a maximum of 4 matches,
    all will be a match for 'cost'.  However, if we increase the cutoff
    to 0.67, 'acosh' will be dropped from the list, which seems sensible.

    However, this cutoff is "too generous" when dealing with long words.
    Using a cutoff up to 0.75 will result in both 'ascii_lowercase'
    and 'ascii_uppercase' matching 'ascii_lowecase'. Increasing the cutoff
    to 0.76 will drop ascii_uppercase as a match which also seems sensible.

    We thus use a heuristic cutoff based on length which ends up
    matching our expectation as to what a close match should be.

    We also do not return any matches for single character variables,
    nor do we consider single character variable potential matches.
    """
    if len(word_with_typo) == 1:
        return []
    words = [word for word in words if len(word) > 1]

    get = difflib.get_close_matches

    cutoff = min(0.8, 0.63 + 0.01 * len(word_with_typo))
    if len(word_with_typo) > 2:
        result = get(word_with_typo, words, n=5, cutoff=cutoff)
        if result:
            return result
    # In the absence of results, we try see if the typos could have been
    # caused by using the wrong case; this works well also
    # for words of length 2, such as writing Pi instead of pi.
    result = get(word_with_typo.lower(), words, n=1, cutoff=cutoff)
    if result:
        return result
    result = get(word_with_typo.upper(), words, n=1, cutoff=cutoff)
    if result:
        return result

    # Finally, for words of length 2, such as writing 'it' instead of 'if',
    # we lower the cutoff but make sure that the matched words
    # are not too long: difflib finds that 'with' is much more similar to
    # 'it' than 'if' would be!
    if len(word_with_typo) == 2:
        cutoff = 0.5
        words = [word for word in words if len(word) <= 3]
        result = get(word_with_typo, words, n=5, cutoff=cutoff)
    return result


def list_to_string(list_, sep=", "):
    """Transforms a list of names, like ['a', 'b', 'c'], into a single
    string of names, like "a, b, c"."""
    result = ["{c}".format(c=c.replace("'", "")) for c in list_]
    return sep.join(result)
