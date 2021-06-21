from typing import TYPE_CHECKING, AnyStr, Optional

if TYPE_CHECKING:
    from ruleau.dependent_results import DependentResults
    from ruleau.process import Process
    from ruleau.rule import Rule
    from ruleau.structures import RuleauDict


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
