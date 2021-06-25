import argparse
from pathlib import Path
import datetime
TODAY = datetime.date.today()
DAY = datetime.timedelta(days=1)

from vinca.lib import classes

# type checking
def card_type(arg):
	arg = arg.split()[0]  # grab the first field of the argument
	assert arg.isdigit()
	return classes.Card(int(arg))
def date_type(arg):
	try:
		return TODAY + int(arg) * DAY
	except:
		pass  # arg cannot be interpreted as an integer
	try:
		return datetime.datetime.strptime(arg, '%Y-%m-%d').date()
	except:
		raise argparse.ArgumentTypeError(f'''\n\n
			Invalid Date: {arg}. Valid dates are:
			1) -7		(one week ago)
			2) 2021-06-03	(June 3rd)''')

# argument parsing
parser = argparse.ArgumentParser()
parser.set_defaults(cards = [], func = 'statistics', generator = 'two_lines', review_date = TODAY, scrollback = False)
subparsers = parser.add_subparsers()
# commands which take a nothing as an argument
two_lines = subparsers.add_parser('two_lines',aliases=['2'],
	help='add a card quickly')
two_lines.set_defaults(func = 'generate', generator = 'two_lines')

verses = subparsers.add_parser('verses_add',aliases=['v'],
	help='for lyrics, poetry, oratory, etc.')
verses.set_defaults(func = 'generate', generator = 'verses')

media = subparsers.add_parser('media',aliases=['m'],
	help='add a basic card with optional audio or images')
media.set_defaults(func = 'generate', generator = 'media')

add_many= subparsers.add_parser('add_many',aliases=['a'],
	help='add several basic cards')
add_many.set_defaults(func = 'add_many')

# filter
filter= subparsers.add_parser('filter',aliases=['f'], help='')
filter.add_argument('pattern',nargs='?',default='')
# optional args of filter function
filter.add_argument('-v','--invert',action='store_true')
filter.add_argument('--cards',type=card_type,nargs='+', default=[])
filter.add_argument('--tags_include',nargs='+', metavar='TAGS')
filter.add_argument('--tags_exclude',nargs='+', metavar='TAGS')
filter.add_argument('--create_date_min',type=date_type, metavar='DATE')
filter.add_argument('--create_date_max',type=date_type, metavar='DATE')
filter.add_argument('--seen_date_min',type=date_type, metavar='DATE')
filter.add_argument('--seen_date_max',type=date_type, metavar='DATE')
filter.add_argument('--due_date_min',type=date_type, metavar='DATE')
filter.add_argument('--due_date_max',type=date_type, metavar='DATE')
filter.add_argument('--due_only',action='store_true')
filter.add_argument('--not_due_only',action='store_true')
filter.add_argument('--editor', type=str)
filter.add_argument('--reviewer', type=str)
filter.add_argument('--scheduler', type=str)
filter.add_argument('--deleted_only',action='store_true')
filter.add_argument('--show_deleted',action='store_true')
filter.add_argument('--new_only',action='store_true')
filter.add_argument('--not_new_only',action='store_true')
# other
filter.add_argument('-i','--id_only',action='store_true')
filter.set_defaults(func = 'display_filter')

browse = subparsers.add_parser('browse', aliases=['b'], help='')
browse.set_defaults(func = 'browse')

# commands which take cards as an argument 
review= subparsers.add_parser('review',aliases=['r'],
	help='')
review.add_argument('cards', type=card_type, nargs='*')
review.add_argument('--review_date', type=date_type, default=TODAY,
	help='review as if today was [date]')
review.set_defaults(func = 'review')

statistics= subparsers.add_parser('statistics',aliases=['s'],
	help='')
statistics.add_argument('cards', type=card_type, nargs='*')
statistics.set_defaults(func = 'statistics')
# TODO miscellaneous options for more advanced statistics
edit= subparsers.add_parser('edit',aliases=['e'],
	help='')
edit.add_argument('cards',type=card_type,nargs=1)
edit.set_defaults(func = 'edit')

edit_metadata= subparsers.add_parser('edit_metadata',aliases=['E'],
	help='')
edit_metadata.add_argument('cards',type=card_type,nargs=1)
edit_metadata.set_defaults(func = 'edit_metadata')

delete= subparsers.add_parser('delete',aliases=['x'],
	help='')
delete.add_argument('cards',type=card_type, nargs='*')
delete.set_defaults(func = 'delete')

# PURGE
purge= subparsers.add_parser('purge',
	help='permanently delete cards')
purge.set_defaults(func = 'purge')

# commands which take a path as an argument (import / backup)
# IMPORT EXPORT
exp = subparsers.add_parser('export',
	help='')
exp.add_argument('backup_dest',type=Path)
exp.add_argument('cards',type=card_type,nargs='*') 
exp.set_defaults(func = 'backup')

imp = subparsers.add_parser('import',
	help='')
imp.add_argument('import_path',type=Path)
imp.add_argument('-o','--overwrite',action='store_true',
	help='overwrite the existing collection')
imp.set_defaults(func = 'import_collection')

