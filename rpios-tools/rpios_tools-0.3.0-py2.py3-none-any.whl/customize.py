import argparse
import sys
import subprocess
from typing import List
import os
import shutil
import tempfile
import uuid

from .download import get_download_path
from .utils import run

SECTOR_SIZE = 512
# sudo dd if=$IMAGE of=$SD_CARD_DEV bs=4m conv=sync

# sudo losetup -o 272629760 /dev/loop
# sudo losetup -o 272629760 /dev/loop8 2021-05-07-raspios-buster-armhf-lite.img
# 


def mount_raspios_image(image_path: str, mount_target: str, offset: int) -> str:
    device = f'/dev/loop{str(uuid.uuid4())[:4]}'
    run(
        'losetup', '-o', str(offset), device, image_path
    )
    run(
        'mount', device, mount_target
    )
    return device


def unmount_raspios_image(device: str, mount_target: str):
    run(
        'umount', mount_target
    )
    run(
        'losetup', '-d', device
    )

def get_partition_offset(device_size_str: str) -> int:
    print(device_size_str.split(' ')[-1])
    return int(device_size_str.split(' ')[-1]) * SECTOR_SIZE


def prepare_workspace(workspace_dir, image_path):
    temp_img_path = os.path.join(workspace_dir, os.path.basename(image_path))
    boot_partition_mount_dir = os.path.join(workspace_dir, 'boot')
    filesystem_partition_mount_dir = os.path.join(workspace_dir, 'filesystem')
    os.makedirs(boot_partition_mount_dir)
    os.makedirs(filesystem_partition_mount_dir)
    shutil.copyfile(image_path, temp_img_path)
    return temp_img_path, boot_partition_mount_dir, filesystem_partition_mount_dir


def mount_raspios(img_path, boot_partition_mount_dir, filesystem_partition_mount_dir):
    stdout, stderr, returncode = run(
        'fdisk', '-l', '-o', 'Device,Start', img_path
    )
    devices_str = stdout.decode('ascii').split('\n')
    devices_str = [ds for ds in devices_str if os.path.basename(img_path) in ds and not ds.startswith('Disk')]
    assert len(devices_str) == 2, f"Expected there to be only two devices instead found {devices_str}"
    print(devices_str)
    boot_device = mount_raspios_image(img_path, boot_partition_mount_dir, get_partition_offset(devices_str[0]))
    filesystem_device = mount_raspios_image(img_path, filesystem_partition_mount_dir, get_partition_offset(devices_str[1]))
    return boot_device, filesystem_device


def customize_raspios_image(image_path: str, output_path: str):
    with tempfile.TemporaryDirectory() as tmpdir:
        print('preparing workspace...')
        img_path, boot_partition_mount_dir, filesystem_partition_mount_dir = prepare_workspace(tmpdir, image_path)
        # get the partition start offset for boot and filesystem
        print('mounting image partitions...')
        boot_device, filesystem_device = mount_raspios(img_path, boot_partition_mount_dir, filesystem_partition_mount_dir)

        print('customizing raspberry pi os image...')
        run('touch', os.path.join(boot_partition_mount_dir, 'SSH'))
        print('syncing filesystem')
        run('sync')
        print('unmounting partitions....')
        unmount_raspios_image(boot_device, boot_partition_mount_dir)
        unmount_raspios_image(filesystem_device, filesystem_partition_mount_dir)
        shutil.copyfile(img_path, output_path)



def main():
    p = argparse.ArgumentParser()
    p.add_argument('version', type=str, help='raspios version')
    p.add_argument('release', type=str, help='raspios release')
    p.add_argument('output_path', type=str, help='path to save the customized image to')
    p.add_argument('--raspios-image-cache-dir', type=str, help='path to image directory')
    args = p.parse_args()
    image_path = get_download_path(args.raspios_image_cache_dir, args.version, args.release)

    customize_raspios_image(image_path, args.output_path)



if __name__ == '__main__':
    main()