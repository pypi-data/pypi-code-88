from vinca.lib import classes
from vinca.lib import ansi

def generate(args):
	new_card = classes.Card(create=True)
	new_card.editor, new_card.reviewer, new_card.scheduler = 'two_lines', 'two_lines', 'base'
	front = input('Q:   ')
	back = input('A:   ')
	(new_card.path/'front').write_text(front)
	(new_card.path/'back').write_text(back)
	if args.scrollback:
		ansi.up_line(2)
	return [new_card]
