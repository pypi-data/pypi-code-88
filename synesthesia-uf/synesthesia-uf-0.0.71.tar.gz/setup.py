from setuptools import setup, find_packages
from setuptools.command.install import install
import codecs
import os, sys, subprocess


VERSION = '0.0.71'
DESCRIPTION = 'A Python audio image creation tool'
LONG_DESCRIPTION = 'A Python audio image creation tool that takes audio and creates images from them.'
APT_PACKAGES = 'clementine ffmpeg gstreamer1.0-plugins-base dkms gstreamer1.0-plugins-ugly libqt5x11extras5 libcairo2-dev pkg-config'

class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        install.run(self)
        # POST-INSTALL SCRIPT\
        apt = "sudo apt "
        ins = "install "
        packages = APT_PACKAGES

        print("[+] Installation of the ubuntu packages is starting:")

        for items in packages.split():
            command = str(apt) + str(ins) + str(items)

            subprocess.run(command.split())
            print("\t[+] Package [{}] Installed".format(str(items)))



# Setting up
setup(
    name="synesthesia-uf",
    version=VERSION,
    author="Super Fun Adventure Club Dude Man Squad",
    author_email="<georgekolasa@ufl.edu",
    cmdclass= {'install': PostInstallCommand},
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



