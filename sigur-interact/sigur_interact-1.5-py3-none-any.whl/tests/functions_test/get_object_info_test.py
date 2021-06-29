from sigur_interact.tests.make_connection_test import sigur_socket
from sigur_interact import functions

all_points = ['1', '2', '3', '4']
for point in all_points:
    response = functions.get_gate_status(sigur_socket, point)
    print(response)
