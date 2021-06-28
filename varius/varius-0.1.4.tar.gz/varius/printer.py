import re

from IPython.display import Math, display

from . import MagicGlobals as G

__all__ = ["is_ipython", "latex_to_plain", "show", "latex_use_cdot"]


def is_ipython() -> bool:
    import builtins

    return hasattr(builtins, "__IPYTHON__")


def latex_to_plain(latex_string: str) -> str:

    # assume latex string is raw string e.g. r'\text{ab c}'

    pattern = re.compile(r"\\[a-zA-Z]+")  # latex commands like \text \rm

    latex_string = re.sub(pattern, "", latex_string)

    plain = latex_string.replace("{ ", "(").replace("{", "(").replace("}", ")")

    return plain


def show(*args):

    for x in args:

        if G.latex:
            if hasattr(x, "latex_repr"):
                display(Math(x.latex_repr))
            else:
                display(x)
        else:
            if hasattr(x, "latex_repr"):
                print(latex_to_plain(x.latex_repr))
            else:
                print(x)


def latex_use_cdot():
    from sympy.printing.latex import LatexPrinter

    LatexPrinter._default_settings["mul_symbol"] = r"\cdot"
