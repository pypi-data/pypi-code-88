from dvol.dvol_helpers.dvol_remove import determine_remove
from dvol.dvol_helpers.common import *

files_help = 'Also remove local folder'
path_help = 'Override {root}{container}{remote} path logic and use provided folder'
remote_help = 'Remote folder mapping to remove'
all_help = 'Remove all volume mappings. Combine with -f for the nuke.'

cmd_remove_desc = f'Remove volume map, leaving files unless {f_argument("--files")} given.'

def create (subs):
    remove_p = subs.add_parser('remove', help = cmd_remove_desc, aliases = ['rm'])
    remove_p.set_defaults(func = determine_remove)
    remove_p.add_argument('-f', '--files', help = files_help, dest = 'remove_files', action = 'store_true')
    remove_p.add_argument('-p', '--path', help = path_help, dest = 'local_path')
    all_or_something = remove_p.add_mutually_exclusive_group(required = True)
    all_or_something.add_argument('-a', '--all', help = all_help, action = 'store_true', dest = 'all_mappings')
    all_or_something.add_argument('remote', help = remote_help, default = '',  nargs = '?')
