"""
@File    :   __init__.py
@Path    :   agrothon_client/
@Time    :   2021/05/28
@Author  :   Chandra Kiran Viswanath Balusu
@Version :   1.0.7
@Contact :   init Module for Agrothon
"""
__VERSION__ = "1.0.7"
import argparse
import logging
from logging.handlers import RotatingFileHandler
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s [%(filename)s:%(lineno)d]",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler("Agrothon-Client.txt", maxBytes=50000000, backupCount=10),
        logging.StreamHandler(),
    ],
)
LOGGER = logging.getLogger(__name__)

parser = argparse.ArgumentParser()
parser.add_argument("-y", "--hostname", help="API Server host name", required=True)
parser.add_argument("-a", "--apikey", help="API Key of host", required=True)
parser.add_argument("-u", "--usb", help="USB Port of Arduino", type=str, default="/dev/ttyUSB0")
parser.add_argument("-p1", "--pir1", help="GPIO Pin of PIR1", type=int, default=25)
parser.add_argument("-p2", "--pir2", help="GPIO Pin of PIR2", type=int, default=8)
parser.add_argument("-p3", "--pir3", help="GPIO Pin of PIR3", type=int, default=7)
parser.add_argument("-p4", "--pir4", help="GPIO Pin of PIR4", type=int, default=1)
parser.add_argument("-br", "--baudrate", help="Baud rate of USB Port to read sensor data", type=int, default=9600)
parser.add_argument("-r", "--relay", help="Relay Signalling GPIO pin", type=int, default=12)
args = parser.parse_args()

LOGGER.info("Parsed args")
PIR1_GPIO = args.pir1
PIR2_GPIO = args.pir2
PIR3_GPIO = args.pir3
PIR4_GPIO = args.pir4

RELAY_GPIO = args.relay

USB_BAUD_RATE = args.baudrate
USB_PORT = args.usb
SERVER_API_KEY = args.apikey
HOST = args.hostname
if not HOST.endswith("/"):
    HOST = HOST + "/"