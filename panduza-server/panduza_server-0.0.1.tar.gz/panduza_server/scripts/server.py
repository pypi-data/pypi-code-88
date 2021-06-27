import os
import panduza_server
import subprocess

def run_server():
    server_dir = os.path.dirname(panduza_server.__file__)
    print("SERVER DIRECTORY: ", server_dir)

    subprocess.run(["python3" ,  server_dir + "/manage.py", "runserver"])
