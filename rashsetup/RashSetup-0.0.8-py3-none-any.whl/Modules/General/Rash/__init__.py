import sys

from .Docks import *


class Home(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.setLayout(QtWidgets.QVBoxLayout())
        self.arrange()

    def arrange(self):
        pass


class PlugInHandler(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.setLayout(QtWidgets.QVBoxLayout())
        self.search = QtWidgets.QLineEdit(self)
        self.search_it = QtWidgets.QAction(self.search)
        self.arrange()

    def arrange(self):
        self.search.setAlignment(QtCore.Qt.AlignTop)
        self.layout().addWidget(self.search)

        self.search.setClearButtonEnabled(True)
        self.search.addAction(self.search_it, QtWidgets.QLineEdit.TrailingPosition)
        self.search_it.setIcon(QtGui.QIcon(str(Misc.Icons / "search.png")))


class RashMain(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.central = QtWidgets.QFrame(self)
        self.docks = DockWidget(self)
        self.status = StatusBar(self)
        self.tool_bar = QtWidgets.QToolBar(self)

        self.home = Home(self)
        self.stack_pages = QtWidgets.QStackedLayout()
        self.plugin = PlugInHandler(self.docks.project_frame)

        self.arrange()
        self.arrange_misc()
        self.arrange_window()

    # noinspection PyBroadException
    def arrange(self):
        Misc.ensure_paths()
        self.setMinimumSize(QtCore.QSize(600, 300))
        self.setStyleSheet(open(QtCore.QFileInfo(__file__).dir().filePath("dark_theme.qss")).read())
        self.setCentralWidget(self.central)
        self.central.setLayout(self.stack_pages)
        self.stack_pages.addWidget(self.home)

    def arrange_misc(self):
        self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, self.docks)
        self.setStatusBar(self.status)
        self.addToolBar(QtCore.Qt.LeftToolBarArea, self.tool_bar)

        home = QtWidgets.QToolButton(self.tool_bar)
        home.setIcon(QtGui.QIcon(str(Misc.Icons / "house.png")))
        self.tool_bar.addWidget(home)

        self.register_both(home, self.home, self.plugin, home.clicked, "Shop")

        workspace = QtWidgets.QToolButton(self.tool_bar)
        workspace.setIcon(QtGui.QIcon(str(Misc.Icons / "workspace.png")))

        self.tool_bar.addWidget(workspace)

        self.register_dock_channel(workspace, self.docks.tree, workspace.clicked, "Workspace")

        home.click()

    def arrange_window(self):
        self.setWindowTitle("Rash")
        self.setWindowIcon(QtGui.QIcon(str(Misc.Icons / "rash.ico")))

    def register_dock_channel(self, caller, channel, signal, title):
        self.docks.stacked.addWidget(channel)

        register_channel(
            caller,
            lambda: self.docks.stacked.setCurrentWidget(channel),
            lambda: self.docks.title.setText(title)
        )

        signal.connect(lambda: change_channel(getattr(caller, "__channel"))) if signal else None

    def register_both(self, caller, main_channel, dock_channel, signal, title):
        self.stack_pages.addWidget(main_channel)
        self.docks.stacked.addWidget(dock_channel)

        register_channel(
            caller,
            lambda: self.stack_pages.setCurrentWidget(main_channel),
            lambda: self.docks.stacked.setCurrentWidget(dock_channel),
            lambda: self.docks.title.setText(title)
        )

        signal.connect(lambda: change_channel(getattr(caller, "__channel"))) if signal else None
        # signal.connect(lambda: print(caller))

    def close(self):
        LAUNCHER.close()
        super().close()


def change_channel(actions):
    for _ in actions:
        _()


def register_channel(channel, *actions):
    setattr(channel, "__channel", actions)


class Start:
    def __init__(self):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

        self.initiate = QtWidgets.QApplication(sys.argv)
        temp = RashMain()
        temp.show()
        temp.adjustSize()

        self.initiate.exec_()
