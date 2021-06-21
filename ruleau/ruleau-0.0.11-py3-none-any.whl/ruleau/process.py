from typing import TYPE_CHECKING, Any, AnyStr, Dict, Optional

from .rule import Rule

if TYPE_CHECKING:
    from ruleau.adapter import ApiAdapter


class Process:
    """Class holding rule process"""

    def __init__(
        self,
        process_id: str,
        name: str,
        description: str,
        root_rule: Rule,
    ):
        self.id = process_id
        self.name = name
        self.description = description
        self.root_rule = root_rule

    def parse(self):
        self.root_rule.calculate_order_values()
        flattened_rules = self.root_rule.flatten_rule_objects()
        unique_rules = list(set(flattened_rules))

        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "root_rule": self.root_rule.id,
            "rules": [rule.parse() for rule in unique_rules],
        }

    def execute(
        self,
        case_id: AnyStr,
        payload: Dict[AnyStr, Any],
        api_adapter: Optional["ApiAdapter"] = None,
    ):
        return self.root_rule.execute(case_id, payload, self, api_adapter)
