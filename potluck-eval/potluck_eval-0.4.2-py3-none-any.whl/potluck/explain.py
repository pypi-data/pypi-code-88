"""
explain.py

Functions for explaining test results.
"""

import re
import textwrap

from . import mast
from . import harness
from . import html_tools


def summarize_parse_error(e):
    """
    Creates an HTML summary of a parsing-stage error with line number
    info if available.
    """
    # TODO: Line numbers should be links...
    line_info = ''
    if isinstance(e, (SyntaxError, IndentationError)):
        line_info = " (on line {})".format(e.lineno)
    elif isinstance(e, mast.MastParseError):
        if isinstance(e.trigger, (SyntaxError, IndentationError)):
            line_info = " (on line {})".format(e.trigger.lineno)

    estring = str(type(e).__name__) + line_info
    return (
        f"<details>\n<summary>{estring}</summary>\n"
        f"<pre>{str(e)}</pre>\n</details>"
    )
    # TODO: Any file locations to obfuscate in str(e)?


#------------------------#
# Docstring manipulation #
#------------------------#

def grab_docstring_paragraphs(function):
    """
    Given a function, grab its docstring and split it into paragraphs,
    cleaning up indentation. Returns a list of strings. Returns an empty
    list if the target function doesn't have a docstring.
    """
    full_doc = function.__doc__
    if full_doc is None:
        return []
    trimmed = re.sub("\n[ \t]*", "\n", full_doc) # trim indentation
    collapsed = re.sub("\n\n+", "\n\n", trimmed) # multiple blanks -> one
    return [par.strip() for par in collapsed.split("\n\n")]


DOC_WRAP_WIDTH = 73
"""
The width in characters to wrap docstrings to.
"""


def add_docstring_paragraphs(base_docstring, paragraphs):
    """
    Takes a base docstring and a list of strings representing paragraphs
    to be added to the target docstring, and returns a new docstring
    value with the given paragraphs added that has consistent indentation
    and mostly-consistent wrapping.

    Indentation is measured from the first line of the given docstring.
    """
    indent = ''
    for char in base_docstring:
        if char not in ' \t':
            break
        indent += char

    result = base_docstring
    for graf in paragraphs:
        wrapped = textwrap.fill(graf, width=DOC_WRAP_WIDTH)
        indented = textwrap.indent(wrapped, indent)
        result += '\n\n' + indented

    return result


def description_templates_from_docstring(function):
    """
    Given a function, inspects its docstring for a paragraph that just
    says exactly "Description:" and grabs the next 2-4 paragraphs
    (however many are available) returning them as description
    templates. Always returns 4 strings, duplicating the 1st and 2nd
    strings to fill in for missing 3rd and 4th strings, since in 4-part
    descriptions it's okay for the second two to be copies of the first
    two.

    If there is no "Description:" paragraph in the target function's
    docstring, the function's name is used as the title, and the string
    "Details not provided." is used as the description.

    The rest of this docstring provides an example of expected
    formatting:

    Description:

    This paragraph will become the description title template.

    This paragraph will become the description details template.

    This paragraph will become the feedback-level description title
    template.

    This paragraph will become the feedback-level description details
    template.

    Any further paragraphs, like this one, are not relevant, although
    putting description stuff last in the docstring is generally a good
    idea.
    """
    paragraphs = grab_docstring_paragraphs(function)
    if "Description:" in paragraphs:
        where = paragraphs.index("Description:")
        parts = paragraphs[where:where + 4]
    else:
        parts = []

    if len(parts) == 0:
        return (
            function.__name__,
            "Details not provided.",
            function.__name__,
            "Details not provided."
        )
    elif len(parts) == 1:
        return (
            parts[0],
            "Details not provided.",
            parts[0],
            "Details not provided."
        )
    elif len(parts) == 2:
        return ( parts[0], parts[1], parts[0], parts[1] )
    elif len(parts) == 3:
        return ( parts[0], parts[1], parts[2], parts[1] )
    else: # length is >= 4
        return ( parts[0], parts[1], parts[2], parts[3] )


#------------------------#
# Automatic descriptions #
#------------------------#

def code_check_description(
    limits,
    short_desc,
    long_desc,
    details_prefix=None,
    verb="use",
    helper="of"
):
    """
    Creates and returns a 2-item description tuple describing a
    requirement based on an ImplementationCheck with the given limits.
    The short and long description arguments should be strings, and
    should describe what is being looked for. As an example, if a rule
    looks for a for loop and has a sub-rule that looks for an
    accumulation pattern, the arguments could be:

        a for loop,
        a for loop with an accumulator,

    The details_prefix will be prepended to the details part of the
    description that is created.

    The verb will be used to talk about the rule and should be in
    imperative form. For example, for a function call, 'call' could be
    used instead of 'use'. It will be used along with the helper to
    describe instances of the pattern being looked for.
    """
    Verb = verb.capitalize()

    # Decide topic and details
    topic = f"{Verb} {short_desc}"
    if limits[0] in (0, None):
        if limits[1] is None:
            # Note: in this case, probably will be a sub-goal?
            details = f"Each {verb} {helper} {long_desc} will be checked."
        elif limits[1] == 0:
            # Change topic:
            topic = f"Do not {verb} {short_desc}"
            details = f"Do not {verb} {long_desc}."
        elif limits[1] == 1:
            details = f"{Verb} {long_desc} in at most one place."
        else:
            details = f"{Verb} {long_desc} in at most {limits[1]} places."
    elif limits[0] == 1:
        if limits[1] is None:
            details = f"{Verb} {long_desc} in at least once place."
        elif limits[1] == 1:
            details = f"{Verb} {long_desc} in exactly one place."
        else:
            details = (
                f"{Verb} {long_desc} in at least one and at most "
                f"{limits[1]} places."
            )
    else:
        if limits[1] is None:
            details = f"{Verb} {long_desc} in at least {limits[0]} places."
        elif limits[0] == limits[1]:
            details = f"{Verb} {long_desc} in exactly {limits[0]} places."
        else:
            details = (
                f"{Verb} {long_desc} in at least {limits[0]} and at "
                f"most {limits[1]} places."
            )

    if details_prefix is not None:
        details = details_prefix + " " + details[0].lower() + details[1:]

    return topic, details


def function_call_description(
    code_tag,
    details_code,
    limits,
    details_prefix=None
):
    """
    Returns a 2-item description tuple describing what is required for
    an ImplementationCheck with the given limits that matches a function
    call. The code_tag and details_code arguments should be strings
    returned from function_call_code_tags. The given details prefix will
    be prepended to the description details returned.
    """
    return code_check_description(
        limits,
        code_tag,
        details_code,
        details_prefix=details_prefix,
        verb="call",
        helper="to"
    )


def payload_description(
    base_constructor,
    constructor_args,
    augmentations,
    obfuscated=False
):
    """
    Returns an HTML description of the test payload that would be
    constructed using the provided payload constructor, arguments to that
    constructor (as a dictionary) and augmentations dictionary (mapping
    augmentation function names to argument dictionaries).

    If `obfuscated` is set to True, an obfuscated description will
    be returned which avoids key details like which specific
    arguments are used or what inputs are provided. This also puts
    the description into the future tense instead of the past tense.
    """
    if base_constructor == harness.create_run_function_payload:
        fname = constructor_args["fname"]
        posargs = constructor_args["posargs"]
        kwargs = constructor_args["kwargs"]
        # Note: copy_args does not show up in descriptions

        if not posargs and not kwargs: # if there are no arguments
            args_repr = ""
        elif obfuscated:
            args_repr = " with some arguments"
        else:
            args_repr = (
                " with the following arguments:\n"
              + html_tools.args_repr_list(posargs, kwargs)
            )

        if obfuscated:
            result = (
                f"We will run your <code>{fname}</code>"
                f" function{args_repr}"
            )
        else:
            result = (
                f"We ran your <code>{fname}</code>"
                f" function{args_repr}"
            )

    if base_constructor == harness.create_run_harness_payload:
        test_harness = constructor_args["harness"]
        fname = constructor_args["fname"]
        posargs = constructor_args["posargs"]
        kwargs = constructor_args["kwargs"]
        # Note: copy_args does not show up in descriptions

        if not posargs and not kwargs: # if there are no arguments
            args_repr = ""
        elif obfuscated:
            args_repr = " with some arguments"
        else:
            args_repr = (
                " with the following arguments:\n"
              + html_tools.args_repr_list(posargs, kwargs)
            )

        _, obfuscated, _, clear = harness_descriptions(test_harness, fname)

        if obfuscated:
            result = obfuscated
        else:
            result = clear

        result += args_repr

    elif base_constructor == harness.create_module_import_payload:
        prep = constructor_args["prep"]
        wrap = constructor_args["wrap"]
        if prep or wrap:
            mod = " with some modifications"
        else:
            mod = ""

        if obfuscated:
            result = f"We will run your submitted code{mod}"
        else:
            result = f"We ran your submitted code{mod}"

    elif base_constructor == harness.create_read_variable_payload:
        varname = constructor_args["varname"]
        if obfuscated:
            result = (
                f"We will inspect the value of"
                f" <code>{varname}</code>"
            )
        else:
            result = (
                f"We inspected the value of <code>{varname}</code>"
            )

    else: # unsure what our payload is (this shouldn't happen)...
        if obfuscated:
            result = "We will test your submission."
        else:
            result = "We tested your submission."

    # Assemble details from augmentations
    details = []
    if "with_timeout" in augmentations:
        limit = augmentations["with_timeout"]["time_limit"]
        details.append(
            f"Will be terminated if it takes longer than {limit}s."
        )

    if "capturing_printed_output" in augmentations:
        errors_too = augmentations["capturing_printed_output"]\
            .get("capture_errors")

        if errors_too:
            details.append(
                "Printed output and error messages will be recorded."
            )
        else:
            details.append("Printed output will be recorded.")

    if "with_fake_input" in augmentations:
        inputs = augmentations["with_fake_input"]["inputs"]
        policy = augmentations["with_fake_input"]["extra_policy"]

        policy_note = " in a loop" if policy == "loop" else ""

        if obfuscated:
            details.append("Inputs will be provided")
        else:
            details.append(
                f"The following inputs will be provided{policy_note}:\n"
              + html_tools.build_list(
                    html_tools.dynamic_html_repr(text)
                    for text in inputs
                )
            )

    if "with_module_decorations" in augmentations:
        args = augmentations["with_module_decorations"]
        decmap = args["decorations"]
        details.append(
            "Adjustments will be made to the following functions:\n"
          + html_tools.build_list(
                "<pre>{fn}</pre>"
                for fn in decmap
            )
        )

    if "tracing_function_calls" in augmentations:
        args = augmentations["tracing_function_calls"]
        tracing = args["trace_targets"]
        state_function = args["state_function"]
        sfdesc = description_templates_from_docstring(state_function)
        if sfdesc[0] == state_function.__name__:
            # No custom description provided
            tracking = ""
        else:
            tracking = f" ({sfdesc[0]})"

        details.append(
            (
                f"Calls to the following functions will be"
                f" monitored{tracking}:\n"
            )
          + html_tools.build_list(
              f"<pre>{fn}</pre>"
              for fn in tracing
            )
        )

    if "sampling_distribution_of_results" in augmentations:
        args = augmentations["sampling_distribution_of_results"]
        trials = args["trials"]
        details.append(
            f"The distribution of results will be measured across"
            f" {trials} trials."
        )

    # Note that we don't need to mention
    # run_for_base_and_ref_values, as comparing to the solution
    # value is implied.

    result += (
        "<br>\nTesting details:"
      + html_tools.build_list(details)
    )

    return result


def harness_descriptions(test_harness, fname):
    """
    Extracts descriptions of a test harness from its docstring and
    formats them using the given function name, returning a description
    4-tuple of strings.
    """
    hdesc = description_templates_from_docstring(test_harness)

    if hdesc[0] == test_harness.__name__: # no custom description
        result = (
            f"Specialized test of <code>{fname}</code>",
            (
                f"We will test your <code>{fname}</code> using"
                f" <code>{hdesc[0]}</code>"
            ),
            f"Specialized test of <code>{fname}</code>",
            (
                "We tested your <code>{fname}</code> using"
                f" <code>{hdesc[0]}</code>"
            )
        )
    else:
        result = (
            part.format(fname=fname)
            for part in hdesc
        )

    return result
