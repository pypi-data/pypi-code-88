#!/usr/bin/env python
# coding: utf-8


from ._version import __version__


def _jupyter_labextension_paths():
    return [{"src": "lab_static", "dest": "cosapp_lab"}]
