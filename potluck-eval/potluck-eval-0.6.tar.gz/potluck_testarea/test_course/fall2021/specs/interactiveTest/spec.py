"""
interactiveTest rubric specification.

Peter Mawhorter 2021-6-28
"""

from potluck import specifications as spec

# Tests

# Different test cases as different goals using group_name
for category, case in [
    ("core", [ "Valentina", "3", "2", "1" ]),
    ("core", [ "Hamad", "1", "2.5", "0.75" ]),
    ("extra", [ "Wenyu", "1", "1.19201", "0.5842" ]),
    ("extra", [ "Paolo", "0", "0", "0" ]),
]:
    spec.TestCase("__import__", group_name=case[0])\
        .provide_inputs(case, policy="error")\
        .set_context_description(
            (
                f"Program output ('{case[0]}' input)",
                (
                    "We will run your program with some example inputs,"
                    " and observe what it prints."
                ),
                f"Program output ('{case[0]}' input)",
                (
                    "We  ran your program with some example inputs,"
                    " and observed what it printed."
                )
            )
        )
    spec.group("__import__", group_name=case[0])\
        .goal(category)\
        .test_output(capture_errors=True)


# Checks
spec.FunctionCall("input", limits=[4, 4])
spec.FunctionCall("int")
spec.FunctionCall("float")
spec.Check(
    ["7 * _"],
    limits=[1, None],
    name=("multiplication by 7", "multiplications by 7")
)
spec.Check(
    ["7 * _"],
    limits=[1, 1],
    name=("multiplication by 7", "multiplications by 7"),
    category="extra"
)


# Misc goals

spec.NoParseErrors()
spec.DontWasteFruit(category="core")
spec.DontWasteBoxes(category="core")

# Construct our rubric
rubric = spec.rubric()
