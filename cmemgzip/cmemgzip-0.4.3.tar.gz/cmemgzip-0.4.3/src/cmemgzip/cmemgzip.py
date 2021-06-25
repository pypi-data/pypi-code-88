#!/usr/bin/env python3

# By Carles Mateo https://blog.carlesmateo.com
# 2021-02-20
# cmemgzip.py Compresses files in memory, deletes the original, and writes the .gz compressed file.
# You need to have enough RAM Memory to read the file.
#

import gzip
import os
import sys
import datetime
import time
import platform


class DateTimeUtils:

    def get_unix_epoch(self):
        """
        Will return the EPOCH Time. For convenience is returned as String
        :return: s_now_epoch
        """
        s_now_epoch = str(int(time.time()))

        return s_now_epoch

    def get_unix_epoch_as_float(self):
        """
        Will return the EPOCH Time in float with all the decimals.
        :return: f_now_epoch
        """
        f_now_epoch = time.time()

        return f_now_epoch

    def get_datetime(self, b_milliseconds=False, b_remove_spaces_and_colons=False):
        """
        Return the datetime with milliseconds in format YYYY-MM-DD HH:MM:SS.xxxxx
        or without milliseconds as YYYY-MM-DD HH:MM:SS"""
        if b_milliseconds is True:
            s_now = str(datetime.datetime.now())
        else:
            s_now = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        if b_remove_spaces_and_colons is True:
            s_now = s_now.replace(" ", "-")
            s_now = s_now.replace(":", "")

        return s_now

    def p(self, s_text):
        """
        Will print a Date time in front of the text
        :param s_text:
        :return:
        """

        s_now = self.get_datetime(b_milliseconds=False, b_remove_spaces_and_colons=False)
        s_message = s_now + " " + s_text

        print(s_message)


class FileUtils:

    def test_helper(self):
        pass

    def delete(self, s_file):
        """
        This method deletes a given file
        :param s_file: The file path for the file to delete
        :type s_file: str
        :return: Indicate success of deletion
        :rtype boolean
        """

        b_success = True
        try:
            # This will help with Unit Testing by raisin IOError Exception
            self.test_helper()

            if os.path.exists(s_file):
                os.remove(s_file)
            else:
                b_success = False
        except IOError:
            b_success = False

        return b_success

    def get_file_size_in_bytes(self, s_file):

        b_success = False
        i_file_size = 0

        try:
            i_file_size = os.path.getsize(s_file)
            b_success = True
        except:
            b_success = False

        return b_success, i_file_size

    def read_binary(self, s_file):
        """
        This method reads the file in binary format
        :param s_file: The file path for the file to read
        :type s_file: str
        :return: Indicate success reading
        :rtype boolean
        :return: by_result: byte
        :rtype byte
        """
        by_result = bytes()
        b_success = True

        try:
            self.test_helper()

            fh = open(s_file, "rb")
            by_result = fh.read()
            fh.close()

            # For python2
            by_result = bytearray(by_result)

        except IOError:
            by_result = bytes()
            b_success = False

        except:
            # May have crashed due to not more memory available
            by_result = bytes()
            b_success = False

        return b_success, by_result

    def write_binary(self, s_file, by_content):
        """
        This method creates or overwrites a file
        :param s_file: The file path for the file to read
        :type s_file: str
        :param by_content: The text to write
        :type by_content: Binary
        :return: b_result: Indicate success reading, by_content: The binary content of the file
        :rtype bool, binary
        """
        try:
            fh = open(s_file, "wb")
            fh.write(by_content)
            fh.close()

        except IOError:
            return False

        return True


class StringUtils:

    def convert_integer_to_string_thousands(self, i_number, s_thousand_sep=","):
        """
        Puts thousand separator
        :param i_number:
        :param s_thousand_sep:
        :return: s_number_formatted
        """

        s_number = str(i_number)
        s_number_formatted = ""
        i_pos = 0
        for i_index in range(len(s_number)-1, -1, -1):
            i_pos = i_pos + 1
            if i_pos % 3 == 1 and i_pos > 1 and s_number[i_index] != "-":
                s_number_formatted = s_number[i_index] + s_thousand_sep + s_number_formatted
            else:
                s_number_formatted = s_number[i_index] + s_number_formatted

        return s_number_formatted

    def convert_bytes_to_best_size(self, i_bytes):
        """
        Converts a number of bytes to the highest values, and adds the units
        :param i_bytes:
        :return: s_biggest_suggested
        """
        s_value_bytes, s_value_kb, s_value_mb, s_value_gb, s_value_tb, s_value_pb, s_biggest_suggested = self.convert_bytes_to_multiple_units(
            i_bytes)

        return s_biggest_suggested

    def convert_bytes_to_multiple_units(self, i_bytes):
        s_value_bytes, s_value_kb, s_value_mb, s_value_gb, s_value_tb, s_value_pb, s_biggest_suggested = \
            self.convert_to_multiple_units(str(i_bytes), b_add_units=True)

        # @TODO: Pending fixing convert_to_multiple_units to accept bytes. Quick fix.
        s_value_bytes = str(i_bytes)
        if i_bytes < 1024:
            s_biggest_suggested = s_value_bytes + "Bytes"

        return s_value_bytes, s_value_kb, s_value_mb, s_value_gb, s_value_tb, s_value_pb, s_biggest_suggested

    def convert_string_to_integer(self, s_value):
        """
        Convert a string to Integer, checking for errors.
        """

        b_success = True
        i_value = 0

        if s_value == "":
            i_value = 0
        else:
            try:
                i_value = int(s_value)
            except:
                b_success = False
                i_value = 0

        return b_success, i_value

    def convert_to_multiple_units(self, s_amount, b_add_units=False, i_decimals=2):
        """
        Getting the bytes. We multiply per 1024
        :param s_amount:
        :param b_add_units: If we suffix the units, like GiB
        :param i_decimals: Number of decimal positions
        :return: String in Bytes, String in Kbytes, String in Mbytes, String in Gbytes, String in Tbytes,
                 str in Pbytes, biggest suggested unit
        """
        # @TODO: Finish this
        s_value_bytes = "0"
        s_value_kb = "0"
        s_value_mb = "0"
        s_value_gb = "0"
        s_value_tb = "0"
        s_value_pb = "0"

        s_biggest_suggested = ""

        s_amount = s_amount.strip()

        s_unit = s_amount[-2:].upper()
        s_unit3 = s_amount[-3:].upper()

        s_mask = "{:." + str(i_decimals) + "f}"  # "{:.2f}"

        if s_amount.isdigit() is True:
            # Bytes
            i_value = int(s_amount)
            i_value_bytes = i_value
            s_value_bytes = str(i_value_bytes)
            i_value_kb = i_value_bytes/1024
            s_value_kb = s_mask.format(i_value_kb)
            f_value_mb = i_value_bytes/1024/1024
            s_value_mb = s_mask.format(f_value_mb)
            f_value_gb = i_value_bytes/1024/1024/1024
            s_value_gb = s_mask.format(f_value_gb)
            f_value_tb = i_value_bytes/1024/1024/1024/1024
            s_value_tb = s_mask.format(f_value_tb)
            f_value_pb = i_value_bytes/1024/1024/1024/1024/1024
            s_value_pb = s_mask.format(f_value_pb)
        elif s_unit == "KB" or s_unit3 == "KIB":
            s_value = s_amount.replace(' ', '')
            # Remove "KB"
            if s_unit == 'KB':
                s_value = s_value[0:-2]
            elif s_unit3 == 'KIB':
                s_value = s_value[0:-3]
            i_value = int(s_value)
            i_value_bytes = i_value*1024
            s_value_bytes = str(i_value_bytes)
            i_value_kb = i_value
            s_value_kb = str(i_value_kb)
            f_value_mb = int(i_value_kb/1024)
            s_value_mb = s_mask.format(f_value_mb)
            f_value_gb = i_value_kb/1024/1024
            s_value_gb = s_mask.format(f_value_gb)
            f_value_tb = i_value_kb/1024/1024/1024
            s_value_tb = s_mask.format(f_value_tb)
            f_value_pb = i_value_kb/1024/1024/1024/1024
            s_value_pb = s_mask.format(f_value_pb)

        if b_add_units is True:
            s_value_bytes = s_value_bytes + "Bytes"
            s_value_kb = s_value_kb + "KB"
            s_value_mb = s_value_mb + "MB"
            s_value_gb = s_value_gb + "GB"
            s_value_tb = s_value_tb + "TB"
            s_value_pb = s_value_pb + "PB"

        if f_value_pb >= 1:
            s_biggest_suggested = s_value_pb
        elif f_value_tb >= 1:
            s_biggest_suggested = s_value_tb
        elif f_value_gb >= 1:
            s_biggest_suggested = s_value_gb
        elif f_value_mb >= 1:
            s_biggest_suggested = s_value_mb
        elif i_value_kb >= 1:
            s_biggest_suggested = s_value_kb
        elif i_value_bytes >= 1:
            s_biggest_suggested = s_value_bytes

        return s_value_bytes, s_value_kb, s_value_mb, s_value_gb, s_value_tb, s_value_pb, s_biggest_suggested

    def format_float_to_string(self, f_number, i_decimal_positions=2):
        s_format = "%." + str(i_decimal_positions) + "f"

        s_formatted = (s_format % f_number)

        return s_formatted

    def get_bytes_per_second(self, i_bytes, f_seconds):
        """
        Returns the speed in bytes/seconds
        :param i_bytes:
        :param f_seconds:
        :return: i_speed_bytes_per_second, s_biggest_suggested
        """

        i_speed_bytes_per_second = int(i_bytes / f_seconds)
        s_value_bytes, s_value_kb, s_value_mb, s_value_gb, s_value_tb, s_value_pb, s_biggest_suggested = \
            self.convert_bytes_to_multiple_units(i_speed_bytes_per_second)

        return i_speed_bytes_per_second, s_biggest_suggested

    def get_time_and_bytes_per_second(self, i_bytes, f_time_start, f_time_finish):
        """
        Calculates the time between start and end, and the bytes per second, and the best unit for it
        :param i_bytes:
        :param f_time_start:
        :param f_time_finish:
        :return: f_time, s_time, i_bytes_per_second, s_best_unit
        """

        f_time = f_time_finish - f_time_start
        s_time = str(round(f_time, 2))

        i_bytes_per_second, s_best_unit = self.get_bytes_per_second(i_bytes, f_time)

        return f_time, s_time, i_bytes_per_second, s_best_unit


class ArgsUtils:
    # Original List of Args passed to the Constructor
    a_s_args = []
    # Dictionary produced format
    d_s_args = {}

    def __init__(self, a_s_args=sys.argv):
        """
        Get the arguments from Command Line and returns a dictionary with them

        :type: list[str]
        """
        d_s_args = {}
        i_num_args = 0

        self.a_s_args = a_s_args

        try:
            i_index = 0
            for s_arg in a_s_args:
                # Skip the own filename in index 0
                if i_index > 0:
                    i_num_args = i_num_args + 1
                    st_arg_pair = s_arg.split("=")
                    # NOTE: Please be aware that this will also deal with parameters like -p=1=2
                    #       And will return {'-p'} = "1=2"
                    if len(st_arg_pair) > 1:
                        d_s_args[st_arg_pair[0]] = "=".join(st_arg_pair[1:])
                    else:
                        d_s_args[st_arg_pair[0]] = ""

                i_index = i_index + 1

        except:
            # Clean the list of args if something went wrong
            d_s_args = {}

        self.d_s_args = d_s_args

    def get_arg(self, s_arg):
        """
        Returns the argument's value
        :type: str
        :rtype: boolean
        :rtype: str
        """

        s_value = ""
        b_exist = False

        if s_arg in self.d_s_args:
            s_value = self.d_s_args[s_arg]
            b_exist = True

        return b_exist, s_value

    def get_arg_from_list(self, a_s_args, s_default=""):
        """
        Returns the first argument's value, from a list of them, comparing to the
        Parameters sent in the Constructor, or a default value.
        Example is asking for ['-n', '--number']
        :type: Array of str
        :rtype: boolean
        :rtype: str
        """

        s_value = s_default
        b_exist = False

        for s_arg in a_s_args:
            if s_arg in self.d_s_args:
                s_value = self.d_s_args[s_arg]
                b_exist = True

                break

        return b_exist, s_value

    def get_dictionary_of_args(self):
        """
        Returns the produced dictionary
        :rtype: dict
        """

        return self.d_s_args

    def get_list_of_args(self):
        """
        Returns the original list of args passed
        :rtype: list
        """

        return self.a_s_args

    def get_list_of_args_without_dash(self):
        """
        Returns the list of arguments that do not start by dash.
        Useful to get filenames, for example.

        Note: We use d_s_args instead of a_s_args as the name of the script (index 0) is already removed.

        :return: Array filtered
        """

        a_result = []

        for s_item in self.d_s_args:
            if s_item[0] != "-":
                a_result.append(s_item)

        return a_result

#
# Processes Utils
#
# Author: Carles Mateo
# Creation Date: 2014-11-11 18:18 Barcelona
# Last Update: 2021-04-10 11:15 Ireland
# Description: Class to deal with Python functionalities and compatibility
#


class PythonUtils:

    def get_python_version(self):
        """
        Returns the version of Python

        Examples:
        sys.version_info(major=2, minor=7, micro=18, releaselevel='final', serial=0)
        sys.version_info(major=3, minor=8, micro=5, releaselevel='final', serial=0)
        :return: s_version, i_major, i_minor, i_micro, s_releaselevel
        """

        # This only works with Python3, so changing to compatible Python2 and Python3
        # i_major = sys.version_info["major"]
        # i_minor = sys.version_info["minor"]
        # i_micro = sys.version_info["micro"]

        i_major = sys.version_info[0]
        i_minor = sys.version_info[1]
        i_micro = sys.version_info[2]

        s_releaselevel = sys.version_info[3]

        s_version = str(i_major) + "." + str(i_minor) + "." + str(i_micro)

        return s_version, i_major, i_minor, i_micro, s_releaselevel

    def is_python_2(self):
        s_version, i_major, i_minor, i_micro, s_releaselevel = self.get_python_version()

        if i_major == 2:
            return True

        return False

    def is_python_3(self):
        s_version, i_major, i_minor, i_micro, s_releaselevel = self.get_python_version()

        if i_major == 3:
            return True

        return False


class ScreenUtils:

    b_support_colors = True

    # Some colors, in case we want to give Colors to our Application
    # For example Red for Errors.
    # Also in order to clear the screen, and repaint it from top, like top does, instead of just printing lines
    CLEAR = "\x1B[0m"
    CLEAR_SCREEN = "\033c"

    ITALIC_BLUE = "\x1B[34;3m"

    BOLD_BLACK = "\x1B[1;1m"
    BOLD_RED = "\x1B[31;1m"
    BOLD_GREEN = "\x1B[32;1m"
    BOLD_YELLOW = "\x1B[33;1m"
    BOLD_BLUE = "\x1B[34;1m"
    BOLD_DARK_GREY = "\x1B[37;1m"
    BOLD_YELLOW_BLINK = "\x1B[33;5;1m"

    BOLD_BLACK_BG_RED = "\x1B[1;41m"
    BOLD_BLACK_BG_GREEN = "\x1B[1;42m"
    BOLD_BLACK_BG_BLUE = "\x1B[1;44m"

    BLACK = "\x1B[2;49m"
    RED = "\x1B[31;49m"
    GREEN = "\x1B[32;49m"
    YELLOW = "\x1B[33;49m"
    BLUE = "\x1B[34;49m"
    MAGENTA = "\x1B[35;49m"
    CYAN = "\x1B[36;49m"
    WHITE = "\x1B[37;49m"
    DARK_GREY = "\x1B[37;2m"
    ORANGE = "\x1B[33;3m"

    def __init__(self, b_support_colors=True):
        """
        If b_support_colors is False, like in the case of the crons or poor SSH Terminals colors will not be
        added.
        Also in the future when we support different Templates for colors, colors for types, like e.g. LABELS
        would be able to be customized very easily.
        :param b_support_colors:
        """

        self.b_support_colors = b_support_colors

        if b_support_colors is False:
            # Doesn't support colors, so nothing will be rendered without changes in the code
            self.ITALIC_BLUE = ""

            self.BLACK = ""
            self.RED = ""
            self.GREEN = ""
            self.WHITE = ""
            self.BLUE = ""
            self.YELLOW = ""
            self.CYAN = ""
            self.MAGENTA = ""
            self.DARK_GREY = ""
            self.ORANGE = ""

            # Clears current color
            self.CLEAR = ""

            self.BOLD_BLACK = ""
            self.BOLD_RED = ""
            self.BOLD_GREEN = ""
            self.BOLD_YELLOW = ""
            self.BOLD_BLUE = ""
            self.BOLD_DARK_GREY = ""
            self.BOLD_YELLOW_BLINK = ""

            self.BOLD_BLACK_BG_RED = ""
            self.BOLD_BLACK_BG_GREEN = ""
            self.BOLD_BLACK_BG_BLUE = ""

            self.CLEAR_SCREEN = ""
        else:
            self.CLEAR = "\x1B[0m"
            self.CLEAR_SCREEN = "\033c"

            self.ITALIC_BLUE = "\x1B[34;3m"

            self.BOLD_BLACK = "\x1B[1;1m"
            self.BOLD_RED = "\x1B[31;1m"
            self.BOLD_GREEN = "\x1B[32;1m"
            self.BOLD_YELLOW = "\x1B[33;1m"
            self.BOLD_BLUE = "\x1B[34;1m"
            self.BOLD_DARK_GREY = "\x1B[37;1m"
            self.BOLD_YELLOW_BLINK = "\x1B[33;5;1m"

            self.BOLD_BLACK_BG_RED = "\x1B[1;41m"
            self.BOLD_BLACK_BG_GREEN = "\x1B[1;42m"
            self.BOLD_BLACK_BG_BLUE = "\x1B[1;44m"

            self.BLACK = "\x1B[2;49m"
            self.RED = "\x1B[31;49m"
            self.GREEN = "\x1B[32;49m"
            self.YELLOW = "\x1B[33;49m"
            self.BLUE = "\x1B[34;49m"
            self.MAGENTA = "\x1B[35;49m"
            self.CYAN = "\x1B[36;49m"
            self.WHITE = "\x1B[37;49m"
            self.DARK_GREY = "\x1B[37;2m"
            self.ORANGE = "\x1B[33;3m"

    def color_string(self, s_color, s_text):
        s_text = s_color + s_text + self.CLEAR

        return s_text

    def color_error(self, s_text):
        """
        Returns an string with the color code for error, typically red
        :param s_text:
        :return: String
        """
        s_text = self.RED + s_text + self.CLEAR

        return s_text

    def color_label(self, s_text):
        """
        Returns an string with the color code for a label, typically white
        :param s_text:
        :return: String
        """
        s_text = self.BOLD_BLUE + s_text + self.CLEAR

        return s_text

    def color_title(self, s_text):
        """
        Return an string bold in blue, as it is meant to be a title
        :param s_text:
        :return: String
        """
        s_text = self.BOLD_BLUE + s_text + self.CLEAR

        return s_text

    def color_grey_bold(self, s_text):
        return self.color_string(self.BOLD_DARK_GREY, s_text)

    def p(self, s_text):
        """
        Prints whatever is sent to the Standard Output.
        This method could allow to capture the text printed and Log to a file.
        Also allows easily portability from Python2.7 to Python3.6
        :param s_text: Text to Print
        :return:
        """
        print(s_text)

    def p_no_cr(self, s_text):
        """
        Prints whatever is sent to the Standard Output without finishing Enter.
        This method could allow to capture the text printed and Log to a file.
        Also allows easily portability from Python2.7 to Python3.6
        :param s_text: Text to Print
        :return:
        """
        sys.stdout.write(s_text)
        sys.stdout.flush()

    def perror(self, s_text):
        """
        Prints whatever is sent to the Standard Output surrounded by the error escape sequence.
        This method could allow to capture the text printed and Log to a file.
        Also allows easily portability from Python2.7 to Python3.6
        :param s_text: Text to Print
        :return:
        """
        print(self.color_error(s_text))

    def clear_screen(self):
        """"
        Clears the screen if support for colors is enabled
        """
        if self.b_support_colors is False:
            return

        # self.reset_virtual_terminal()
        self.p_no_cr(self.CLEAR_SCREEN)

    def get_i_terminal_height(self):
        return self.i_terminal_height

    def get_i_terminal_width(self):
        return self.i_terminal_width

    def color_alert(self, s_text):
        s_text = self.BOLD_RED + s_text + self.CLEAR

        return s_text

    def color_warning(self, s_text):
        s_text = self.BOLD_YELLOW + s_text + self.CLEAR

        return s_text

    def color_ok(self, s_text):
        s_text = self.BOLD_GREEN + s_text + self.CLEAR

        return s_text


class Cmemgzip:

    VERSION = "0.4.3"

    def __init__(self, o_fileutils, o_stringutils, o_datetime, o_argutils, o_screenutils=ScreenUtils(b_support_colors=True), o_pythonutils=PythonUtils()):
        self.o_fileutils = o_fileutils
        self.o_stringutils = o_stringutils
        self.o_datetime = o_datetime
        self.o_argutils = o_argutils
        self.o_screenutils = o_screenutils
        self.o_pythonutils = o_pythonutils

    def exit_app(self, s_error_message="", i_error_code=0):
        if s_error_message != "":
            if i_error_code > 0:
                s_error_message = self.o_screenutils.color_error(s_error_message)
            self.d_p(s_error_message)

        exit(i_error_code)

    def get_percent_compressed(self, i_bytes_compressed, i_bytes_read, i_decimal_positions=2):
        """
        Return an string formatted in the format of XX.YY%
        :param i_bytes_compressed:
        :param i_bytes_read:
        :param i_decimal_positions:
        :return: String
        """
        i_percent = (i_bytes_compressed / i_bytes_read) * 100
        s_percent = self.o_stringutils.format_float_to_string(i_percent, i_decimal_positions=i_decimal_positions)
        s_percent = s_percent + "%"

        return s_percent

    def main(self):
        """
        Checks Parameters and proceeds
        :return:
        """

        # Get the Filename and Basic Parameters
        b_simulate, i_mem_mb, s_filename = self.validate_parameters_or_exit()

        print(self.o_screenutils.color_title("cmemgzip.py v." + Cmemgzip.VERSION))
        # Python 2 requires ("") otherwise it prints ()
        print("")

        s_python_version, i_major, i_minor, i_micro, s_releaselevel = self.o_pythonutils.get_python_version()
        print("Detected Python: " + s_python_version)
        if self.o_pythonutils.is_python_2() is True:
            self.o_screenutils.perror("Python 2 is not supported.")
            self.exit_app("Minimum version is Python 3.5", i_error_code=1)

        if b_simulate is True:
            self.d_p("Running in Simulate / Dry-Run mode. No file will be deleted or written.")
            print("")

        self.compress(s_filename, b_simulate, i_mem_mb)

    def validate_parameters_or_exit(self):
        """
        Validate the input parameters or exit if they are wrong.

        :return: b_simulate, i_mem_mb, s_filename
        """

        b_black, s_value_black = self.o_argutils.get_arg_from_list(["-b", "--black-and-white"])
        if b_black is True:
            # Override Screenutils
            self.o_screenutils = ScreenUtils(b_support_colors=False)

        s_filename, a_files = self.get_filename_from_parameters()

        b_m_parameter_present, b_success_mem, i_mem_mb = self.get_parameter_m()

        if b_m_parameter_present is True and b_success_mem is False:
            self.exit_app("Parameter memory has an incorrect value. Please specify in the format -m=500M or -m=4G .", i_error_code=1)

        b_help, s_value = self.o_argutils.get_arg_from_list(["-h", "--help"])
        if b_help is True or len(a_files) == 0:
            print(self.return_help())
            self.exit_app("", i_error_code=0)

        b_simulate, s_value = self.o_argutils.get_arg_from_list(["-s", "--simulate"])

        return b_simulate, i_mem_mb, s_filename

    def get_parameter_m(self):
        """
        Return if parameter is present, if returned an error, and the value
        :return: b_m_parameter_present, b_success_mem, i_mem_mb
        """
        b_success_mem = False
        i_mem_mb = 0

        b_m_parameter_present, s_mem = self.o_argutils.get_arg_from_list(["-m", "--memory"])

        if b_m_parameter_present is True and s_mem != "":

            if s_mem[-1].upper() == "M":
                s_mem = s_mem[0:-1]
                b_success_mem, i_mem_mb = self.o_stringutils.convert_string_to_integer(s_mem)
            elif s_mem[-1].upper() == "G":
                s_mem = s_mem[0:-1]
                b_success_mem, i_mem_gb = self.o_stringutils.convert_string_to_integer(s_mem)
                i_mem_mb = i_mem_gb * 1024

        return b_m_parameter_present, b_success_mem, i_mem_mb

    def get_filename_from_parameters(self):
        """
        Get the first file, and the list of files as array
        :return: s_filename, a_files
        """
        s_filename = ""

        a_files = self.o_argutils.get_list_of_args_without_dash()
        if len(a_files) > 0:
            s_filename = a_files[0]

        return s_filename, a_files

    def d_p(self, s_text):
        """
        Prints text, with Date time in front in color
        :param s_text:
        :return:
        """
        s_datetime = self.o_screenutils.color_grey_bold(self.o_datetime.get_datetime(b_milliseconds=False, b_remove_spaces_and_colons=False))

        print(s_datetime + " " + s_text)

    def compress(self, s_file, b_simulate=False, i_mem_mb=0):

        s_compressed_filename = s_file + ".gz"

        i_filesize = self.verify_access_and_get_filesize_or_exit(s_file)

        s_filesize_in_bytes = self.o_stringutils.convert_integer_to_string_thousands(i_filesize)
        s_value_bytes, s_value_kb, s_value_mb, s_value_gb, s_value_tb, s_value_pb, s_biggest_suggested = self.o_stringutils.convert_bytes_to_multiple_units(i_filesize)
        s_message = "Size of file: " + self.o_screenutils.color_label(s_file) + " is " + \
                    self.o_screenutils.color_label(s_biggest_suggested) + " (" + s_filesize_in_bytes + " bytes)"
        self.d_p(s_message)

        self.verify_file_size_min_value_or_exit(i_filesize)

        self.verifiy_destination_does_not_exist_with_data_or_exit(i_filesize, s_compressed_filename)

        if i_mem_mb == 0:
            by_compressed, i_bytes_read = self.compress_loading_file_completely_in_memory(i_filesize, s_file, s_filesize_in_bytes)
        else:
            self.d_p("Reading and compressing the file into Memory using blocks of memory of: " +
                     self.o_screenutils.color_label(str(i_mem_mb) + " MB"))

            b_success_compression, by_compressed, i_bytes_read = self.compress_by_blocks(s_file, i_filesize, i_mem_mb)
            if b_success_compression is False:
                self.exit_app("Error! There has been a problem compressing the file.", i_error_code=1)

        # Give a chance to free the memory from the uncompressed file
        by_file_contents = None

        i_bytes_compressed = len(by_compressed)
        self.print_stats_of_compressed_data(i_bytes_compressed, i_bytes_read)

        if i_filesize != i_bytes_read:
            self.exit_app("The file size changed while it was being compressed in memory. Will not delete it. Cancelling.", i_error_code=1)

        self.verify_compressed_size_or_exit(i_bytes_read=i_bytes_read, i_bytes_compressed=i_bytes_compressed)

        if b_simulate is True:
            self.exit_app("Running in simulation code. Exiting now.", i_error_code=0)

        print("Attempting to create the gzip file empty to ensure write permissions")
        by_empty = bytes()
        b_success_write_gzip = self.o_fileutils.write_binary(s_compressed_filename, by_empty)
        if b_success_write_gzip is False:
            self.exit_app("Error! You don't have permissions to create an empty file, so we will not delete the original file")

        print("Deleting the original file to get free space")
        b_success_delete = self.o_fileutils.delete(s_file)
        if b_success_delete is False:
            self.exit_app("Error. Unable to delete the file: " + s_file)

        b_succes_write_gzip = False
        while b_succes_write_gzip is False:
            self.d_p("Writing compressed file: " + self.o_screenutils.color_label(s_compressed_filename))
            b_succes_write_gzip = self.o_fileutils.write_binary(s_compressed_filename, by_compressed)
            if b_succes_write_gzip is False:
                self.d_p(self.o_screenutils.color_error("Error! Problems writing file") + ": " +
                         self.o_screenutils.color_label(s_compressed_filename))
                self.d_p("The original file has been deleted, so if you don't specify another path and filename, original contents")
                self.d_p("from the file: " + self.o_screenutils.color_label(s_file) + " will be lost.")
                s_compressed_filename = input("Please specify a new path and file (e.g. /tmp/error.log.gz) or press CTRL + C: ")

        # with open(s_compressed_filename, "wb") as o_file:
        #     o_file.write(by_compressed)

        self.d_p("Verifying space written match size of compressed file in Memory")
        b_result, i_filesize_compresed = self.o_fileutils.get_file_size_in_bytes(s_compressed_filename)
        if i_filesize_compresed != i_bytes_compressed:
            self.exit_app("Error! The file written does not match the size in Memory. Maybe you ran out of space?", 1)
            # @TODO: Would be nice to offer the possibility to save elsewhere.

        self.d_p(self.o_screenutils.color_ok("Write verification completed."))

    def compress_loading_file_completely_in_memory(self, i_filesize, s_file, s_filesize_in_bytes):
        """
        Compress the file completely in memory, loading all of it in memory.
        :param i_filesize:
        :param s_file:
        :param s_filesize_in_bytes:
        :return: by_compressed, i_bytes_read
        """

        f_time_start_reading = self.o_datetime.get_unix_epoch_as_float()
        self.d_p("Reading file: " + self.o_screenutils.color_label(s_file) + " (" + s_filesize_in_bytes + " bytes) to memory.")
        self.d_p("The file will be attempted to be completely loaded into memory.")

        b_result, by_file_contents = self.o_fileutils.read_binary(s_file)
        f_time_finish_reading = self.o_datetime.get_unix_epoch_as_float()

        i_bytes_read = len(by_file_contents)

        f_time_reading, s_time_reading, i_speed_bytes_per_second, s_biggest_suggested = \
            self.o_stringutils.get_time_and_bytes_per_second(i_bytes_read, f_time_start_reading, f_time_finish_reading)

        if b_result is False:
            self.exit_app("There has been a problem reading the file.", i_error_code=1)

        s_best_units_for_read = self.o_stringutils.convert_bytes_to_best_size(i_bytes_read)

        s_bytes_read = self.o_stringutils.convert_integer_to_string_thousands(i_bytes_read)
        self.d_p(self.o_screenutils.color_label(s_bytes_read + " bytes") + " loaded, in " +
                 self.o_screenutils.color_label(s_time_reading + " seconds") + ", at " +
                 self.o_screenutils.color_label(s_biggest_suggested + "/s") + ".")

        if i_filesize != i_bytes_read:
            self.exit_app("There is a mismatch between the file size reported by the system and the bytes read. Is the file in use?", i_error_code=1)

        self.d_p("Compressing to Memory with maximum compression level...")

        try:
            f_time_start_compressing = self.o_datetime.get_unix_epoch_as_float()
            by_compressed = gzip.compress(by_file_contents, compresslevel=9)
            f_time_finish_compressing = self.o_datetime.get_unix_epoch_as_float()
        except:
            self.exit_app("Problem compressing in memory. Do you have enough memory? If not try parameter -m=100M", 1)

        f_time_compressing = f_time_finish_compressing - f_time_start_compressing

        return by_compressed, i_bytes_read

    def verify_compressed_size_or_exit(self, i_bytes_read, i_bytes_compressed):
        b_success = True

        if i_bytes_compressed == 0:
            self.exit_app("Final compressed size is 0. Cancelling.", i_error_code=1)
        elif i_bytes_compressed >= i_bytes_read:
            self.exit_app("Compressed size is bigger or equal than the original. Cancelling.", i_error_code=1)

        return b_success

    def print_stats_of_compressed_data(self, i_bytes_compressed, i_bytes_read):

        s_bytes_compressed = self.o_stringutils.convert_integer_to_string_thousands(i_bytes_compressed)
        s_value_bytes, s_value_kb, s_value_mb, s_value_gb, s_value_tb, s_value_pb, s_biggest_suggested = self.o_stringutils.convert_bytes_to_multiple_units(
            i_bytes_compressed)
        s_percent = self.get_percent_compressed(i_bytes_compressed, i_bytes_read, i_decimal_positions=2)
        self.d_p("Size compressed: " + self.o_screenutils.color_label(s_biggest_suggested) +
                 " (" + s_bytes_compressed + " bytes). " +
                 self.o_screenutils.color_label(s_percent) + " of the original file.")

    def verifiy_destination_does_not_exist_with_data_or_exit(self, i_filesize, s_compressed_filename):
        b_result, i_filesize_compressed = self.o_fileutils.get_file_size_in_bytes(s_compressed_filename)
        if b_result is True and i_filesize > 0:
            self.exit_app("Destination file " + s_compressed_filename + " already exists. Cancelling.", i_error_code=1)

    def verify_file_size_min_value_or_exit(self, i_filesize):
        if i_filesize < 100:
            self.exit_app("I will not attempt to compress a file less than 100 bytes! Use gzip for that", i_error_code=1)

        return True

    def verify_access_and_get_filesize_or_exit(self, s_file):
        """
        Will get the file size and if it's unable, will exit
        :param s_file: The input file name
        :return: i_filesize
        """
        print("Verifying access to: " + s_file)
        b_result, i_filesize = self.o_fileutils.get_file_size_in_bytes(s_file)
        if b_result is False:
            self.exit_app("I cannot access the file: " + s_file, i_error_code=1)

        return i_filesize

    def get_how_many_blocks(self, i_size_bytes, i_block_size_mb):
        i_block_size_bytes = i_block_size_mb * 1024 * 1024

        i_blocks = i_size_bytes // i_block_size_bytes
        if (i_size_bytes / i_block_size_bytes) > i_blocks:
            # Note: 7.01 will always require 8 blocks.
            i_blocks = i_blocks + 1

        return i_blocks

    def compress_by_blocks(self, s_file, i_file_size, i_mem_mb):

        b_success = True
        i_mem_bytes = i_mem_mb * 1024 * 1024

        i_total_blocks = str(self.get_how_many_blocks(i_size_bytes=i_file_size, i_block_size_mb=i_mem_mb))
        s_total_blocks = str(i_total_blocks)

        i_blocks = 0
        i_total_uncompressed = 0
        i_total_compressed = 0
        i_bytes_read = 0
        by_compressed_sum = bytes()
        f_time_start_reading = self.o_datetime.get_unix_epoch_as_float()
        try:
            with open(s_file, "rb") as f:
                while True:
                    f_time_start_reading_block = self.o_datetime.get_unix_epoch_as_float()
                    by_chunk = f.read(i_mem_bytes)

                    if by_chunk:
                        i_bytes_chunk = len(by_chunk)
                        i_blocks = i_blocks + 1
                        i_total_uncompressed = i_total_uncompressed + len(by_chunk)
                        i_bytes_read = i_bytes_read + len(by_chunk)

                        f_time_finish_reading_block = self.o_datetime.get_unix_epoch_as_float()
                        f_time_reading_block, s_time_reading_block, i_speed_bytes_per_second, s_biggest_suggested = \
                            self.o_stringutils.get_time_and_bytes_per_second(i_bytes_chunk, f_time_start_reading_block, f_time_finish_reading_block)

                        # Compress Block and get stats
                        f_time_start_compressing_block = self.o_datetime.get_unix_epoch_as_float()
                        by_compressed = gzip.compress(by_chunk, compresslevel=9)
                        by_compressed_sum = by_compressed_sum + by_compressed
                        i_size_compressed = len(by_compressed)
                        f_time_finish_compressing_block = self.o_datetime.get_unix_epoch_as_float()
                        f_time_compressing_block, s_time_compressing_block, i_compression_speed_bytes_per_second, s_compression_biggest_suggested = \
                            self.o_stringutils.get_time_and_bytes_per_second(i_bytes_chunk, f_time_start_compressing_block, f_time_finish_compressing_block)


                        i_total_compressed = i_total_compressed + i_size_compressed
                        s_percent = self.get_percent_compressed(i_bytes_compressed=i_size_compressed, i_bytes_read=i_bytes_chunk, i_decimal_positions=2)
                        s_best_units_for_read = self.o_stringutils.convert_bytes_to_best_size(i_bytes_chunk)
                        s_best_units_for_compressed = self.o_stringutils.convert_bytes_to_best_size(i_size_compressed)

                        self.d_p("Block " + str(i_blocks) + "/" + s_total_blocks + " Read: " + s_best_units_for_read + " in " + s_time_reading_block +
                                 " s. at " + s_biggest_suggested + "/s vs Compressed: " +
                                 s_best_units_for_compressed + " in " + s_time_compressing_block +
                                 " s. at " + s_compression_biggest_suggested + "/s. " +
                                 self.o_screenutils.color_label(s_percent) + " of the original")
                    else:
                        self.d_p("Read total blocks: " + str(i_blocks) + " of " + str(i_mem_mb) + " MB")
                        break
        except IOError:
            b_success = False

        f_time_finish_reading = self.o_datetime.get_unix_epoch_as_float()
        f_time_reading = f_time_finish_reading - f_time_start_reading
        s_time_reading = str(round(f_time_reading, 2))

        return b_success, by_compressed_sum, i_bytes_read

    def return_help(self):
        s_help = """cmemgzip.py v.""" + self.VERSION + """ by Carles Mateo
        
        An utility to compress files in systems with 0 or nearly 0 bytes free of Disk Space.
        It compresses a file in Memory, deletes the original, and writes the .gz version to disk.
        You can later uncompress i twith gzip or see it with zcat.
        
        Usage:
        
            cmemgzip [OPTIONS] filename
        
        Options:
        
        -h --help                Display this help.
        
        -b --black-and-white     Use no colors.

        -m --memory              Use chunks of X MB or GB instead of loading all the file in Memory.
                                 Examples:
                                 cmemgzip -m=100M /var/log/www/error.log
                                 Will read blocks of only 100 MB from error.log file.
                         
                                 cmemgzip -m=4G /var/log/www/access.log
                                 Will read blocks of up to 4 GB from access.log file.
                         
                                 The bigger the memory used is, the better compression is achieved.
                         
                         
        -s --simulate            Dry-run. Compresses into Memory, show the potential gains and quits without altering anything.
        """

        return s_help


def is_windows_host():
    """
    Returns true if is a windows machine
    :return: Boolean
    """
    if platform.system() == 'Windows':
        return True
    else:
        return False


def main_cmemgzip():
    # A function is created, so cmemgzip can be imported and used as a Library

    b_is_windows = is_windows_host()
    if b_is_windows is True:
        b_support_colors = False
    else:
        b_support_colors = True

    o_fileutils = FileUtils()
    o_stringutils = StringUtils()
    o_argutils = ArgsUtils()
    o_timeutils = DateTimeUtils()
    o_screenutils = ScreenUtils(b_support_colors=b_support_colors)
    o_pythonutils = PythonUtils()

    o_cmemgzip = Cmemgzip(o_fileutils, o_stringutils, o_timeutils, o_argutils, o_screenutils, o_pythonutils)
    try:
        o_cmemgzip.main()
    except KeyboardInterrupt:
        o_cmemgzip.exit_app("CTRL + C pressed. Exiting", 0)


if __name__ == "__main__":
    main_cmemgzip()
