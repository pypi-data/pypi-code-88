from dvol.dvol_helpers.compose_tools import disable_dvol

def create (subs):
    parser = subs.add_parser('disable', help = 'removes dvol mapping')
    parser.set_defaults(func = disable_dvol)
