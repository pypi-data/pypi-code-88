# TODO: maybe manage to not bypass this strict check
#       https://github.com/python-qt-tools/qts/issues/8
# mypy: implicit_reexport

import qts


if qts.wrapper is None:
    qts.autoset_wrapper()

if qts.is_pyqt_5_wrapper:
    from PyQt5.QtGui import *
elif qts.is_pyqt_6_wrapper:
    from PyQt6.QtGui import *
elif qts.is_pyside_5_wrapper:
    from PySide2.QtGui import *
elif qts.is_pyside_6_wrapper:
    from PySide6.QtGui import *
else:
    raise qts.InvalidWrapperError(wrapper=qts.wrapper)
