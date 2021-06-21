import json

from django.conf import settings


class GoalTrackFailure(Exception):
    pass


FATHOM_GOALS = getattr(settings, "FATHOM_GOALS", dict())


def track(request, goal: str, value: int = 0):
    """Track Fathom goal

    Args:
        request ([type]): HttpRequest
        goal (str): Fathom goal code or alias
        value (int, optional): Monetary value attached to goal. Defaults to 0.

    Raises:
        TypeError: Passing something else than request
        GoalTrackFailure:  not enabled

    Returns:
        [type]: [description]
    """
    try:
        goals = request.session.get("_fathom_goals", None)
        if not goals:
            goals = []
        else:
            goals = json.loads(goals)
    except AttributeError:
        if not hasattr(request, "META"):
            raise TypeError(
                "track() first argument must be an HttpRequest object, not "
                "'%s'." % request.__class__.__name__
            )
    else:
        if goal in FATHOM_GOALS:
            goal = FATHOM_GOALS[goal]
        goals.append(dict(goal=goal, value=value))
        request.session["_fathom_goals"] = json.dumps(goals)


def fetch_goals(request):
    goals = request.session.pop("_fathom_goals", None)
    if not goals:
        return []
    return json.loads(goals)
