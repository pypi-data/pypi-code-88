import sys
from parsearg import ParseArg

def create_user(args):
    print(f'created user: {args.name!r} (email: {args.email}, phone: {args.phone})')
    
def create_todo(args):
    print(f'created TO-DO for user {args.user!r}: {args.title} (due: {args.due_date})')
    
view = {
    'create|user': {
        'callback':   create_user,
        'name':       {'help': 'create user name', 'action': 'store'},
        '-e|--email': {'help': "create user's email address", 'action': 'store', 'default': ''},
        '-p|--phone': {'help': "create user's phone number", 'action': 'store', 'default': ''},
    },
    'create|todo': {
        'callback':   create_todo,
        'user':       {'help': 'user name', 'action': 'store'},
        'title':      {'help': 'title of TO-DO', 'action': 'store'},
        '-d|--due-date': {'help': 'due date for the TO-DO', 'action': 'store', 'default': None},
    },
}

def main(args):
    # ParseArg takes the place of argparse.ArgumentParser
    parser = ParseArg(d=view)

    # parser.parse_args returns an argparse.Namespace
    ns     = parser.parse_args(args)

    # ns.callback contains the function in the 'callback' key of 'view'
    result = ns.callback(ns)

if __name__ == "__main__":
    args = sys.argv[1:] if len(sys.argv) > 1 else []
    
    main(' '.join(args))
