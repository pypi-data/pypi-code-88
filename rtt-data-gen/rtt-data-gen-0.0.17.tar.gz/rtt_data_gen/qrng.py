#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import binascii
import sys
import math
import time
import random
import logging
import itertools
import requests
from typing import BinaryIO, Optional


logger = logging.getLogger(__name__)


class Qrng:
    def __init__(self, user=None, passwd=None):
        self.user = user
        self.passwd = passwd
        self.session = None

        self.url_login = 'https://qrng.physik.hu-berlin.de/download'
        self.url_file = 'http://qrng.physik.hu-berlin.de/download/sampledata-100MB.bin'
        # self.url_file = 'http://qrng.physik.hu-berlin.de/download/sampledata-15MB.bin'

    def login(self):
        """
        POST https://qrng.physik.hu-berlin.de/download
        Content-Type: application/x-www-form-urlencoded

        username: ""
        password: ""
        submit: "Login"

        PHPSESSID=63grkkj1vl7ovrbdpqgs200012
	    """
        self._maybe_init_session()

        data = {'username': self.user, 'password': self.passwd, 'submit': 'Login'}
        r = self.session.post(self.url_login, data=data, verify=False)
        r.raise_for_status()
        return r

    def _maybe_init_session(self):
        if not self.session:
            self.session = requests.Session()

    def _fetch_data(self):
        self._maybe_init_session()
        for att in range(2):
            r = self.session.get(self.url_file)
            if r.status_code == 403:
                logger.info("Download failed, login needed, trying to log in")
                self.login()

        r.raise_for_status()
        return r

    def download(self, ostream: Optional[BinaryIO] = None, writer=None):
        self._maybe_init_session()
        r = self._fetch_data()

        for chunk in r.iter_content(chunk_size=4192):
            if not chunk:
                continue
            if ostream:
                ostream.write(chunk)
            elif writer:
                writer(chunk)
            else:
                yield chunk


def main():
    import coloredlogs
    import json
    coloredlogs.install(level=logging.INFO)

    parser = argparse.ArgumentParser(description='QRNG downloader')
    parser.add_argument('-c', '--creds', default=None, required=True,
                        help='Credentials JSON config')
    parser.add_argument('-f', '--data-path', dest='data_path', default=None,
                        help='Where to generate resulting file, if not defined, stdout is used')
    parser.add_argument('-s', '--size', dest='total_size', default=None, type=int,
                        help='Number of bytes to generate')
    args = parser.parse_args()

    proc_stdout = None
    if args.data_path:
        proc_stdout = open(args.data_path, 'wb+')
    else:
        proc_stdout = sys.stdout.buffer

    with open(args.creds) as fh:
        creds_js = json.load(fh)

    qrng = Qrng(user=creds_js['user'], passwd=creds_js['passwd'])
    nread = 0
    while not args.total_size or (nread < args.total_size):
        for chunk in qrng.download():
            csize = len(chunk)
            if args.total_size and (csize + nread > args.total_size):
                chunk = chunk[:args.total_size - nread]
            proc_stdout.write(chunk)
            nread += len(chunk)
            if args.total_size and nread >= args.total_size:
                break

    proc_stdout.flush()
    if proc_stdout != sys.stdout:
        proc_stdout.close()


if __name__ == '__main__':
    main()
