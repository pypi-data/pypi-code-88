"""
PASSWORD ADMIN
You can start the program from module main.py with function run_program('JSON file name').

This is a simple password admin program.
It is made to ask the user for username and password input data which
is then written and collected in a JSON file. There is also other functions
like editing created usernames and passwords, deleting information etc.

The main program has 3 modes:
- Main mode
- Admin mode
- User mode

In Main mode you have the options to login as admin, sign in a new user and login as user.

When you log in as an admin you enter in Admin mode, where you can view the users data, or
delete users data.
If there is no admin data for login you are asked to sign in as admin which admin data is then collected
in the JSON file. There can be only one admin.

When you sign in a new user it's data is also collected in the JSON file and you can log in after that.
There can be multiple users.
When you log in as a user you enter in User mode, where you can edit your username and password.
You can also add a nickname and have the option to view all your data.

"""