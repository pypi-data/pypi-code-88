from __future__ import annotations

import functools
import inspect
from typing import TYPE_CHECKING, Any, AnyStr, Dict, List, Optional

import regex as re

from ruleau.constants import OverrideLevel
from ruleau.dependent_results import DependentResults
from ruleau.docs import clean_source, comments, description, doctests, parameters
from ruleau.exceptions import (
    CannotOverrideException,
    RuleIdIllegalCharacterException,
    RuleRequiresIdException,
    RuleRequiresNameException,
)
from ruleau.structures import ExecutionResult, RuleauDict

if TYPE_CHECKING:
    from ruleau.adapter import ApiAdapter
    from ruleau.process import Process
    from ruleau.types import Function


class Rule:
    def __init__(
        self,
        func: "Function",
        id_: AnyStr,
        name: AnyStr,
        depends_on: List["Rule"],
        override_level: OverrideLevel,
        lazy_dependencies: bool,
    ):
        """
        :param func: User defined rule
        :param name: User defined human readable name of the rule
        :param depends_on: Rule dependencies
        :param override_level: Override level
        :param lazy_dependencies: Flag to switch loading of rule dependencies lazily
        """
        self.id = id_
        self.name = name
        # Validate the rule, make sure the name is always set for a rule
        self.validate()
        # Set the user defined function
        self.func = func
        self.depends_on = depends_on
        self.override_level = override_level
        self.__name__ = func.__name__
        self.lazy_dependencies = lazy_dependencies
        self.order = None

        # This preserves the original Docstring on the decorated function
        # which allows DocTest to detect the function
        functools.update_wrapper(self, func)

    def __str__(self) -> str:
        return self.__name__

    def __call__(self, *args, **kwargs) -> bool:
        return self.func(*args, **kwargs)

    def validate(self):
        """
        Validator to check if top level rule has a human readable name and
        and id
        :raises: TopLevelRuleRequiresNameException
        :raises: RuleRequiresIdException
        """
        if not self.name or not isinstance(self.name, str):
            raise RuleRequiresNameException()
        if not self.id or not isinstance(self.id, str):
            raise RuleRequiresIdException()

        # Validate the Rule ID
        if not re.match(r"^([a-zA-Z0-9-_.~]+)+$", self.id):
            raise RuleIdIllegalCharacterException()

    def _get_source(self) -> AnyStr:
        return clean_source(inspect.getsource(self.func))

    @property
    def description(self) -> AnyStr:
        return description(self.func.__doc__)

    def calculate_order_values(self, index=None):
        """
        This sets the `order` value for this rule
        and all of the dependencies below it.

        :param index: Used internally, do not set
        """
        if index is None:
            self.order = 0
        else:
            if self.order is not None:
                self.order = max(self.order, index + 1)
            else:
                self.order = index + 1
        for rule in self.depends_on:
            rule.calculate_order_values(self.order)

    def flatten_rule_objects(self, flat_rules=None) -> [Rule]:
        if flat_rules is None:
            flat_rules = []
        flat_rules.append(self)
        for dependency in self.depends_on:
            dependency.flatten_rule_objects(flat_rules)
        return flat_rules

    def parse(self):
        return {
            "id": self.id,
            "name": self.name,
            "order": self.order,
            "override_level_name": self.override_level.name,
            "override_level": self.override_level.value,
            "source": self._get_source(),
            "comments": comments(self._get_source()),
            "docstring": self.func.__doc__,
            "description": self.description,
            "parameters": parameters(self.func.__doc__),
            "dependencies": [dependent.id for dependent in self.depends_on],
            "doctests": doctests(self.func),
        }

    def execute(
        self,
        case_id: AnyStr,
        payload: Dict[AnyStr, Any],
        process: "Process",
        api_adapter: Optional["ApiAdapter"] = None,
    ):
        api_result = {}
        # Create the rule result so that the execution can store the result
        if api_adapter:
            api_result = api_adapter.create_result(case_id, self, process)
        # Prep the rule payload
        rule_payload = RuleauDict(payload)
        # Prep the dependent results
        depend_results = DependentResults(
            case_id,
            self.depends_on,
            payload,
            process,
            api_adapter,
            lazy=self.lazy_dependencies,
        )
        # Prepare execution result for context from all dependencies
        context = ExecutionResult(self, process, rule_payload, None, depend_results)
        # Prepare execution result for the rule to be executed
        execution_result = ExecutionResult(
            self,
            process,
            rule_payload,
            self(context, rule_payload),
            depend_results,
        )
        # Store the rule result
        if api_adapter:
            # Apply overrides on the rule result
            execution_result = self.apply_override(
                case_id, execution_result, api_adapter
            )

            api_adapter.update_result(case_id, self, api_result, execution_result)
        # Return the rule result
        return execution_result

    def apply_override(
        self,
        case_id,
        execution_result: "ExecutionResult",
        api_adapter: ApiAdapter,
    ):
        # Get overrides for the rule in a case
        override = api_adapter.fetch_override(
            case_id, execution_result.process.id, self.id
        )

        # Apply override to the executed rule result, if any
        # Overrides should only be applied to allowed rule and if they're present
        if override:
            # Throw an exception if the backend is trying to override a NO_OVERRIDE rule
            if self.override_level == OverrideLevel.NO_OVERRIDE:
                raise CannotOverrideException(f"Cannot override {self.name}")
            else:
                # Override the rule result and set the overridden flag
                execution_result.override = override["id"]
                execution_result.original_result = execution_result.result
                execution_result.result = override["applied"]
        return execution_result
