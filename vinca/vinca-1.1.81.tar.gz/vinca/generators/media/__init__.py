from vinca.lib import classes

def generate(args):
	new_card = classes.Card(create=True)
	new_card.editor, new_card.reviewer, new_card.scheduler = 'media', 'media', 'base'
	new_card.edit()  
	return [new_card]
