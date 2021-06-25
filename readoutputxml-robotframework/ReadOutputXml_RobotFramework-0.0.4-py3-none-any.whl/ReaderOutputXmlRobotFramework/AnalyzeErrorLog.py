import os
from datetime import datetime, timedelta
from typing import TypedDict
from ReaderRobotFramework import ReaderRobotFramework
import json

OUTPUT_XML_PATH: str = r'C:\Users\mcdev\Downloads\All_Output (1).xml'
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


def main():
    analyzer = AnalyzeErrorLog()
    robot_result: dict = analyzer.read_output_xml(OUTPUT_XML_PATH, './suite/suite')
    modify_robot_result: dict = analyzer.set_structure_robot_result(robot_result)
    analyzer.write_archive_json(modify_robot_result)


if __name__ == '__main__':
    main()
