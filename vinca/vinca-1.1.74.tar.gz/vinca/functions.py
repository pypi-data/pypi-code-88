# Functions
from pathlib import Path
from shutil import copytree, rmtree
import subprocess
import inspect
import readchar  # 3rd party module for reading a character one at a time

from vinca.lib import classes
from vinca.lib import filter
from vinca.lib.ansi import ansi
from vinca.lib.terminal import COLUMNS, LINES, TAB_WIDTH
from vinca import generators

vinca_path = Path(__file__) # /path/to/vinca/functions.py
vinca_path = vinca_path.parent # /path/to/vinca
cards_path = vinca_path / 'cards'
ALL_CARDS = [classes.Card(int(id.name)) for id in cards_path.iterdir()]

def generate(args):
	generators.generate(args)

def add_many(args): 
	add_cmds = {'a': add, 'l': linear_add, '1': one_liner}
	print(ansi['hide_cursor'],end='')
	print('Add Cards')
	print(*[f'{key}\t{cmd.__name__}' for key,cmd in add_cmds.items()],sep='\n')
	k = readchar.readchar()
	if k not in add_cmds:
		print(ansi['show_cursor'],end='')
		return
	new_card = add_cmds[k](args)
	print(ansi['move_up_line']*(1+len(add_cmds)) + ansi['clear_to_bottom'],end='')
	visual_select(args,[new_card],mode='cards')
def statistics(args):
	if len(args.cards) == 1:
		card = args.cards[0]
		print(f'\nCard #{card.id}')
		print(str(card)[:COLUMNS])
		print(f'Tags: {" ".join(card.tags)}')
		print(f'Due: {card.due_date}')
		print('Date\t\tTime\tGrade')
		print(*[f'{date}\t{time}\t{grade}' for date, time, grade in card.history],sep='\n',end='')
		if args.mode=='visual':
			print(ansi['move_up_line']*(5+len(card.history)), end='')
		return
	due_cards = filter.filter(ALL_CARDS, due_only=True)
	new_cards = filter.filter(ALL_CARDS, new_only=True)
	print(f'Total\t{len(ALL_CARDS)}')
	print(f'Due\t{len(due_cards)}')
	print(f'New\t{len(new_cards)}')
	if args.mode=='visual':
		print(ansi['move_up_line']*3,end='')
def edit(args):
	if args.cards:
		card = args.cards[0]
		card.edit()
		# refresh the card's summary string
		card.make_string()
		return
def advanced_edit(args):
	card = args.cards[0]
	subprocess.run(['vim', card.metadata_path])
	card.load_metadata()
def delete(args):
	for card in args.cards:
		if card.deleted: card.undelete()
		else: card.delete()

# visual selection
cmd_dict = {'A':add_many,
	    'e':edit,
	    'x':delete,
	    'S':statistics, }
def visual_select(args, cards):
	# TODO convert my card_id list into a card list on the fly
	
	n = len(iterable)
	sel = 0  # selected number
	print('\n'*n,end='')  # move down n lines
	while True:
		print(ansi['move_up_line']*n,end='') # move up n lines
		for i, item in enumerate(iterable):
			d = (ansi['red']+'[deleted] ' + ansi['reset_color'] + ' ')*item.deleted
			print(f'{ansi["reverse"]*(i==sel)}{item.id}\t{d}{item}{ansi["reset"]}')
		k = readchar.readchar()  # get key
		sel = (sel + (k=='j') - (k=='k') ) % n

		if k in ['q', readchar.key.ESC, '\n', '\r']:
			print(ansi['clear_to_bottom'],end='')
			return
		if k in cmd_dict:
			print(ansi['clear_to_bottom'],end='')
			if mode=='cards': args.cards = [iterable[sel]]
			new_card = cmd_dict[k](args)
			if new_card and mode=='cards':
				iterable = [new_card] + iterable
				print('')  # print a blank newline
				n += 1
				sel = 0
def filter(args):
	unfiltered_cards = args.cards if args.cards else ALL_CARDS
	# get filter parameters as a list of strings
	filter_kwargs = inspect.getargspec(filter.filter).args[1:]
	# check that args has these. (E.g. if reviewer is a parameter, check args.reviewer exists.)
	assert all([hasattr(args, param) for param in filter_kwargs])
	matches = filter.filter(unfiltered_cards,
		# feed the keyword args editor=args.editor, due=args.due, 
		**{param : getattr(args, param) for param in filter_kwargs})
	if not matches:
		print('No matches.')
		return
	if args.mode=='visual':
		visual_select(args, matches, mode='cards')
		return
	for card in matches:
		d = (ansi['red']+'[deleted]' + ansi['reset_color'] + ' ')*card.deleted
		print(card.id if args.id_only else f'{card.id}\t{d}{card}')

def purge(args):
	for card in filter.filter(deleted_only=True):
		rmtree(card.path)
# backup / export
def backup(args):
	backup_cards = args.cards if args.cards else filter.filter()

	for card in backup_cards:
		copytree(card.path, args.backup_dest / str(card.id))
def import_collection(args):
	if args.overwrite:
		rmtree(cards_path)
		copytree(args.import_path, cards_path)
		return
	old_ids = [card.id for card in ALL_CARDS]
	for new_id,card_path in enumerate(args.import_path.iterdir(), max(old_ids) + 1):
		copytree(card_path, cards_path / str(new_id))

