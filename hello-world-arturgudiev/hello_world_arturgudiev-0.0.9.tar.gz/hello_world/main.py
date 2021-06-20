# main.py
from colour_text import ColourText


def hello_world():
	print("Hello World")


def foo():
	return 555


def f():
	ct = ColourText()
	ct.initTerminal()

	print(ct.convert("The next section is in green: <>green example<>."))
	print(ct.convert("<>red HERE! HERE! HERE! HERE! HERE! HERE! HERE! <>."))
