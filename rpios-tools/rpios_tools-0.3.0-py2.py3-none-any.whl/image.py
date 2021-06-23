import argparse
import sys
from typing import List

import psutil
# sudo dd if=$IMAGE of=$SD_CARD_DEV bs=4m conv=sync

def find_sdcards() -> List[str]:
    disk_partitions = psutil.disk_partitions()
    print('\n'.join(str(x) for x in disk_partitions))


def create_image_build_docker(image_dir: str, version: str, release: str):




def build_custom_image(raspios_image_dir: str, version: str, release: str, wifi_ssid: str, wifi_pw: str, static_ip: str):
    img = create_image_build_docker(raspios_image_dir, version, release)


def main():
    p = argparse.ArgumentParser()
    args = p.parse_args()

    find_sdcards()



if __name__ == '__main__':
    main()