from setuptools import setup, find_packages
import codecs
import os


VERSION = '0.0.68'
DESCRIPTION = 'A Python audio image creation tool'
LONG_DESCRIPTION = 'A Python audio image creation tool that takes audio and creates images from them.'



# Setting up
setup(
    name="synesthesia-uf",
    version=VERSION,
    author="Super Fun Adventure Club Dude Man Squad",
    author_email="<georgekolasa@ufl.edu",
    description=DESCRIPTION,
    packages=find_packages(),
    package_data={'synesthesia': ['images/*.png', 'images/*.svg' ]},
    url="https://github.com/cbaddeley/Synesthesia",
    license="GPL 3",
    install_requires=['PyQt5', 'librosa', 'essentia',
                      'pillow', 'pycairo', 'musicnn'],
    keywords=['audio', 'visualizer', "image"],

    entry_points =
    {   "console_scripts":
        [
            "syne = synesthesia:pip_main_func"
        ]
    }

)

import os, sys, subprocess

def apt_installation():
    apt = "sudo apt "
    ins = "install "
    packages = "clementine ffmpeg gstreamer1.0-plugins-base dkms gstreamer1.0-plugins-ugly libqt5x11extras5 libcairo2-dev pkg-config"

    print("[+] Installation of the ubuntu packages is starting:")

    for items in packages.split():
        command = str(apt) + str(ins) + str(items)

        subprocess.run(command.split())
        print("\t[+] Package [{}] Installed".format(str(items)))


apt_installation()