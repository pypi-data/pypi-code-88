#!/usr/bin/env python

__author__ = "Ilya Baldin"
__version__ = "0.1"
__maintainer__ = "Ilya Baldin"


import uuid

from pyforms.basewidget import BaseWidget
from pyforms.controls import ControlText
from pyforms.controls import ControlButton
from pyforms.controls import ControlTextArea
from pyforms.controls import ControlFile

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5 import QtWidgets

from wp_dso_publish import safe_helper
from os import path
import sys
import pkg_resources

"""
Displays appropriate forms for a Data Provider/DataSet Owner to issue GUIDs
to workflows and a dataset and register the policy for the dataset with the
associated SAFE server.
"""


class AppGUI(BaseWidget):

    _safe_default_url = 'http://localhost:7777/'
    _saved_settings = pkg_resources.resource_filename(__name__, 'saved-settings.py')
    _saved_settings_module = 'wp_dso_publish.saved-settings'

    def __init__(self):
        super(AppGUI, self).__init__('Dataset Policy Registration')

        # merge settings
        if path.exists(self._saved_settings):
            from confapp import conf
            conf += self._saved_settings_module
            confLoaded = True
        else:
            confLoaded = False

        # form fields
        self._wp1 = ControlText('Research Approval Workflow ID      ')
        if confLoaded and hasattr(conf, 'RESEARCH_APPROVAL_ID'):
            self._wp1.value = conf.RESEARCH_APPROVAL_ID
        self._wp1gen = ControlButton('Generate')
        self._wp2 = ControlText('Infrastructure Approval Workflow ID')
        if confLoaded and hasattr(conf, 'INFRASTRUCTURE_APPROVAL_ID'):
            self._wp2.value = conf.INFRASTRUCTURE_APPROVAL_ID
        self._wp2gen = ControlButton('Generate')
        self._ds = ControlText('Dataset ID                         ')
        if confLoaded and hasattr(conf, 'DATASET_ID'):
            self._ds.value = conf.DATASET_ID
        self._dsgen = ControlButton('Generate')
        self._safeURL = ControlText('SAFE Server URL', default=self._safe_default_url,
                                    helptext='Root URL of the SAFE server')
        if confLoaded and hasattr(conf, 'SAFE_URL'):
            self._safeURL.value = conf.SAFE_URL
        self._safePubKeyPath = ControlFile('SAFE Public Key Path')
        if confLoaded and hasattr(conf, 'PUBLIC_KEY_PATH'):
            self._safePubKeyPath.value = conf.PUBLIC_KEY_PATH
        self._push = ControlButton('Push Combined Policy to SAFE')
        self._save = ControlButton('Save Settings')
        self._quit = ControlButton('Quit')
        self._results = ControlTextArea()
        self._results.readonly = True
        self._results.autoscroll = True

        # button actions
        self._wp1gen.value = self._getGUIDClosure(self._wp1)
        self._wp2gen.value = self._getGUIDClosure(self._wp2)
        self._dsgen.value = self._getGUIDClosure(self._ds)
        self._push.value = self.__pushToSafe
        self._save.value = self.__save
        self._quit.value = self.__quit

        # formset layout
        self.formset = [{'B. SAFE Parameters': ['_safeURL', '_safePubKeyPath'],
                        'A. Workflows and Datasets': [('_wp1', '_wp1gen'), ('_wp2', '_wp2gen'), ('_ds', '_dsgen')]},
                        '=',
                        ('_quit', '_save', '_push'), '=', ('_results')]

    def _getGUIDClosure(self, field):
        """ couldn't find a way to determine the field for which the button is pressed """

        def genGUID(self):
            field.value = uuid.uuid4().__str__()

        return genGUID

    @staticmethod
    def _findMainWindow():
        """ find the main window of the app """
        app = QApplication.instance()
        for widget in app.topLevelWidgets():
            if isinstance(widget, QMainWindow):
                return widget
        return None

    @staticmethod
    def _resizeWindow():
        win = AppGUI._findMainWindow()
        if win is not None:
            sizePolicy = QtWidgets.QSizePolicy(
                QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
            win.setSizePolicy(sizePolicy)
            win.resize(800, 600)
            #win.show()
        else:
            print("Unable to find main window")

    @staticmethod
    def _warningWindow(message, explain):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Error: " + message)
        msg.setInformativeText(explain)
        msg.setWindowTitle("Error")
        msg.exec_()

    @staticmethod
    def _infoWindow(message, explain):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(message)
        msg.setInformativeText(explain)
        msg.setWindowTitle("Information")
        msg.exec_()

    def __save(self):
        with open(self._saved_settings, 'w') as f:
            if len(self._wp1.value) != 0:
                f.write(f"RESEARCH_APPROVAL_ID = '{self._wp1.value}'\n")
            if len(self._wp2.value) != 0:
                f.write(f"INFRASTRUCTURE_APPROVAL_ID = '{self._wp2.value}'\n")
            if len(self._ds.value) != 0:
                f.write(f"DATASET_ID = '{self._ds.value}'\n")
            if len(self._safePubKeyPath.value) != 0:
                f.write(f"PUBLIC_KEY_PATH = '{self._safePubKeyPath.value}'\n")
            if len(self._safeURL.value) != 0:
                f.write(f"SAFE_URL = '{self._safeURL.value}'\n")
        self._infoWindow("Settings Saved", "All settings have been saved and will be loaded "
                                           "next time you start the program")

    def __quit(self):
        sys.exit(0)

    def __pushToSafe(self):
        """ post the necessary rules"""

        # hash the pulic key of the principal
        try:
            principal = safe_helper.hash_key(self._safePubKeyPath.value)
        except safe_helper.SafeException as e:
            AppGUI._warningWindow(e.__str__(), "Please use the 'B' tab to fill the parameters")
            return

        if len(self._wp1.value) == 0 or \
                len(self._wp2.value) == 0 or \
                len(self._ds.value) == 0:
            AppGUI._warningWindow("Workflow or Dataset IDs are not unique",
                                  "Please specify or generate unique IDs for workflows "
                                  "and the dataset using the 'A' tab")
            return

        # create complete IDs for WF1, WF2 and DS
        wf1_id = ":".join([principal, self._wp1.value])
        wf2_id = ":".join([principal, self._wp2.value])
        dataset_id = ":".join([principal, self._ds.value])

        res1 = res2 = res3 = res4 = None

        try:
            res1 = safe_helper.post_raw_id_set(headUrl=self._safeURL.value, principal=principal)
            res2 = safe_helper.post_per_flow_rule(headUrl=self._safeURL.value, principal=principal, flowId=wf1_id)
            res3 = safe_helper.post_per_flow_rule(headUrl=self._safeURL.value, principal=principal, flowId=wf2_id)
            res4 = safe_helper.post_two_flow_data_owner_policy(headUrl=self._safeURL.value, principal=principal,
                                                          dataset=dataset_id, wf1=wf1_id, wf2=wf2_id)
        except safe_helper.SafeException as e:
            AppGUI._warningWindow(e.__str__(), f"Unable to post to SAFE server {self._safeURL.value}")
            self._results.value = "There was an error communicating with SAFE server"

        if self._results.value is None or self._results.value == "":
            # output the results needed by the user for Notary Service
            self._results.value = f"All policies have been posted to the SAFE server. \n\
Please take note of the following identifiers for the Notary Service: \n\n\
Research Approval Workflow ID: {wf1_id}\n\n\
Infrastructure Approval Workflow ID: {wf2_id}\n\n\
Dataset ID: {dataset_id}\n\n\n\
For debugging purposes here are SAFE identifiers for the posted policies:\n\
postRawIdSet = {res1}\n\
postPerFlowRule (Research Approval) = {res2}\n\
postPerFlowRule (Infrastructure Approval) = {res3}\n\
postTwoFlowDataOwnerPolicy = {res4}"
