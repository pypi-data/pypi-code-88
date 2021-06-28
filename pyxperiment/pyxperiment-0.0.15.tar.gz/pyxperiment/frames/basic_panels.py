"""
    pyxperiment/frames/basic_panels.py: Defines basic controls commonly used in
    applications

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

class TextPanel(wx.Panel):
    def __init__(self, parent, initval='', size=(35, -1), style=0, show_mod=False):
        super().__init__(parent, wx.ID_ANY)
        self.parent = parent
        self.last_value = initval
        self.edit = wx.TextCtrl(
            self, wx.ID_ANY,
            size=size,
            value=initval,
            style=style
            )
        if show_mod:
            self.Bind(wx.EVT_TEXT, self._on_text_change, self.edit)

    def _on_text_change(self, event):
        if self.IsModified():
            self.edit.SetForegroundColour((255, 0, 0))
        else:
            self.edit.SetForegroundColour((0, 0, 0))
        wx.PostEvent(self.parent.GetEventHandler(), event)

    def SetEnabled(self, value):
        if value:
            self.edit.Enable()
        else:
            self.edit.Disable()

    def SetEditable(self, value):
        self.edit.SetEditable(value)

    def GetValue(self):
        return self.edit.Value

    def SetValue(self, value):
        self.last_value = value
        self.edit.Value = value
        self.edit.SetForegroundColour((0, 0, 0))

    def IsModified(self):
        return self.edit.Value != self.last_value

class CaptionTextPanel(TextPanel):
    def __init__(self, parent, label, initval='', size=(35, -1), style=0, show_mod=False):
        super().__init__(parent, initval, size, style, show_mod)
        box = wx.StaticBox(self, -1, label)
        self.sizer = wx.StaticBoxSizer(box)
        self.sizer.Add(self.edit, 1, wx.ALL | wx.EXPAND, 2)
        self.SetSizer(self.sizer)
        self.sizer.Fit(self)

class CaptionDropBox(wx.Panel):
    def __init__(self, parent, label, values=None, style=wx.CB_READONLY):
        super().__init__(parent, wx.ID_ANY)

        box = wx.StaticBox(self, -1, label)
        sizer = wx.StaticBoxSizer(box)
        self.style = style

        self.combo = wx.ComboBox(self, style=style)
        if values:
            for value in values:
                self.combo.Append(value)
        self.Bind(wx.EVT_COMBOBOX, self.on_combo_change, self.combo)
        if self.style != wx.CB_READONLY:
            self.Bind(wx.EVT_TEXT, self.on_combo_change, self.combo)
        self.last_value = -1

        sizer.Add(self.combo, 1, wx.ALL | wx.EXPAND, 2)
        self.SetSizer(sizer)
        sizer.Fit(self)

    def SetItems(self, items):
        self.combo.Clear()
        for item in items:
            self.combo.Append(item)

    def SetEnabled(self, value):
        if value:
            self.combo.Enable()
        else:
            self.combo.Disable()

    def on_combo_change(self, event):
        del event
        if self.IsModified():
            self.combo.SetForegroundColour((255, 0, 0))
        else:
            self.combo.SetForegroundColour((0, 0, 0))

    def SetValue(self, value):
        if self.style == wx.CB_READONLY:
            self.last_value = self.combo.FindString(value)
            self.combo.SetSelection(self.last_value)
        else:
            self.last_value = value
            self.combo.SetValue(value)
        self.combo.SetForegroundColour((0, 0, 0))

    def GetValue(self):
        if self.style == wx.CB_READONLY:
            return self.combo.GetString(self.combo.GetSelection())
        return self.combo.GetValue()

    def IsModified(self):
        if self.style == wx.CB_READONLY:
            return self.last_value != self.combo.GetSelection()
        return self.last_value != self.combo.GetValue()

class ModifiedCheckBox(wx.CheckBox):

    def __init__(self, parent, label):
        super().__init__(parent, wx.ID_ANY, label=label, style=wx.CHK_3STATE)
        self.Set3StateValue(wx.CHK_UNDETERMINED)
        self.last_value = wx.CHK_UNDETERMINED
        self.Bind(wx.EVT_CHECKBOX, self._on_check_change, self)

    def _on_check_change(self, event):
        del event
        if self.IsModified():
            self.SetForegroundColour((255, 0, 0))
        else:
            self.SetForegroundColour((0, 0, 0))

    def SetValue(self, value):
        self.last_value = wx.CHK_CHECKED if value else wx.CHK_UNCHECKED
        self.Set3StateValue(self.last_value)
        self.SetForegroundColour((0, 0, 0))

    def GetValue(self):
        return self.Get3StateValue() == wx.CHK_CHECKED

    def IsModified(self):
        return self.last_value != self.Get3StateValue()

    def SetEnabled(self, value):
        if value:
            self.Enable()
        else:
            self.Disable()

class ActionButton(wx.Button):

    def __init__(self, parent, label, handler):
        super().__init__(parent, label=label)
        self._action_handler = handler
        self.Bind(wx.EVT_BUTTON, self._on_button, self)

    def IsModified(self):
        return False

    def _on_button(self, event):
        del event
        self._action_handler()

    def SetEnabled(self, value):
        if value:
            self.Enable()
        else:
            self.Disable()
