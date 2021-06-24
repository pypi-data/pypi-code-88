import os, sys, glob, json, logging, subprocess, paramiko
from dataclasses import dataclass
from typing import Callable, List
import win32api, win32con, win32gui
from mhealth_datasets_upload import config


if not os.path.exists(config.outFold):
    os.mkdir(config.outFold)


logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    filename=os.path.join(config.outFold,'data_upload.log'), filemode='a', level=logging.DEBUG)
logger = logging.getLogger(__name__)


@dataclass
class Drive:
    letter: str
    label: str
    drive_type: str

    @property
    def is_removable(self) -> bool:
        return self.drive_type == 'Removable Disk'

class DeviceListener:
    """
    Listens to Win32 `WM_DEVICECHANGE` messages
    and trigger a callback when a device has been plugged in or out

    See: https://docs.microsoft.com/en-us/windows/win32/devio/wm-devicechange
    """
    WM_DEVICECHANGE_EVENTS = {
        0x0019: ('DBT_CONFIGCHANGECANCELED', 'A request to change the current configuration (dock or undock) has been canceled.'),
        0x0018: ('DBT_CONFIGCHANGED', 'The current configuration has changed, due to a dock or undock.'),
        0x8006: ('DBT_CUSTOMEVENT', 'A custom event has occurred.'),
        0x8000: ('DBT_DEVICEARRIVAL', 'A device or piece of media has been inserted and is now available.'),
        0x8001: ('DBT_DEVICEQUERYREMOVE', 'Permission is requested to remove a device or piece of media. Any application can deny this request and cancel the removal.'),
        0x8002: ('DBT_DEVICEQUERYREMOVEFAILED', 'A request to remove a device or piece of media has been canceled.'),
        0x8004: ('DBT_DEVICEREMOVECOMPLETE', 'A device or piece of media has been removed.'),
        0x8003: ('DBT_DEVICEREMOVEPENDING', 'A device or piece of media is about to be removed. Cannot be denied.'),
        0x8005: ('DBT_DEVICETYPESPECIFIC', 'A device-specific event has occurred.'),
        0x0007: ('DBT_DEVNODES_CHANGED', 'A device has been added to or removed from the system.'),
        0x0017: ('DBT_QUERYCHANGECONFIG', 'Permission is requested to change the current configuration (dock or undock).'),
        0xFFFF: ('DBT_USERDEFINED', 'The meaning of this message is user-defined.'),
    }

    def __init__(self, on_change: Callable[[List[Drive]], None]):
        self.on_change = on_change

    def _create_window(self):
        """
        Create a window for listening to messages
        https://docs.microsoft.com/en-us/windows/win32/learnwin32/creating-a-window#creating-the-window

        See also: https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-createwindoww

        :return: window hwnd
        """
        wc = win32gui.WNDCLASS()
        wc.lpfnWndProc = self._on_message
        wc.lpszClassName = self.__class__.__name__
        wc.hInstance = win32api.GetModuleHandle(None)
        class_atom = win32gui.RegisterClass(wc)
        return win32gui.CreateWindow(class_atom, self.__class__.__name__, 0, 0, 0, 0, 0, 0, 0, wc.hInstance, None)

    def start(self):
        logger.info('Listening to drive changes')
        hwnd = self._create_window()
        # logger.debug('Created listener window with hwnd={hwnd:x}' + )
        logger.debug('Listening to messages')
        win32gui.PumpMessages()

    def _on_message(self, hwnd: int, msg: int, wparam: int, lparam: int):
        if msg != win32con.WM_DEVICECHANGE:
            return 0
        event, description = self.WM_DEVICECHANGE_EVENTS[wparam]
        # logger.debug('Received message: {event} = {description}', (event,description))
        if event in ('DBT_DEVICEREMOVECOMPLETE'):
            logger.info('A device has been plugged out')
            # self.on_change(self.list_drives())
        if event in ('DBT_DEVICEARRIVAL'):
            logger.info('A device has been plugged in')
            self.on_change(self.list_drives())

        return 0

    @staticmethod
    def list_drives() -> List[Drive]:
        """
        Get a list of drives using WMI
        :return: list of drives
        """
        proc = subprocess.run(
            args=[
                'powershell',
                '-noprofile',
                '-command',
                'Get-WmiObject -Class Win32_LogicalDisk | Select-Object deviceid,volumename,drivetype | ConvertTo-Json'
            ],
            text=True,
            stdout=subprocess.PIPE
        )
        if proc.returncode != 0 or not proc.stdout.strip():
            logger.error('Failed to enumerate drives')
            return []
        devices = json.loads(proc.stdout)

        drive_types = {
            0: 'Unknown',
            1: 'No Root Directory',
            2: 'Removable Disk',
            3: 'Local Disk',
            4: 'Network Drive',
            5: 'Compact Disc',
            6: 'RAM Disk',
        }
        return [Drive(letter=d['deviceid'],label=d['volumename'],drive_type=drive_types[d['drivetype']]) for d in devices]


def on_devices_changed(drives: List[Drive]):
    removable_drives = [d for d in drives if d.letter in device_id]
    if removable_drives:
        drive = removable_drives[0]
        logger.info(drive)
        backup(drive)


def backup(drive: Drive):
    logger.info('Backup drive has been plugged in')
    logger.info('Backing up ' + drive.letter)
    folder = config.dataFold
    driveName = drive.letter

    inFolder = driveName + "/" + folder
    ## list all files in the input folder
    try:
        inFileLis = glob.glob(os.path.join(inFolder,'*.mp4'))
    except FileNotFoundError:
        logger.error(inFolder + " does not exist")
        return
    except:
        logger.error("Other error")
        return


    if(not inFileLis):
        logger.error("No files present in the folder " + inFolder)
        return


    ## server and authentication related variables
    host = config.host
    port = config.port
    username = config.username
    keyfile_path = config.keyfile_path
    password = config.password

    ## check if the server is accessible
    sftpclient = create_sftp_client(host, port, username, password, keyfile_path, 'DSA')

    if not sftpclient:
        logger.error("Error connecting with the server")
        return
    else:
        logger.info("Connected to the server")

    project_name = config.project_name

    sftpclient.chdir(project_name)

    dirlist = sftpclient.listdir(project_name)
    participant_folder_created = False
    if (participant not in dirlist):
        sftpclient.mkdir(participant)
        participant_folder_created = True

    sftpclient.chdir(participant)
    # upload all the files in the external drive one at a time
    fileLis = sftpclient.listdir('.')


    for inFile in inFileLis:
        fileName = os.path.basename(inFile)
        logger.info("Working on " + fileName)
        if not participant_folder_created:
            if fileName not in fileLis:
                logger.info(inFile + ' not present in server. Uploading...')
                try:
                    sftpclient.put(inFile, fileName, callback=uploading_info, confirm=True)
                except Exception as e:
                    logger.info(inFile + ' not uploaded completely.')
                    return
                else:
                    logger.info(inFile + ' uploaded successfully.')

            else:
                logger.info(inFile + ' already present in server. Checking if the file sizes match...')
                this_filesize_bytes = os.stat(inFile).st_size
                ref_filesize_bytes = paramiko.SFTPClient.lstat(sftpclient,fileName).st_size
                if(this_filesize_bytes > ref_filesize_bytes):
                    logger.info("Previously uploaded file is smaller in size than the original file: " +
                                str(ref_filesize_bytes) + " vs. " + str(this_filesize_bytes))
                    logger.info("Deleting file in server, and uploading again..")
                    ## delete file in server
                    try:
                        paramiko.SFTPClient.remove(sftpclient,fileName)
                    except Exception as e:
                        logger.info("Issue removing the file in the server.")
                        logger.info("Not attempting upload of " + inFile)
                        continue
                    else:
                        logger.info("Removed the incomplete file " + fileName + " Proceeding to upload...")
                    ## upload again
                    try:
                        sftpclient.put(inFile, fileName, callback=uploading_info, confirm=True)
                    except Exception as e:
                        logger.info(inFile + ' not uploaded completely.')
                        return
                    else:
                        logger.info(inFile + ' uploaded successfully.')
                else:
                    logger.info("File sizes match. So, not uploading " + inFile)

        else:
            logger.info('uploading file ' + inFile)
            try:
                sftpclient.put(inFile, fileName, callback=uploading_info, confirm=True)
            except Exception as e:
                logger.info(inFile + ' not uploaded completely.')
                return
            else:
                logger.info(inFile + ' uploaded successfully.')


    sftpclient.close()
    logger.info('Done uploading files to the server.')


def uploading_info(uploaded_file_size, total_file_size):
    logger.info('uploaded_file_size : {} total_file_size : {}'.format(uploaded_file_size, total_file_size))

def create_sftp_client(host, port, username, password, keyfilepath, keyfiletype):
    """
    create_sftp_client(host, port, username, password, keyfilepath, keyfiletype) -> SFTPClient

    Creates a SFTP client connected to the supplied host on the supplied port authenticating as the user with
    supplied username and supplied password or with the private key in a file with the supplied path.
    If a private key is used for authentication, the type of the keyfile needs to be specified as DSA or RSA.
    :rtype: SFTPClient object.
    """
    sftp = None
    key = None
    transport = None
    try:
        if keyfilepath is not None:
            # Get private key used to authenticate user.
            if keyfiletype == 'DSA':
                # The private key is a DSA type key.
                key = paramiko.DSSKey.from_private_key_file(keyfilepath)
            else:
                # The private key is a RSA type key.
                key = paramiko.RSAKey.from_private_key(keyfilepath)

        # Create Transport object using supplied method of authentication.
        transport = paramiko.Transport((host, port))
        transport.connect(None, username, password, key)

        sftp = paramiko.SFTPClient.from_transport(transport)

        return sftp
    except Exception as e:
        logger.error('An error occurred creating SFTP client: %s: %s' % (e.__class__, e))
        if sftp is not None:
            sftp.close()
        if transport is not None:
            transport.close()
        pass

def main(device=None,pid=None):
    global device_id, participant

    device_id = device
    participant = pid

    if(device_id is None):
        logger.error("Missing device identifier.")
        return
    if(participant is None):
        logger.error("Missing particpant identigier.")
        return

    listener = DeviceListener(on_change=on_devices_changed)
    listener.start()
