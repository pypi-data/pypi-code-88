"""
functionsTest rubric specification

Note that this example specification also appears in the documentation
for the `potluck.evaluation.specifications` module.

Peter Mawhorter 2021-6-22
"""

import turtle

from potluck import specifications as spec
from potluck import compare
from potluck import harness

# Define a few simple unit tests
# Note each TestCase created in this loop will be part of a TestGroup for
# the function it's testing.
for case in [ ("hello", 10), ("hi", 12) ]:
    spec.TestCase("indentMessage", case)
    spec.TestCase("printMessage", case)

# These tests don't get grouped with the test cases above because they
# have an explicit non-default group name.
spec.TestCase("indentMessage", ("longword", 4), group_name="advanced")
spec.TestCase("printMessage", ("longword", 4), group_name="advanced")

# Tests in this loop will again form a TestGroup
for case in [ (5, 5), (5, 10), (12.6, 7.3) ]:
    spec.TestCase("ellipseArea", case)


# Tests in this loop are also grouped
for case in [ (90, 4), (50, 5), (30, 12) ]:
    spec.TestCase("polygon", case)

# Extra test case that doesn't start at the origin
spec.TestCase("polygon", (40, 6), group_name="advanced").do_setup(
    lambda context: (turtle.lt(45), turtle.fd(20), context)[-1]
)


# Build two goals based on our TestCases for "indentMessage"
spec.group("indentMessage").goal("core")
spec.group("indentMessage", group_name="advanced").goal("extra")

# Similar goals for printMessage, but here we need to go beyond the
# default (test values for strict equality, as a "product"-type goal) and
# test outputs.
spec.group("printMessage").test_output().goal("core").compare_strings_firmly()
spec.group("printMessage", "advanced").test_output().goal("extra")

# Here we create and refine our core printMessage tests to look just at
# the initial whitespace.
spec.group("printMessage").test_output()\
    .refine(spec.Find, pattern="^ *", pattern_desc="the indentation")\
    .goal("core")\
    .set_goal_description(
        (
            (
                " <code>printMessage</code> uses correct indentation"
            ),
            (
                "We will verify that <code>printMessage</code> includes"
                " the correct number of spaces before the message itself."
            ),
            (
                " <code>printMessage</code> uses correct indentation"
            ),
            (
                "We checked whether <code>printMessage</code> included"
                " the correct number of spaces before the message itself."
            ),
        )
    )


# A comparison function that will treat two numbers as equal if they
# agree to 3 significant figures:
# TODO: This should be standard procedure!
fequals = compare.build_float_equality_checker(3)
# A goal for ellipseArea that uses this equality checker
spec.group("ellipseArea").goal("core").compare_using(fequals)


# For polygon, we'll trace calls to forward and to polygon itself
to_trace = [ "polygon", ("fd", "forward") ]
core_state = [ "position", "heading" ]
traces = spec.group("polygon")\
    .goal("core")\
    .do_setup(harness.warp_turtle)\
    .do_cleanup(harness.finalize_turtle)\
    .test_trace(to_trace, harness.capture_turtle_state)\
    .check_trace_state(core_state, check_args=True, only=["fd"])
adv_traces = spec.group("polygon", "advanced")\
    .goal("extra")\
    .do_setup(harness.warp_turtle)\
    .do_cleanup(harness.finalize_turtle)\
    .test_trace(to_trace, harness.capture_turtle_state)\
    .check_trace_state(core_state, check_args=True, only=["fd"])

# check that the position and heading of the turtle are the same
# before/after the call to polygon.
traces.also()\
    .goal("core")\
    .check_invariant(core_state, only=["polygon"])
adv_traces.also()\
    .goal("extra")\
    .check_invariant(core_state, only=["polygon"])

# Implementation checks: functions must be defined and must use certain
# constructs internally. Note that the second argument to FunctionDef
# should usually be omitted, and can either be an integer requiring a
# specific number of arguments or a string specifying argument names in
# `evaluation.mast` style (e.g., "firstArg, _, thirdArg").
spec.FunctionDef("indentMessage", 2).require(
    spec.FunctionCall(
        "len",
        limits=[1, 1]
    )
)
spec.FunctionDef("printMessage").require(
    spec.FunctionCall("print"),
    spec.FunctionCall("indentMessage")
)
spec.FunctionDef("ellipseArea").require(
    spec.Return()
)
spec.FunctionDef("polygon").require(
    spec.Loop(only="block").require(
        spec.FunctionCall(["fd", "forward"]) # must be in the loop
    )
)

# Construct our rubric
rubric = spec.rubric()

