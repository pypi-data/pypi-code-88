# Functions
from pathlib import Path
from shutil import copytree, rmtree
import sys
import inspect
import readchar  # 3rd party module for reading a character one at a time

from vinca.lib import classes
from vinca.lib import filter
from vinca.lib.ansi import ansi
from vinca import generators
COLORIZE = sys.stdout.isatty()
GENERATORS_DICT = {'m': 'media', 'v':'verses', '2': 'two_lines'}
QUIT_KEYS = ['q', readchar.key.ESC, '\n', '\r']


cards_path = Path(__file__).parent / 'cards'

def generate(args):
	return generators.generate(args)

def add_many(args): 
	print(ansi['hide_cursor'],end='')
	print(*[f'{key}\t{generator}' for key, generator in GENERATORS_DICT.items()],sep='\n')
	k = readchar.readchar()
	if k not in GENERATORS_DICT: return
	args.generator = GENERATORS_DICT[k]
	args.cards = generators.generate(args)
	print(ansi['move_up_line']*(len(GENERATORS_DICT)+2) + ansi['clear_to_bottom'],end='')
	browse(args)
def statistics(args):
	if len(args.cards) == 1:
		card = args.cards[0]
		print(f'\nCard #{card.id}')
		print(str(card))
		print(f'Tags: {" ".join(card.tags)}')
		print(f'Due: {card.due_date}')
		print('Date\t\tTime\tGrade')
		print(*[f'{date}\t{time}\t{grade}' for date, time, grade in card.history],sep='\n',end='')
		lines = 5+len(card.history)
	else:
		due_cards = filter.filter(args.cards, due_only=True)
		new_cards = filter.filter(args.cards, new_only=True)
		print('Total', len(args.cards), sep='\t')
		print('Due', len(due_cards), sep='\t')
		print('Total', len(new_cards), sep='\t')
		lines = 3
	if args.scrollback:
		print(ansi['move_up_line']*lines,end='')
def edit(args):
	card = args.cards[0]
	card.edit()
def edit_metadata(args):
	card = args.cards[0]
	card.edit_metadata()
def delete(args):
	for card in args.cards:
		card.deleted = not card.deleted
def review(args):
	if len(args.cards) == 1:
		card =  args.cards[0]
		card.review()
		card.schedule()
	else:
		args.cards = filter.filter(args.cards, due_only = True)
		if not args.cards:
			print('No cards due.')
			return
		browse(args, reviewing = True)

CMD_DICT = {'r': review, 'R': review,
	    's': statistics, 'S': statistics,
	    'x': delete, 'X': delete,
	    'e': edit, 'E': edit_metadata}
def browse(args, reviewing = False):
	args.scrollback = True
	cards = args.cards
	# TODO max frame of ten cards
	n = len(cards); sel = 0
	print('\n'*n,end='')  # move down n lines
	while True:
		print(ansi['hide_cursor'],end='')
		print(ansi['line_wrap_off'], end='')

		print(ansi['move_up_line']*n, end='') # move up n lines
		print(ansi['clear_to_bottom'],end='')
		for i, card in enumerate(cards):
			x = (ansi['red']+'[deleted] ' + ansi['reset_color'])*card.deleted
			d = (ansi['red'] + '[due] ' + ansi['reset_color'])*card.due_as_of(args.review_date)
			hi = ansi['reverse']*(i==sel)
			print(f'{hi}{x}{card}{ansi["reset"]}')

		k = 'R' if reviewing else readchar.readchar()

		sel += k=='j'
		sel -= k=='k'
		sel %= n

		if k in QUIT_KEYS:
				print(ansi['show_cursor'],end='')
				print(ansi['line_wrap_on'], end='')
				break
		if k in CMD_DICT:
			args.cards = cards if k in ('S','X') else [cards[sel]]
			CMD_DICT[k](args)
			reviewing = (k == 'R' and cards[sel].last_grade != 'exit')
			if reviewing and sel == n - 1:
				print(ansi['show_cursor'],end='')
				print(ansi['line_wrap_on'], end='')
				break
			elif reviewing and sel < n - 1:
				sel += 1 
		if k in GENERATORS_DICT:
			args.generator = GENERATORS_DICT[k]
			new_cards = generators.generate(args)
			cards = new_cards + cards
			print('\n'*len(new_cards))
			n += len(new_cards)
			
def display_filter(args):
	# get filter parameters as a list of strings
	filter_kwargs = inspect.getargspec(filter.filter).args[1:]
	# check that args specifies these parameters
	assert all([hasattr(args, param) for param in filter_kwargs])
	matches = filter.filter(args.cards,
		# feed the keyword args editor=args.editor, due=args.due, 
		**{param : getattr(args, param) for param in filter_kwargs})
	for card in matches:
		d = (ansi['red']+'[deleted]' + ansi['reset_color'] + ' ')*card.deleted
		print(str(card.id) + f'\t{d}{card}'*(not args.id_only))
	
def purge(args):
	for card in filter.filter(args.cards, deleted_only=True):
		rmtree(card.path)

def exp(args):
	backup_cards = args.cards

	for card in backup_cards:
		copytree(card.path, args.backup_dest / str(card.id))
def imp(args):
	if args.overwrite:
		rmtree(cards_path)
		copytree(args.import_path, cards_path)
		return
	old_ids = [card.id for card in args.cards]
	for new_id,card_path in enumerate(args.import_path.iterdir(), max(old_ids) + 1):
		copytree(card_path, cards_path / str(new_id))

