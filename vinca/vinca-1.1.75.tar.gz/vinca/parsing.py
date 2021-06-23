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
parser.set_defaults(cards = [], func = 'statistics', generator = 'one_liner')
subparsers = parser.add_subparsers()
# commands which take a nothing as an argument
one_liner = subparsers.add_parser('one_liner',aliases=['1'],
	help='add a basic card quickly')
one_liner.set_defaults(func = 'generate', generator = 'one_liner')

linear_add = subparsers.add_parser('linear_add',aliases=['l'],
	help='for lyrics, poetry, oratory, etc.')
linear_add.set_defaults(func = 'generate', generator = 'linear')

add= subparsers.add_parser('add_vim',aliases=['a'],
	help='add a basic card')
add.set_defaults(func = 'generate', generator = 'vim')

add_many= subparsers.add_parser('add_many',aliases=['A'],
	help='add several basic cards')
add_many.set_defaults(func = 'add_many')


image_cloze= subparsers.add_parser('image_cloze',aliases=['ic'],
	help='generate an image cloze card')
image_cloze.add_argument('image_path',type=Path)
image_cloze.set_defaults(func = 'image_cloze')

# filter
filter= subparsers.add_parser('filter',aliases=['f'])
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
filter.add_argument('--no_fancy',action='store_true')
# other
filter.add_argument('-i','--id_only',action='store_true')
filter.set_defaults(func = 'display_filter')

browse = subparsers.add_parser('browse', aliases=['b'])
browse.set_defaults(func = 'browse')

# commands which take cards as an argument 
review= subparsers.add_parser('review',aliases=['r'],
	help='review the collection or selected card(s)')
review.add_argument('cards', type=card_type, nargs='*')
review.add_argument('--date', type=int,
	help='review as if today was [date]')
review.set_defaults(func = 'review')

statistics= subparsers.add_parser('statistics',aliases=['s'],
	help='statistics about the selected cards')
statistics.add_argument('cards', type=card_type, nargs='*')
statistics.set_defaults(func = 'statistics')
# TODO miscellaneous options for more advanced statistics
edit= subparsers.add_parser('edit',aliases=['e'],
	help='edit the selected card(s)')
edit.add_argument('cards',type=card_type,nargs=1)
edit.set_defaults(func = 'edit')

edit_metadata= subparsers.add_parser('edit_metadata',aliases=['E'],
	help='edit the selected card(s)')
edit_metadata.add_argument('cards',type=card_type,nargs=1)
edit_metadata.set_defaults(func = 'edit_metadata')

delete= subparsers.add_parser('delete',aliases=['x'],
	help='delete the selected card(s)')
delete.add_argument('cards',type=card_type, nargs='*')
delete.set_defaults(func = 'delete')

# PURGE
purge= subparsers.add_parser('purge',
	help='permanently delete all deleted cards')
purge.set_defaults(func = 'purge')

# commands which take a path as an argument (import / backup)
# IMPORT EXPORT
exp = subparsers.add_parser('export',
	help='backup all cards')
exp.add_argument('backup_dest',type=Path)
exp.add_argument('cards',type=card_type,nargs='*') 
exp.set_defaults(func = 'backup')

imp = subparsers.add_parser('import',
	help='import a collection of cards')
imp.add_argument('import_path',type=Path)
imp.add_argument('-o','--overwrite',action='store_true',
	help='overwrite the existing collection')
imp.set_defaults(func = 'import_collection')

