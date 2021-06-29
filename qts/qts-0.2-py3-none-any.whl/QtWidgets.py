# TODO: maybe manage to not bypass this strict check
#       https://github.com/python-qt-tools/qts/issues/8
# mypy: implicit_reexport

import qts


if qts.wrapper is None:
    qts.autoset_wrapper()

if qts.is_pyqt_5_wrapper:
    from PyQt5.QtWidgets import *
elif qts.is_pyqt_6_wrapper:
    from PyQt6.QtWidgets import *
elif qts.is_pyside_5_wrapper:
    from PySide2.QtWidgets import *
elif qts.is_pyside_6_wrapper:
    from PySide6.QtWidgets import *
else:
    raise qts.InvalidWrapperError(wrapper=qts.wrapper)
