from argparse import RawDescriptionHelpFormatter

from dvol.dvol_helpers.dvol_add import determine_add
from dvol.dvol_helpers.common import *

cmd_add_help = "Add a new volume mapping, or update an existing one."
force_help = 'Force re-copying remote folder contents, destroying the specified folder and any contents'
path_help = 'Override {root}{container}{remote} path logic and use provided folder'
solution_help = 'If remote volume is mapped to a different folder, should dvol [u]se, [d]elete or [i]gnore it'
remote_help = 'Remote folder to add/map'
cmd_add_desc = cmd_add_help + f"""

Docker Compose: dvol will only alter its own compose file. If a mapping is
found in another config for {f_argument('remote')}, dvol will abort.

Docker: dvol will create a new image based on the current state of the
container before re-running the machine with the new mapping.

For new or {f_argument('--force')} remote folders, dvol will copy the contents
to the default path:
    {{root}}/{{container}}_volumes/{{remote}}
or --path if provided, then initialize a new local git repository to make
tracking changes easier.
"""

def create (subs):
    parser = subs.add_parser('add', help = cmd_add_help, description = cmd_add_desc, formatter_class=RawDescriptionHelpFormatter, aliases = ['a'])
    parser.set_defaults(func = determine_add)
    parser.add_argument('--force', '-f', help = force_help, action = 'store_true')
    parser.add_argument('--path', '-p', help = path_help, dest = 'local_path')
    parser.add_argument('--solution', '-s', help = solution_help, choices = ['use', 'delete', 'ignore', 'u', 'd', 'i'])
    parser.add_argument('remote', help = remote_help, nargs=1)
