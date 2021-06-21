from typing import Callable

from ruleau.structures import ExecutionResult, RuleauDict

Function = Callable[[ExecutionResult, RuleauDict], bool]
