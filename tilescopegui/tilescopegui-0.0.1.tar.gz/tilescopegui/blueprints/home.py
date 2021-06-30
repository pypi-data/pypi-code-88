from typing import Text

from flask import Blueprint, render_template, send_from_directory
from werkzeug import Response
from werkzeug.exceptions import BadRequest, NotFound

from ..utils import PathUtil

home_blueprint = Blueprint(
    "home_blueprint", __name__, template_folder=PathUtil.tempalte_dir()
)


@home_blueprint.route("/", methods=["GET"])
def home() -> Text:
    """Render the default html page."""
    return render_template("index.html")


@home_blueprint.route("/static/<path:path>", methods=["GET"])
def static(path: str) -> Response:
    """Serve static files."""
    if ".." in path:
        raise BadRequest()
    if path == "index.html":
        raise NotFound()
    return send_from_directory(PathUtil.static_dir(), path)
