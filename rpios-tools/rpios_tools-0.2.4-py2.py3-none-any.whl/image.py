import argparse
import sys
from typing import List

import psutil
# sudo dd if=$IMAGE of=$SD_CARD_DEV bs=4m conv=sync

def find_sdcards() -> List[str]:
    disk_partitions = psutil.disk_partitions()
    print('\n'.join(str(x) for x in disk_partitions))





def main():
    p = argparse.ArgumentParser()
    args = p.parse_args()

    find_sdcards()



if __name__ == '__main__':
    main()