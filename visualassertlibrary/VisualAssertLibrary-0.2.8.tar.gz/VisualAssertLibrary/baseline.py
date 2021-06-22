import os
from mega import Mega
from robot.libraries.BuiltIn import _Variables as Variables
from .config import *


class MegaBaseLine:
    """
    Works with baseline placed on mega.nz

    To work with this mega.nz in Robot Framework tests these variables are used:

    - ${MEGA_EMAIL}, ${MEGA_PASSW} - e-mail and password of the Mega account used to store baseline screenshots

    - ${MEGA_BASELINE_DIR_NAME} - Name of the directory where baseline screenshots are saved.

    Directory with baseline screenshots must have a unique name. The first found directory with needed name is used.
    These three scalar variables can be created in any suitable for Robot Framework way: in Variable sections in
    test case files and resource files, in variable file, using Set Test/Suite/Global Variable keyword,
    and in command line.
    """

    def __init__(self):
        mega_account_email = Variables().get_variable_value("${MEGA_EMAIL}")
        mega_account_passw = Variables().get_variable_value("${MEGA_PASSW}")

        self.mega = Mega()
        self.m = self.mega.login(mega_account_email, mega_account_passw)

    def get(self, temp_dir, baseline_dir_name, baseline_screenshot_name):
        """
        Gets previously saved screenshot from Mega
        :param temp_dir: Absolute path to local temp directory to download file to.
        :param baseline_dir_name: Name of the directory with a baseline on Mega
        :param baseline_screenshot_name: Name of the screenshot file with expected result.
        :return: Absolute path to downloaded baseline file
        """
        mega_dir = self.m.find(baseline_dir_name, exclude_deleted=True)
        files_in_target_folder = self.m.get_files_in_node(mega_dir[0])
        found_baseline_screenshot = False

        for file_id in files_in_target_folder.keys():
            if files_in_target_folder[file_id]['a']['n'] == baseline_screenshot_name:
                found_baseline_screenshot = True
                file_obj = (file_id, files_in_target_folder[file_id])
                self.m.download(
                    file_obj,
                    dest_path=temp_dir,
                    dest_filename=f"expected-{baseline_screenshot_name}")
                break
        if found_baseline_screenshot:
            return {"expected_result_file_path": os.path.join(temp_dir, f"expected-{baseline_screenshot_name}"),
                    "baseline_screenshot_name": baseline_screenshot_name,
                    "baseline_dir_name": baseline_dir_name,
                    "baseline_dir_id": mega_dir[0]}
        else:
            print(
                f"Not found baseline screenshot '{baseline_screenshot_name}' in the dir '{baseline_dir_name}'")
            return None

    def save(self, temp_local_baseline_screenshot_path, remote_mega_dir):
        """
        Save new baseline to Mega
        :param temp_local_baseline_screenshot_path: Absolute path to local file to be saved in Mega.
        :param remote_mega_dir: Name of the directory with a baseline on Mega
        """
        mega_dir = self.m.find(remote_mega_dir, exclude_deleted=True)
        if mega_dir:
            files_in_target_folder = self.m.get_files_in_node(mega_dir[0])
            if len(files_in_target_folder) == 0:
                self.m.upload(
                    temp_local_baseline_screenshot_path,
                    dest=mega_dir[0])
            else:
                existing_file_nodes = files_in_target_folder.keys()
                for file_uuid in existing_file_nodes:
                    if files_in_target_folder[file_uuid]['a']['n'] == os.path.split(
                            temp_local_baseline_screenshot_path)[1]:
                        self.m.delete(file_uuid)
                        break
                self.m.upload(
                    temp_local_baseline_screenshot_path,
                    dest=mega_dir[0])
        else:
            raise Exception(f"Not found '{remote_mega_dir}' in MEGA")


class LocalBaseline:
    """
    Works with baseline placed on local machine
    """
    pass


class FtpServerBaseline:
    """
    Works with baseline placed on a remote server via FTP
    """
    pass
