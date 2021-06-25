import base64
import fileinput
import hashlib
import json
import logging
import os
import platform
import shutil
import socket
import sys
import zipfile
from datetime import datetime
from subprocess import Popen, PIPE, TimeoutExpired
from xml.dom import minidom
from xml.dom.minidom import Element

import winrm
from requests.exceptions import ConnectionError
from winrm import Protocol
from winrm.exceptions import (InvalidCredentialsError,
                              WinRMError,
                              WinRMTransportError,
                              WinRMOperationTimeoutError)

__author__ = 'Andrey Komissarov'
__email__ = 'a.komisssarov@gmail.com'
__date__ = '12.2019'
__version__ = '1.1.7'

logger_name = 'WinOSClient'
logger = logging.getLogger(logger_name)
logger.setLevel(logging.INFO)
formatter = logging.Formatter(fmt='%(asctime)-15s | %(levelname)s | %(name)s | %(message)s',
                              datefmt='%Y-%m-%d %H:%M:%S')

# Console logger
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
ch.setFormatter(formatter)
logger.addHandler(ch)


class ResponseParser:
    """Response parser"""

    def __init__(self, response, command: str = None):
        self.response = response
        self.command = command

    def __repr__(self):
        return str(self.response)

    @staticmethod
    def _decoder(response):
        return response.decode('cp1252').strip()

    @property
    def stdout(self) -> str:
        try:
            stdout = self._decoder(self.response.std_out)
        except AttributeError:
            stdout = self._decoder(self.response[1])
        out = stdout if stdout else None
        return out

    @property
    def stderr(self) -> str:
        try:
            stderr = self._decoder(self.response.std_err)
        except AttributeError:
            stderr = self._decoder(self.response[2])
        err = stderr if stderr else None
        return err

    @property
    def exited(self) -> int:
        """Get exit code"""

        try:
            exited = self.response.status_code
        except AttributeError:
            exited = self.response[0]
        return exited

    @property
    def ok(self) -> bool:
        try:
            return self.response.status_code == 0
        except AttributeError:
            return self.response[0] == 0

    def json(self) -> dict:
        """Convert string response into dict"""
        return json.loads(self.stdout)

    @property
    def cmd(self) -> str:
        """Show executed command"""
        return self.command

    def decoded(self, encoding: str = 'utf8'):
        """Decode stdout response.

        :param encoding: utf8 by default
        :return:
        """

        return base64.b64decode(self.stdout).decode(encoding)


class WinOSClient:
    """The cross-platform tool to work with remote and local Windows OS.

    Returns response object with exit code, sent command, stdout/sdtderr, json.
    Check response methods.
    """

    _URL = 'https://pypi.org/project/pywinrm/'

    def __init__(
            self,
            host: str = None,
            username: str = None,
            password: str = None,
            logger_enabled: bool = True):

        self.host = host
        self.username = username
        self.password = password
        self.logger_enabled = logger_enabled
        self.logger = logger

        logger.disabled = not self.logger_enabled

    def __str__(self):
        return (f'Local host: {self.get_current_os_name_local()}\n'
                f'Remote IP: {self.host}\n'
                f'Username: {self.username}\n'
                f'Password: {self.password}\n'
                f'Logger enabled: {self.logger_enabled}')

    @property
    def version(self):
        return __version__

    def list_all_methods(self):
        """Returns all available public methods"""

        methods = [
            method for method in self.__dir__()
            if not method.startswith('_')
        ]
        index = methods.index('list_all_methods') + 1
        return methods[index:]

    @property
    def is_local(self) -> bool:
        """Verify client is configured to work with local OS only"""

        return not self.host or self.host == 'localhost' or self.host == '127.0.0.1'

    def is_host_available(self, port: int = 5985, timeout: int = 5) -> bool:
        """Check remote host is available using specified port.

        Port 5985 used by default
        """

        if self.is_local:
            return True

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout)
            response = sock.connect_ex((self.host, port))
            result = False if response else True
            logger.info(f'{self.host} is available: {result}')
            return result

    # ---------- Service section ----------
    @property
    def session(self):
        """Create WinRM session connection to a remote server"""

        session = winrm.Session(self.host, auth=(self.username, self.password))
        return session

    def _protocol(self, endpoint: str, transport: str):
        """Create Protocol using low-level API"""

        session = self.session

        protocol = Protocol(endpoint=endpoint,
                            transport=transport,
                            username=self.username,
                            password=self.password,
                            server_cert_validation='ignore',
                            message_encryption='always')

        session.protocol = protocol
        return session

    def _client(self, command: str, ps: bool = False, cmd: bool = False, use_cred_ssp: bool = False, *args):
        """The client to send PowerShell or command-line commands

        :param command: Command to execute
        :param ps: Specify if PowerShell is used
        :param cmd: Specify if command-line is used
        :param use_cred_ssp: Specify if CredSSP is used
        :param args: Arguments for command-line
        :return: ResponseParser
        """

        response = None

        try:
            logger.info(f'[{self.host}] {command}')
            if ps:  # Use PowerShell
                endpoint = (f'https://{self.host}:5986/wsman'
                            if use_cred_ssp
                            else f'http://{self.host}:5985/wsman')
                transport = 'credssp' if use_cred_ssp else 'ntlm'
                client = self._protocol(endpoint, transport)
                response = client.run_ps(command)
            elif cmd:  # Use command-line
                client = self._protocol(
                    endpoint=f'http://{self.host}:5985/wsman',
                    transport='ntlm')
                response = client.run_cmd(command, [arg for arg in args])
            return ResponseParser(response, command=command)

        # Catch exceptions
        except InvalidCredentialsError as err:
            logger.error(f'Invalid credentials: {self.username}@{self.password}. {err}')
            raise InvalidCredentialsError
        except ConnectionError as err:
            logger.error(f'Connection error: {err}')
            raise ConnectionError
        except (WinRMError,
                WinRMOperationTimeoutError,
                WinRMTransportError) as err:
            logger.error(f'WinRM error: {err}')
            raise err
        except Exception as err:
            logger.error(f'Unhandled error: {err}. Try to use "run_cmd_local" method instead.')
            raise err

    @staticmethod
    def _run_local(cmd: str, timeout: int = 60):
        """Main function to send commands using subprocess LOCALLY.

        Used command-line (cmd.exe, powershell or bash)

        :param cmd: string, command
        :param timeout: timeout for command
        :return: Decoded response
        """

        with Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE) as process:
            try:
                logger.info(f'[LOCAL] {cmd}')
                stdout, stderr = process.communicate(timeout=timeout)
                exitcode = process.wait(timeout=timeout)
                response = exitcode, stdout, stderr
                return ResponseParser(response, command=cmd)

            except TimeoutExpired as err:
                process.kill()
                logger.error(f'Timeout exception: {err}')
                raise err

    # ----------------- Main low-level methods ----------------
    def run_cmd(self, command: str, *args) -> ResponseParser:
        """
        Allows to execute cmd command on a remote server.

        Executes command locally if host was not specified
        or host == "localhost/127.0.0.1"

        :param command: command
        :param args: additional command arguments
        :return: Object with exit code, stdout and stderr
        """

        return self._client(command, cmd=True, *args)

    def run_cmd_local(self, command: str, timeout: int = 60) -> ResponseParser:
        """
        Allows to execute cmd command on a remote server.

        Executes command locally if host was not specified
        or host == "localhost/127.0.0.1"

        :param command: command
        :param timeout: timeout
        :return: Object with exit code, stdout and stderr
        """

        return self._run_local(command, timeout)

    def run_ps(self, command: str = None, use_cred_ssp: bool = False) -> ResponseParser:
        """Allows to execute PowerShell command or script using a remote shell and local server.

        >>> self.run_ps('d:\\script.ps1')  # Run script located on remote server

        >>> script_path = r'c:\Progra~1\Directory\Samples\script.py'  # Doesn't work with path containig spaces
        >>> params = '-param1 10 -param2 50'
        >>> self.run_ps(f'{script_path} {params}')  # Run script located on remote server with parameters

        :param command: Command
        :param use_cred_ssp: Use CredSSP.
        :return: Object with exit code, stdout and stderr
        """

        return self._client(command, ps=True, use_cred_ssp=use_cred_ssp)

    def run_ps_local(self, command: str = None, script: str = None, timeout: int = 60, **params) -> ResponseParser:
        cmd = f"powershell -command \"{command}\""
        if script:
            params_ = ' '.join([f'-{key} {value}' for key, value in params.items()])
            cmd = f'powershell -file {script} {params_}'

        return self._run_local(cmd, timeout=timeout)

    # ----------------- High-level methods ----------------
    def remove(self, path: str) -> bool:
        """Remove file or directory recursively on remote server

        :param path: Full file\\directory path
        """

        cmd = f'Remove-Item -Path "{path}" -Recurse -Force'
        result = self.run_ps(cmd)
        if result.exited:
            logger.error(result.stderr)
            return False
        return True

    @staticmethod
    def remove_local(path: str, ignore_errors: bool = False):
        """Remove file or directory recursively using local path

        :param path: execute command on local server. Path C:\test_dir
        :param ignore_errors: If ignore_errors is set, errors are ignored. Used for local directory and only
        """

        logger.info(f'[LOCAL] Removing {path}')

        try:
            if os.path.isfile(path):
                os.remove(path)
            else:
                shutil.rmtree(path, ignore_errors=ignore_errors)
            return True
        except PermissionError as err:
            logger.error(err)
            if not ignore_errors:
                raise err
        except OSError as err:
            logger.error(err)
            if not ignore_errors:
                raise err

    def get_os_info(self) -> dict:
        """Get OS info"""

        cmd = 'Get-CimInstance Win32_OperatingSystem | ConvertTo-Json'
        return self.run_ps(cmd).json()

    def get_os_info_local(self) -> dict:
        """Get OS info"""

        cmd = 'Get-CimInstance Win32_OperatingSystem | ConvertTo-Json'
        return self.run_ps_local(cmd).json()

    def get_os_name(self) -> str:
        """Get OS name only"""

        return self.get_os_info().get('Caption')

    def get_os_name_local(self) -> str:
        """Get OS name only"""

        return self.get_os_info_local().get('Caption')

    @staticmethod
    def get_current_os_name_local():
        """Returns current OS name"""

        return platform.system()

    def ping(self, host: str = '', packets_number: int = 4):
        """Ping remote host from current one.

        :param host: IP address to ping. Used host IP from init by default
        :param packets_number: Number of packets. 4 by default
        """

        ip_ = host if host else self.host
        command = f'ping -n {packets_number} {ip_}'
        return self._run_local(cmd=command)

    def exists(self, path: str) -> bool:
        """Check file/directory exists from remote server

        :param path: Full path. Can be network path. Share must be attached!
        :return:
        """

        result = self.run_ps(f'Test-Path -Path "{path}"')
        return True if result.stdout == 'True' else False

    @staticmethod
    def exists_local(path: str) -> bool:
        """Check local file/directory exists

        :param path: Full path. Can be network path. Share must be attached!
        :return:
        """

        logger.info(f'[LOCAL] Exists {path}')
        return os.path.exists(path)

    def get_content(self, path):
        """Get remote file content"""
        return self.run_ps(f'Get-Content "{path}"')

    def get_content_local(self, path):
        """Get local file content"""
        return self.run_ps_local(f'Get-Content "{path}"')

    def get_json(self, path: str) -> dict:
        """Read JSON file as string and pretty print it into console """

        file = self.get_content(path)
        if file.ok:
            return file.json()
        err_msg = f'File {path} not found on the {self.host}'
        logger.error(err_msg)
        raise FileNotFoundError(err_msg)

    def get_json_local(self, path: str) -> dict:
        """Read JSON file as string and pretty print it into console """

        file = self.get_content_local(path)
        if file.ok:
            return file.json()
        err_msg = f'[LOCAL] File {path} not found.'
        logger.error(err_msg)
        raise FileNotFoundError(err_msg)

    @staticmethod
    def get_local_hostname_ip():
        """Get local IP and hostname

        :return: Object with "ip" and "hostname" properties
        """

        host_name = socket.gethostname()
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        return type(
            'HostnameIP', (),
            {
                'ip': s.getsockname()[0],
                'hostname': host_name
            }
        )

    def get_dirs_files(self, directory: str, mask: str = None, last: bool = False):
        """File/directory manager on remote server.

        :param directory: Root directory to search. List dir if specified this param only.
        :param mask: List dir by mask by filter. "*.txt"
        :param last: Get last modified entity
        :return: list of files
        """

        cmd_pattern = f'Get-ChildItem -path "{directory}"'
        if mask:
            cmd_pattern = f'{cmd_pattern} -Filter "{mask}"'
        if last:
            cmd_pattern = f'{cmd_pattern} | Sort LastWriteTime | Select -last 1'
        cmd = f'({cmd_pattern}).Name'

        result = self.run_ps(cmd).stdout
        if result is None:
            logger.info('Nothing found. Dont\'t forget to use wildcards.')
            return []

        result_list = result.splitlines()
        if last:
            return result_list[0]
        return result_list

    @staticmethod
    def get_dirs_files_local(directory: str, mask: str = '', last: bool = False):
        """List dir or search for file(s) in specific local directory

        :param directory: Root directory to search
        :param mask: Search files by mask. Set ".exe" for extension.
        :param last: Get last modified file.
        :return: list of files
        """

        try:
            mask = mask.replace('*', '')
        except AttributeError:
            ...

        entities_list = [os.path.join(directory, file.lower()) for file in os.listdir(directory)]

        if last and not mask:
            return max(entities_list, key=os.path.getmtime)
        if mask and not last:
            return list(filter(lambda x: mask.lower() in x, entities_list))
        if mask and last:
            filtered = list(filter(lambda x: mask.lower() in x, entities_list))
            return max(filtered, key=os.path.getmtime)

        return entities_list

    def get_file_version(self, path: str, version: str = 'Product') -> str:
        """Get remote windows file version from file property

        :param path: Full path to the file
        :param version: ProductVersion | File
        :return: 51.1052.0.0
        """

        cmd = fr"(Get-Item '{path}').VersionInfo.{version}Version"
        return self.run_ps(cmd).stdout

    def get_file_version_local(self, path: str, version: str = 'Product') -> str:
        """Get local windows file version from file property

        :param path: Full path to the file
        :param version: ProductVersion | File
        :return: 51.1052.0.0
        """

        exists = os.path.exists(path)
        if exists:
            cmd = fr"(Get-Item '{path}').VersionInfo.{version}Version"
            return self.run_ps_local(cmd).stdout
        logger.error(f'File {path} not found.')

    def get_file_size(self, path: str) -> int:
        """Get remote windows file size. Returns size in bytes.

        :param path: Full path to the file
        :return:
        """

        result = self.run_ps(f'(Get-Item "{path}").Length')
        if 'Cannot find path' in result.stderr:
            logger.error(f'File [{path}] not found.')
            return 0
        return int(result.stdout)

    @staticmethod
    def get_file_size_local(path: str) -> int:
        """Get local windows file size. Returns size in bytes.

        :param path: Full path to the file
        :return:
        """

        try:
            return os.path.getsize(path)
        except FileNotFoundError as err:
            logger.error(f'File [{path}] not found. {err}')
            raise err

    @staticmethod
    def replace_text_local(path: str, old_text: str, new_text: str, backup: str = '.bak'):
        """Replace all string mention with a new string

        :param path: Full file path
        :param old_text: Text to replace
        :param new_text: Replacements text
        :param backup: Create backup file with specific extension in a current directory. Use blank string "" if you do
        """

        with fileinput.FileInput(path, inplace=True, backup=backup) as file:
            for line in file:
                print(line.replace(old_text, new_text), end='')

    def get_hash(self, path: str, algorithm: str = 'MD5') -> str:
        """Get file hash on remote server.

        :param path: Full file path
        :param algorithm: Algorithm type. MD5, SHA1(256, 384, 512), RIPEMD160
        :return: File's hash
        """

        result = self.run_ps(f'(Get-FileHash -Path {path} -Algorithm {algorithm}).Hash')
        return result.stdout

    def get_available_hash_algorithm(self) -> list:
        """Get available HASH algorithms on remote server"""

        cmd = '(Get-Command Get-FileHash).Parameters.Algorithm.Attributes.ValidValues'
        result = self.run_ps(cmd)
        return result.stdout.split()

    @staticmethod
    def get_hash_local(path: str, algorithm: str = 'MD5') -> str:
        """Open file and calculate hash

        :param path: Full file path
        :param algorithm: Algorithm type. MD5, SHA1(224, 256, 384, 512) etc.
        :return: File's hash
        """

        # Verify algorithm
        algorithm_lower = algorithm.lower()
        assert hasattr(hashlib, algorithm_lower), \
            f'Unsupported algorithm type: {algorithm}. Algorithms allowed: {hashlib.algorithms_available}'

        # Get file hash
        with open(path, 'rb') as f:
            hash_ = getattr(hashlib, algorithm_lower)()
            while True:
                data = f.read(8192)
                if not data:
                    break
                hash_.update(data)
            return hash_.hexdigest()

    def get_xml(self):
        # (Select-Xml -Path D:\Test.xml -XPath "/configuration/parameters/logging/LogLevel").Node.Value
        msg = 'Use .run_ps() and "Select-Xml" cmdlet. Select-Xml -Path D:\\Test.xml -XPath "/configuration"'
        raise NotImplementedError(msg)

    @staticmethod
    def get_xml_dom_local(path: str, tag: str = None) -> Element:
        """Parse local XML file using dom.

        Methods to get info from dom: getElementsByTagName(), getElementById()

        >>> root = WinOSClient.get_xml_dom_local(path)
        >>> root.getElementsByTagName('LogLevel')
        >>> root.getElementsByTagName('LogLevel')[0].attributes['value'].value
        >>> WinOSClient.get_xml_dom_local(path, tag='LogLevel')

        :param path: File path
        :param tag: Get tag element. "GuiMonitoringAllowed"
        :return: root or tag element
        """

        root = minidom.parse(path)
        if tag:
            return root.getElementsByTagName(tag)
        return root

    @staticmethod
    def get_xml_tree_local(path: str, tag: str = None):
        """Parse local XML file using tree.

        :param path: file path
        :param tag: Get tag text. "flags/GuiMonitoringAllowed"
        :return: root or tag text
        """

        import xml.etree.ElementTree as ET

        try:
            root = ET.parse(path).getroot()
        except ET.ParseError as err:
            logger.error(f'Failed to open file. {err}')
            raise RuntimeError(err)

        if tag:
            tag_text = root.find(tag).text
            if tag_text.isdigit():
                return int(tag_text)
            return tag_text
        return root

    def clean_directory(self, path: str, ignore_errors: bool = False):
        """Clean (remove) all files from a remote windows directory.

        :param path: Full directory path. Example, C:\test | D:
        :param ignore_errors: Suppress all errors during execution.
        """

        rm_cmd = f'Remove-Item -Path {path}\\* -Recurse -Force'
        if ignore_errors:
            rm_cmd += ' -ErrorAction SilentlyContinue'

        cmd = f"""if (Test-Path {path})
        {{
            {rm_cmd}
        }}
        else{{
            exit 2
        }}"""

        result = self.run_ps(cmd)

        # Raise exception if such directory does not exist.
        if result.exited == 2:
            msg = f'Directory "{path}" not found.'
            logger.error(msg)
            raise FileNotFoundError(msg)
        # Suppress error if they are and ignore_errors=True
        elif not result.ok and ignore_errors:
            return True
        return result.stderr

    def clean_directory_local(self, path: str, ignore_errors: bool = False):
        """Clean (remove) all files from a windows directory

        :param path: Full directory path. D:\test
        :param ignore_errors: Suppress errors during execution.
        """

        for the_file in os.listdir(path):
            file_path = os.path.join(path, the_file)
            self.remove_local(file_path, ignore_errors=ignore_errors)
        return True

    def copy(self, source: str, destination: str, new_name: str = None) -> bool:
        """Copy file on remote server.

        Creates destination directory if it does not exist.

        - Copy to the root of disk and preserve file name

        >>> self.copy(source='d:\\zen.txt', destination='e:')

        - Copy to the root of disk with new name

        >>> self.copy(source='d:\\zen.txt', destination='e:\', new_name='new_name.txt')

        - Copy to nonexistent directory with original name

        >>> self.copy(source='d:\\zen.txt', destination=r'e:\\dir1')

        - Copy all content from "dir" to nonexistent e:\\\\all

        >>> self.copy(source='d:\\dir\\*', destination=r'e:\\all')

        You can copy data from network attached share to remote server to it.

        >>> self.copy(source='d:\\dir\\*', destination=r'e:\\all')

        :param source: Source path to copy. d:\\zen.txt, d:\\dir\\*
        :param destination: Destination root directory. e:, e:\\, e:\\dir1
        :param new_name: Copy file with new name if specified.
        :return:
        """

        base_name = os.path.basename(source)
        destination = f'{destination}\\' if destination.endswith(':') else destination

        dst_full = os.path.join(destination, base_name).replace('*', '')
        if new_name is not None:
            dst_full = os.path.join(destination, new_name)

        cmd = fr"""
        if (!(Test-Path "{destination}")){{
            New-Item "{destination}" -Type Directory -Force | Out-Null
        }}
        Copy-Item -Path "{source}" -Destination "{dst_full}" -Recurse -Force
        """

        self.run_ps(cmd)
        return self.exists(dst_full)

    def copy_local(self, source: str, destination: str, new_name: str = None) -> bool:
        """Copy local file to a local/remote server.

        Creates destination directory if does not exist.

        :param source: Source file to copy
        :param destination: Destination directory name. Not full file path.
        :param new_name: Copy file with a new name if specified.
        :return: Check copied file exists
        """

        # Get full destination path
        dst_full = os.path.join(destination, new_name) if new_name is not None else destination

        # Create directory
        dir_name = os.path.dirname(dst_full) if new_name else destination
        self.create_directory_local(dir_name)

        try:
            shutil.copy(source, dst_full)
        except FileNotFoundError as err:
            logger.error(f'ERROR occurred during file copy. {err}')
            raise err

        return self.exists_local(dst_full)

    def create_directory(self, path: str) -> bool:
        """Create directory on remote server. Directories will be created recursively.

        >>> self.create_directory(r'e:\1\2\3')

        :param path:
        :return:
        """

        cmd = fr"""
        if (!(Test-Path "{path}")){{
            New-Item "{path}" -Type Directory -Force | Out-Null
        }}
        """

        result = self.run_ps(cmd)
        return result.ok

    def create_directory_local(self, path: str):
        """Create directory. No errors if it already exists.

        :param path: C:\test_dir
        :return:
        """

        os.makedirs(path, exist_ok=True)
        return self.exists_local(path)

    def unzip(self, path: str, target_directory: str):
        """Extract .zip archive to destination folder on remote server.

        Creates destination folder if it does not exist

        :param path: C:\Archives\Draft[v1].Zip
        :param target_directory: C:\Reference
        :return:
        """

        cmd = f'Expand-Archive -Path "{path}" -DestinationPath "{target_directory}"'
        result = self.run_ps(cmd)
        return result

    @staticmethod
    def unzip_local(path: str, target_directory=None):
        """Extract .zip archive to destination folder

        Creates destination folder if it does not exist

        :param path: Full path to archive
        :param target_directory: Full path to archive
        """

        directory_to_extract_to = target_directory

        if not target_directory:
            directory_to_extract_to = os.path.dirname(path)

        with zipfile.ZipFile(path, 'r') as zip_ref:
            zip_ref.extractall(directory_to_extract_to)
        logger.info(f'[{path}] unpacked to the [{directory_to_extract_to}]')

        return target_directory

    # ---------- Service / process management ----------
    def get_service(self, name: str) -> json:
        """Check windows service"""

        result = self.run_ps(f'Get-Service -Name {name} | ConvertTo-Json')
        try:
            return result.json()
        except TypeError:
            logger.error(f'Exit code: {result.exited}. {result.stderr}')
            return {}

    def get_service_local(self, name: str) -> json:
        """Check windows service"""

        result = self.run_ps_local(f'Get-Service -Name {name} | ConvertTo-Json')
        try:
            return result.json()
        except TypeError:
            logger.error(f'Exit code: {result.exited}. {result.stderr}')
            return {}

    def get_service_status(self, name: str) -> str:
        """Check windows service status"""

        result = self.run_ps(f'(Get-Service -Name {name}).Status')
        return result.stdout

    def get_service_status_local(self, name: str) -> str:
        """Check windows service status"""

        result = self.run_ps_local(f'(Get-Service -Name {name}).Status')
        return result.stdout

    def start_service(self, name: str) -> bool:
        """Start service"""
        return self.run_ps(f'Start-Service -Name {name}').ok

    def start_service_local(self, name: str) -> bool:
        """Start service"""
        return self.run_ps_local(f'Start-Service -Name {name}').ok

    def restart_service(self, name: str):
        """Restart service"""
        return self.run_ps(f'Restart-Service -Name {name}').ok

    def restart_service_local(self, name: str):
        """Restart service"""
        return self.run_ps_local(f'Restart-Service -Name {name}').ok

    def stop_service(self, name: str) -> bool:
        """Stop service"""
        return self.run_ps(f'Stop-Service -Name {name}').ok

    def stop_service_local(self, name: str) -> bool:
        """Stop service"""
        return self.run_ps_local(f'Stop-Service -Name {name}').ok

    def get_process(self, name: str) -> json:
        """Check windows process status"""

        result = self.run_ps(f'Get-Process -Name {name} | ConvertTo-Json')

        try:
            return result.json()
        except TypeError:
            logger.error(f'Exit code: {result.exited}. {result.stderr}')
            return {}

    def get_process_local(self, name: str) -> json:
        """Check windows process status"""

        result = self.run_ps_local(f'Get-Process -Name {name} | ConvertTo-Json')

        try:
            return result.json()
        except TypeError:
            logger.error(f'Exit code: {result.exited}. {result.stderr}')
            return {}

    def kill_process(self, name: str) -> bool:
        """Kill windows local service status. Remote and local"""

        result = self.run_cmd(f'taskkill -im {name} /f')
        if result.exited == 128:
            logger.error(f'Service [{name}] not found')
            raise FileNotFoundError(f'Service [{name}] not found')
        return result.ok

    def kill_process_local(self, name: str) -> bool:
        """Kill windows local service status. Remote and local"""

        result = self.run_cmd_local(f'taskkill -im {name} /f')
        if result.exited == 128:
            logger.error(f'Service [{name}] not found')
            return True
        return result.ok

    def wait_service_start(self, name: str, timeout: int = 30, interval: int = 3):
        """Wait for service start specific time

        :param name: Service name
        :param timeout: Timeout in sec
        :param interval: How often check service status
        :return:
        """

        cmd = f"""
        if (!(Get-Service -Name {name} -ErrorAction SilentlyContinue)){{
            throw "Service [{name}] not found!"
        }}
        
        $timeout = {timeout}
        $timer = 0
        While ((Get-Service -Name {name}).Status -ne "Running"){{
            Start-Sleep {interval}
            $timer += {interval}
            if ($timer -gt $timeout){{
                throw "The service [{name}] was not started within {timeout} seconds."
            }}
        }}
        """

        result = self.run_ps(cmd)

        if 'not found' in result.stderr:
            logger.error(f'Service [{name}] not found.')
        elif 'was not started' in result.stderr:
            logger.error(f'Service [{name}] was not started within {timeout} seconds.')
        return result.ok

    def wait_service_start_local(self, name: str, timeout: int = 30, interval: int = 3):
        """Wait for service start specific time

        :param name: Service name
        :param timeout: Timeout in sec
        :param interval: How often check service status
        :return:
        """

        cmd = f"""
        if (!(Get-Service -Name {name} -ErrorAction SilentlyContinue)){{
            throw "Service [{name}] not found!"
        }}

        $timeout = {timeout}
        $timer = 0
        While ((Get-Service -Name {name}).Status -ne "Running"){{
            Start-Sleep {interval}
            $timer += {interval}
            if ($timer -gt $timeout){{
                throw "The service [{name}] was not started within {timeout} seconds."
            }}
        }}
        """

        result = self.run_ps_local(cmd)

        if 'not found' in result.stderr:
            logger.error(f'Service [{name}] not found.')
        elif 'was not started' in result.stderr:
            logger.error(f'Service [{name}] was not started within {timeout} seconds.')
        return result.ok

    def get_service_file_version(self, name: str) -> str:
        """Get FileVersion from the process"""

        return self.run_ps(f'(Get-Process -Name {name}).FileVersion').stdout

    def get_service_file_version_local(self, name: str) -> str:
        """Get FileVersion from the process"""

        return self.run_ps_local(f'(Get-Process -Name {name}).FileVersion').stdout

    def is_service_running(self, name: str) -> bool:
        """Check local windows service is running"""

        cmd = f'(Get-Service -Name {name}).Status -eq "running"'
        response = self.run_ps(cmd)
        if response.stdout == 'True':
            return True
        return False

    def is_service_running_local(self, name: str) -> bool:
        """Check local windows service is running"""

        cmd = f'(Get-Service -Name {name}).Status -eq "running"'
        response = self.run_ps_local(cmd)
        if response.stdout == 'True':
            return True
        return False

    def is_process_running(self, name: str) -> bool:
        """Verify process is running"""

        cmd = f"""
        $process = Get-Process -Name "{name}" -ErrorAction SilentlyContinue
        if ($process) {{exit 0}}
        exit 1        
        """

        result = self.run_ps(cmd)
        return True if not result.exited else False

    def is_process_running_local(self, name: str) -> bool:
        """Verify process is running"""

        cmd = f"""
        $process = Get-Process -Name "{name}" -ErrorAction SilentlyContinue
        if ($process) {{exit 0}}
        exit 1        
        """

        result = self.run_ps_local(cmd)
        return True if not result.exited else False

    # ------------------ Networking ----------------------
    def get_network_adapter_state(self, name: str) -> str:
        """Get network adapter state in Windows by it's name

        :param name: DATA, SYNC
        :return:
        """

        cmd = f"""
        try
        {{
            (Get-NetAdapter -Name "{name}" -ErrorAction Stop).Status
        }}
        catch
        {{
            Write-Host $_.Exception.Message
        }}
        """

        result = self.run_ps(cmd)
        if 'objects found with property' in result.stdout:
            msg = f'Adapter [{name}] not found. Verify the value of the property and retry'
            self.logger.error(msg)
            raise ValueError(msg)
        return result.stdout

    def get_network_adapter_state_local(self, name: str) -> str:
        """Get network adapter state in Windows by it's name

        :param name: DATA, SYNC
        :return:
        """

        cmd = f"""
        try
        {{
            (Get-NetAdapter -Name "{name}" -ErrorAction Stop).Status
        }}
        catch
        {{
            Write-Host $_.Exception.Message
        }}
        """

        result = self.run_ps_local(cmd)
        if 'objects found with property' in result.stdout:
            msg = f'Adapter [{name}] not found. Verify the value of the property and retry'
            self.logger.error(msg)
            raise ValueError(msg)
        return result.stdout

    def disable_network_adapter(self, name: str) -> bool:
        """Disable network adapter in Windows by it's name

        Log info is adapter already disabled and return

        :param name: DATA, SYNC
        :return:
        """

        cmd = f"""
        $state = Get-NetAdapter | ? {{$_.Name -like "{name}"}} | % {{$_.ifOperStatus}}
        write-host $state

        if ($state){{
            if ($state -eq "Up")
            {{
                Disable-NetAdapter -Name "{name}" -Confirm:$false  | Out-Null
                exit 0
            }}
            else{{exit 10}}
        }}
        else
        {{exit 20}}
        """

        result = self.run_ps(cmd)
        if result.exited == 10:
            self.logger.info(f'Adapter {name} already disabled.')
            return True
        elif result.exited == 20:
            msg = f'Adapter {name} not found.'
            self.logger.error(msg)
            raise ValueError(msg)
        return result.ok

    def disable_network_adapter_local(self, name: str) -> bool:
        """Disable network adapter in Windows by it's name

        Log info is adapter already disabled and return

        :param name: DATA, SYNC
        :return:
        """

        cmd = f"""
        $state = Get-NetAdapter | ? {{$_.Name -like "{name}"}} | % {{$_.ifOperStatus}}
        write-host $state

        if ($state){{
            if ($state -eq "Up")
            {{
                Disable-NetAdapter -Name "{name}" -Confirm:$false  | Out-Null
                exit 0
            }}
            else{{exit 10}}
        }}
        else
        {{exit 20}}
        """

        result = self.run_ps_local(cmd)
        if result.exited == 10:
            self.logger.info(f'Adapter {name} already disabled.')
            return True
        elif result.exited == 20:
            msg = f'Adapter {name} not found.'
            self.logger.error(msg)
            raise ValueError(msg)
        return result.ok

    def enable_network_adapter(self, name: str) -> bool:
        """Enable network adapter in Windows by it's name

        Log info is adapter already disabled and return

        :param name: DATA, SYNC
        :return:
        """

        cmd = f"""
        $state = Get-NetAdapter | ? {{$_.Name -like "{name}"}} | % {{$_.ifOperStatus}}
        write-host $state

        if ($state){{
            if ($state -eq "Down")
            {{
                Enable-NetAdapter -Name "{name}" -Confirm:$false  | Out-Null
                exit 0
            }}
            else{{exit 10}}
        }}
        else
        {{exit 20}}
        """

        result = self.run_ps(cmd)
        if result.exited == 10:
            self.logger.info(f'Adapter {name} already enabled.')
            return True
        elif result.exited == 20:
            msg = f'Adapter {name} not found.'
            self.logger.error(msg)
            raise ValueError(msg)
        return result.ok

    def enable_network_adapter_local(self, name: str) -> bool:
        """Enable network adapter in Windows by it's name

        Log info is adapter already disabled and return

        :param name: DATA, SYNC
        :return:
        """

        cmd = f"""
        $state = Get-NetAdapter | ? {{$_.Name -like "{name}"}} | % {{$_.ifOperStatus}}
        write-host $state

        if ($state){{
            if ($state -eq "Down")
            {{
                Enable-NetAdapter -Name "{name}" -Confirm:$false  | Out-Null
                exit 0
            }}
            else{{exit 10}}
        }}
        else
        {{exit 20}}
        """

        result = self.run_ps_local(cmd)
        if result.exited == 10:
            self.logger.info(f'Adapter {name} already enabled.')
            return True
        elif result.exited == 20:
            msg = f'Adapter {name} not found.'
            self.logger.error(msg)
            raise ValueError(msg)
        return result.ok

    def get_process_working_set_size(self, name: str, dimension: str = None) -> float:
        """Gets the amount of physical memory, allocated for the associated process.

        In bytes by default.

        :param name: Service name
        :param dimension: KB | MB | GB
        :return: float
        """

        cmd = f'(Get-Process -Name {name} | Measure-Object WorkingSet64 -Sum).Sum'
        if dimension is not None:
            cmd += f' / 1{dimension}'

        return float(self.run_ps(cmd).stdout)

    def get_process_working_set_size_local(self, name: str, dimension: str = None) -> float:
        """Gets the amount of physical memory, allocated for the associated process.

        In bytes by default.

        :param name: Service name
        :param dimension: KB | MB | GB
        :return: float
        """

        cmd = f'(Get-Process -Name {name} | Measure-Object WorkingSet64 -Sum).Sum'
        if dimension is not None:
            cmd += f' / 1{dimension}'

        return float(self.run_ps_local(cmd).stdout)

    @staticmethod
    def timestamp_local(sec: bool = False):
        """Get time stamp"""

        if sec:
            return datetime.now().strftime('%Y%m%d_%H%M%S')
        return datetime.now().strftime('%Y%m%d_%H%M')

    def set_date_adjustment(self, date: str) -> str:
        """Set specific date with current hh:mm adjustment on remote server.

        :param date: 30/05/2019
        :return:
        """

        cmd = f'Set-Date -Date ("{date} " + (Get-Date).ToString("HH:mm:ss"))'

        # disable logger nin order not to catch WinRM connection error
        self.logger.disabled = True

        try:
            result = self.run_ps(cmd)
            self.logger.disabled = False
            self.logger.info(f'Date adjusted to {date}.')
            return result.stdout
        except WinRMTransportError as err:
            self.logger.disabled = False
            self.logger.warning(f'Date adjusted to {date}. Remote session was broken after date changing. {err}')
            return self.run_ps('Get-Date').stdout

    def is_disk_offline(self, disk_number: int) -> bool:
        """Is underline disk offline?

        :param disk_number: 1 | 2 | 3
        :return:
        """

        result = self.run_ps(f'(Get-Disk -Number {disk_number}).IsOffline')
        return True if result.stdout == 'True' else False

    def is_disk_offline_local(self, disk_number: int) -> bool:
        """Is underline disk offline?

        :param disk_number: 1 | 2 | 3
        :return:
        """

        result = self.run_ps_local(f'(Get-Disk -Number {disk_number}).IsOffline')
        return True if result.stdout == 'True' else False

    def set_disk_state(self, disk_number: int, enabled: bool) -> bool:
        """Set underline disk state.

        :param enabled: True | False
        :param disk_number: 1 | 2 | 3
        :return: Bool after successful execution.
        """

        cmd = f'Set-Disk -Number {disk_number} -IsOffline ${not enabled}'
        result = self.run_ps(cmd)
        return result.ok

    def set_disk_state_local(self, disk_number: int, enabled: bool) -> bool:
        """Set underline disk state.

        :param enabled: True | False
        :param disk_number: 1 | 2 | 3
        :return: Bool after successful execution.
        """

        cmd = f'Set-Disk -Number {disk_number} -IsOffline ${not enabled}'
        result = self.run_ps_local(cmd)
        return result.ok

    # ---------------- NEED REFACTORING ------------------
    def attach_share(self, share, username, password):
        """Attach network share"""

        command = f'net use {share} /u:{username} {password}'
        return self.run_cmd(command)

    def debug_info(self):
        logger.info('Linux client created')
        logger.info(f'Local host: {self.get_current_os_name_local()}')
        logger.info(f'Remote IP: {self.host}')
        logger.info(f'Username: {self.username}')
        logger.info(f'Password: {self.password}')
        logger.info(f'Available: {self.is_host_available()}')
        logger.info(sys.version)
