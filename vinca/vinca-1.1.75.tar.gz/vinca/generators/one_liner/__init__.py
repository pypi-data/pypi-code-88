from vinca.lib import classes
from vinca.lib.ansi import ansi

def generate():
	new_card = classes.Card(create=True)
	new_card.editor, new_card.reviewer, new_card.scheduler = 'base', 'base', 'base'
	front = input('Q:   ')
	back = input('A:   ')
	(new_card.path/'front').write_text(front)
	(new_card.path/'back').write_text(back)
	return [new_card]
