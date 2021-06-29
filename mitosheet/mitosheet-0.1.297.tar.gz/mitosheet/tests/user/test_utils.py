"""
Contains tests for the user utils, which determine the current
state of the user (e.g. should they upgrade).
"""
import pytest
from datetime import datetime, timedelta
import os

from mitosheet.user.schemas import USER_JSON_VERSION_1, USER_JSON_VERSION_2
from mitosheet.user.db import USER_JSON_PATH
from mitosheet.user import initialize_user, is_local_deployment, is_on_kuberentes_mito, is_running_test, should_display_feedback, should_upgrade_mitosheet
from mitosheet.tests.user.conftest import write_fake_user_json, today_str


def test_is_local():
    assert is_local_deployment()
    assert not is_on_kuberentes_mito()

def test_detects_tests():
    assert is_running_test()


def test_should_not_upgrade_on_first_creation():
    initialize_user()
    assert not should_upgrade_mitosheet()
    os.remove(USER_JSON_PATH)


def test_should_prompt_upgrade_after_21_days():
    write_fake_user_json(
        USER_JSON_VERSION_2,
        mitosheet_last_upgraded_date=(datetime.today() - timedelta(days=20)).strftime('%Y-%m-%d'),
    )

    initialize_user()
    assert not should_upgrade_mitosheet()

    write_fake_user_json(
        USER_JSON_VERSION_1,
        mitosheet_last_upgraded_date=(datetime.today() - timedelta(days=22)).strftime('%Y-%m-%d'),
    )

    initialize_user()
    assert should_upgrade_mitosheet()
    os.remove(USER_JSON_PATH)


FEEDBACK_TESTS = [
    (1, 2, True),
    (2, 2, False),
    (2, 7, True),
    (3, 7, False),
    (2, 8, False),
    (3, 8, False),
    (3, 19, False),
    (3, 20, True),
    (4, 20, False),
    (4, 34, False),
    (4, 35, True),
    (5, 35, False),
    (5, 36, False),
    (5, 48, False),
    (5, 49, True),
    (6, 50, False),
]
@pytest.mark.parametrize("num_feedbacks, num_usages, display_feedback", FEEDBACK_TESTS)
def test_should_ask_for_feedback_at_correct_time(num_feedbacks, num_usages, display_feedback):
    write_fake_user_json(
        USER_JSON_VERSION_2,
        feedbacks=['A'] * num_feedbacks,
        mitosheet_last_fifty_usages=[today_str] * num_usages
    )
    initialize_user()

    assert should_display_feedback() == display_feedback

