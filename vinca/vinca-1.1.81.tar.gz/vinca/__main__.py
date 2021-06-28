import sys
import inspect
import readchar
import argparse
import datetime
from pathlib import Path
from shutil import copytree, rmtree

from vinca.lib.classes import Card
from vinca.lib.ansi import ansi
from vinca.lib import filter
from vinca.generators import generate, GENERATORS_DICT

TODAY = datetime.date.today()

COLORIZE = sys.stdout.isatty()
QUIT_KEYS = ['q', readchar.key.ESC, '\n', '\r']

vinca_path = Path(__file__).parent 
cards_path = vinca_path / 'cards'
ALL_CARDS = [Card(int(id.name)) for id in cards_path.iterdir()]

# ARGUMENT PARSING
parser = argparse.ArgumentParser(usage=argparse.SUPPRESS)
subparsers = parser.add_subparsers()
def card_type(arg):
	id = int(arg.split()[0])  # grab the first field of the argument
	return Card(id)
def date_type(s):
	if s[s[0] in ['+','-']:].isdigit():
		return TODAY + int(arg) * DAY
	try:
		return datetime.datetime.strptime(s, '%Y-%m-%d').date()
	except ValueError:
		raise argparse.ArgumentTypeError(f'''\n\n
			Invalid Date: {s}. Valid dates are:
			1) -7		(one week ago)
			2) 2021-06-03	(June 3rd)''')
def arg(*names_or_flags, **kwargs):
	return names_or_flags, kwargs
CARDS = arg('cards',nargs='*',type=card_type, default=ALL_CARDS)
CARD = arg('card',type=card_type)
OPTIONAL_CARD = arg('card', nargs='?', type=card_type)
OPTIONAL_CARDS = arg('--cards',nargs='*',type=card_type,default=ALL_CARDS)
OPTIONAL_CARDS_DEFAULT_NONE = arg('--cards',nargs='*',type=card_type,default=[])
def subcommand(*subparser_args, parent=subparsers, alias='', name=None):
	def decorator(func, alias=alias, name=name):
		name = name if name else func.__name__
		description = func.__doc__
		aliases = [alias] if alias else []
		parser = parent.add_parser(name, help='', description=description, aliases=aliases,
		                           usage=argparse.SUPPRESS, formatter_class=argparse.RawDescriptionHelpFormatter)
		for args, kwargs in subparser_args:
			parser.add_argument(*args, **kwargs)
		parser.set_defaults(func=func)
		return func
	return decorator

@subcommand(alias='a')
def add(args): 
	print(ansi['hide_cursor'],end='')
	print(*[f'{key}\t{generator}' for key, generator in GENERATORS_DICT.items()],sep='\n')
	k = readchar.readchar()
	if k not in GENERATORS_DICT: return
	args.generator = GENERATORS_DICT[k]
	args.cards = generate(args)
	print(ansi['move_up_line']*(len(GENERATORS_DICT)+2) + ansi['clear_to_bottom'],end='')
	browse(args)

@subcommand(OPTIONAL_CARD, OPTIONAL_CARDS, alias='s')
def statistics(args):
	if args.card:
		card = args.card
		print(f'\nCard #{card.id}')
		print(str(card))
		print(f'Tags: {" ".join(card.tags)}')
		print(f'Due: {card.due_date}')
		print('Date\t\tTime\tGrade')
		print(*[f'{date}\t{time}\t{grade}' for date, time, grade in card.history],sep='\n',end='')
		lines = 5+len(card.history)
	elif args.cards:
		due_cards = filter.filter(args.cards, due_only=True)
		new_cards = filter.filter(args.cards, new_only=True)
		print('Total', len(args.cards), sep='\t')
		print('Due', len(due_cards), sep='\t')
		print('New', len(new_cards), sep='\t')
		lines = 3
	if args.scrollback:
		print(ansi['move_up_line']*lines,end='')

@subcommand(CARD,alias='e')
def edit(args):
	''' edit a single card '''
	args.card.edit()

@subcommand(CARD,alias='E')
def edit_metadata(args):
	''' edit the metadata of a card '''
	args.card.edit_metadata()

@subcommand(OPTIONAL_CARD, OPTIONAL_CARDS_DEFAULT_NONE, alias='x')
def delete(args):
	if args.card:
		args.card.deleted = not args.card.deleted
	elif args.cards:
		for card in args.cards:
			card.deleted = not card.deleted

@subcommand(CARDS, alias='r')
def review(args):
	if args.card:
		args.card.review()
		args.card.schedule()
	elif args.cards:
		args.cards = filter.filter(args.cards, due_only = True)
		if not args.cards:
			print('No cards due.')
			return
		browse(args, reviewing = True)

CMD_DICT = {'r': review, 'R': review,
	    's': statistics, 'S': statistics,
	    'x': delete, 'X': delete,
	    'e': edit, 'E': edit_metadata}
@subcommand(CARDS, alias='b')
def browse(args, reviewing = False):
	args.scrollback = True
	cards = args.cards
	# TODO max frame of ten cards
	n = len(cards); sel = 0

	def quit():
		print(ansi['show_cursor'],end='')
		print(ansi['line_wrap_on'], end='')
		print(ansi['clear_to_bottom'],end='')
		exit()
	def draw_browser():
		print(ansi['hide_cursor'],end='')
		print(ansi['line_wrap_off'], end='')

		for i, card in enumerate(cards):
			x = f'{ansi["red"]}deleted{ansi["reset_color"]} '*card.deleted
			d = f'{ansi["blue"]}due{ansi["reset_color"]} '*card.due_as_of(args.review_date)
			hi = ansi['reverse']*(i==sel)
			print(hi + x + d + str(card) + ansi['reset'])
	def redraw_browser():
		print(ansi['move_up_line']*n, end='') 
		print(ansi['clear_to_bottom'],end='')
		draw_browser()
		
	draw_browser()
	while True:

		k = 'R' if reviewing else readchar.readchar()

		sel += k=='j'
		sel -= k=='k'
		sel %= n

		if k in QUIT_KEYS:
				quit()
		if k in CMD_DICT:
			args.card = cards[sel] if k in ('x','s','r','R','e','E') else None
			CMD_DICT[k](args)
			reviewing = (k == 'R' and cards[sel].last_grade != 'exit')
			if reviewing and sel == n - 1:
				quit()
			elif reviewing and sel < n - 1:
				sel += 1 
		if k in GENERATORS_DICT:
			args.generator = GENERATORS_DICT[k]
			new_cards = generate(args)
			cards[sel:sel] = new_cards
			n = len(cards)
			print('\n'*(len(new_cards)), end='')

		if k not in ('s','S'):
			redraw_browser()
			

@subcommand(arg('pattern',nargs='?',default=''),
	arg('-v','--invert',action='store_true'),
	arg('-i','--id_only',action='store_true'),
	arg('--cards',nargs='*',type=card_type, default=ALL_CARDS),
	arg('--tags_include',nargs='*', metavar='TAGS'),
	arg('--tags_exclude',nargs='*', metavar='TAGS'),
	arg('--create_date_min',type=date_type, metavar='DATE'),
	arg('--create_date_max',type=date_type, metavar='DATE'),
	arg('--seen_date_min',type=date_type, metavar='DATE'),
	arg('--seen_date_max',type=date_type, metavar='DATE'),
	arg('--due_date_min',type=date_type, metavar='DATE'),
	arg('--due_date_max',type=date_type, metavar='DATE'),
	arg('--due_only',action='store_true'),
	arg('--not_due_only',action='store_true'),
	arg('--editor', type=str),
	arg('--reviewer', type=str),
	arg('--scheduler', type=str),
	arg('--deleted_only',action='store_true'),
	arg('--show_deleted',action='store_true'),
	arg('--new_only',action='store_true'),
	arg('--not_new_only',action='store_true'),
	alias='f', name='filter')
def display_filter(args):
	''' Filter a set of cards using a variety of parameters.
	Piping the output of this \033[32m command to another vinca command will
	provide a list of cards.'''

	# get filter parameters as a list of strings
	filter_kwargs = inspect.getfullargspec(filter.filter).args[1:]
	# check that args specifies these parameters
	assert all([hasattr(args, param) for param in filter_kwargs])
	matches = filter.filter(args.cards,
		# feed the keyword args editor=args.editor, due=args.due, 
		**{param : getattr(args, param) for param in filter_kwargs})
	for card in matches:
		d = (ansi['red']+'[deleted]' + ansi['reset_color'] + ' ')*card.deleted
		print(str(card.id) + f'\t{d}{card}'*(not args.id_only))
	
@subcommand()
def purge(args):
	for card in filter.filter(ALL_CARDS, deleted_only=True):
		rmtree(card.path)

@subcommand(arg('backup_path',type=Path), CARDS, name='export')
def exp(args):
	for card in args.cards:
		copytree(card.path, args.backup_path / str(card.id))

@subcommand(arg('import_path',type=Path), arg('-o','--overwrite', action='store_true'), name='import')
def imp(args):
	if args.overwrite:
		rmtree(cards_path)
		copytree(args.import_path, cards_path)
		return
	old_ids = [card.id for card in ALL_CARDS]
	for new_id,card_path in enumerate(args.import_path.iterdir(), max(old_ids, default=1) + 1):
		copytree(card_path, cards_path / str(new_id))

for alias, generator in GENERATORS_DICT.items():
	p = subparsers.add_parser(generator, aliases=[alias], help='')
	p.set_defaults(func = generate, generator = generator)

# parse the command line arguments
parser.set_defaults(cards = [], func = None, review_date = TODAY, scrollback = False, card = None)
args = parser.parse_args()
if not args.func:
	args.func = statistics
	args.card = None
	args.cards = ALL_CARDS
# accept a file of newline separated card ids
if not sys.stdin.isatty():
	ids = [int(line.strip().split()[0]) for line in sys.stdin]
	args.cards = [Card(id) for id in ids]
	sys.stdin = open('/dev/tty')  
args.func(args)
