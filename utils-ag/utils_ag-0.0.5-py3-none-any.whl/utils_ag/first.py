from colour_text import ColourText

from utils_ag.filesystem import get_file_content


def f():
    ct = ColourText()
    ct.initTerminal()

    print(ct.convert("The next section is in green: <>green example<>."))
    print(ct.convert("<>red HERE! HERE! HERE! HERE! HERE! HERE! HERE! <>."))


def fff2():
    print(123)

