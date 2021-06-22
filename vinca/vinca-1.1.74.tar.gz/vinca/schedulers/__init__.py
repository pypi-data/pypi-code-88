import importlib

def schedule(card):

	if card.last_grade == -1:
		card.delete()
		return 0

	# import the specific scheduler module
	m = importlib.import_module('.' + card.scheduler, package = 'vinca.schedulers')
	# invoke the specific scheduler
	return m.schedule(card)
