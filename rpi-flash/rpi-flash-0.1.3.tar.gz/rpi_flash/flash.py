#!/usr/bin/env python

"""Flash image to drive. Only flashes changed blocks to minimise writes."""

# pyright: reportUnusedVariable = false

import logging
import os
import sys
from functools import wraps
from gzip import GzipFile
from io import BufferedReader
from os import listdir, makedirs
from subprocess import run
from time import sleep
from typing import ForwardRef, List

import humanize
import requests
import typer
from pydantic import BaseModel, BaseSettings, Field

log = logging.getLogger(__name__)
logging.basicConfig(level='INFO')

BLOCK_SIZE = 64 * 1024

class Disk(BaseModel):
    name: str
    size: str
    path: str

def platform_specific(f):
    try:
        platform_f = globals()[f'_{f.__name__}_{sys.platform}']
    except KeyError:
        raise NotImplementedError(f'Support for {sys.platform} hasn\'t been implemented yet')
    @wraps(f)
    def wrap(*args, **kwargs):
        return platform_f(*args, **kwargs)
    return wrap

def _get_removable_drives_darwin(): # type: ignore
    class Media(BaseModel):
        name: str = Field(..., alias='_name')
        bsd_name: str
        removable_media: bool
        size: str
    
    class Device(BaseModel):
        items: List[ForwardRef('Device')] = Field([], alias='_items')
        media: List[Media] = Field([], alias='Media')
    Device.update_forward_refs()
    
    class Profile(BaseModel):
        sp_usb_data_type: List[Device] = Field([], alias='SPUSBDataType')
        
    result = run(['system_profiler', '-json', 'SPUSBDataType'], capture_output=True)
    profile = Profile.parse_raw(result.stdout)
    devices = profile.sp_usb_data_type
    for dev in devices:
        if dev.media:
            for medium in dev.media:
                if medium.removable_media:
                    yield Disk(name=medium.name, size=medium.size, path=f'/dev/r{medium.bsd_name}')
        devices.extend(dev.items)

@platform_specific
def get_removable_drives():
    pass

def _umount_darwin(dev):  # type: ignore
    run(['diskutil', 'unmountDisk', f'{dev}'])

@platform_specific
def umount(dev):  # type: ignore
    pass

def try_close(f):
    try:
        f.close()
    except:
        pass

def strip(doc: str):
    return '\n'.join([ l.strip() for l in doc.split('\n') ])

CONFIG_FLAG = '.configure_me'

WPA_SUPPLICANT = """\
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country={country}

network={{
ssid="{ssid}"
psk="{pw}"
}}
"""

class Config(BaseSettings):

    ssh_key: str = Field(None, description=strip("""\
        If set, RPi will have this SSH public key loaded and SSH enabled."""))

    ssh_ca_key: str = Field(None, description=strip("""\
        If set, RPi's SSH host key will be signed with this CA key. Not kept.
        You probably shouldn't save this secret here. Maybe pass as an env var instead.
        (not implemented yet)"""))

    wifi_country: str = 'NZ'

    wifi_ssid: str = Field(None, description=strip("""\
        If set, RPi will be configured to use this WiFi after configuration (i.e. to download the final image)"""))

    wifi_password: str = Field(None, description=strip("""\
        See WIFI_SSID.
        You probably shouldn't save this secret here. Maybe pass as an env var instead."""))

    class Config:
        env_prefix = 'RPI_'
        env_file = '.env'    

    def get_mounts(self):
        # macos
        try:
            return [ f'/Volumes/{d}' for d in listdir('/Volumes') ]
        except FileNotFoundError:
            pass
        # linux
        try:
            with open('/proc/mounts') as f:
                return [ m.split()[1] for m in f.readlines() ]
        except FileNotFoundError:
            pass
        raise Exception("Couldn't list mounts. Maybe you're on Windows (not implemented)")
        
    def find_data_mount(self):
        for mount in self.get_mounts():
            flag_file = os.path.join(mount, CONFIG_FLAG)
            try:
                with open(flag_file, 'r') as _:
                    pass
            except:
                continue
            return mount
        raise Exception("Couldn't find the flashed drive. Maybe it's already configured")

    def make_supplicant(self, country, ssid, pw):
        return WPA_SUPPLICANT.format(
            country=country,
            ssid=ssid,
            pw=pw
        )

    def configure(self):
        data_mount = self.find_data_mount()
        def make_data_dir(name):
            dir = os.path.join(data_mount, name)
            makedirs(dir, exist_ok=True)
            return dir

        # SSH
        if vars.ssh_key:
            log.info('Configuring ssh')
            ssh_dir = make_data_dir('ssh')
            with open(os.path.join(ssh_dir, 'authorized_keys'), 'w') as f:
                f.write(vars.ssh_key + '\n')

        # WiFi
        if vars.wifi_ssid:
            log.info('Configuring wifi')
            wifi_dir = make_data_dir('wifi')
            with open(os.path.join(wifi_dir, 'wpa_supplicant.conf'), 'w') as f:
                f.write(self.make_supplicant(vars.wifi_country, vars.wifi_ssid, vars.wifi_password))

        flag_file = os.path.join(data_mount, CONFIG_FLAG)
        os.remove(flag_file)

        log.info('Configuration completed')


    @staticmethod
    def write_env():
        properties = Config.schema()['properties']
        vars = Config(final_image='<url_to_image>')

        with open('.env', 'w') as f:
            f.write(strip("""\
                # Fill these in then run ./config.py
                # You can also set any of these as environment variables instead.
                
                """))
            for var_name, var in properties.items():
                if 'description' in var:
                    desc = var['description']
                    f.write('\n'.join([ f'# {l}' for l in desc.split('\n') ]))
                    f.write('\n')
                f.write(f'{next(iter(var["env_names"])).upper()}={getattr(vars, var_name) or ""}')
                f.write('\n\n')


def flash_disk(source: str, destination, always_write):
    """Yields tuple of positions of input,scanned,written exactly 1000 times"""

    CHUNK_SIZE = 64 * 1024
    YIELD_COUNT = 1000

    umount(destination)

    http_resp = None
    buffered_f = None
    dest_reader = None
    dest_writer = None
    try:
        if source.startswith('http:') or source.startswith('https:'):
            http_resp = requests.get(source, stream=True)
            http_resp.raise_for_status()
            source_length = http_resp.headers.get('content-length', 0)
            buffered_f = BufferedReader(http_resp.raw)
        else:
            source_length = os.path.getsize(source)
            buffered_f = BufferedReader(open(source, 'rb'))
        
        # Gzip?
        header = buffered_f.peek(2)
        if header.startswith(b'\x1f\x8b'):
            source_f = GzipFile(fileobj=buffered_f)
        else:
            source_f = buffered_f

        dest_writer = open(destination, 'ab')

        try:
            dest_reader = open(destination, 'rb')
        except FileNotFoundError:
            pass

        scanned = 0
        written = 0
        yield_count = 0
        dest_eof = always_write or dest_reader is None
        dest_writer.seek(0)
        while True:
            chunk = source_f.read(CHUNK_SIZE)
            if not chunk:
                break
            length = len(chunk)
            if not dest_eof:
                existing_chunk = dest_reader.read(length)
                if not existing_chunk:
                    dest_eof = True
            if not dest_eof and chunk == existing_chunk:
                dest_writer.seek(length, 1)
            else:
                dest_writer.write(chunk)
                written += length
            scanned += length
            yield_now = int((buffered_f.tell() / source_length) * YIELD_COUNT)
            for _ in range(yield_count, yield_now):
                yield scanned, written
            yield_count = yield_now
        dest_writer.flush()
        os.fsync(dest_writer.fileno())
    finally:
        try_close(source_f)
        try_close(http_resp)
        try_close(buffered_f)
        try_close(dest_reader)
        try_close(dest_writer)

def main(
    source: str, 
    destination: str = typer.Argument(None), 
    flash: bool = typer.Option(True, help='Turn on or off flashing, for example if you want to configure only.'),
    configure: bool = typer.Option(True, help='Turn on or off configuring, for example if you want to flash only.'),
    extra_config_file: str = typer.Option('config.py'),
    yes: bool = typer.Option(False, is_flag=True),
    always_write: bool = typer.Option(False, is_flag=True),
    write_env: bool = typer.Option(False, help='If set, write config .env then exit.')
):
    if write_env:
        Config.write_env()
        return

    if extra_config_file:
        try:
            with open(extra_config_file, 'r') as f:
                if yes or typer.confirm(f'Load extra config file "{extra_config_file}"? Only proceed if you trust this file.'):
                    exec(f.read())
        except FileNotFoundError:
            pass

    if flash:
        if destination:
            if not (yes or typer.confirm(f'Flash to {destination}?')):
                destination = None
        else:
            waiting_message = False
            removable_drives = []
            while not removable_drives:
                removable_drives = list(get_removable_drives())
                if not removable_drives:
                    if yes:
                        typer.echo('No removable drives were found.')
                        return
                    else:
                        if not waiting_message:
                            typer.echo('Please connect the drive to flash.')
                            waiting_message = True
                        sleep(1)

            for n, dev in enumerate(removable_drives):
                prompt = f'Flash to {dev.path} ({dev.name}, {dev.size})?'
                if n < len(removable_drives) - 1:
                    prompt += ' Choose n for the next drive.'
                if yes or typer.confirm(prompt):
                    destination = dev.path
                    break
        
            if not destination:
                typer.echo('Nothing to do')
                return

        try:
            flash_iter = flash_disk(source, destination, always_write)
            scanned = 0
            written = 0
            show_func = lambda _: f'{humanize.naturalsize(written)} written' + ('' if always_write else f' / {humanize.naturalsize(scanned)} scanned')
            with typer.progressbar(flash_iter, length=1000, label='Flashing', show_eta=True, item_show_func=show_func) as progress:
                for prog in progress:
                    scanned, written = prog
        except PermissionError as err:
            typer.echo(err)
            typer.echo('Perhaps you should re-run with sudo.')
            return

    typer.echo('Done')
