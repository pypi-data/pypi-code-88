"""
    pyxperiment/frames/app_settings_frame.py: The window for basic application
    settings

    This file is part of the PyXperiment project.

    Copyright (c) 2021 PyXperiment Developers

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in
    all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
    THE SOFTWARE.
"""

import wx
import pyvisa

from pyxperiment.settings.core_settings import CoreSettings
from pyxperiment.settings.view_settings import ViewSettings

from .basic_panels import CaptionTextPanel, CaptionDropBox

class AppSettingsFrame(wx.Frame):
    """
    Application setup window
    """

    VISA_BACKENDS =  {
        'Default': '',
        'Python (pyvisa-py)': '@py',
        'Default IVI': '@ivi',
        'Keysight 32 bit': 'agvisa32.dll',
        'Visa dll 32 bit': 'visa32.dll',
        'Visa dll 64 bit': 'visa64.dll'
        }

    def __init__(self, parent):
        super().__init__(parent, wx.ID_ANY, 'Application settings',
                         style=wx.DEFAULT_FRAME_STYLE & (~(wx.RESIZE_BORDER|wx.MAXIMIZE_BOX)))
        self.parent = parent
        self.panel = wx.Panel(self)
        self.combo_visa_backend = CaptionDropBox(
            self.panel,
            'VISA backend',
            AppSettingsFrame.VISA_BACKENDS,
            wx.CB_DROPDOWN
            )
        self.combo_visa_backend.combo.SetFont(ViewSettings().MAIN_FONT)
        self.edit_x_devices = CaptionTextPanel(
            self.panel, 'X devices', size=(120, -1), show_mod=True
            )
        self.edit_x_devices.edit.SetFont(ViewSettings().MAIN_FONT)
        self.edit_y_devices = CaptionTextPanel(
            self.panel, 'Y devices', size=(120, -1), show_mod=True
            )
        self.edit_y_devices.edit.SetFont(ViewSettings().MAIN_FONT)

        self.btn_save = wx.Button(self.panel, label='Save', size=(120, -1))
        self.Bind(wx.EVT_BUTTON, self.on_save_button, self.btn_save)
        self.btn_save.SetFont(ViewSettings().BUTTON_FONT)
        self.btn_load = wx.Button(self.panel, label='Load', size=(120, -1))
        self.Bind(wx.EVT_BUTTON, self.on_load_button, self.btn_load)
        self.btn_load.SetFont(ViewSettings().BUTTON_FONT)

        self.vbox = wx.BoxSizer(wx.VERTICAL)
        self.vbox.Add(self.combo_visa_backend, flag=wx.ALIGN_CENTER_HORIZONTAL)
        self.vbox.Add(self.edit_x_devices, flag=wx.ALIGN_CENTER_HORIZONTAL)
        self.vbox.Add(self.edit_y_devices, flag=wx.ALIGN_CENTER_HORIZONTAL)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(self.btn_save, 0, border=10, flag=wx.ALL)
        hbox.Add(self.btn_load, 0, border=10, flag=wx.ALL)
        self.vbox.Add(hbox, 0, wx.ALIGN_CENTER_HORIZONTAL)
        self.panel.SetSizer(self.vbox)
        self.vbox.Fit(self)
        self.read_control()

    def on_save_button(self, _):
        self.write_control()
        self.read_control()
        self.Refresh()

    def on_load_button(self, _):
        self.read_control()
        self.Refresh()

    def read_control(self):
        self.edit_x_devices.SetValue(str(CoreSettings.get_writers()))
        self.edit_y_devices.SetValue(str(CoreSettings.get_readers()))
        manager = CoreSettings.get_resource_manager()
        for code,val in AppSettingsFrame.VISA_BACKENDS.items():
            if manager == val:
                manager = code
                break
        self.combo_visa_backend.SetValue(manager)

    def write_control(self):
        if (
            self.edit_x_devices.IsModified() or
            self.edit_y_devices.IsModified() or
            self.combo_visa_backend.IsModified()
            ):
            dlg = wx.MessageDialog(
                self,
                'Changing any parameters on this window requires application restart.',
                'Restart required',
                wx.YES_NO | wx.ICON_WARNING
                )
            if dlg.ShowModal() != wx.ID_YES:
                return
        if self.edit_x_devices.IsModified():
            CoreSettings.set_writers(str(self.edit_x_devices.GetValue()))
        if self.edit_y_devices.IsModified():
            CoreSettings.set_readers(str(self.edit_y_devices.GetValue()))
        if self.combo_visa_backend.IsModified():
            manager = self.combo_visa_backend.GetValue()
            if manager in AppSettingsFrame.VISA_BACKENDS:
                manager = AppSettingsFrame.VISA_BACKENDS[manager]
            # Test the connection
            try:
                pyvisa.ResourceManager(manager)
            except Exception as err:
                dlg = wx.MessageDialog(
                self,
                'The specified VISA backend is not valid. Please select a correct one or install pyvisa-py: ' + str(err),
                'Library not found', wx.OK | wx.ICON_ERROR
                )
                dlg.ShowModal()
                return
            CoreSettings.set_resource_manager(manager)
