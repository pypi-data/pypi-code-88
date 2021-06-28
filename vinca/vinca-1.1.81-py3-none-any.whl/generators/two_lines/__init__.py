from vinca.lib import classes
from vinca.lib.ansi import ansi

def generate(args):
	new_card = classes.Card(create=True)
	new_card.editor, new_card.reviewer, new_card.scheduler = 'two_lines', 'two_lines', 'base'
	front = input('Q:   ')
	back = input('A:   ')
	(new_card.path/'front').write_text(front)
	(new_card.path/'back').write_text(back)
	if args.scrollback:
		print(ansi['move_up_line']*2, end='')
	return [new_card]
