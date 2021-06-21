import logging
from typing import TYPE_CHECKING, Any, AnyStr, Dict, List, Optional

from jsonpath_ng import parse

from ruleau.adapter import ApiAdapter
from ruleau.exceptions import (
    CaseIdRequiredException,
    DuplicateRuleIdException,
    DuplicateRuleNameException,
)
from ruleau.process import Process
from ruleau.rule import Rule

if TYPE_CHECKING:
    from ruleau.structures import ExecutionResult

logger = logging.getLogger(__name__)


def validate_no_duplicate_rule_names(rules: List[Rule]) -> None:
    """Returns True if there are no duplicate Rule Names are used
    A name can only be re-used if the same rule is included multiple times
    """
    rules_dict = {}
    for rule in rules:
        if rule.name not in rules_dict:
            rules_dict[rule.name] = rule
        else:
            if rule != rules_dict[rule.name]:
                raise DuplicateRuleNameException()


def validate_no_duplicate_rule_ids(rules: List[Rule]) -> None:
    """Returns True if there are no duplicate Rule IDs used
    An ID can only be re-used if the same rule is included multiple times
    """
    rules_dict = {}
    for rule in rules:
        if rule.id not in rules_dict:
            rules_dict[rule.id] = rule
        else:
            if rule != rules_dict[rule.id]:
                raise DuplicateRuleIdException()


def execute(
    executable_rule: Rule,
    payload: Dict[AnyStr, Any],
    case_id_jsonpath: AnyStr = None,
    case_id: Optional[AnyStr] = None,
    api_adapter: Optional[ApiAdapter] = None,
) -> "ExecutionResult":
    """
    Executes the provided rule, following dependencies and
    passing in results accordingly
    """

    # If neither case_id_jsonpath or case_id are present, raise exception
    if not case_id_jsonpath and not case_id:
        raise CaseIdRequiredException()

    # If case_id is not present in parameters, find it
    if not case_id:
        case_id_results = parse(case_id_jsonpath).find(payload)
        if not case_id_results:
            raise ValueError("Case ID not found in payload")
        case_id = str(case_id_results[0].value)

    # If there's no case ID, don't run
    if not case_id:
        raise ValueError("Case ID not found")

    # Validate unique rule name
    flattened_rules_as_objects = executable_rule.flatten_rule_objects()
    validate_no_duplicate_rule_names(flattened_rules_as_objects)

    # Validate unique rule ids
    validate_no_duplicate_rule_ids(flattened_rules_as_objects)

    # If API adapter was was passed sync the case
    executable_rule.calculate_order_values()
    process = Process(
        executable_rule.id,
        executable_rule.name,
        executable_rule.description,
        executable_rule,
    )

    if api_adapter:

        # Sync the process rules
        api_adapter.sync_process(process)

        # Sync the case
        api_adapter.sync_case(case_id, process.id, payload)

    # Trigger the rule execution, from the top level rule
    return process.execute(case_id, payload, api_adapter)
