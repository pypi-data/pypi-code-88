import logging
import os
import socket
import traceback

import paramiko

logger = logging.getLogger(__name__)


class SSH_Client:
    def __init__(self, hostname, username, password, port=22):

        hostkey = None
        try:
            host_keys = paramiko.util.load_host_keys(
                os.path.expanduser("~/.ssh/known_hosts")
            )
        except IOError:
            try:
                # try ~/ssh/ too, because windows can't have a folder named ~/.ssh/
                host_keys = paramiko.util.load_host_keys(
                    os.path.expanduser("~/ssh/known_hosts")
                )
            except IOError:
                logger.debug("*** Unable to open host keys file")
                host_keys = {}

        if hostname in host_keys:
            hostkeytype = host_keys[hostname].keys()[0]
            hostkey = host_keys[hostname][hostkeytype]
            logger.debug("Using host key of type %s" % hostkeytype)

        try:
            t = paramiko.Transport((hostname, port))
            t.connect(
                hostkey,
                username,
                password,
                gss_host=socket.getfqdn(hostname),
                gss_auth=False,
                gss_kex=False,
            )
            self.sftp = paramiko.SFTPClient.from_transport(t)
        except Exception as e:
            logger.error("*** Caught exception: %s: %s" % (e.__class__, e))
            traceback.print_exc()
            try:
                self.t.close()
            except:
                pass

    def get(self, remotepath, localpath, callback=None):
        try:
            self.sftp.get(remotepath=remotepath, localpath=localpath, callback=callback)
        except IOError as ex:
            logger.error(f'{remotepath} {str(ex)}')

    def put(self, localpath, remotepath, callback=None, confirm=True):
        try:
            self.sftp.put(localpath=localpath, remotepath=remotepath, callback=callback, confirm=confirm)
        except:
            pass
