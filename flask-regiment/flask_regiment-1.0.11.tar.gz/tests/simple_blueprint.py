from flask import Blueprint, render_template

bp = Blueprint('bp', __name__)

@bp.route('/test')
def view():
    return "blueprint"