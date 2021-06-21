from typing import TYPE_CHECKING, AnyStr, Optional

from .dependent_results import MockDependentResults

if TYPE_CHECKING:
    from ruleau.process import Process
    from ruleau.rule import Rule
    from ruleau.structures import DependentResults, RuleauDict


class ExecutionResult:
    def __init__(
        self,
        executed_rule: "Rule",
        process: "Process",
        payload: "RuleauDict",
        result,
        dependent_results: "DependentResults",
        override: AnyStr = None,
        original_result: Optional[bool] = None,
    ):
        self.executed_rule = executed_rule
        self.process = process
        self.payload = payload
        self.result = result
        self.override = override
        self.original_result = original_result
        self.dependent_results = dependent_results


class MockExecutionResult(ExecutionResult):
    def __init__(self, dependent_results: MockDependentResults):
        self.dependent_results = dependent_results

    def parse(self):
        return {"dependent_results": self.dependent_results.parse()}


def mock_context(rule_results: dict[str, bool]):
    """
    Given an dictionary containing the rule function name
    as the key and the mocked result as the value, creates
    an ExecutionResult.

    :param rule_results: A dictionary containing the mock
    results for the depedent rules

    :return: ExecutionResult containing mocked results
    """

    dependent_results = MockDependentResults(rule_results)
    return MockExecutionResult(dependent_results)
