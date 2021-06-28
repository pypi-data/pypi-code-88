__version__ = '0.0.4'

from .jupyter_xml import JupyterXML
from IPython.display import display_javascript


def load_ipython_extension(ipython):
    # Activates syntax highlighting for sparql, turtle and json-ld in jupyter notebook.
    # This does not work on JupyterLab because the global IPython object is not defined there.
    js_highlight = """
    if (typeof IPython !== "undefined") {
        IPython.CodeCell.options_default.highlight_modes['application/xml'] = {'reg':[/^%%xml/]};
        IPython.notebook.get_cells().map(function(cell){ if (cell.cell_type == 'code'){ cell.auto_highlight(); } });
    }
    """
    display_javascript(js_highlight, raw=True)

    ipython.push({
        "xmlsources": dict(),
        "xmltrees": dict(),
        "xmlschemasources": dict(),
        "xmlschemas": dict(),
        "xmlschematrees": dict(),
        "xmlpaths": dict(),
        "xmlpathresults": dict()
    }, True)
    ipython.register_magics(JupyterXML)
