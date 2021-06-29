from datetime import datetime
import logging
from time import sleep
from serial import SerialException
import re
import os
import string

from .serialib import SerialComm
from .ziva import Ziva

logger = logging.getLogger(__name__)


class SmMonitor(Ziva):
    sm_date = '%d/%m/%Y %H:%M:%S'
    sm_chunk = r'([^=,:\x00]*)'
    sm_pattern = re.compile(r'(?:\s|\x00)*((?:\d|[a-fA-F]){4}):' + sm_chunk + '=' + sm_chunk + ',' + sm_chunk)
    timestamp_format = '%Y-%m-%d %H:%M:%S'

    def __init__(self):
        super().__init__()
        self.running = False
        self.directory = None
        self.data = []
        self.stop_process = False

    def write_dtv(self, device: str, channel: str, value: float, timestamp: datetime, unit: str) -> str:
        """Write data to txt file
        :return: Filepath
        """
        # Create dir d/m/y if it does not exists
        dir_path = os.path.join(self.directory, datetime.strftime(datetime.now(), '%d%m%Y'))
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

        # create output filepath
        # Remove all hex characters and invalid chars from filename
        filename = f'{device}_{datetime.strftime(datetime.now(), "%d%m%Y")}_{channel.strip()}.txt'
        invalid_chars = '<>:"/\|?*'
        valid_characters = string.printable
        filename = ''.join(i for i in filename if i in valid_characters)
        for char in invalid_chars:
            filename = filename.replace(char, '')
        filepath = os.path.join(dir_path, filename.strip())

        write_data = []
        if not os.path.exists(filepath):
            write_data.append(f'\n\n{unit}\n\n\n\n\n\n\n')

        write_data.append(f'{datetime.strftime(timestamp, "%d/%m/%Y %H:%M:%S")},{value}\n')
        with open(filepath, 'a+') as f:
            f.writelines(write_data)
        logger.debug(f'Data saved to {filepath}: {write_data}')

        return filepath

    def test_router(self):
        """Raise Exception if the router is set to invalid mode (as transmit/receive)"""

        try:
            # If this passes without exceptions it means that the router is in invalid mode
            self.recv_address = 1
            self.ping_router()
            raise ValueError
        except ValueError:
            raise Exception('USB router is not configured properly')
        except Exception as e:
            pass

    def start(self):
        if self.running:
            raise Exception('Already running')

        if not self.directory:
            raise Exception('Directory is not set')

        logger.info('Sm monitor started')

        self.stop_process = False
        self.running = True

        while True:
            if self.stop_process:
                self.running = False
                break

            line = None
            try:
                line = self.readline().strip()
            except (SerialException, AttributeError) as e:
                logger.error(e)
                while True:
                    if self.stop_process:
                        self.running = False
                        break
                    try:
                        self.open()
                        break
                    except SerialException:
                        sleep(2)
            if not line:
                continue
            logger.debug(f"Received: {line}")
            hits = self.sm_pattern.fullmatch(line.decode('latin1'))
            if hits:
                try:
                    device = str(int(hits.group(1), 16))
                    channel = hits.group(2)
                    value = float(hits.group(3))
                    unit = hits.group(4)
                    timestamp = datetime.now().replace(microsecond=0)
                    data = {'device': device, 'channel': channel, 'value': value, 'timestamp': str(timestamp),
                            'unit': unit}
                    filepath = self.write_dtv(device=device, channel=channel,
                                              value=value, timestamp=timestamp, unit=unit)
                    data['filepath'] = filepath
                    for i, item in enumerate(self.data):
                        if item['device'] == device and item['channel'] == channel:
                            self.data[i] = data
                            break
                    else:
                        self.data.append(data)

                except Exception as e:
                    logger.exception(e)
            else:
                logger.warning(f'Invalid data: {line}')

    def stop(self):
        if not self.running:
            raise Exception('Not running')
        self.stop_process = True
        if self.ser is not None:
            self.close_port()
        logger.info('Sm monitor stopped')
