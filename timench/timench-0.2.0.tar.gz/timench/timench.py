import time
import logging

from .templates import RESULTS

logging.basicConfig(level=logging.INFO)


class Timench:
    def __init__(self):
        self.funcs = {}
        self.times = {}
        self.reports = {}
        self.ctx_time_start = None
        self.ctx_time_end = None

    def __enter__(self):
        logging.info('Time measurement has begun ')
        self.ctx_time_start = time.perf_counter()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.ctx_time_end = time.perf_counter()
        exec_time = self.ctx_time_end - self.ctx_time_start
        logging.info('Run time = %g sec' % exec_time)

    def add_func(self, case_name: str, func):
        """
        Add function for time measurement to self.funcs dict

        :param case_name: case name as string
        :param func: function without ()
        :return: name variable
        """
        self.funcs[case_name] = func
        return case_name

    def add_results(self, case_name: str, times: list, report: str):
        """
        Add results of measurement to self.times and self.reports
        :param case_name: case name as string
        :param times: list with time values from output of time measurement
        :param report: report as string from output of time measurement
        :return:
        """
        self.times[case_name] = times
        self.reports[case_name] = report
        return case_name

    def get_report(self, case_name: str) -> str:
        """
        Get report by case name as string
        :param case_name: case name as string
        :return: str as report
        """
        return 'Case: %s\n%s' % (case_name, self.reports.get(case_name) or 'Report is not found. Rerun benchmark.')

    def get_reports(self):
        """
        Get all reports as dict
        :return: Timench.reports as dict
        """
        return self.reports

    def write_reports(self, filename: str = 'timench_report.txt', cases_names: list = None):
        """
        Write all reports to txt-file
        :param filename: filename for report writing as string
        :param cases_names: names of cases for report writing. All reports will be written if names is None
        :return: None
        """
        if self.reports:
            if not cases_names:
                cases_names = [_ for _ in self.reports]
            with open(filename, 'w') as file:
                file.write('TIMENCH REPORT\n---\n')
                for name in cases_names:
                    file.write('\nResults for %s\n' % name)
                    file.write(self.reports.get(name) or 'Report was not found\n')
        else:
            logging.info('No reports to write. Run all tests again')

    def get_times_by_name(self, case_name: str):
        """
        Get times list by case name
        :param case_name: case name as string
        :return: list of execution times as list
        """
        return self.times.get(case_name)

    def get_all_times(self):
        """
        Get times lists for all cases as dict
        :return: dict with Timench.times
        """
        return self.times

    def run(self, case_name: str, repeats: int, *args, **kwargs):
        """
        Run benchmark of single function by case name
        :param case_name: case name as string
        :param repeats: count of repeats as int
        :param args: *args for function by case name
        :param kwargs: **kwargs for function by case name
        :return: report as string
        """
        logging.info('Running: %s' % case_name)
        times, report = self.run_func(self.funcs[case_name], repeats, *args, **kwargs)
        self.add_results(case_name, times, report)
        return report

    def multiple_run(self, repeats, env_args: dict = None):
        """
        Batch run for multiple functions
        :param repeats: count of repeats as int
        :param env_args: dict with func(*args1, **kwargs1) by case name - {case_name1: [args, kwargs],}
                         args = list(...), kwargs = dict(...)
        :return: None
        """
        for case_name in self.funcs:
            args_case, kwargs_case = env_args[case_name] or [[], {}]
            self.run(case_name, repeats, *(args_case or []), **(kwargs_case or {}))

    @staticmethod
    def run_func(func, repeat_count: int = 1, *args, **kwargs):
        times = []
        for _ in range(repeat_count):
            time_start = time.perf_counter()
            func(*args, **kwargs)
            time_end = time.perf_counter()
            times.append(time_end - time_start)
        report = RESULTS % (func.__name__, sum(times), min(times), sum(times) / len(times), repeat_count)
        return times, report
