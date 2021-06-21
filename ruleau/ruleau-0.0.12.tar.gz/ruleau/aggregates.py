from typing import AnyStr

from ruleau.decorators import rule
from ruleau.structures import ExecutionResult


def Any(rule_id: AnyStr, name: AnyStr, *args):
    """Aggregator to implement OR operation
    Returns truthy, if any one of the rule result is truthy
    """

    @rule(rule_id=rule_id, name=name, depends_on=args)
    def any_aggregator(context: ExecutionResult, _):
        return any(result.result for result in context.dependent_results)

    return any_aggregator


def All(rule_id: AnyStr, name: AnyStr, *args):
    """Aggregator to implement AND operation
    Returns truthy, if and all of the rule results are truthy
    """

    @rule(rule_id=rule_id, name=name, depends_on=args)
    def all_aggregator(context: ExecutionResult, _):
        return all(result.result for result in context.dependent_results)

    return all_aggregator
