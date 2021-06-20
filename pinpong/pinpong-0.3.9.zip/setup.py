# -*- coding: utf-8 -*-  
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if "win" in sys.platform:
    install_requires=['pyserial','Pillow']
else:
    install_requires=['pyserial','Pillow','smbus','spidev']


with open('README.md') as f:
    long_description = f.read()

setup(
    name='pinpong',
    packages=['pinpong','pinpong/base','pinpong/libs','pinpong/examples','pinpong/examples/xugu','pinpong/examples/nezha','pinpong/examples/RPi','pinpong/examples/handpy','pinpong/examples/microbit','pinpong/examples/GD32V','pinpong/extension/','pinpong/examples/PinPong Board/','pinpong/examples/PinPong Board/example/Many_board_control','pinpong/examples/PinPong Board/example/serial_example','pinpong/examples/PinPong Board/example/tcp_example'],
    install_requires=install_requires,

    include_package_data=True,
    entry_points={
      "console_scripts":["pinpong = pinpong.base.help:main"],
    },
    version='0.3.9',
    description="a middleware based on Firmata protocol and compatible with micropython API",
    long_description=long_description,
    long_description_content_type='text/markdown',
    
    python_requires = '>=3.5.*',
    author='Ouki Wang',
    author_email='ouki.wang@dfrobot.com',
    url='https://github.com/DFRobot/pinpong-docs',
    download_url='https://github.com/DFRobot/pinpong-docs',
    keywords=['Firmata', 'Arduino', 'Protocol', 'Python'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)

