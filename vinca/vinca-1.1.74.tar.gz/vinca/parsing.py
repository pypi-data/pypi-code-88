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
one_liner_parser = subparsers.add_parser('one_liner',aliases=['1'],
	help='add a basic card quickly')
one_liner_parser.set_defaults(func = 'generate', generator = 'one_liner')

linear_add_parser = subparsers.add_parser('linear_add',aliases=['l'],
	help='for lyrics, poetry, oratory, etc.')
linear_add_parser.set_defaults(func = 'generate', generator = 'linear')

add_parser = subparsers.add_parser('add_vim',aliases=['a'],
	help='add a basic card')
add_parser.set_defaults(func = 'generate', generator = 'vim')

add_many_parser = subparsers.add_parser('add_many',aliases=['A'],
	help='add several basic cards')
add_many_parser.set_defaults(func = 'add_many')


image_cloze_parser = subparsers.add_parser('image_cloze',aliases=['ic'],
	help='generate an image cloze card')
image_cloze_parser.add_argument('image_path',type=Path)
image_cloze_parser.set_defaults(func = 'image_cloze')

# filter
filter_parser = subparsers.add_parser('filter',aliases=['f'])
filter_parser.add_argument('pattern',nargs='?',default='')
# optional args of filter function
filter_parser.add_argument('-v','--invert',action='store_true')
filter_parser.add_argument('--cards',type=card_type,nargs='+', default=[])
filter_parser.add_argument('--tags_include',nargs='+', metavar='TAGS')
filter_parser.add_argument('--tags_exclude',nargs='+', metavar='TAGS')
filter_parser.add_argument('--create_date_min',type=date_type, metavar='DATE')
filter_parser.add_argument('--create_date_max',type=date_type, metavar='DATE')
filter_parser.add_argument('--seen_date_min',type=date_type, metavar='DATE')
filter_parser.add_argument('--seen_date_max',type=date_type, metavar='DATE')
filter_parser.add_argument('--due_date_min',type=date_type, metavar='DATE')
filter_parser.add_argument('--due_date_max',type=date_type, metavar='DATE')
filter_parser.add_argument('--due_only',action='store_true')
filter_parser.add_argument('--not_due_only',action='store_true')
filter_parser.add_argument('--editor', type=str)
filter_parser.add_argument('--reviewer', type=str)
filter_parser.add_argument('--scheduler', type=str)
filter_parser.add_argument('--deleted_only',action='store_true')
filter_parser.add_argument('--show_deleted',action='store_true')
filter_parser.add_argument('--new_only',action='store_true')
filter_parser.add_argument('--not_new_only',action='store_true')
filter_parser.add_argument('--no_fancy',action='store_true')
filter_parser.set_defaults(func = 'filter')
# other
filter_parser.add_argument('-i','--id_only',action='store_true')

# commands which take cards as an argument 
study_parser = subparsers.add_parser('study',aliases=['s'],
	help='study the collection or selected card(s)')
study_parser.add_argument('cards', type=card_type, nargs='*')
study_parser.add_argument('--date', type=int,
	help='study as if today was [date]')
study_parser.set_defaults(func = 'study')

preview_parser = subparsers.add_parser('preview',aliases=['p'],
	help='preview the collection or selected card(s)')
preview_parser.add_argument('cards', type=card_type, nargs='*')
preview_parser.add_argument('--date', type=int,
	help='preview as if today was [date]')
preview_parser.set_defaults(func = 'preview')

statistics_parser = subparsers.add_parser('statistics',aliases=['S'],
	help='statistics about the selected cards')
statistics_parser.add_argument('cards', type=card_type, nargs='*')
statistics_parser.set_defaults(func = 'statistics')
# TODO miscellaneous options for more advanced statistics
edit_parser = subparsers.add_parser('edit',aliases=['e'],
	help='edit the selected card(s)')
edit_parser.add_argument('cards',type=card_type,nargs='*')
edit_parser.set_defaults(func = 'edit')

advanced_edit_parser = subparsers.add_parser('advanced_edit',aliases=['E'],
	help='edit the selected card(s)')
advanced_edit_parser.add_argument('cards',type=card_type,nargs=1)
advanced_edit_parser.set_defaults(func = 'advanced_edit')

delete_parser = subparsers.add_parser('delete',aliases=['x'],
	help='delete the selected card(s)')
delete_parser.add_argument('cards',type=card_type, nargs='*')
delete_parser.set_defaults(func = 'delete')

# PURGE
purge_parser = subparsers.add_parser('purge',
	help='permanently delete all deleted cards')
purge_parser.set_defaults(func = 'purge')

# commands which take a path as an argument (import / backup)
# IMPORT EXPORT
backup_parser = subparsers.add_parser('backup',aliases=['b','export'],
	help='backup all cards')
backup_parser.add_argument('backup_dest',type=Path)
backup_parser.add_argument('cards',type=card_type,nargs='*') 
backup_parser.set_defaults(func = 'backup')

import_parser = subparsers.add_parser('import',aliases=['i'],
	help='import a collection of cards')
import_parser.add_argument('import_path',type=Path)
import_parser.add_argument('-o','--overwrite',action='store_true',
	help='overwrite the existing collection')
import_parser.set_defaults(func = 'import_collection')

