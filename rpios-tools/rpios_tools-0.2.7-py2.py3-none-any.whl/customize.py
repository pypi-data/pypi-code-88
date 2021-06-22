import argparse
import sys
import subprocess
from typing import List
import os
import shutil
import tempfile
import uuid

from .download import get_download_path

SECTOR_SIZE = 512
# sudo dd if=$IMAGE of=$SD_CARD_DEV bs=4m conv=sync

# sudo losetup -o 272629760 /dev/loop
# sudo losetup -o 272629760 /dev/loop8 2021-05-07-raspios-buster-armhf-lite.img
# 

def run(*args, capture_output: bool = True):
    p = subprocess.run(args, capture_output=capture_output)
    if capture_output:
        return (p.stdout, p.stderr)
    else:
        return (None, None)

def mount_raspios_image(image_path: str, mount_target: str, offset: int) -> str:
    device = f'/dev/loop{uuid.uuid4()[:4]}'
    run(
        'losetup', '-o', offset, device, image_path
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
    return int(' '.split(device_size_str)[-1]) * SECTOR_SIZE


def prepare_workspace(workspace_dir, image_path):
    temp_img_path = os.path.join(workspace_dir, os.path.basename(image_path))
    boot_partition_mount_dir = os.path.join(workspace_dir, 'boot')
    filesystem_partition_mount_dir = os.path.join(workspace_dir, 'filesystem')
    os.makedirs(boot_partition_mount_dir)
    os.makedirs(filesystem_partition_mount_dir)
    shutil.copyfile(image_path, temp_img_path)
    return temp_img_path, boot_partition_mount_dir, filesystem_partition_mount_dir


def mount_raspios(img_path, boot_partition_mount_dir, filesystem_partition_mount_dir):
    stdout, stderr = run([
        'fdisk', '-l', '-o', 'Device,Start', img_path
    ])
    devices_str = stdout.split('\n')
    devices_str = [ds for ds in devices_str if os.path.basename(image_path) in ds]
    assert len(devices_str) == 2, f"Expected there to be only two devices instead found {devices_str}"
    boot_device = mount_raspios_image(img_path, boot_partition_mount_dir, get_partition_offset(devices_str[0]))
    filesystem_device = mount_raspios_image(img_path, filesystem_partition_mount_dir, get_partition_offset(devices_str[1]))
    return boot_device, filesystem_device


def customize_raspios_image(image_path: str, output_path: str):
    with tempfile.TemporaryDirectory() as tmpdir:
        img_path, boot_partition_mount_dir, filesystem_partition_mount_dir = prepare_workspace(tmpdir, image_path)
        # get the partition start offset for boot and filesystem
        boot_device, filesystem_device = mount_raspios(img_path, boot_partition_mount_dir, filesystem_partition_mount_dir)

        run('touch', os.path.join(boot_partition_mount_dir, 'SSH'))

        run('sync')
        unmount_raspios_image(boot_device)
        unmount_raspios_image(filesystem_device)



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