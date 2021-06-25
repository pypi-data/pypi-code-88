from Alexandria.general.console import print_color


def latex_eq(var, formula):
    print_color(r"\begin{equation}", "blue")
    print_color(f"   {var} = {formula}", "blue")
    print_color(r"\end{equation}", "blue")


