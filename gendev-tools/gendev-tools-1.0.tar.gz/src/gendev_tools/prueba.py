import yaml
from gendev_tools.nat_mch.nat_mch import NATMCH, BackplaneType
from gendev_tools.gendev_interface import ConnType
from collections import OrderedDict


def represent_dictionary_order(self, dict_data):
    return self.represent_mapping("tag:yaml.org,2002:map", dict_data.items())


def setup_yaml():
    yaml.add_representer(OrderedDict, represent_dictionary_order)


setup_yaml()

mch = NATMCH(
    ip_address="172.30.5.238",
    allowed_conn=[ConnType.ETHER, ConnType.TELNET, ConnType.MOXA],
    backplane=BackplaneType.B3U,
    conn_ip_address="173.30.5.102",
)

_, info = mch.device_info()

_, basecfg = mch.get_configuration("basecfg")
_, pciecfg = mch.get_configuration("pcie")
# backplane = dev.get_configuration("backplane")
cfg = OrderedDict(**info, **basecfg, **pciecfg)


# with open('mch_113522-1426.yaml', 'w') as configfile:    # save
#     yaml.dump(cfg, configfile)

with open("mch_test.yaml", "r") as configfile:  # save
    config = yaml.safe_load(configfile)

valid, message = mch.check_configuration("backplane", config)
if valid:
    print("Backplane configuration ok")
else:
    print(message)
