import base64
from typing import Dict, List, Tuple

from permuta.patterns.perm import Perm
from tilings.tiling import Tiling

from .strategies import verify_to_json

LabelCache = Dict[Tuple[Tuple[Perm, ...], bool], str]


class Labeller:
    """Symbols for cells to plot tiling."""

    # pylint: disable=too-many-instance-attributes

    _EMPTY_STR = " "
    _POS_POINT_STR = "\u25cf"
    _NPOS_POINT_STR = "\u25cb"
    _DECREASING_STR = "\\"
    _INCREASING_STR = "/"

    _EMPTY = (Perm((0,)),)
    _POINT = (Perm((0, 1)), Perm((1, 0)))
    _DECREASING = (Perm((0, 1)),)
    _INCREASING = (Perm((1, 0)),)

    _INIT_CACHE: LabelCache = {
        (_EMPTY, False): _EMPTY_STR,
        (_EMPTY, True): _EMPTY_STR,
        (_POINT, True): _POS_POINT_STR,
        (_POINT, False): _NPOS_POINT_STR,
        (_DECREASING, True): _DECREASING_STR,
        (_DECREASING, False): _DECREASING_STR,
        (_INCREASING, True): _INCREASING_STR,
        (_INCREASING, False): _INCREASING_STR,
    }

    @classmethod
    def get_gui_format(cls, tiling: Tiling) -> dict:
        """Return a matrix corresponding to the tiling of symbols that should be
        drawn in each cell."""
        labeller = cls(tiling)
        labeller.find_symbols()
        labeller.find_requirements()
        labeller.find_crossing()
        labeller.find_assumptions()
        return {
            "matrix": labeller.img,
            "label_map": labeller.labels_to_basis,
            "crossing": labeller.crossing_obs,
            "requirements": labeller.requirements,
            "assumptions": labeller.assumptions,
        }

    def __init__(self, tiling: Tiling) -> None:
        self.tiling = tiling
        self.curr_label = 1
        self.cache: LabelCache = dict(Labeller._INIT_CACHE.items())
        cols, self.rows = self.tiling.dimensions
        self.img: List[List[str]] = [
            [Labeller._EMPTY_STR for _ in range(cols)] for _ in range(self.rows)
        ]
        self.labels_to_basis: Dict[str, str] = {}
        self.crossing_obs: List[str] = []
        self.requirements: List[List[str]] = []
        self.assumptions: List[List[str]] = []

    def _get_label(self, basis: List[Perm], positive: bool) -> str:
        key = (tuple(basis), positive)
        label = self.cache.get(key, None)
        if label is None:
            label = str(self.curr_label)
            self.cache[key] = label
            self.curr_label += 1
        return label

    def find_symbols(self) -> None:
        """Find symbols for a tiling."""
        if self.tiling.is_epsilon():
            self.img[0][0] = "ε"
            return
        blacklist = set(Labeller._INIT_CACHE.values())
        for cell, (obstructions, _) in sorted(self.tiling.cell_basis().items()):
            positive = cell in self.tiling.positive_cells
            label = self._get_label(sorted(obstructions), positive)
            self.img[self.rows - cell[1] - 1][cell[0]] = label
            if label not in blacklist:
                bases = ", ".join(
                    "".join(str(val + 1) for val in perm) for perm in obstructions
                )
                if positive:
                    self.labels_to_basis[label] = f"Av+({bases})"
                else:
                    self.labels_to_basis[label] = f"Av({bases})"
        if Labeller._EMPTY_STR in self.labels_to_basis:
            del self.labels_to_basis[Labeller._EMPTY_STR]

    def find_crossing(self) -> None:
        """Find crossing obstructions for a tiling."""
        for obs in self.tiling.obstructions:
            if not obs.is_single_cell():
                self.crossing_obs.append(str(obs))

    def find_requirements(self) -> None:
        """Find requirements for a tiling."""
        for reqs in self.tiling.requirements:
            self.requirements.append(list(str(req) for req in reqs))

    def find_assumptions(self) -> None:
        """Find assumptions for a tiling."""
        for assumption in self.tiling.assumptions:
            self.assumptions.append(list(str(gp) for gp in assumption.gps))


def tiling_to_gui_json(tiling: Tiling) -> dict:
    """Convert tiling to a json for the ui."""
    return {
        "tiling": tiling.to_jsonable(),
        "plot": Labeller.get_gui_format(tiling),
        "key": base64.b64encode(tiling.to_bytes()).decode("utf-8"),
        "verified": verify_to_json(tiling),
    }
    # TODO: Stop sending reqs, assumptions and obstructions in plot and make js
    # process those from the json
