from dvol.dvol_helpers.dvol_print import determine_print

cmd_get_volumes_desc = "Get list of volumes and their sources"

def create (subs):
    parser = subs.add_parser('get', help = cmd_get_volumes_desc)
    parser.set_defaults(func = determine_print)
