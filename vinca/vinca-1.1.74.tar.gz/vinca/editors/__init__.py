import datetime
today = datetime.date.today()
import importlib

def edit(card, mode):
	start = datetime.datetime.now()

	m = importlib.import_module('.' + card.editor, package = 'vinca.editors')
	m.edit(card, mode)

	stop = datetime.datetime.now()
	elapsed_time = min(240, (stop - start).seconds)

	card.add_history(today, elapsed_time, 0)
