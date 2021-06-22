#!/usr/bin/env python
"""
.. current_module:: simple_log.py
.. created_by:: Darren Xie
.. created_on:: 04/25/2021

This python script is a simple log.
"""
import sys
from datetime import datetime
from inspect import getframeinfo, stack

TIME_FORMAT = '%m/%d/%Y %H:%M:%S'


class SimpleLog:
    """
    Basic log class
    """
    start_time = ''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def start_log(self):
        """print out start time"""
        self.start_time = datetime.now()
        self.print_log(f"Starting program: {getframeinfo(stack()[1][0]).filename}")
        self.break_section()

    def print_log(self, msg=''):
        """
        Print out the log message
        :param msg: Log message
        """
        caller = getframeinfo(stack()[1][0])
        sys.stdout.write(f"[{self._curr_time()}][{caller.function} - {caller.lineno}]: {msg}\n")

    def stop_log(self):
        """print out duration time"""
        duration = datetime.now() - self.start_time
        self.break_section()
        self.print_log(f"Done to spend time: {str(duration)}")

    def _curr_time(self):
        """
        return: current time
        """
        return datetime.now().strftime(TIME_FORMAT)

    def break_section(self):
        """
        :return: break section lines
        """
        sys.stdout.write(f"{'-' * 120}\n")
