from typing import Optional

import tilings.strategies as strats
from comb_spec_searcher.exception import StrategyDoesNotApply
from comb_spec_searcher.strategies.rule import VerificationRule
from tilings import Tiling


def _basic_verify(tiling: Tiling) -> Optional[VerificationRule]:
    try:
        return strats.BasicVerificationStrategy()(tiling)
    except StrategyDoesNotApply:
        return None


def _locally_factorable(tiling: Tiling) -> Optional[VerificationRule]:
    try:
        return strats.LocallyFactorableVerificationStrategy()(tiling)
    except StrategyDoesNotApply:
        return None


def _insertion_encodable(tiling: Tiling) -> Optional[VerificationRule]:
    try:
        return strats.InsertionEncodingVerificationStrategy()(tiling)
    except StrategyDoesNotApply:
        return None


def verify(tiling: Tiling) -> Optional[VerificationRule]:
    """Try to verify tiling and return the rule if any."""
    strat = _basic_verify(tiling)
    if strat is not None:
        return strat
    strat = _locally_factorable(tiling)
    if strat is not None:
        return strat
    return _insertion_encodable(tiling)


def verify_to_json(tiling: Tiling) -> Optional[dict]:
    """Try to verify tiling and return the rule as json if any."""
    rule = verify(tiling)
    if rule:
        json_rule = rule.to_jsonable()
        json_rule["formal_step"] = rule.formal_step
        return json_rule
    return None
