import asyncio, socket
from time import sleep
import pathlib
import argparse
import logging

parser = argparse.ArgumentParser()
parser.add_argument("torrent_path",
                    type=pathlib.Path,
                    help="path to .torrent file")
parser.add_argument("download_path",
                    type=pathlib.Path,
                    help="where to download the file")
parser.add_argument("-v", "--verbosity",
                    action="count",
                    default=0,
                    help="debug level")
parser.add_argument("--delay",
                    type=float,
                    default=0,
                    help="delay for every sent message (only debug)")

# parser.parse_args(" ".join([
#     "-v -v",
#     "--delay 0.25",
#     "/home/groucho/Un gioco di specchi.mp4.torrent",
#     "/home/groucho/torrent/downloads/film.mp4",
# ]))

def int_to_loglevel(n):
    if n == 0:
        return logging.WARNING
    if n == 1:
        return logging.INFO

    return logging.ERROR
    
a = vars(parser.parse_args())
a["verbosity"] = int_to_loglevel(a["verbosity"])
print(a)

