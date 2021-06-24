import xml.dom.minidom 
import os

class Report:

    __config = None
    __root = None
    __testsuites = None
    __testsuite = None
    __tests = 0
    __fauilures = 0

    def __init__(self, config):
        self.__config = config
        self.__root = xml.dom.minidom.Document()
        self.__testsuites = self.__root.createElement("testsuites") 
        self.__root.appendChild(self.__testsuites)
        self.__testsuite = self.__root.createElement("testsuite")
        self.__testsuite.setAttribute("name", self.__config["name"])
        self.__testsuites.appendChild(self.__testsuite)

    def add_test_result(self, test, passed):
        self.__tests += 1
        testcase = self.__root.createElement("testcase")
        testcase.setAttribute("name", test)
        if not passed:
            self.__fauilures += 1
            failure = self.__root.createElement("failure")
            failure.setAttribute("message", "Failed")
            testcase.appendChild(failure)
        self.__testsuite.appendChild(testcase)

    def flush(self):
        self.__testsuite.setAttribute("tests", str(self.__tests))
        self.__testsuite.setAttribute("errors", "0")
        self.__testsuite.setAttribute("failures", str(self.__fauilures))

        file_path = os.path.join(self.__config["reports_dir"], self.__config["name"] + ".xml")
        with open(file_path, "w") as file:
            self.__root.writexml(file, addindent="  ", newl="\n", encoding="UTF-8")
