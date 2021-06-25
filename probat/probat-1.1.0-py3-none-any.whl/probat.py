from subprocess import call
from time import time
from os import remove
from pathlib import PosixPath

from .dict_conf import DictConfig

from termcolor import colored

# TODO args (quiet and verbose and more)


SYS_POWER_BASE_PATH = PosixPath('/sys/class/power_supply')

config_defaults = {  # Li-poli
    'full_lvl': 96,
    'full_pad_time': 600,  # In seconds
    'almost_charge_lvl': 20,
    'please_charge_lvl': 15,
}


def _read_int(path: PosixPath) -> int:
    return int(path.read_text().strip())


def main() -> int:
    config = DictConfig('~/.config/probat.conf', config_defaults)

    # Check env
    # TODO Get list of all batteries?
    # bat_ids = []

    # get status
    adp_path = SYS_POWER_BASE_PATH / 'ADP0'
    adp_online = bool(_read_int(adp_path / 'online'))

    # TODO if len(bat_ids) == 1 ...
    bat_id = 0
    sys_path = SYS_POWER_BASE_PATH / f'BAT{bat_id}'

    # # Is battery charging
    # is_charging = 'Charging' == (
    #     sys_path / 'status').read_text().strip()

    # lvl (percentage)
    full = _read_int(sys_path / 'energy_full')
    full_design = _read_int(sys_path / 'energy_full_design')
    now = _read_int(sys_path / 'energy_now')
    lvl = round(now / full * 100, 1)
    lvl_design = round(now / full_design * 100, 1)
    capacity = round(full / full_design * 100, 1)

    # process status and notice
    probat_ts = PosixPath.home().joinpath('.config', 'probat.ts')
    notice = None
    if adp_online:
        if lvl >= config['full_lvl']:
            if not probat_ts.exists():
                probat_ts.write_text(str(time()))
            else:
                time_delta = (time() - float(probat_ts.read_text().strip()))
                notice = f'Fully charged for: {round(time_delta / 60, 1)} minutes'
                if time_delta > config['full_pad_time']:
                    notice += '\n    Stop charging NOW to avoid battery wear!'
    else:
        if lvl < config['full_lvl']:
            if probat_ts.exists():
                remove(probat_ts)

        if lvl < config['almost_charge_lvl']:
            notice = 'Connect charger soon!'
        elif lvl < config['please_charge_lvl']:
            notice = 'Connect charger NOW ffs!'

    status = (
        colored("Discharging", "red"),
        colored("Charging", "green"))[adp_online]
    print(colored('[*]', 'cyan'),
          f'{bat_id}: {status} - {lvl}% (Design: {lvl_design}%/{capacity}%)')
    if notice:
        print(colored('[Notice]', 'yellow'), notice)
        call(['notify-send', '--urgency=critical',
              '--icon=battery-charged', notice])
