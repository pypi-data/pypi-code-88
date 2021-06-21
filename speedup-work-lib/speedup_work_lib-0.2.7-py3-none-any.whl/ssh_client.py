#!/usr/bin/env python
"""
.. current_module:: ssh_client.py
.. created_by:: Darren Xie
.. created_on:: 04/26/2021

This python script is base script to connect Linux server by SSH.
"""
import sys
from datetime import datetime
from io import StringIO

import paramiko
from paramiko.auth_handler import AuthenticationException
from scp import SCPClient, SCPException

TIME_FORMAT = '%m/%d/%Y %H:%M:%S'


class SshClient:
    """A wrapper of paramiko.SSHClient"""
    TIMEOUT = 180  # 3 minutes

    def __init__(self, host, port, username, password, key=None, passphrase=None):
        self.username = username
        self.password = password
        self.client = paramiko.SSHClient()
        self.scp = None
        self.iface_ip = {}
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        if key is not None:
            key = paramiko.RSAKey.from_private_key(StringIO(key), password=passphrase)
        try:
            self.client.connect(host, port, username=username, password=password, pkey=key, timeout=self.TIMEOUT)
            self.scp = SCPClient(self.client.get_transport(), socket_timeout=self.TIMEOUT)
        except AuthenticationException as e:
            self._print_log(f"Authentication failed: did you remember to create an SSH key? {e}")
            # raise str(e)
        except Exception as e:
            self._print_log(f"ERROR: Could be wrong User Id, Password and IP.")
            raise str(e)

    def close(self):
        """Close client."""
        if self.client is not None:
            if self.scp:
                self.scp.close()
            self.client.close()
            self.client = None

    def execute(self, command, sudo=False, verbose=False):
        """
        Excecute a single command.
        :param command: Command to be executed
        :param sudo: Add sudo for this command if True
        :param verbose: print out the command if True.
        """
        if verbose:
            self._print_log(f"Running command: [{command}]")
        feed_password = False
        if sudo and self.username != "root":
            command = "sudo -S -p '' %s" % command
            feed_password = self.password is not None and len(self.password) > 0
        stdin, stdout, stderr = self.client.exec_command(command, timeout=self.TIMEOUT)
        if feed_password:
            stdin.write(self.password + "\n")
            stdin.flush()
        return {'out': stdout.readlines(),
                'err': stderr.readlines(),
                'retval': stdout.channel.recv_exit_status()}

    def execute_cmd_list_sudo(self, cmd_list):
        """
        Execute command list with sudo.
        :param cmd_list: Commands list
        """
        for cmd in cmd_list:
            result = self.execute(cmd, sudo=True, verbose=True)
            self._print_log(result)

    def execute_cmd_list(self, cmd_list):
        """
        Execute command list without sudo.
        :param cmd_list: Commands list
        """
        for cmd in cmd_list:
            result = self.execute(cmd, verbose=True)
            self._print_log(result)

    def _print_log(self, msg=''):
        """
        Print out the log message
        :param msg: message
        """
        sys.stdout.write(f"[{datetime.now().strftime(TIME_FORMAT)}]: {msg}\n")

    def append_line_to_file(self, line, to_file):
        """
        Append a line in a remote file
        :param line: A line of string
        :param to_file: The file to be added the line
        """
        ftp = self.client.open_sftp()
        try:
            edit_file = ftp.file(to_file, 'a+')
            edit_file.write(f"\n{line}\n")
            edit_file.flush()
            self._print_log(f"Just added line [{line}] in file [{to_file}]")
        finally:
            ftp.close()

    def is_line_in_file(self, line, to_file):
        """
        Append a line in a remote file
        :param line: A line of string
        :param to_file: The file to be added the line
        :return: True if the line in the to_file, else False
        """
        ftp = self.client.open_sftp()
        result = False
        try:
            edit_file = ftp.open(to_file, mode='r')
            edit_file.prefetch()  # increase the read speed
            if line in edit_file.read().decode():
                result = True
        finally:
            ftp.close()
            return result

    def is_file_empty(self, check_f):
        """
        Check if the passing in file is empty
        :param check_f: passing in file
        :return: True if empty, otherwise False
        """
        ftp = self.client.open_sftp()
        result = False
        try:
            edit_file = ftp.open(check_f, mode='r')
            edit_file.prefetch()  # increase the read speed
            if not edit_file.read():
                result = True
        finally:
            ftp.close()
            return result

    def create_file_by_content(self, content, to_file):
        """
        Create a file with giving content.
        :param content: content of file
        :param to_file: The file to be created
        :return:
        """
        ftp = self.client.open_sftp()
        try:
            edit_file = ftp.file(to_file, 'w')
            edit_file.write(f"{content}")
            edit_file.flush()
            self._print_log(f"The file [{to_file}] was just created.")
        finally:
            ftp.close()

    def set_iface_ip(self):
        """
        Get dict {iface: ip}
        :return: dict {iface: ip}
        """
        cmd = "/sbin/ip -4 -o a | cut -d ' ' -f 2,7 | cut -d '/' -f 1"
        result = self.execute(cmd)
        for n_ip in result['out']:
            k, v = n_ip.split(' ')
            self.iface_ip[k] = v.replace('\n', '')
        return self.iface_ip

    def get_iface(self, ip_addr):
        """
        Get interface name given ip address
        :param ip_addr: input ip address
        :return: interface name if exist, otherwise None
        """
        self.set_iface_ip()
        for k, v in self.iface_ip.items():
            if v == ip_addr:
                return k
        return None

    def scp_folder(self, from_f, to_f):
        """
        Scp the whole folder from from_f to to_f.
        :param from_f: from folder path
        :param to_f: to folder path
        :return:
        """
        try:
            self._print_log(f"Running: [scp {from_f} {to_f}]")
            self.scp.put(from_f, recursive=True, remote_path=to_f)
        except SCPException as e:
            raise str(e)
        except Exception as e:
            raise str(e)

    def does_dir_exist(self, dir_t):
        """
        Checi if the test directory exists
        :param dir_t: passing in directory to test
        :return: True if exists, False if not.
        """
        cmd = f'test -d {dir_t} && echo $?'
        result = self.execute(cmd)['out']
        if result and result[0].strip() == '0':
            return True
        else:
            return False

    def does_file_exist(self, file_t):
        """
        Checi if the test file exists
        :param file_t: passing in file to test
        :return: True if exists, False if not.
        """
        cmd = f'test -f {file_t} && echo $?'
        result = self.execute(cmd)['out']
        if result and result[0].strip() == '0':
            return True
        else:
            return False
