from argparse import ArgumentParser
from dvol.dvol_helpers.common import *

from dvol import __version__

cmd_main_desc = "Manage docker and docker compose volume mappings easily!"
container_help = f"Container name; use with {f_command('config')} to save default, or with {f_command('add')}/{f_command('remove')} to override"
root_help = f"Local root folder (/tmp); use with {f_command('config')} to save default, or with {f_command('add')}/{f_command('remove')} to override"
execute_help = f"Replace {f_command('docker [compose] up -d')}; use with {f_command('config')} to save default, or with {f_command('add')}/{f_command('remove')} to override"
no_git_help = "Disable default volume-specific change tracking"
profile_help = "Name of profile from config to use."

def create ():
    parser = ArgumentParser(prog = 'dvol', description = cmd_main_desc)
    parser.add_argument( "--version", "-v", action='version',  version = f'%(prog)s v{__version__}' )
    parser.add_argument( "--container", "-c", help = container_help)
    parser.add_argument( "--root", "-r", help = root_help)
    parser.add_argument( "--execute", "-e", help = execute_help)
    parser.add_argument( "--no-git", help = no_git_help, action = 'store_true')
    parser.add_argument( "--profile", "-p", help = profile_help, default = 'default')
    return parser
