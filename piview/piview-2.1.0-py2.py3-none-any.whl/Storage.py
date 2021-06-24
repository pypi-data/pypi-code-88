# Project:    PiView
# Filename:   Storage.py
# Location:   ./piview
# Author:     Adrian Gould <adrian.gould@nmtafe.wa.edu.au>
# Created:    10/04/21
#
# This file provides the following features, methods and associated
# supporting code:
# - total ram and free ram (tuple)
# - total disk storage and free storage space (tuple)
# - disc storage for all disks connected to Pi (Total and Free) as a list or
# dictionary (To be determined)

import subprocess


class Storage:
    @staticmethod
    def ram():
        """
        Provide the total RAM and free RAM to the user as a tuple

        :rtype: tuple (int)
        :return: (Total, Free)  Approximate bytes

        """
        output = subprocess.check_output(['free', '-m'])
        lines = output.splitlines()
        line = str(lines[1])
        ram = line.split()
        # total/free
        return int(ram[1]), int(ram[3])

    @staticmethod
    def disc():
        """
        Provide the total disc space and the disc space that is free

        :rtype: tuple (int)
        :return: (Total, Free)  Approximate bytes

        """
        output = subprocess.check_output(['df', '-k'])
        lines = output.splitlines()
        line = str(lines[1])
        disk = line.split()
        # total/free
        return int(disk[1])*1024, int(disk[3])*1024

    @staticmethod
    def all_discs():
        """
        Provide the user with the storage space (Total, Free) for each
        disc attached to the Pi as a dictionary.

        The dictionary will have: "disc name" : (total storage, free storage)
        for each disc.

        :return disc stats: dictionary of tuples
        """
        disc_stats = {'ERROR':"NOT IKMPLEMENTED"}
        # TODO: Create list of all drives and the total and free space for each
        # For each disc:
        #   obtain free space and total space
        #   add "disk_name" :(total, free) to 'disc_stats' dictionary
        return disc_stats

    @staticmethod
    def disk():
        """
        Alias for disc()

        see :func:`~piview.Storage.disc`
        """
        return Storage.disc()

    @staticmethod
    def all_disks():
        """
        Alias for all_discs()

        see :func:`~piview.Storage.all_discs`
        """
        return Storage.all_discs()
