from dvol.dvol_helpers.compose_tools import enable_dvol

def create (subs):
    parser = subs.add_parser('enable', help = 'adds dvol override without adding new mappings')
    parser.set_defaults(func = enable_dvol)
