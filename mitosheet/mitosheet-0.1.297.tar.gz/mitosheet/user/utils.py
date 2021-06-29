#!/usr/bin/env python
# coding: utf-8

# Copyright (c) Mito.
# Distributed under the terms of the Modified BSD License.

"""
Contains functions that are useful for determining the state of the
current user.
"""
import os
import getpass
from datetime import datetime

from mitosheet._version import __version__
from mitosheet.user.db import get_user_field
from mitosheet.user.schemas import (
    UJ_FEEDBACKS, UJ_MITOSHEET_LAST_UPGRADED_DATE, UJ_MITOSHEET_LAST_FIFTY_USAGES
)

def is_running_test():
    """
    A helper function that quickly returns if the current code is running 
    inside of a test, which is useful for making sure we don't generate 
    tons of logs.
    """
    # Pytest injects PYTEST_CURRENT_TEST into the current enviornment when running
    running_pytests = "PYTEST_CURRENT_TEST" in os.environ
    # Github injects CI into the enviornment when running
    running_ci = 'CI' in os.environ and os.environ['CI'] is not None

    return running_pytests or running_ci

def is_on_kuberentes_mito():
    """
    Returns True if the user is on Kuberentes Mito, on staging or on app
    """
    user = getpass.getuser()
    return user == 'jovyan'


def is_local_deployment():
    """
    Helper function for figuring out if this a local deployment or a
    Mito server deployment
    """
    return not is_on_kuberentes_mito()  


def should_upgrade_mitosheet():
    """
    A helper function that calculates if a user should upgrade, which does so by 
    checking if the user has upgraded in the past 21 days (3 weeks), since this is
    about how often we release big features.

    Always returns false if it is not a local installation, for obvious reasons.

    NOTE: if the user clicks the upgrade button in the app, then we change the upgraded 
    date to this date, so that the user doesn't get a bunch of annoying popups. This just
    pushes back when they are annoyed to upgrade!
    """
    if not is_local_deployment():
        return False

    mitosheet_last_upgraded_date = datetime.strptime(get_user_field(UJ_MITOSHEET_LAST_UPGRADED_DATE), '%Y-%m-%d')
    return (datetime.now() - mitosheet_last_upgraded_date).days > 21


def should_display_feedback():
    """
    The user gives an initial piece of feedback when they first sign up
    for Mito. Thus, all users have 1 piece of feedback. 
    
    We then expect them to give feedback on days: 2, 7, 20, 35, 49 
    of using the tool. We thus check the number of feedbacks they have
    given to that point.

    NOTE: as the user can submit feedback manually, this might be annoying
    for some users, as they might get prompted after they submit feedback.
    However, as we have never seen a user do this, we don't worry about it
    for now.
    """
    num_feedbacks = len(get_user_field(UJ_FEEDBACKS))
    num_days = len(get_user_field(UJ_MITOSHEET_LAST_FIFTY_USAGES))

    return (num_feedbacks <= 1 and num_days == 2) or \
        (num_feedbacks == 2 and num_days == 7) or \
        (num_feedbacks <= 3 and num_days == 20) or \
        (num_feedbacks <= 4 and num_days == 35) or \
        (num_feedbacks <= 5 and num_days == 49)

