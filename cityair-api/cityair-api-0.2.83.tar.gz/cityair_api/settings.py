import re

TOKEN_VAR_NAME = 'CITYAIR_TOKEN'

DEFAULT_HOST = "https://my.cityair.io/harvester/v1"
DEVICES_URL = "DevicesApi2/GetDevices"
DEVICES_PACKETS_URL = "DevicesApi2/GetPackets"
STATIONS_URL = "MoApi2/GetMoItems"
STATIONS_PACKETS_URL = "MoApi2/GetMoPackets"
FATHER_RE = re.compile(r"(EK|CA|ROOFTOP|LAB|KTH)\w+")
