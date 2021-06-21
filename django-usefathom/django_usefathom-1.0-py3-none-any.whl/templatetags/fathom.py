from django import template

from usefathom import GOALS

register = template.Library()


@register.inclusion_tag("usefathom/click.html")
def click_goal(goal: str):
    if goal in GOALS:
        goal = GOALS[goal]
    return {
        "goal": goal,
    }
