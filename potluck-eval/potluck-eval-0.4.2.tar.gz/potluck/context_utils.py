"""
context_utils.py

Support functions for contexts that are also needed by modules which the
`contexts.py` module depends on.
"""

from . import html_tools


#---------------#
# Error classes #
#---------------#

class ContextError(Exception):
    """
    Custom exception class to use when context builders fail.
    """
    pass


class MissingContextError(ContextError):
    """
    Error indicating that required context is missing during
    testing/checking (i.e., an internal error in the construction of a
    Goal or Rubric).
    """
    pass


class ContextCreationError(ContextError):
    """
    Error indicating that context could not be created, usually because a
    submission was missing the required function or module, or because
    attempting to evaluate a function/module caused an error.
    """
    def __init__(self, context, message, cause=None):
        """
        Supply a Context object within which this error was generated, a
        message describing the error, and if there is one, an earlier
        Exception that caused this error.
        """
        self.context = context
        self.message = message
        self.cause = cause

    def __str__(self):
        return (
            "(arising in context '{}') {}"
        ).format(
            self.context.feedback_topic(), # errors won't appear in rubric
            (
                "<br>\n  caused by: {}".format(self.cause)
                if self.cause
                else ""
            )
        )

    def __repr__(self):
        return "ContextCreationError({}, {}, {})".format(
            repr(self.context), repr(self.message), repr(self.cause)
        )

    def explanation(self):
        """
        Chains through causes to return an HTML string describing why
        this context could not be established. Makes use of the html_tb
        property of our cause if it's present and the cause is not a
        ContextCreationError.
        """
        result = "Failed to establish context {}: {}".format(
            self.context.feedback_topic(), # errors won't appear in rubric
            self.message
        )
        if self.cause and isinstance(self.cause, ContextCreationError):
            # Short-circuit the extra builder failed step if we can:
            if self.cause.message == "Builder failed." and self.cause.cause:
                result += "<br>\n" + html_tools.build_html_details(
                    "Caused by error in context {}:".format(
                        self.cause.context.feedback_topic()
                    ),
                    getattr(self.cause.cause, "html_tb", str(self.cause))
                )
            else:
                result += "<br>\n" + html_tools.build_html_details(
                    "Caused by",
                    self.cause.explanation()
                )
        elif self.cause:
            result += "<br>\n" + html_tools.build_html_details(
                "Caused by",
                getattr(self.cause, "html_tb", str(self.cause))
            )
        return result


#------------------#
# Extract function #
#------------------#

def extract(context, slot):
    """
    Returns the value for the given slot of the given Context, raising a
    MissingContextError if there is no such value.
    """
    if slot in context:
        return context[slot]
    else:
        raise MissingContextError(
            f"Required context slot '{slot}' not found."
        )


#---------------------------#
# ContextualValue machinery #
#---------------------------#

class ContextualValue:
    """
    This class and its subclasses represent values that may appear as
    part of arguments in a code behavior test (see
    create_code_behavior_context_builder). Before testing, those
    arguments will be replaced (using the instance's replace method). The
    replace method will receive the current context as its first
    argument, along with a boolean indicating whether the value is being
    requested to test the submitted module (True) or solution module
    (False).

    The default behavior (this class) is to accept a function when
    constructed and run that function on the provided context dictionary,
    using the function's return value as the actual argument to the
    function being tested.

    Your extractor function should ideally raise MissingContextError in
    cases where a context value that it depends on is not present,
    although this is not critical.
    """
    def __init__(self, value_extractor):
        """
        There is one required argument: the value extractor function,
        which will be given a context dictionary and a boolean indicating
        submitted vs. solution testing, and will be expected to produce
        an argument value.
        """
        self.extractor = value_extractor

    def __str__(self):
        return "a contextual value based on {}".format(
            self.extractor.__name__
        )

    def __repr__(self):
        return "<a ContextualValue based on {}>".format(
            self.extractor.__name__
        )

    def replace(self, context):
        """
        This method is used to provide an actual argument value to take
        the place of this object.

        The argument is the context to use to retrieve a value.

        This implementation simply runs the provided extractor function
        on the two arguments it gets.
        """
        return self.extractor(context)


class ContextSlot(ContextualValue):
    """
    A special case ContextualValue where the value to be used is simply
    stored in a slot in the context dictionary, with no extra processing
    necessary. This class just needs the string name of the slot to be
    used.
    """
    def __init__(self, slot_name):
        """
        One required argument: the name of the context slot to use.
        """
        self.slot = slot_name

    def __str__(self):
        return "the current '{}' value".format(self.slot)

    def __repr__(self):
        return "<a ContextSlot for " + str(self) + ">"

    def replace(self, context):
        """
        We retrieve the slot value from the context. Notice that if the
        value is missing, we generate a MissingContextError that should
        eventually bubble out.
        """
        # Figure out which slot we're using
        slot = self.slot

        if slot not in context:
            raise MissingContextError(
                (
                    "Context slot '{}' is required by a ContextSlot dynamic"
                    " value, but it is not present in the testing context."
                ).format(slot)
            )
        return context[slot]


class ModuleValue(ContextualValue):
    """
    A kind of ContextualValue that evaluates a string containing Python
    code within the module stored in the "module" context slot.
    """
    def __init__(self, expression):
        """
        One required argument: the expression to evaluate, which must be
        a string that contains a valid Python expression.
        """
        self.expression = expression

    def __str__(self):
        return "the result of " + self.expression

    def __repr__(self):
        return "<a ModuleValue based on {}>".format(str(self))

    def replace(self, context):
        """
        We retrieve the "module" slot value from the provided context.

        We then evaluate our expression within the retrieved module, and
        return that result.
        """
        if "module" not in context:
            raise MissingContextError(
                "ModuleValue argument requires a 'module' context"
              + " key, but there isn't one."
            )
        module = context["module"]

        return eval(self.expression, module.__dict__)
