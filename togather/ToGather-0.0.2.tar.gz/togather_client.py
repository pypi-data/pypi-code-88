import socket
import sys
import threading
import pickle
import sqlite3
import os

from user import User
from event import Event
from group import Group
from _calendar import GroupCalendar
from option import Option
# TODO: Use CamelCase for class names


# TODO: Implementing compression on blobs may be needed if object sizes become large.
# TODO: Remove traceback from exception handlers before release. Useful for testing right now.  Logging instead?
# TODO: Change tables to use primary keys and possibly relationships between object types.
# TODO: Specify object type/name in message header so we don't have to unpickle in Receiver thread.
# TODO: Pass info from header to generic methods that interact with database, instead of separate methods for each type. 
#       For easier maintenance, the different classes for adding objects could be combined into a single class.

class Data(threading.local):
    """
    Using name as primary key, stores serialized class objects as blobs (Binary Large Objects) in a sqlite3 database.

    Each method uses a new database connection because sqlite throws an error if a single connection is accessed by more
    than one thread.

    For testing, each client instance has to opened from its own directory so that they are each using their own
    database file.
    """

    DB_FILENAME = "db.db"  # Constant for database filename.

    # Method to create tables if they don't already exist in file.
    @staticmethod
    def create_tables():
        try:
            db_connection = sqlite3.connect(Data.DB_FILENAME)
            cursor = db_connection.cursor()
            # Wrapping identifiers in `` prevents conflicts with SQLite keywords i.e. GROUP
            cursor.execute('''CREATE TABLE `users` (`name` TEXT, `user` BLOB)''')
            cursor.execute('''CREATE TABLE `events` (`name` TEXT, `event` BLOB)''')
            cursor.execute('''CREATE TABLE `groups` (`name` TEXT, `group` BLOB)''')
            cursor.execute('''CREATE TABLE `calendars` (`name` TEXT, `calendar` BLOB)''')
            cursor.execute('''CREATE TABLE `options` (`name` TEXT, `option` BLOB)''')
            db_connection.commit()
            db_connection.close()
        except Exception as e:
            print(e)

    # Deletes database file. Useful if corrupted.
    @staticmethod
    def db_reset():
        try:
            os.remove(Data.DB_FILENAME)  # Dangerous :)
            Data.create_tables()
        except Exception as e:
            print(e.with_traceback())

    # Requests a copy of database from server.  Fulfilled by other clients.
    @staticmethod
    def db_request():
        sender = Client.Send("request_db()", 2)  # Second parameter specifies fifth byte in message header
        sender.start()

    # Replaces local database using file received from server.
    @staticmethod
    def db_reload(db):
        Data.db_reset()
        try:
            with open(Data.DB_FILENAME, "wb") as file:  # Write bytes back to file
                file.write(db)
        except Exception as e:
            print(e.with_traceback())

    # Sends db file to server when Receiver thread gets request.
    @staticmethod
    def db_send():
        try:
            with open(Data.DB_FILENAME, "rb") as file:
                db_file = file.read()
                sender = Client.Send(db_file, 1)
                sender.start()
        except Exception as e:
            print(e)

    # Adds an object to database if it doesn't exist.
    @staticmethod
    def add_user(user):
        try:
            db_connection = sqlite3.connect(Data().DB_FILENAME)
            cursor = db_connection.cursor()
            if Data.get_users(user.name) is None:
                cursor.execute("INSERT INTO `users` VALUES (?, ?)", (user.name, pickle.dumps(user)))
                db_connection.commit()
                sender = Client.Send(pickle.dumps(user))
                sender.start()
            db_connection.close()
        except Exception as e:
            print(e.with_traceback())  # Can't have duplicate name.

    # Returns User object if parameter is given, otherwise returns list of all users
    # Returns None if nothing is found.
    @staticmethod
    def get_users(name=None):
        try:
            if name is None:
                db_connection = sqlite3.connect(Data().DB_FILENAME)
                cursor = db_connection.cursor()
                cursor.execute("SELECT `user` FROM `users`")
                users = cursor.fetchall()  # fetchall() returns a list of rows returned from executed SQL query 
                db_connection.commit()
                db_connection.close()

                # Unpickle each object into new list to return.
                unpickled_users = []
                for user in users:
                    # Attributes for each row returned by fetchall() are accessed through a tuple.
                    # We are only selecting for one attribute (the pickled object), so we access with user[0]
                    unpickled_users.append(pickle.loads(user[0]))  
                return unpickled_users
            
            else:
                db_connection = sqlite3.connect(Data().DB_FILENAME)
                cursor = db_connection.cursor()
                cursor.execute("SELECT `user` FROM `users` WHERE `name`=?", (name,))  # Parameter must be tuple
                user = cursor.fetchone()  # Returns None if nothing found, otherwise one object in a tuple.
                db_connection.commit()
                db_connection.close()
                # TODO: This if statement is not working correctly.  Handled with exception for now
                if user is not None:  
                    user = pickle.loads(user[0])  # Get object out of tuple and pickle before returning.
                return user
        except Exception as e:
            return None

    # Adds an object to database if it doesn't exist.
    @staticmethod
    def add_event(event):
        try:
            db_connection = sqlite3.connect(Data().DB_FILENAME)
            cursor = db_connection.cursor()
            if Data.get_events(event.name) is None:
                cursor.execute("INSERT INTO `events` VALUES (?, ?)", (event.name, pickle.dumps(event)))
                db_connection.commit()
                sender = Client.Send(pickle.dumps(event))
                sender.start()
            db_connection.close()
        except Exception as e:
            print(e.with_traceback())  # Can't have duplicate name.

    # Returns User object if parameter is given, otherwise returns list of all events
    # Returns None if nothing is found.
    @staticmethod
    def get_events(name=None):
        try:
            if name is None:
                db_connection = sqlite3.connect(Data().DB_FILENAME)
                cursor = db_connection.cursor()
                cursor.execute("SELECT `event` FROM `events`")
                events = cursor.fetchall()  # fetchall() returns a list of rows returned from executed SQL query 
                db_connection.commit()
                db_connection.close()

                # Unpickle each object into new list to return.
                unpickled_events = []
                for event in events:
                    # Attributes for each row returned by fetchall() are accessed through a tuple.
                    # We are only selecting for one attribute (the pickled object), so we access with event[0]
                    unpickled_events.append(pickle.loads(event[0]))
                return unpickled_events

            else:
                db_connection = sqlite3.connect(Data().DB_FILENAME)
                cursor = db_connection.cursor()
                cursor.execute("SELECT `event` FROM `events` WHERE `name`=?", (name,))  # Parameter must be tuple
                event = cursor.fetchone()  # Returns None if nothing found, otherwise one object in a tuple.
                db_connection.commit()
                db_connection.close()
                # TODO: This if statement is not working correctly.  Handled with exception for now
                if event is not None:
                    event = pickle.loads(event[0])  # Get object out of tuple and pickle before returning.
                return event
        except Exception as e:
            return None
        
    # Adds an object to database if it doesn't exist.
    @staticmethod
    def add_group(group):
        try:
            db_connection = sqlite3.connect(Data().DB_FILENAME)
            cursor = db_connection.cursor()
            if Data.get_groups(group.name) is None:
                cursor.execute("INSERT INTO `groups` VALUES (?, ?)", (group.name, pickle.dumps(group)))
                db_connection.commit()
                sender = Client.Send(pickle.dumps(group))
                sender.start()
            db_connection.close()
        except Exception as e:
            print(e.with_traceback())  # Can't have duplicate name.

    # Returns User object if parameter is given, otherwise returns list of all groups
    # Returns None if nothing is found.
    @staticmethod
    def get_groups(name=None):
        try:
            if name is None:
                db_connection = sqlite3.connect(Data().DB_FILENAME)
                cursor = db_connection.cursor()
                cursor.execute("SELECT `group` FROM `groups`")
                groups = cursor.fetchall()  # fetchall() returns a list of rows returned from executed SQL query 
                db_connection.commit()
                db_connection.close()

                # Unpickle each object into new list to return.
                unpickled_groups = []
                for group in groups:
                    # Attributes for each row returned by fetchall() are accessed through a tuple.
                    # We are only selecting for one attribute (the pickled object), so we access with group[0]
                    unpickled_groups.append(pickle.loads(group[0]))
                return unpickled_groups

            else:
                db_connection = sqlite3.connect(Data().DB_FILENAME)
                cursor = db_connection.cursor()
                cursor.execute("SELECT `group` FROM `groups` WHERE `name`=?", (name,))  # Parameter must be tuple
                group = cursor.fetchone()  # Returns None if nothing found, otherwise one object in a tuple.
                db_connection.commit()
                db_connection.close()
                # TODO: This if statement is not working correctly.  Handled with exception for now
                if group is not None:
                    group = pickle.loads(group[0])  # Get object out of tuple and pickle before returning.
                return group
        except Exception as e:
            return None
        
    # Adds an object to database if it doesn't exist.
    @staticmethod
    def add_calendar(calendar):
        try:
            db_connection = sqlite3.connect(Data().DB_FILENAME)
            cursor = db_connection.cursor()
            if Data.get_calendars(calendar.name) is None:
                cursor.execute("INSERT INTO `calendars` VALUES (?, ?)", (calendar.name, pickle.dumps(calendar)))
                db_connection.commit()
                sender = Client.Send(pickle.dumps(calendar))
                sender.start()
            db_connection.close()
        except Exception as e:
            print(e.with_traceback())  # Can't have duplicate name.

    # Returns User object if parameter is given, otherwise returns list of all calendars
    # Returns None if nothing is found.
    @staticmethod
    def get_calendars(name=None):
        try:
            if name is None:
                db_connection = sqlite3.connect(Data().DB_FILENAME)
                cursor = db_connection.cursor()
                cursor.execute("SELECT `calendar` FROM `calendars`")
                calendars = cursor.fetchall()  # fetchall() returns a list of rows returned from executed SQL query 
                db_connection.commit()
                db_connection.close()

                # Unpickle each object into new list to return.
                unpickled_calendars = []
                for calendar in calendars:
                    # Attributes for each row returned by fetchall() are accessed through a tuple.
                    # We are only selecting for one attribute (the pickled object), so we access with calendar[0]
                    unpickled_calendars.append(pickle.loads(calendar[0]))
                return unpickled_calendars

            else:
                db_connection = sqlite3.connect(Data().DB_FILENAME)
                cursor = db_connection.cursor()
                cursor.execute("SELECT `calendar` FROM `calendars` WHERE `name`=?", (name,))  # Parameter must be tuple
                calendar = cursor.fetchone()  # Returns None if nothing found, otherwise one object in a tuple.
                db_connection.commit()
                db_connection.close()
                # TODO: This if statement is not working correctly.  Handled with exception for now
                if calendar is not None:
                    calendar = pickle.loads(calendar[0])  # Get object out of tuple and pickle before returning.
                return calendar
        except Exception as e:
            return None
        
    # Adds an object to database if it doesn't exist.
    @staticmethod
    def add_option(option):
        try:
            db_connection = sqlite3.connect(Data().DB_FILENAME)
            cursor = db_connection.cursor()
            if Data.get_options(option.name) is None:
                cursor.execute("INSERT INTO `options` VALUES (?, ?)", (option.name, pickle.dumps(option)))
                db_connection.commit()
                sender = Client.Send(pickle.dumps(option))
                sender.start()
            db_connection.close()
        except Exception as e:
            print(e.with_traceback())  # Can't have duplicate name.

    # Returns User object if parameter is given, otherwise returns list of all options
    # Returns None if nothing is found.
    @staticmethod
    def get_options(name=None):
        try:
            if name is None:
                db_connection = sqlite3.connect(Data().DB_FILENAME)
                cursor = db_connection.cursor()
                cursor.execute("SELECT `option` FROM `options`")
                options = cursor.fetchall()  # fetchall() returns a list of rows returned from executed SQL query 
                db_connection.commit()
                db_connection.close()

                # Unpickle each object into new list to return.
                unpickled_options = []
                for option in options:
                    # Attributes for each row returned by fetchall() are accessed through a tuple.
                    # We are only selecting for one attribute (the pickled object), so we access with option[0]
                    unpickled_options.append(pickle.loads(option[0]))
                return unpickled_options

            else:
                db_connection = sqlite3.connect(Data().DB_FILENAME)
                cursor = db_connection.cursor()
                cursor.execute("SELECT `option` FROM `options` WHERE `name`=?", (name,))  # Parameter must be tuple
                option = cursor.fetchone()  # Returns None if nothing found, otherwise one object in a tuple.
                db_connection.commit()
                db_connection.close()
                # TODO: This if statement is not working correctly.  Handled with exception for now
                if option is not None:
                    option = pickle.loads(option[0])  # Get object out of tuple and pickle before returning.
                return option
        except Exception as e:
            return None
        
        
class Receive(threading.Thread):
    """
    A class to create a thread and listen on socket passed as parameter.
    Parses the data type and calls appropriate Data method.
    """
    def __init__(self, sock):
        super().__init__()
        self._sock = sock

    # If a message is received from server, unpickle it.  Otherwise, keep listening until the connection is closed.
    def run(self):
        while True:
            try:
                length = int.from_bytes(self._sock.recv(4), "big")  # Get length of message from first 4 bytes
                is_db = int.from_bytes(self._sock.recv(1), "big")
                msg = self._sock.recv(length)
                if msg:
                    try:  # Parse for string commands received from server.
                        cmd = msg.decode()
                        if cmd == "request_db()":  # Send db if requested
                            print("Request for database file received. Sending.")
                            Data.db_send()
                    except UnicodeDecodeError:
                        try:  # Try to unpickle if you can't decode
                            unpickled_message = pickle.loads(msg)
                            # Add received user to local db.
                            if type(unpickled_message) is User:
                                Data.add_user(unpickled_message)
                            elif type(unpickled_message) is Event:
                                Data.add_event(unpickled_message)
                            elif type(unpickled_message) is Group:
                                Data.add_group(unpickled_message)
                            elif type(unpickled_message) is GroupCalendar:
                                Data.add_calendar(unpickled_message)
                            elif type(unpickled_message) is Option:
                                Data.add_option(unpickled_message)
                        except pickle.PickleError as e:
                            # Must be a database file we need to load.
                            # TODO: Check if received file is actually db.db
                            try:
                                print("Database file received.  Reloading.")
                                Data.db_reload(msg)
                            except Exception as e:
                                # print(e.with_traceback())
                                pass

            except OSError as e:  # Catch exception when loop trys to connect after program closes socket.
                print(e)
                break


# Client class calls listener thread to run perpetually and sender method as needed to send data.
# Changed so that connection is stored as class variable and can be accessed from other classes we define.
class Client(threading.Thread):

    sock = socket.socket()  # Store connection info outside of instances.

    def __init__(self, addr):
        super().__init__()
        self._address = addr
        Data()
        self.srv = socket.create_connection(self._address)
        self.rcv = Receive(self.srv)

    def run(self):
        with self.srv as srv:
            Client.sock = srv

            # Start Receive thread to listen for data from server.
            self.rcv.start()

            print("Connected to server: %s:%d\n" % self._address)
            print("Menu:")
            print("-1. Request database.")
            print("0. Reset database.\n")
            
            print("1. Add first user.")
            print("11. Add second user.")
            print("111. Add third user.")
            print("2. Print users.\n")
            
            print("3. Add first event.")
            print("33. Add second event.")
            print("333. Add third event.")
            print("4. Print events\n")
            
            print("5. Add first group.")
            print("55. Add second group.")
            print("555. Add third group.")
            print("6. Print groups\n")

            print("7. Add first calendar.")
            print("77. Add second calendar.")
            print("777. Add third calendar.")
            print("8. Print calendars\n")
            
            print("9. Add first option.")
            print("99. Add second option.")
            print("999. Add third option.")
            print("10. Print options\n")
            
            print("exit() to Exit")

            # TODO: Implement menu w/ UI
            # Create and send dummy class objects for testing.
            # If there are other clients connected, they should receive what is sent with their receive thread.
            selection = input("\nEnter selection:")
            while selection != "exit()":

                if selection == "-1":  # Request database from server.
                    Data.db_request()

                elif selection == "0":  # Deletes database and reinitializes.
                    Data.db_reset()

                elif selection == "1":  # Add different users for testing
                    Data.add_user(User("User1", ["Constraint1"], ["Group1", "Group2"]))
                elif selection == "11":
                    Data.add_user(User("User2", ["Constraint1", "Constraint2"], ["Group2"]))
                elif selection == "111":
                    Data.add_user(User("User3", ["Constraint12"], ["Group12", "Group22"]))
                    
                elif selection == "2":  # Print users from local database
                    for user in Data().get_users():
                        print(user.name, user.constraints, user.groups)
                    
                if selection == "3":  # Add different events for testing
                    Data.add_event(Event("Event1", "Description1", ["Option1", "Option2"]))
                elif selection == "33":
                    Data.add_event(Event("Event2", "Description2", ["Option11", "Option22"]))
                elif selection == "333":
                    Data.add_event(Event("Event3", "Description3", ["Option111", "Option222"]))

                elif selection == "4":  # Print events from local database
                    for event in Data().get_events():
                        print(event.name, event.description, event.options, event.status)

                if selection == "5":  # Add different groups for testing
                    Data.add_group(Group("Group1", "Calendar1", ["User1", "User2"], ["Event1", "Event2"]))
                elif selection == "55":
                    Data.add_group(Group("Group2", "Calendar2", ["User11", "User22"], ["Event11", "Event22"]))
                elif selection == "555":
                    Data.add_group(Group("Group3", "Calendar3", ["User111", "User222"], ["Event111", "Event222"]))

                elif selection == "6":  # Print groups from local database
                    for group in Data().get_groups():
                        print(group.name, group.calendar, group.users, group.events)
                        
                if selection == "7":  # Add different calendars for testing
                    Data.add_calendar(GroupCalendar("Calendar1", ["Event1", "Event2"]))
                elif selection == "77":
                    Data.add_calendar(GroupCalendar("Calendar2", ["Event11", "Event22"]))
                elif selection == "777":
                    Data.add_calendar(GroupCalendar("Calendar3", ["Event111", "Event222"]))

                elif selection == "8":  # Print calendars from local database
                    for calendar in Data().get_calendars():
                        print(calendar.name, calendar.events)
                        
                if selection == "9":  # Add different options for testing
                    Data.add_option(Option("Option1", "Activity1", ["Vote1", "Vote2"]))
                elif selection == "99":
                    Data.add_option(Option("Option2", "Activity2", ["Vote11", "Vote22"]))
                elif selection == "999":
                    Data.add_option(Option("Option3", "Activity3", ["Vote1111", "Vote2222"]))

                elif selection == "10":  # Print options from local database
                    for option in Data().get_options():
                        print(option.name, option.activity, option.time, option.chosen, option.votes)

                selection = input("\nEnter selection:")

            Client.exit()

    @staticmethod
    def exit():
        ex = Client.Send("exit()", 3)  # Send exit command to server.
        ex.start()

    # Creates a thread to accept an object and then encode or pickle before sending to server, depending on object type.
    # Attaches a 4 byte header to the object that specifies size
    # is_db is added to header, let's server know to only request from newest connection
    class Send(threading.Thread):
        def __init__(self, obj, is_db=0):
            super().__init__()
            self.obj = obj
            self.is_db = is_db

        def run(self):
            try:
                if type(self.obj) is str:
                    self.obj = self.obj.encode()

                self.attach_header()
                Client.sock.sendall(self.obj)
            except Exception as e:
                print(e)

        # Appends length of object being sent to beginning of it's byte string
        # Also adds a byte to specify if this is a database file.
        def attach_header(self):
            prefix = sys.getsizeof(self.obj)  # Get length of message so we can create header.
            prefix = prefix.to_bytes(4, "big")  # Convert length to bytes
            self.is_db = bytes([self.is_db])
            # Create bytearray to add header then convert back to bytes.
            self.obj = bytes(bytearray(prefix + self.is_db + self.obj))


if __name__ == '__main__':
    # TODO: Make host IP configurable by user.
    address = ("localhost", 55557)
    client = Client(address)
    client.start()
    print("Client started.")
