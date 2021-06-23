#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Populate testapi with testscases - get local config.
"""

import os
import re
from collections import defaultdict
from yaml import load
from yaml import CLoader as Loader
from .output import (print_job, print_success, print_failed_and_exit,
                     print_skipped)

TESTCASE_FILE = 'testcases.yaml'
TESTAPI_URI_VAR = 'TEST_DB_URL'
PODS_FILE = 'pods.yaml'
NODE_NAME_VAR = 'NODE_NAME'

def get_testapi_url():
    """Get the testapi url from env vars."""
    print_job('🎯 get testapi url')
    api = os.environ.get(TESTAPI_URI_VAR) or ''
    if api == '':
        return print_failed_and_exit(
            f'Missing testapi url variable {TESTAPI_URI_VAR}')
    re_groups = re.findall(r"^(https?://.*/api/v\d?).*$", api)
    if re_groups:
        testapi_uri = re_groups[0]
        print_success()
        return testapi_uri
    return print_failed_and_exit(
        f'Bad testapi url variable {TESTAPI_URI_VAR} format: {api}')

def get_pods_list():
    """Get pods list."""
    print_job(f'📤 read {PODS_FILE}')
    try:
        with open(PODS_FILE, 'r') as file:
            pods = load(file, Loader=Loader)['pods']
        print_success()
        return pods
    except IOError:
        if os.environ.get(NODE_NAME_VAR):
            print_skipped()
            print_job(f'📤 get pods from ENV {NODE_NAME_VAR}')
            print_success()
            return [os.environ.get(NODE_NAME_VAR)]
        return print_failed_and_exit(
            f"Missing file '{PODS_FILE}' or var '{NODE_NAME_VAR}")

def get_testcases():
    """Get testscases from file."""
    print_job(f'📤 read {TESTCASE_FILE}')
    try:
        with open(TESTCASE_FILE, 'r') as file:
            testcases = load(file, Loader=Loader)
        print_success()
        return tests_by_project(testcases)
    except IOError:
        return print_failed_and_exit(f"Missing file'{TESTCASE_FILE}'")
    except KeyError:
        return print_failed_and_exit(f"Bad file syntax '{TESTCASE_FILE}'")

def tests_by_project(testcases):
    """Get tests by project mapping."""
    tests = defaultdict(list)
    for tiers in testcases['tiers']:
        for case in tiers['testcases']:
            tests[case['project_name']].append(case['case_name'])
    return tests
