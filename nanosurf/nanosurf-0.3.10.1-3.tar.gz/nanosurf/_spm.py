"""Package for scripting the Nansurf control software.
Copyright (C) Nanosurf AG - All Rights Reserved (2021)
License - MIT"""

import nanosurf.lowlevel
import win32com.client
import time
import psutil


class Spm():
    """Base class for dealing with Nanosurf SPMs."""
    _class_id = ""  # class_id  The COM class id string, if equal to SPM.Application: try to connect to any running application.

    def __init__(self, lu_shared_file_path: str=""):
        """Create the COM client to deal with the SPM.

        Parameter
        ---------
        lu_shared_file_path  Path to interface definition file, if empty, query the application for the path
        """

        # Connect or start application
        self.application = None
        if self._class_id == "SPM.Application":
            if not self._connect_to_running_app():
                print("Could not find a running Nanosurf SPM application.\nPlease start one first.")
                return
        else:
            try:
                self.application = win32com.client.Dispatch(self._class_id)
            except:
                print("Could not start application", self._class_id)
                pass

        #  If scripting is enabled finish startup and prepare subclasses
        if self.is_scripting_enabled():
            self._wait_for_end_of_startup()

        if self.is_lowlevel_scripting_enabled():
            self.lowlevel = nanosurf.lowlevel.Lowlevel(
                self.application.SPMCtrlManager, lu_shared_file_path)

    def _connect_to_running_app(self):
        """ try to connect to a running spm application instance """
        self._class_id = ""
        _known_spm_app_names_lowercase = [i.lower() for i in nanosurf._known_spm_app_names]
        
        for process in psutil.process_iter(['name']):
            procname = str(process.info['name'])
            if procname.endswith('.exe'):
                app_name = procname[:-4]
                if  app_name.lower() in _known_spm_app_names_lowercase:
                    self._class_id = app_name + ".Application"
                    self.application = win32com.client.Dispatch(self._class_id)
                    print("Connected to running app:" + app_name)
                    break
        return (self._class_id != "")
        # Should work like this but to watherever reason it gives only a runtime exception:
        # for app_name in _known_spm_app_names:
        #     if self._class_id == "":
        #         try:
        #             self._class_id = app_name + ".Application"
        #             self.application = win32com.client.GetActiveObject(self._class_id)
        #         except:
        #             pass

    def is_scripting_enabled(self):
        script_enabled = False
        if self.application is not None:
            self._wait_for_end_of_startup()
            if self.application.Scan is not None:
                script_enabled = True
        return script_enabled

    def is_lowlevel_scripting_enabled(self):
        ll_enabled = False
        if self.is_scripting_enabled():
            if self.application.SPMCtrlManager is not None:
                ll_enabled = True
        return ll_enabled

    def _wait_for_end_of_startup(self):
        if self.application.IsStartingUp:
            print("Waiting for controller startup.", end="")
            while self.application.IsStartingUp:
                time.sleep(1)
                print(".", end="")
            print()
