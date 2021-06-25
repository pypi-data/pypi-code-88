import datetime
import imaplib
import email
import logging
import re
import os

from six import ensure_text

from fload import Source

logger = logging.getLogger(__name__)


class ImapClient:
    def __init__(self, host, port, user, _pass, folder, debug=False) -> None:
        self._host = host
        self._port = port
        self._user = user
        self._pass = _pass
        self._folder = folder
        self._inner_conn: imaplib.IMAP4 = None
        self._debug = debug
        self._cache_enabled = False

    def connect(self):
        self._inner_conn = imaplib.IMAP4_SSL(self._host, self._port)
        if self._debug:
            self._inner_conn.debug = 4
        self._inner_conn.login(self._user, self._pass)
        self._inner_conn.select(self._folder)

    def uid(self, command, *args):
        try:
            return self._inner_conn.uid(command, *args)
        except (ConnectionResetError, imaplib.IMAP4.abort):
            self.connect()
            return self._inner_conn.uid(command, *args)

    def select(self, folder):
        self._folder = folder
        self._inner_conn.select(folder)

    def list(self):
        try:
            return self._inner_conn.list()
        except (ConnectionResetError, imaplib.IMAP4.abort):
            self.connect()
            return self._inner_conn.list()

    @property
    def folder(self):
        return self._folder

    @folder.setter
    def folder(self, value):
        if value != self._folder:
            self.select(value)

    def get_email_by_uid(self, uid):
        message = self.get_message_from_cache(uid)
        if message:
            return message

        status, data = self.uid('fetch', uid, '(RFC822)')
        if data is None or not data[0]:
            return None

        self.save_message_cache(uid, data[0][1])
        message = email.message_from_bytes(data[0][1])
        return message

    def header(self, uid):
        status, data = self.uid('fetch', uid, '(BODY.PEEK[HEADER])')
        if data is None or not data[0]:
            return None

        message = email.message_from_bytes(data[0][1])
        return message

    def get_message_from_cache(self, uid):
        key = f'.cache/{self._user}/{self._folder}/{uid}.eml'
        if os.path.exists(key):
            with open(key, 'rb') as f:
                return email.message_from_binary_file(f)

    def save_message_cache(self, uid, message_raw):
        key = f'.cache/{self._user}/{self._folder}/{uid}.eml'
        file_dir = os.path.dirname(key)
        if not os.path.exists(file_dir):
            os.makedirs(file_dir)

        with open(key, 'wb') as f:
            f.write(message_raw)


def try_decode(b, encodings):
    last_ex = None
    for encoding in encodings:
        try:
            return b.decode(encoding)
        except UnicodeDecodeError as ex:
            last_ex = ex
    raise last_ex 


def get_header(message, header_name):
    header = message.get(header_name)
    if not header:
        return header
    dh = email.header.decode_header(header)
    default_charset = 'ascii'
    try:
        return ''.join([ensure_text(t[0], t[1] or default_charset) for t in dh])
    except (UnicodeDecodeError, LookupError):
        try:
            return ''.join([try_decode(t[0], ['ascii', 'gbk', 'utf8']) for t in dh])
        except UnicodeDecodeError:
            return str(header)


class ImapScaner(Source):
    imap_client: ImapClient = None
    mailbox: str = None
    list_mailboxes: bool = False
    start_uid: int = None

    def add_arguments(self, parser):
        parser.add_argument('--imap-server')
        parser.add_argument('--imap-port', type=int)
        parser.add_argument('--imap-ssl', type=bool, default=True, nargs='?')
        parser.add_argument('--imap-user')
        parser.add_argument('--imap-pass')
        parser.add_argument('--mailbox', default='INBOX')
        parser.add_argument('--list-mailboxes', action='store_true', default=False)
        parser.add_argument('--start-uid', type=int, default=1)
        parser.add_argument('--start-uid-file')

    def init(self, ops):
        imap_server = ops.imap_server
        imap_port = ops.imap_port
        imap_ssl = ops.imap_ssl
        imap_user = ops.imap_user
        imap_pass = ops.imap_pass
        self.mailbox = ops.mailbox
        self.list_mailboxes = ops.list_mailboxes
        if ops.start_uid_file:
            start_uid_text = ''
            if os.path.exists(ops.start_uid_file):
                with open(ops.start_uid_file, 'r') as f:
                    start_uid_text = f.read()
            
            if start_uid_text:
                self.start_uid = int(start_uid_text)
        else:
            self.start_uid = ops.start_uid

        debug = False
        self.imap_client = ImapClient(imap_server, imap_port, imap_user, imap_pass, ops.mailbox, debug=debug)
        self.imap_client.connect()

    def start(self):
        logger.debug('start, start_uid %s', self.start_uid)
        imap_conn = self.imap_client
        if self.list_mailboxes:
            for item in self.list_dirs():
                yield item
            return

        if self.start_uid:
            search_results = self.imap_client.uid('search', None, f'UID {self.start_uid}:*')[1][0].split()
        else:
            search_results = self.imap_client.uid('search', None, 'ALL')[1][0].split()

        len_results = len(search_results)
        for i, uid in enumerate(search_results):
            uid = uid.decode()
            logger.debug('%s %s/%s' % (uid, i, len_results))
            status, data = imap_conn.uid('fetch', uid, '(BODY.PEEK[HEADER])')

            if data is None or not data[0]:
                continue

            message = email.message_from_bytes(data[0][1])
            subject = get_header(message, 'subject')
            email_from = get_header(message, 'from')
            email_to = get_header(message, 'to')
            msg_id = get_header(message, 'Message-ID')
            date_tuple = email.utils.parsedate_tz(message['Date'])
            local_date = datetime.datetime.fromtimestamp(
                email.utils.mktime_tz(date_tuple)).strftime('%Y-%m-%d %H:%M:%S')

            doc = {
                'subject': subject, 
                'from': email_from, 
                'to': email_to, 
                'msg_id': msg_id, 
                'date': local_date, 
                'mailbox': self.mailbox,
                'uid': int(uid),  
            }
            yield doc

    def list_dirs(self):
        for item in self.imap_client.list()[1]:
            l = item.decode().split(' "/" ')
            mailbox_id = re.search('^"(.*)"$', l[1]).group(1)
            yield {'name': mailbox_id}
