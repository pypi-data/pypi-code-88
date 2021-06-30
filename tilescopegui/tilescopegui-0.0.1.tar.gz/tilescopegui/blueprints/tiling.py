from typing import Optional, Union

from flask import Blueprint, request
from tilings.tiling import Tiling
from werkzeug.exceptions import BadRequest

from ..combinatorics import tiling_to_gui_json

tiling_blueprint = Blueprint("tiling_blueprint", __name__, url_prefix="/api/tiling")


@tiling_blueprint.route("/init", methods=["POST"])
def tiling_from_basis() -> dict:
    """Get a root tiling."""
    data: Optional[Union[dict, str]] = request.get_json(silent=False)
    if data is None:
        raise BadRequest()
    try:
        if isinstance(data, str):
            tiling: Tiling = Tiling.from_string(data)
        else:
            tiling = Tiling.from_dict(data)
    except (TypeError, KeyError, ValueError) as exc:
        raise BadRequest() from exc
    return tiling_to_gui_json(tiling)
