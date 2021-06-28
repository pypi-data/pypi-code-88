import os
from datetime import datetime, timedelta
from typing import TypedDict
from ReaderRobotFramework import ReaderRobotFramework
import json

LIMIT_DAYS_ARCHIVE = 3
BACKUP_PATH: str = r'C:\Users\mcdev\Downloads'
ARCHIVE_PATH: str = r'C:\Users\mcdev\Downloads\TestRobotOutput'
ARCHIVE_JSON_FILE: str = 'archive_robot_result.json'


class TestCaseDetailLog(TypedDict):
    testcase_name: str
    test_result: str
    msg_error: str
    full_msg_error_robot: str
    script_robot_rerun: str


class AnalyzeErrorLog:
    def __init__(self):
        self.current_month: str = self.get_current_date()

    @staticmethod
    def read_output_xml(path_output_xml, main_suite_xpath) -> dict:
        reader = ReaderRobotFramework(path_output_xml, main_suite_xpath)
        robot_result: dict = reader.read_output_xml_file_to_dict()
        return robot_result

    @staticmethod
    def set_structure_robot_result(robot_result: dict) -> dict:
        for project in robot_result.keys():
            project_detail: dict = robot_result[project]
            testcase_detail: list = project_detail['TestcaseDetail']
            new_structure_robot_result: list = []

            for detail in testcase_detail:
                testcase_fullname = detail['testcase_name']
                testcase: list = testcase_fullname.split(' ', 1)
                testcase_id: str = testcase[0]
                testcase_name: str = testcase[1]
                detail['testcase_name'] = testcase_name
                detail['testcase_id'] = testcase_id
                new_structure_robot_result.append(detail)
            project_detail['TestcaseDetail'] = new_structure_robot_result
            robot_result[project] = project_detail
        archive_result_robot: dict = {f'{datetime.today():%Y%m%d}': robot_result}
        return archive_result_robot

    def write_archive_json(self, robot_result: dict):
        path_current_month: str = f'{ARCHIVE_PATH}/{self.current_month}'
        self.check_archive_path(path_current_month)
        path_json_file: str = f'{path_current_month}/{ARCHIVE_JSON_FILE}'
        if os.path.isfile(f'{path_json_file}'):
            self.update_archive_json_file(robot_result, path_json_file)
        else:
            self.write_new_archive_json_file(robot_result, path_json_file)

    @staticmethod
    def update_archive_json_file(robot_result: dict, path_json_file: str):
        with open(f'{path_json_file}', 'r', encoding='utf8') as json_file:
            data_archive_result_robot = json.load(json_file)
            print(f'Read file \"f"{path_json_file}"\" completed.')

        data_archive_result_robot.update(robot_result)
        json_object = json.dumps(data_archive_result_robot, indent=4)
        with open(f'{path_json_file}', 'w', encoding='utf8') as json_file:
            json_file.write(json_object)
            print(f'Write file \"f"{path_json_file}"\" completed.')

    @staticmethod
    def write_new_archive_json_file(robot_result: dict, path_json_file: str):
        json_object = json.dumps(robot_result, indent=4)
        with open(f'{path_json_file}', 'w', encoding='utf8') as json_file:
            json_file.write(json_object)
            print(f'Write file \"f"{path_json_file}"\" completed.')

    @staticmethod
    def check_archive_path(path):
        if not os.path.isdir(f'{ARCHIVE_PATH}'):
            os.mkdir(ARCHIVE_PATH)
        if not os.path.isdir(f'{path}'):
            os.mkdir(path)

    @staticmethod
    def get_current_date() -> str:
        current_month = f'{datetime.today():%B}'
        return current_month

    @staticmethod
    def get_archive_latest_output_xml_path() -> str:
        all_archive_log: list = [path for path in os.listdir(BACKUP_PATH) if path != 'Archive']
        all_archive_log.sort(reverse=True)
        latest_log_path: str = all_archive_log[0]
        latest_output_xml_absolute_path: str = f'{BACKUP_PATH}/{latest_log_path}/AllReport/RobotResult/All_Output.xml'
        return latest_output_xml_absolute_path

    @staticmethod
    def manage_archive_file(limit_days_archive):
        all_archive_log: list = [path for path in os.listdir(BACKUP_PATH) if path != 'Archive']
        all_archive_log.sort(reverse=True)
        if len(all_archive_log) > limit_days_archive:
            old_archive_log: list = all_archive_log[limit_days_archive:]
            for archive_log in old_archive_log:
                os.system(f'rm -f -r {BACKUP_PATH}/{archive_log}')


def main():
    analyzer = AnalyzeErrorLog()
    # analyzer.manage_archive_file(LIMIT_DAYS_ARCHIVE)
    # output_xml_path = analyzer.get_archive_latest_output_xml_path()
    robot_result: dict = analyzer.read_output_xml(f'{BACKUP_PATH}/20210628 12-39-22/output.xml', './suite/suite')
    modify_robot_result: dict = analyzer.set_structure_robot_result(robot_result)
    analyzer.write_archive_json(modify_robot_result)


if __name__ == '__main__':
    main()
