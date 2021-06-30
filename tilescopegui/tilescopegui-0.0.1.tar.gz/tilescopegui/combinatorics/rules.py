from comb_spec_searcher.strategies.rule import AbstractRule
from tilings import GriddedPerm, Tiling

from .tilings import tiling_to_gui_json


def rule_as_json(rule: AbstractRule[Tiling, GriddedPerm]) -> dict:
    """Convert rule to json."""
    return {
        "class_module": rule.__class__.__module__,
        "rule_class": rule.__class__.__name__,
        "strategy": rule.strategy.to_jsonable(),
        "children": [tiling_to_gui_json(child) for child in rule.children],
        "formal_step": rule.formal_step,
        "op": rule.get_op_symbol(),
    }
