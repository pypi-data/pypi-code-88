from dvol.dvol_helpers.compose_tools import manage_config
from dvol.dvol_helpers.common import *


cmd_config_help = f"""Set default/profile {f_argument("container")}, {f_argument("executed")}, and {f_argument("root")}.
Always prints resulting config."""

cmd_config_desc = cmd_config_help + """
Pass in empty string to clear values"""

def create():
    parser = subs.add_parser('config', help = cmd_config_help, description = cmd_config_desc, aliases = ['config'])
    parser.set_defaults(func = manage_config)
