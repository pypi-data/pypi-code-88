import sys
from parsearg.parser import ParseArg
from parsearg.utils import (
    underline,
)
import model

# CONTROLLER (Part I):
def setup_model():
    model.Schema()
    
def purge_users(args=None):
    model.User().purge()
    
def purge_todos(args=None):
    model.Todo().purge()

def show_users(args=None):
    model.User().show()
    
def show_todos(args=None):
    model.Todo().show()

def create_user(args):
    model.User().create(
        name=args.name,
        email=args.email,
        phone=args.phone
    )

def create_todo(args):
    model.Todo().create(
        user=args.user,
        title=args.title,
        description=args.description,
        due=args.due_date
    )

def update_user_email(args):
    model.User().update_email(
        name=args.name,
        email=args.email)

def update_user_phone(args):
    model.User().update_phone(
        name=args.name,
        phone=args.phone
    )

def update_todo_title(args):
    model.Todo().update_title(
        _id=args.id,
        title=args.title
    )

def update_todo_description(args):
    model.Todo().update_description(
        _id=args.id,
        description=args.description
    )

# VIEW:
view = {
    'purge|users': {
        'callback':   purge_users,
    },
    'purge|todos': {
        'callback':   purge_todos,
    },
    'show|users': {
        'callback':   show_users,
    },
    'show|todos': {
        'callback':   show_todos,
    },
    'create|user': {
        'callback':   create_user,
        'name':       {'help': 'create user name', 'action': 'store'},
        '-e|--email': {'help': "create user's email address", 'action': 'store', 'default': ''},
        '-p|--phone': {'help': "create user's phone number", 'action': 'store', 'default': ''},
    },
    'create|todo': {
        'callback':   create_todo,
        'user':       {'help': 'user name', 'action': 'store'},
        'title':      {'help': 'title of to-do', 'action': 'store'},
        '-c|--description': {'help': 'description of to-do', 'action': 'store', 'default': ''},
        '-d|--due-date': {'help': 'due date for the to-do', 'action': 'store', 'default': None},
    },
    'update|user|email': {
        'callback':   update_user_email,
        'name':       {'help': 'user name', 'action': 'store'},
        'email':      {'help': 'user email', 'action': 'store'},
    },
    'update|user|phone': {
        'callback':   update_user_phone,
        'name':       {'help': 'user name', 'action': 'store'},
        'phone':      {'help': 'user phone', 'action': 'store'},
    },
    'update|todo|title': {
        'callback':   update_todo_title,
        'id':         {'help': 'ID of to-do', 'action': 'store'},
        'title':      {'help': 'title of to-do', 'action': 'store'},
    },
    'update|todo|description': {
        'callback':   update_todo_description,
        'id':         {'help': 'ID of to-do', 'action': 'store'},
        'description':{'help': 'description of to-do', 'action': 'store'},
    },
}

# CONTROLLER (Part II):
def main(args):
    setup_model()

    # create the parser from the dict (flat tree):
    parser = ParseArg(d=view, root_name='todos')

    # generate the argparse.Namespace by parsing the arguments:
    ns     = parser.parse_args(args)

    # perform the associated callback:
    result = ns.callback(ns)

    # display the result:
    print('{}\n\t{}\n'.format(underline(f'{args!r}'), result if result is not None else "SUCCESS"))


if __name__ == "__main__":
    args = sys.argv[1:] if len(sys.argv) > 1 else []
    
    main(' '.join(args))
