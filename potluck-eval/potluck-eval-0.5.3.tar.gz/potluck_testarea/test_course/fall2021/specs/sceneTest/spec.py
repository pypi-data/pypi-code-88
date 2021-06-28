"""
sceneTest rubric specification

Peter Mawhorter 2021-6-28
"""

from potluck import specifications as spec

# Require 'from turtleBeads import *' (since this will also pull in
# turtle stuff, we don't require a separate turtle import.
spec.Import("turtleBeads", '*')

for fcn in [
    ["forward", "fd", "backward", "bk", "back"],
    ["left", "lt", "right", "rt"],
]:
    spec.FunctionCall(fcn, limits=[1, None])

for fcn in [
    "drawCircle",
    ["pencolor", "color"],
    "begin_fill",
    "end_fill"
]:
    spec.FunctionCall(fcn, limits=[1, None], category="extra")


# Construct our rubric
rubric = spec.rubric()
