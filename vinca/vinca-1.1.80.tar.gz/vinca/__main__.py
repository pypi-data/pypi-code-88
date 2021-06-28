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
parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest='subcommand')
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
def subcommand(*subparser_args, parent=subparsers, alias=''):
	def decorator(func):
		parser = parent.add_parser(func.__name__, help=func.__doc__, aliases = [alias] if alias else [])
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

@subcommand(arg('card',type=card_type),alias='s')
def statistics(args):
	card = args.card
	print(f'\nCard #{card.id}')
	print(str(card))
	print(f'Tags: {" ".join(card.tags)}')
	print(f'Due: {card.due_date}')
	print('Date\t\tTime\tGrade')
	print(*[f'{date}\t{time}\t{grade}' for date, time, grade in card.history],sep='\n',end='')
	lines = 5+len(card.history)
	if args.scrollback:
		print(ansi['move_up_line']*lines,end='')

@subcommand(arg('cards',nargs='*',type=card_type, default=ALL_CARDS), alias='S')
def group_statistics(args):
		''' Summary statistics for a set of cards '''
		due_cards = filter.filter(args.cards, due_only=True)
		new_cards = filter.filter(args.cards, new_only=True)
		print('Total', len(args.cards), sep='\t')
		print('Due', len(due_cards), sep='\t')
		print('Total', len(new_cards), sep='\t')
		lines = 3

@subcommand(arg('card',type=card_type),alias='e')
def edit(args):
	''' edit a single card '''
	args.card.edit()

@subcommand(arg('card',type=card_type),alias='E')
def edit_metadata(args):
	''' edit the metadata of a card '''
	args.card.edit_metadata()

@subcommand(arg('cards',type=card_type, default=[]), alias='x')
def delete(args):
	for card in args.cards:
		card.deleted = not card.deleted

@subcommand(arg('cards', type=card_type, default=ALL_CARDS), alias='r')
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
@subcommand(arg('cards', type=card_type, default=ALL_CARDS), alias='b')
def browse(args, reviewing = False):
	args.scrollback = True
	cards = args.cards
	# TODO max frame of ten cards
	n = len(cards); sel = 0
	print('\n'*n,end='')  # move down n lines

	def quit():
		print(ansi['show_cursor'],end='')
		print(ansi['line_wrap_on'], end='')
		exit()
		
	while True:
		print(ansi['hide_cursor'],end='')
		print(ansi['line_wrap_off'], end='')

		print(ansi['move_up_line']*n, end='') # move up n lines
		print(ansi['clear_to_bottom'],end='')
		for i, card in enumerate(cards):
			x = f'{ansi["red"]}deleted{ansi["reset_color"]} '*card.deleted
			d = f'{ansi["blue"]}due{ansi["reset_color"]} '*card.due_as_of(args.review_date)
			hi = ansi['reverse']*(i==sel)
			# print(hi + x + d + str(card) + ansi['reset'])
			print(card.id)
			print(card)
			print(str(card))

		k = 'R' if reviewing else readchar.readchar()

		sel += k=='j'
		sel -= k=='k'
		sel %= n

		if k in QUIT_KEYS:
				quit()
		if k in CMD_DICT:
			args.cards = cards if k in ('S','X') else [cards[sel]]
			CMD_DICT[k](args)
			reviewing = (k == 'R' and cards[sel].last_grade != 'exit')
			if reviewing and sel == n - 1:
				quit()
			elif reviewing and sel < n - 1:
				sel += 1 
		if k in GENERATORS_DICT:
			args.generator = GENERATORS_DICT[k]
			new_cards = generate(args)
			print(new_cards, file = open('log.txt','w+'))
			cards = new_cards + cards
			n += len(new_cards)
			print('\n'*(len(new_cards)), end='')
			
@subcommand(arg('pattern',nargs='?',default=''),
	arg('-v','--invert',action='store_true'),
	arg('-i','--id_only',action='store_true'),
	arg('--cards',type=card_type,nargs='*', default=ALL_CARDS),
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
	alias='f')
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
	
@subcommand()
def purge(args):
	for card in filter.filter(args.cards, deleted_only=True):
		rmtree(card.path)

@subcommand(arg('backup_path',type=Path), arg('--cards', type=card_type, nargs='*', default=ALL_CARDS))
def exp(args):
	backup_cards = args.cards

	for card in backup_cards:
		copytree(card.path, args.backup_dest / str(card.id))

@subcommand(arg('import_path',type=Path), arg('-o','--overwrite', action='store_true'))
def imp(args):
	if args.overwrite:
		rmtree(cards_path)
		copytree(args.import_path, cards_path)
		return
	old_ids = [card.id for card in args.cards]
	for new_id,card_path in enumerate(args.import_path.iterdir(), max(old_ids) + 1):
		copytree(card_path, cards_path / str(new_id))


for alias, generator in GENERATORS_DICT.items():
	p = subparsers.add_parser(generator, aliases=[alias], help='')
	p.set_defaults(func = 'generate', generator = generator)


# parse the command line arguments
parser.set_defaults(cards = [], func = None, review_date = TODAY, scrollback = False)
args = parser.parse_args()
if not args.func:
	args.func = group_statistics
	args.cards = ALL_CARDS
# accept a file of newline separated card ids (from a pipe probably)
if not sys.stdin.isatty():
	ids = [int(line.strip().split()[0]) for line in sys.stdin()]
	args.cards = [Card(id) for id in ids]
	sys.stdin = open('/dev/tty')  
args.func(args)
