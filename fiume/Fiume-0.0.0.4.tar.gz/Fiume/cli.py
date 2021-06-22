import argparse
import pathlib
import logging
import bencodepy

import Fiume.metainfo_decoder as md
import Fiume.state_machine as sm

# TODO move to utils
def int_to_loglevel(n):
    if n == 0:
        return logging.WARNING
    if n == 1:
        return logging.INFO

    return logging.ERROR



##################################################


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("torrent_path",
                        type=pathlib.Path,
                        help="path to .torrent file")
    parser.add_argument("output_file",
                        type=pathlib.Path,
                        help="where to download the file")

    parser.add_argument("-p", "--port",
                        action="store",
                        type=int,
                        default=50146,
                        help="port for this client")

    parser.add_argument("-v", "--verbosity",
                        action="count",
                        default=0,
                        help="debug level")

    parser.add_argument("--delay",
                        type=float,
                        default=0,
                        help="delay for every sent message (only debug)")

    options = vars(parser.parse_args())
    options["verbosity"] = int_to_loglevel(options["verbosity"])
    options["debug"] = False

    #############
    
    with open(options["torrent_path"], "rb") as f:
        metainfo = md.MetaInfo(
            bencodepy.decode(f.read()) | options
        )

    tm = md.TrackerManager(metainfo, options)

    t = sm.ThreadedServer(
        options["port"],
        metainfo, tm,
        **options
    )

    t.main()
