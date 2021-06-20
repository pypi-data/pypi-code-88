"""
junitmgr is a JUnit XML file management tool that provides management of test results, supports queries, and creation operations.

:copyright: (c) H20Dragon
:license: Apache2
"""

from __future__ import with_statement
from __future__ import absolute_import
from __future__ import print_function
import argparse
import html
import logging

#import lxml.etree
from lxml.etree import XMLParser, parse
from junitparser import JUnitXml, Error, Failure, Skipped, TestSuite, TestCase

class JUnitMgr(object):
    """JUnitMgr object.

    Sample 1.
        <testsuite tests="10">
            <testcase classname="testcase_1" name="LoginValidTest"/>
            <testcase classname="testcase_2" name="LoginInvalidPasswordTest"/>
            <testcase classname="elvis" name="LoginAsElvisTest">
                <failure type="NotRealElvis">Elvis has left the building</failure>
            </testcase>
        </testsuite>


    Sample 2.  junit-4.xsd (http://windyroad.com.au/dl/Open%20Source/JUnit.xsd)

    <?xml version="1.0" encoding="UTF-8"?>
    <!-- a description of the JUnit XML format and how Jenkins parses it. See also junit.xsd -->

    <!-- if only a single testsuite element is present, the testsuites
         element can be omitted. All attributes are optional. -->
    <testsuites disabled="" <!-- total number of disabled tests from all testsuites. -->
                errors=""   <!-- total number of tests with error result from all testsuites. -->
                failures="" <!-- total number of failed tests from all testsuites. -->
                name=""
                tests=""    <!-- total number of successful tests from all testsuites. -->
                time=""     <!-- time in seconds to execute all test suites. -->
            >

      <!-- testsuite can appear multiple times, if contained in a testsuites element.
           It can also be the root element. -->
      <testsuite name=""      <!-- Full (class) name of the test for non-aggregated testsuite documents.
                                   Class name without the package for aggregated testsuites documents. Required -->
             tests=""     <!-- The total number of tests in the suite, required. -->
             disabled=""  <!-- the total number of disabled tests in the suite. optional -->
                 errors=""    <!-- The total number of tests in the suite that errored. An errored test is one that had an unanticipated problem,
                                   for example an unchecked throwable; or a problem with the implementation of the test. optional -->
                 failures=""  <!-- The total number of tests in the suite that failed. A failure is a test which the code has explicitly failed
                                   by using the mechanisms for that purpose. e.g., via an assertEquals. optional -->
                 hostname=""  <!-- Host on which the tests were executed. 'localhost' should be used if the hostname cannot be determined. optional -->
             id=""        <!-- Starts at 0 for the first testsuite and is incremented by 1 for each following testsuite -->
             package=""   <!-- Derived from testsuite/@name in the non-aggregated documents. optional -->
             skipped=""   <!-- The total number of skipped tests. optional -->
             time=""      <!-- Time taken (in seconds) to execute the tests in the suite. optional -->
             timestamp="" <!-- when the test was executed in ISO 8601 format (2014-01-21T16:17:18). Timezone may not be specified. optional -->
             >

        <!-- Properties (e.g., environment settings) set during test
         execution. The properties element can appear 0 or once. -->
        <properties>
          <!-- property can appear multiple times. The name and value attributres are required. -->
          <property name="" value=""/>
        </properties>

        <!-- testcase can appear multiple times, see /testsuites/testsuite@tests -->
        <testcase name=""       <!-- Name of the test method, required. -->
              assertions="" <!-- number of assertions in the test case. optional -->
              classname=""  <!-- Full class name for the class the test method is in. required -->
              status=""
              time=""       <!-- Time taken (in seconds) to execute the test. optional -->
              >

          <!-- If the test was not executed or failed, you can specify one
               the skipped, error or failure elements. -->

          <!-- skipped can appear 0 or once. optional -->
          <skipped/>

          <!-- Indicates that the test errored. An errored test is one
               that had an unanticipated problem. For example an unchecked
               throwable or a problem with the implementation of the
               test. Contains as a text node relevant data for the error,
               for example a stack trace. optional -->
          <error message="" <!-- The error message. e.g., if a java exception is thrown, the return value of getMessage() -->
             type=""    <!-- The type of error that occured. e.g., if a java execption is thrown the full class name of the exception. -->
             ></error>

          <!-- Indicates that the test failed. A failure is a test which
           the code has explicitly failed by using the mechanisms for
           that purpose. For example via an assertEquals. Contains as
           a text node relevant data for the failure, e.g., a stack
           trace. optional -->
          <failure message="" <!-- The message specified in the assert. -->
               type=""    <!-- The type of the assert. -->
               ></failure>

          <!-- Data that was written to standard out while the test was executed. optional -->
          <system-out></system-out>

          <!-- Data that was written to standard error while the test was executed. optional -->
          <system-err></system-err>
        </testcase>

        <!-- Data that was written to standard out while the test suite was executed. optional -->
        <system-out></system-out>
        <!-- Data that was written to standard error while the test suite was executed. optional -->
        <system-err></system-err>
      </testsuite>
    </testsuites>

     Example:
        <?xml version="1.0" encoding="UTF-8"?>
        <testsuites disabled="" errors="" failures="" name="" tests="" time="">
            <testsuite disabled="" errors="" failures="" hostname="" id=""
                       name="" package="" skipped="" tests="" time="" timestamp="">
                <properties>
                    <property name="" value=""/>
                </properties>
                <testcase assertions="" classname="" name="" status="" time="">
                    <skipped/>
                    <error message="" type=""/>
                    <failure message="" type=""/>
                    <system-out/>
                    <system-err/>
                </testcase>
                <system-out/>
                <system-err/>
            </testsuite>
        </testsuites>


    Attributes:
        options: Management options
        file_name: XML file name
        summary: Summary of results
        test_suite: JUnit test suite object
    """

    def __init__(self, file_name=None, options=None):
        if options is None:
            options = {'verbose': False}

        self.options = options
        self.file_name = file_name
        self.summary = None
        self._test_suite = None


    def load(self):
        """Load the target XML file.
        :return:
        """
        retobj = JUnitMgr.parseJUnit(file_name=self.file_name, options=self.options)
        self._test_suite = retobj.get('test_suite')
        self._fails = retobj.get('failed_tests')
        self.summary = retobj.get('summary')


    def results(self):
        return self.summary

    def show_fails(self):
        logging.info('*' * 72)
        logging.info("== Failed Tests ==")
        n = 0
        for tc in self._fails:
            print("{n}. {name}\n\t{message}\n".format(n=n, name=tc.name, message=html.unescape(tc.result.message)))
            n += 1

    def show_summary(self, display_only_failures=False, pretty=True):
        logging.info('*' * 72)
        logging.info("== SUMMARY ==")
        n = 0

        for ts in self._test_suite:
            if display_only_failures:
                if hasattr(ts, 'result') and (isinstance(ts.result, Failure) or isinstance(ts.result, Error)):
                    #print("{name}\n\t{message}".format(name=ts.name, message=ts.result.message))
                    print("{name}\n\t{message}\n".format(name=ts.name, message=html.unescape(ts.result.message)))
            else:
                _msg = None
                _result = None
                _tm = None

                if hasattr(ts, 'result'):

                    if hasattr(ts, 'time'):
                        _tm = ": {tm}".format(tm=ts.time)

                    if isinstance(ts.result, Error):
                        # results['message'] = ts.result.message
                        #print(ts.result.message)
                        _msg = ts.result.message
                        _result = "ERROR"

                    elif isinstance(ts.result, Failure):
                        # results['message'] = ts.result.message
                        #print(ts.result.message)
                        _msg = ts.result.message
                        _result = "FAIL"

                    elif ts.result is None:
                        _result = "PASS"
                        _msg = "PASS"

                if pretty and _msg is not None:
                    if _msg == "PASS":
                        print("{name} ... {result} {tm}".format(name=ts.name, result=_result, tm=_tm))
                    else:
                        print("{name} ... {result} {tm}\n\t{message}\n".format(name=ts.name, result=_result, tm=_tm, message=html.unescape(_msg)))
                elif not pretty:
                    print("== {} ==".format(n))
                    print("o name  : {}".format(ts.name))
                    print("o tag   : {}".format(ts._tag))
                    print("o time  : {}".format(ts.time))
                    print("o tests : {}".format(self._test_suite.tests))


            n += 1

        print('*' * 72)
        print("== SUMMARY ==")
        print("name: {}".format(self.summary.get('name')))
        print("failures: {}".format(self.summary.get('failures')))
        print("errors: {}".format(self.summary.get('errors')))
        print("tests: {}".format(self.summary.get('tests')))
        print("skipped: {}".format(self.summary.get('skipped')))
        print("time: {}".format(self.summary.get('time')))
        print("Results: {}".format(self.summary))

    def test_suite(self):
        return self._test_suite


    def readXML(self, f):
        suite = TestSuite('name')
        results = {'failures': 0, 'errors': 0, 'tests': 0, 'skipped': 0, 'time': 0 } #, 'message': None}
        p = XMLParser(huge_tree=True)
        tree = parse(f, parser=p)
        testsuite = tree.xpath('//testsuite')
        test_cases = tree.xpath('//testcase')

        if self.options.get('verbose'):
            logging.info("\ntest_cases.count => {}\n".format(test_cases.count))
            logging.info(dir(testsuite))

        for t in test_cases:
            tc = TestCase(t.get('name'))

            if self.options.get('verbose'):
                logging.info("[DEBUG] => {}\n".format(dir(t)))
                logging.info("[DEBUG] keys => {}\n".format(t.keys()))

            for child in t.iter():
                if self.options.get('verbose'):
                    logging.info("[DEBUG][child] {}".format(child))
                    logging.info("[DEBUG][child] tag : {}".format(child.tag))

                if child.tag == "failure":
                    tc.result = Failure()
                    logging.info("== failure found ==")

                elif child.tag == "error":
                    tc.result = Error()
                    tc.result.message = child.text

                    logging.info("[DEBUG][child] error: {}\n".format(child.text))

                elif child.tag == "skip" or child.tag == 'skipped':
                    tc.result = Skipped()

            if self.options.get('verbose'):
                logging.info("[DEBUG][TC] => classname: {}".format(t.get('classname')))
                logging.info("[DEBUG][TC] => name     : {}".format(t.get('name')))
                logging.info("[DEBUG][TC] => time     : {}".format(t.get('time')))

            tc.time = float(t.get('time'))
            tc.update_statistics()
            suite.add_testcase(tc)

        testSuites = testsuite[0]
        results['errors'] += int(testSuites.get('errors'))
        results['failures'] += int(testSuites.get('failures'))
        results['tests'] += int(testSuites.get('tests'))
        if hasattr(testSuites, 'skipped'):
            results['skipped'] += int(testSuites.get('skipped'))
            suite.add_property('skipped', int(testSuites.get('skipped')))

        suite.add_property('errors', int(testSuites.get('errors')))
        suite.add_property('failures', int(testSuites.get('failures')))
        suite.add_property('tests', int(testSuites.get('tests')))
        if hasattr(testSuites, 'time'):
            suite.add_property('time', int(testSuites.get('time')))

        if self.options.get('verbose'):
            logging.info(testsuite)
            logging.info(dir(testsuite[0].get('name')))
            logging.info("| name:{}".format(testSuites.get('name')))
            logging.info("| errors:{}".format(testSuites.get('errors')))
            logging.info("| failures:{}".format(testSuites.get('failures')))
            logging.info("| skipped:{}".format(testSuites.get('skipped')))
            logging.info("| tests:{}".format(testSuites.get('tests')))
            logging.info("| time:{}".format(testSuites.get('time')))

        # TODO: Save testsuite as Surefire XML file.
        # xml = JUnitXml()
        # xml.add_testsuite(suite)
        # xml.write('/tmp/x.xml')

        return suite


    @staticmethod
    def parse_xml(file_name, huge_tree=True, options=None):
        """Read a SureFire XML (JUNIT) formatted file.
        :param options:
        :param file_name:
        :param huge_tree:
        :return: TestSuite
        """
        if options is None:
            options = {'verbose': False}

        suite = TestSuite('name')
        results = {'failures': 0, 'errors': 0, 'tests': 0, 'skipped': 0, 'time': 0 } #, 'message': None}
        p = XMLParser(encoding='utf-8', huge_tree=huge_tree)

        tree = parse(source=file_name, parser=p)
        testsuite = tree.xpath('//testsuite')
        test_cases = tree.xpath('//testcase')

        if options.get('verbose'):
            logging.info("\ntest_cases.count => {}\n".format(test_cases.count))
            logging.info(dir(testsuite))

        for t in test_cases:
            tc = TestCase(t.get('name') if t.get('name') else 'case')

            if options.get('verbose'):
                logging.info("[DEBUG] => {}\n".format(dir(t)))
                logging.info("[DEBUG] keys => {}\n".format(t.keys()))

            for child in t.iter():
                if options.get('verbose'):
                    logging.info("[DEBUG][child] {}".format(child))
                    logging.info("[DEBUG][child] tag : {}".format(child.tag))

                src_line = ""
                if hasattr(child, 'sourceline'):
                    src_line = "(source line:{src})".format(src=child.sourceline)

                if child.tag == "testcase":
                    pass
                elif child.tag == "failure":
                    logging.info("== failure found ==")
                    tc.result = [ Failure(message="{text} {src}".format(text=child.text, src=src_line)) ]
                elif child.tag == "error":
                    tc.result = [ Error(message="{text} {src}".format(text=child.text, src=src_line)) ]
                elif child.tag == "skip" or child.tag == 'skipped':
                    tc.result = [ Skipped(message="{text} {src}".format(text=child.text, src=src_line)) ]
                elif child.tag == "system-out" or child.tag == "system-in":
                    pass
                else:
                    logging.debug("====== UNKNOWN TAG:{}".format(child.tag))


            logging.debug("=> classname: {}".format(t.get('classname')))
            logging.debug(" => name     : {}".format(t.get('name')))
            logging.debug(" => time     : {}".format(t.get('time')))

            tc.time = float(t.get('time'))

            logging.info("DEBUG => {}".format(type(tc)))
            logging.info("DEBUG.dir => {}".format(dir(tc)))

            suite.update_statistics()
            suite.add_testcase(tc)


        # logging.info(testsuite)
        # logging.info(dir(testsuite[0].get('name')))

        testSuites = testsuite[0]

        if options.get('verbose'):
            logging.info("| name:{}".format(testSuites.get('name')))
            logging.info("| errors:{}".format(testSuites.get('errors')))
            logging.info("| failures:{}".format(testSuites.get('failures')))
            logging.info("| skipped:{}".format(testSuites.get('skipped')))
            logging.info("| tests:{}".format(testSuites.get('tests')))
            logging.info("| time:{}".format(testSuites.get('time')))

        results['errors'] += int(testSuites.get('errors'))
        results['failures'] += int(testSuites.get('failures'))

        if hasattr(testSuites, 'skipped'):
            results['skipped'] += int(testSuites.get('skipped'))
            suite.add_property('skipped', int(testSuites.get('skipped')))

        results['tests'] += int(testSuites.get('tests'))

        suite.name = testsuite[0].attrib.get('name')
        suite.add_property('errors', int(testSuites.get('errors')))
        suite.add_property('failures', int(testSuites.get('failures')))
        suite.add_property('tests', int(testSuites.get('tests')))

        if hasattr(testSuites, 'name'):
            suite.add_property('name', testsuite[0].attrib.get('name'))

        if hasattr(testSuites, 'time'):
            suite.add_property('time', int(testSuites.get('time')))

        # logging.info(tree.xpath('//@name')[0])
        # return results
        # logging.info("****** tests:{}\n".format(suite.tests))

        # xml = JUnitXml()
        # xml.add_testsuite(suite)
        # xml.write('/tmp/x.xml')
        return suite


    @staticmethod
    def parseJUnit(file_name, options=None, parms=None):
        """
        Load XML file and manage overall metrics based on existing <testcase>'s.
        :param options:
        :param file_name:
        :param parms:
        :return:
        """
        if options is None:
            options = {'verbose': False}

        test_suites = None
        results = {'name': None, 'failures': 0, 'errors': 0, 'tests': 0, 'skipped': 0, 'time': 0 } #, 'message': None}
        try:
            # <class 'junitparser.junitparser.TestSuite'>
            # testSuites = JUnitXml.fromfile(f)
            test_suites = JUnitMgr.parse_xml(file_name, options)
        except Exception as ex:
            logging.critical(ex)

        results['name'] = test_suites.name
        results['errors'] += test_suites.errors
        results['failures'] += test_suites.failures

        if hasattr(test_suites, 'skipped'):
            results['skipped'] += test_suites.skipped

        results['tests'] += test_suites.tests
        results['time'] += test_suites.time

        failed_tests = []

        for ts in test_suites:
            if options.get('verbose'):
                logging.info("o name  : {}".format(ts.name))
                logging.info("o title : {}".format(ts._tag))
                logging.info("o time  : {}".format(ts.time))
                logging.info("o tests : {}".format(test_suites.tests))

            if hasattr(ts, 'result'):
                if isinstance(ts.result, Error):
                    #results['message'] = ts.result.message
                    failed_tests.append(ts)

                if isinstance(ts.result, Failure):
                    #results['message'] = ts.result.message
                    failed_tests.append(ts)

        return {'summary': results, 'test_suite': test_suites, 'failed_tests': failed_tests}


def parse_args():
    descr = """Manage reports to KineticaDB.
Kinetica Quality Engineering (2019)"""

    parser = argparse.ArgumentParser(description=descr, formatter_class=argparse.RawTextHelpFormatter,
                                     epilog="Kinetica Quality Engineering (2019)")
    parser.add_argument("--junit-file", type=str, help="JUNIT File")
    parser.add_argument("--log-level", choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
                        help="Set the logging level", default='ERROR')
    parser.add_argument("--summary", default=False, help="Summary", action="store_true")
    parser.add_argument("-v", "--verbose", default=False, help="Verbose", action="store_true")
    return parser.parse_args()


if __name__ == "__main__":
    ARGS = parse_args()

    if ARGS.log_level:
        logging.basicConfig(format='%(levelname)s: %(message)s [%(filename)s:%(lineno)d]', level=ARGS.log_level)

    junit_mgr = JUnitMgr(ARGS.junit_file, options={"verbose": ARGS.verbose})
    junit_mgr.load()

    print(junit_mgr.results()) if ARGS.summary else None
    junit_mgr.show_summary() if ARGS.verbose else None

    # logging.info("[DEBUG] {}".format(ARGS.junit_file))
    # results = JUnitMgr.parseJUnit(ARGS.junit_file)
    # logging.info(results)
