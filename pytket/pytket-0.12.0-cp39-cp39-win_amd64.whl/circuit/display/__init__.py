"""Display a circuit as html."""

import os
from typing import Dict, Union, Optional
import jinja2
from pytket.circuit import Circuit  # type: ignore
from .utils import is_control_gate, get_target_args, get_op_name, parse_circuit


# Set up jinja to access our templates
dirname = os.path.dirname(__file__)

loader = jinja2.FileSystemLoader(searchpath=dirname)
env = jinja2.Environment(loader=loader)

# Register the filters we need to use
env.filters["is_control_gate"] = is_control_gate
env.filters["get_target_args"] = get_target_args
env.filters["get_op_name"] = get_op_name
env.filters["parse_circuit"] = parse_circuit


def render_circuit_as_html(
    circuit: Union[Dict[str, Union[str, float, dict]], Circuit],
    recursive: bool = False,
    condensed: bool = True,
    jupyter: bool = False,
) -> Optional[str]:
    """
    Render a circuit as HTML for inline display.

    :param circuit: the circuit to render.
    :param recursive: whether to display nested circuits as circuits themselves,
        or as generic boxes
    :param condensed: whether to render the circuit on one line only
        (may require scrolling),
        or allow the circuit to wrap around onto multiple lines
    :param jupyter: set to true to render generated HTML in cell output
    """
    if not isinstance(circuit, Circuit):
        circuit = Circuit.from_dict(circuit)

    options = {
        "recursive": recursive,
        "condensed": condensed,
    }

    template = env.get_template("circuit.html")
    html = template.render(
        {
            "circuit": circuit,
            "display_options": options,
        }
    )

    if jupyter:
        # If we are in a notebook, we can tell jupyter to display the html.
        # We don't import at the top in case we are not in a notebook environment.
        from IPython.core.display import (  # type: ignore
            HTML,
            display,
        )  # pylint: disable=C0415

        display(HTML(html))
        return None

    return html


def render_circuit_jupyter(
    circuit: Union[Dict[str, Union[str, float, dict]], Circuit],
    recursive: bool = False,
    condensed: bool = True,
) -> None:
    """Render a circuit as jupyter cell output.

    :param circuit: the circuit to render.
    :param recursive: whether to display nested circuits as circuits themselves,
        or as generic boxes
    :param condensed: whether to render the circuit on one line only
        (may require scrolling), or allow the circuit to wrap around
        onto multiple lines
    """
    render_circuit_as_html(circuit, recursive, condensed, True)
