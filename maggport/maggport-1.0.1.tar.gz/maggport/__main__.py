"""
This file calls module command function in src.maggport file

Example:
    python -m maggport --host <host> --port <port> --db <db> --collection <collection>
        --pipeline_path <pipeline_path> --out <out>
"""
from src.maggport import maggport

if __name__ == '__main__':
    maggport.maggport()  # pylint: disable=no-value-for-parameter
