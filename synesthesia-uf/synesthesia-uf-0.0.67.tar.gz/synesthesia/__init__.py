import glob, os, shutil, os, sys, subprocess, asyncio
sys.path.append("synesthesia")

def package_installation():
    apt = "sudo apt "
    ins = "install "
    packages = "clementine ffmpeg gstreamer1.0-plugins-base dkms gstreamer1.0-plugins-ugly libqt5x11extras5 libcairo2-dev pkg-config"

    print("[+] Installation of the ubuntu packages is starting:")

    for items in packages.split():
        command = str(apt) + str(ins) + str(items)

        subprocess.run(command.split())
        print("\t[+] Package [{}] Installed".format(str(items)))


package_installation()

from synesthesia.gui import *
from synesthesia.wsl import *
from synesthesia import *