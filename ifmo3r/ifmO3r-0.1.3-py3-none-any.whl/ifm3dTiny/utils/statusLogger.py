"""
Author: ifm CSR
This script provides logging features for logging status messages to file

This is sample code. Use at your own risk.
"""

import logging

class StatusLogger:
    """
    This status logger class provides helper functions for writing status messages to file while using the standard
    Python logging class
    """
    def __init__(self, nameLogFile):
        """
        creates a logger object for asynchronous message logging
        :param nameLogFile: log file name
        """

        # create logger and set logging level to info
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)

        # create a fileHandler for writing the the logging messages to file
        fh = logging.FileHandler(nameLogFile + '.log')
        fh.setLevel(logging.INFO)

        # create formatter and add it to the handlers
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)

        # add the handlers to the logger
        self.logger.addHandler(fh)

    def __enter__(self):
        return self

    def info(self, message):
        """
        logs a info message

        :param message: content of the message
        :return:
        """
        self.logger.info(message)

    def critical(self, message):
        """
        logs a critical message
        :param message: content of the message
        :return:
        """
        self.logger.critical(message)