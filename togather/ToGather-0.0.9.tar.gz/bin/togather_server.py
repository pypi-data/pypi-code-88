from socketserver import *
import threading
import socket


# Overrides socketserver.BaseRequestHandler class.
# Class methods setup, handle, and finish are called automatically by superclass constructor.
class PythonHandler(BaseRequestHandler):
    _connections = []  # Static variable to keep track of active connections
    _db_requester = socket.socket()

    data = ""

    def setup(self):
        print("setting up new connection")
        PythonHandler._connections.append(self.request)  # self.request is the socket object being handled.

    def handle(self):

        print("Connected to client: %s:%d" % self.client_address)

        # TODO: Handle when connection is closed incorrectly by client.
        # TODO: Create method to handle header
        while PythonHandler.data != "exit()":
            length = int.from_bytes(self.request.recv(4), "big")  # Get length of message from first 4 bytes

            is_db = int.from_bytes(self.request.recv(1), "big")

            PythonHandler.data = self.request.recv(length)
            prefix = length.to_bytes(4, "big")  # Convert length to bytes
            is_db = is_db.to_bytes(1, "big")
            # Create bytearray to append then convert back to bytes.
            PythonHandler.data = bytes(bytearray(prefix + is_db + PythonHandler.data))

            # Added a check in header to prevent server from sending db to everyone
            if int.from_bytes(is_db, "big") == 0:  # Broadcast to everyone
                PythonHandler.broadcast(PythonHandler.data, self.request)
            if int.from_bytes(is_db, "big") == 1:  # Broadcast db to requester only.
                PythonHandler.send(PythonHandler.data, PythonHandler._db_requester)
            # Broadcast db request to second newest connection.
            if int.from_bytes(is_db, "big") == 2:
                # TODO: Handle if second newest connection was caller
                # TODO: Handle if no other users request database from
                PythonHandler._db_requester = self.request
                target = PythonHandler._connections.pop(-2)
                PythonHandler.send(PythonHandler.data, target)
                PythonHandler._connections.insert(-2, target)
            if int.from_bytes(is_db, "big") == 3:  # Exit command.  Close connection.
                PythonHandler.data = "exit()"
                break
        self.request.close()

    def finish(self):
        print("Connection to %s:%d closed" % self.client_address)
        PythonHandler._connections.remove(self.request)
        self.request.close()

    # Sends a message to all connected clients.
    @staticmethod  # Static method has access to static variable connections[]
    def broadcast(message, source):
        source_exists = False
        for connection in PythonHandler._connections:
            if connection.getpeername() == source.getpeername():
                source_exists = True

        if source_exists is True:
            # Iterate through connections and send data if remote address is not same as source's
            print("Broadcasting from: %s:%d" % source.getpeername())
            for connection in PythonHandler._connections:
                if connection.getpeername() != source.getpeername():  # getpeername() returns remote address.
                    connection.sendall(message)

    # Sends a message to one client.
    @staticmethod  # Static method has access to static variable connections[]
    def send(message, destination):
        print("Sending to: %s:%d" % destination.getpeername())
        destination.sendall(message)


class StartServer(threading.Thread):
    def __init__(self):
        super().__init__()
        self.server = ThreadingTCPServer(("localhost", 55557), PythonHandler)

    def run(self):
        try:
            # TODO: Run server in a thread to allow for exit command that calls _server.shutdown()
            # Creates an instance of PythonHandler class whenever connection is received from server.
            # ThreadingTCPServer uses threads to connect to each client.
            with self.server as _server:
                _server.allow_reuse_address = True
                print("Python server started.")
                _server.serve_forever()
                _server.shutdown()
        except:
            self.kill()

    def kill(self):
        self.server.shutdown()

