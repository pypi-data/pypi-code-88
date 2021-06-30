import itertools
from typing import TYPE_CHECKING, Iterable, List, Tuple, TypeVar

from comb_spec_searcher.exception import StrategyDoesNotApply
from flask import Blueprint, request
from permuta.patterns.perm import Perm
from tilings.assumptions import TrackingAssumption
from tilings.griddedperm import GriddedPerm
from tilings.strategies import FactorFactory, RowAndColumnPlacementFactory
from tilings.strategies.assumption_insertion import AddAssumptionsStrategy
from tilings.strategies.requirement_insertion import RequirementInsertionStrategy
from tilings.strategies.requirement_placement import RequirementPlacementStrategy
from tilings.strategies.row_and_col_separation import RowColumnSeparationStrategy
from tilings.tiling import Tiling
from werkzeug.exceptions import BadRequest

from ..combinatorics import rule_as_json

if TYPE_CHECKING:
    ItType = TypeVar("ItType")

strategies_blueprint = Blueprint(
    "strategies_blueprint", __name__, url_prefix="/api/strategies"
)


def _any_neg(iterable: Iterable[int]) -> bool:
    return any(z < 0 for z in iterable)


def _get_request_json() -> dict:
    data = request.get_json()
    if data is None or not isinstance(data, dict):
        raise BadRequest()
    return data


def _first_or_bad(iterable: Iterable["ItType"]) -> "ItType":
    for element in iterable:
        return element
    raise BadRequest()


def _get_tiling_input() -> Tiling:
    data = _get_request_json()
    try:
        tiling: Tiling = Tiling.from_dict(data)
    except (TypeError, KeyError, ValueError) as exc:
        raise BadRequest() from exc
    return tiling


@strategies_blueprint.route("/factor", methods=["POST"])
def factor() -> dict:
    """Apply factor strategy to given tiling."""
    tiling = _get_tiling_input()
    strats = FactorFactory()(tiling)
    strat = _first_or_bad(strats)
    rule = strat(tiling)
    return rule_as_json(rule)


def _get_row_col_placement_input() -> Tuple[Tiling, int, bool, int]:
    data = _get_request_json()
    try:
        tiling: Tiling = Tiling.from_dict(data["tiling"])
        direction: int = data["dir"]
        row: bool = data["row"]
        idx: int = data["idx"]
    except (TypeError, KeyError, ValueError) as exc:
        raise BadRequest() from exc
    if not isinstance(direction, int) or not isinstance(row, bool):
        raise BadRequest()
    if direction < 0 or direction > 3:
        raise BadRequest()
    if (
        idx < 0
        or (row and idx >= tiling.dimensions[1])
        or (not row and idx >= tiling.dimensions[0])
    ):
        raise BadRequest()
    return tiling, direction, row, idx


@strategies_blueprint.route("/rowcolplace", methods=["POST"])
def row_col_placement() -> dict:
    """Apply row column placement strategy to given tiling."""
    tiling, direction, row, idx = _get_row_col_placement_input()
    for rule in RowAndColumnPlacementFactory(row, not row, dirs=(direction,))(tiling):
        assert isinstance(rule.strategy, RequirementPlacementStrategy)
        if row and rule.strategy.gps[0].pos[0][1] == idx:
            if len(rule.non_empty_children()) == 1:
                return rule_as_json(rule.to_equivalence_rule())
            return rule_as_json(rule)
        if not row and rule.strategy.gps[0].pos[0][0] == idx:
            if len(rule.non_empty_children()) == 1:
                return rule_as_json(rule.to_equivalence_rule())
            return rule_as_json(rule)
    raise BadRequest()


def _get_cell_insertion_input() -> Tuple[Tiling, GriddedPerm]:
    data = _get_request_json()
    try:
        tiling: Tiling = Tiling.from_dict(data["tiling"])
        x: int = data["x"]
        y: int = data["y"]
        patt: str = data["patt"]
    except (TypeError, KeyError, ValueError) as exc:
        raise BadRequest() from exc
    if not (isinstance(x, int) and isinstance(y, int) and isinstance(patt, str)):
        raise BadRequest()
    if not patt.isdecimal():
        raise BadRequest()
    _x, _y = tiling.dimensions
    if x < 0 or x >= _x or y < 0 or y >= _y:
        raise BadRequest()
    n, value_set = len(patt), set(map(int, patt))
    if len(value_set) != n or not all(
        i in value_set for i in (range(n) if 0 in value_set else range(1, n + 1))
    ):
        raise BadRequest()
    return tiling, GriddedPerm.single_cell(Perm.to_standard(patt), (x, y))


@strategies_blueprint.route("/cellinsertion", methods=["POST"])
def cell_insertion() -> dict:
    """Apply cell insertion strategy to given tiling."""
    tiling, gp = _get_cell_insertion_input()
    try:
        rule = RequirementInsertionStrategy((gp,))(tiling)
    except StrategyDoesNotApply as exc:
        raise BadRequest() from exc
    if all(
        tiling == ne_child
        for ne_child in filter(lambda t: not t.is_empty(), rule.children)
    ):
        raise BadRequest()
    return rule_as_json(rule)


@strategies_blueprint.route("/rowcolsep", methods=["POST"])
def row_col_separation() -> dict:
    """Apply row/column separation to given tiling."""
    tiling = _get_tiling_input()
    try:
        rule = RowColumnSeparationStrategy()(tiling)
    except StrategyDoesNotApply as exc:
        raise BadRequest() from exc
    return rule_as_json(rule)


def _get_requirement_placement_input() -> Tuple[Tiling, GriddedPerm, int, int]:
    data = _get_request_json()
    try:
        tiling: Tiling = Tiling.from_dict(data["tiling"])
        x: int = data["x"]
        y: int = data["y"]
        direction: int = data["dir"]
        idx: int = data["idx"]
    except (TypeError, KeyError, ValueError) as exc:
        raise BadRequest() from exc
    if not (
        isinstance(x, int) and isinstance(y, int) and isinstance(idx, int),
        isinstance(direction, int),
    ):
        raise BadRequest()
    _x, _y = tiling.dimensions
    if _any_neg((idx, x, y, direction)) or x >= _x or y >= _y or direction > 3:
        raise BadRequest()
    cell = (x, y)
    reqs = list(
        filter(
            lambda req: req.is_single_cell() and req.pos[0] == cell,
            itertools.chain(*tiling.requirements),
        )
    )
    if len(reqs) != 1 or idx >= len(reqs[0]):
        raise BadRequest()
    return tiling, reqs[0], idx, direction


@strategies_blueprint.route("/reqplace", methods=["POST"])
def requirement_placement() -> dict:
    """Apply requirement placement to given tiling."""
    tiling, gp, idx, direction = _get_requirement_placement_input()
    try:
        rule = RequirementPlacementStrategy(
            (gp,), (idx,), direction, include_empty=True
        )(tiling)
    except StrategyDoesNotApply as exc:
        raise BadRequest() from exc
    if all(
        tiling == ne_child
        for ne_child in filter(lambda t: not t.is_empty(), rule.children)
    ):
        raise BadRequest()
    if len(rule.non_empty_children()) == 1:
        return rule_as_json(rule.to_equivalence_rule())
    return rule_as_json(rule)


def _get_add_assumption_input() -> Tuple[Tiling, List[GriddedPerm]]:
    data = _get_request_json()
    try:
        tiling: Tiling = Tiling.from_dict(data["tiling"])
        pos: List[List[int]] = data["pos"]
    except (TypeError, KeyError, ValueError) as exc:
        raise BadRequest() from exc
    if not isinstance(pos, list) or len(pos) == 0:
        raise BadRequest()
    _x, _y = tiling.dimensions
    gps: List[GriddedPerm] = []
    for coord in pos:
        if not isinstance(coord, list) or len(coord) != 2:
            raise BadRequest()
        x, y = coord
        if not (isinstance(x, int) and isinstance(y, int)):
            raise BadRequest()
        if x < 0 or y < 0 or x >= _x or y >= _y:
            raise BadRequest()
        gps.append(GriddedPerm.single_cell((0,), (x, y)))
    return tiling, gps


@strategies_blueprint.route("/addassumption", methods=["POST"])
def add_assumption() -> dict:
    """Apply add assumption strategy to given tiling."""
    tiling, gps = _get_add_assumption_input()
    try:
        rule = AddAssumptionsStrategy((TrackingAssumption(gps),))(tiling)
    except StrategyDoesNotApply as exc:
        raise BadRequest() from exc
    if not rule.children or rule.children[0] == tiling:
        raise BadRequest()
    return rule_as_json(rule)
