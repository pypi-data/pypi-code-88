#!/usr/bin/env python3
# coding: utf-8
"""Define useful methods to be used globally."""

from http.cookiejar import MozillaCookieJar
import collections
import io
import sys


class ZoomdlCookieJar(MozillaCookieJar):
    """
    Code freely adapted from Youtube-DL's YoutubeCookieJar
    https://github.com/ytdl-org/youtube-dl/
    For file format, see https://curl.haxx.se/docs/http-cookies.html
    """
    _HTTPONLY_PREFIX = '#HttpOnly_'
    _ENTRY_LEN = 7
    _CookieFileEntry = collections.namedtuple(
        'CookieFileEntry',
        ('domain_name', 'include_subdomains', 'path',
         'https_only', 'expires_at', 'name', 'value'))

    def load(self, filename=None, ignore_discard=True, ignore_expires=True):
        """Load cookies from a file."""
        if filename is None:
            if self.filename is not None:
                filename = self.filename
            else:
                raise ValueError()

        def prepare_line(line):
            # print("Prepping line '{}'".format(line))
            if line.startswith(self._HTTPONLY_PREFIX):
                line = line[len(self._HTTPONLY_PREFIX):]
            # comments and empty lines are fine
            if line.startswith('#') or not line.strip():
                return line
            cookie_list = line.split('\t')
            if len(cookie_list) != self._ENTRY_LEN:
                raise ValueError('invalid length %d' % len(cookie_list))
            cookie = self._CookieFileEntry(*cookie_list)
            if cookie.expires_at and not cookie.expires_at.isdigit():
                raise ValueError('invalid expires at %s' % cookie.expires_at)
            return line

        cf = io.StringIO()
        with io.open(filename, encoding='utf-8') as f:
            for line in f:
                try:
                    cf.write(prepare_line(line))
                except ValueError as e:
                    print(
                        'WARNING: skipping cookie file entry due to %s: %r\n'
                        % (e, line), sys.stderr)
                    continue
        cf.seek(0)
        self._really_load(cf, filename, ignore_discard, ignore_expires)
        # Session cookies are denoted by either `expires` field set to
        # an empty string or 0. MozillaCookieJar only recognizes the former
        # (see [1]). So we need force the latter to be recognized as session
        # cookies on our own.
        # Session cookies may be important for cookies-based authentication,
        # e.g. usually, when user does not check 'Remember me' check box while
        # logging in on a site, some important cookies are stored as session
        # cookies so that not recognizing them will result in failed login.
        # 1. https://bugs.python.org/issue17164
        for cookie in self:
            # Treat `expires=0` cookies as session cookies
            if cookie.expires == 0:
                cookie.expires = None
                cookie.discard = True


