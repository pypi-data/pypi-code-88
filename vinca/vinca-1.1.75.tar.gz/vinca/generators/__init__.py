import importlib
import datetime, time
TODAY = datetime.date.today()


def generate(args):
	start = time.time()
	generator = args.generator
	m = importlib.import_module('.'+generator, package = 'vinca.generators')
	new_cards = m.generate()
	stop = time.time()
	elapsed = int(stop - start)
	
	for card in new_cards:
		# card.tags = card.tags + args.tags
		card.make_string()
		card.add_history(TODAY, elapsed, 'create')
