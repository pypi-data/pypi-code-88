from .Modules import *


class DockWidget(QtWidgets.QDockWidget):
    remote = QtCore.Signal(QtCore.QObject)

    def __init__(self, parent):
        super().__init__(parent)
        self.project_frame = QtWidgets.QFrame(self)
        self.stacked = QtWidgets.QStackedLayout(self.project_frame)
        self.blank = QtWidgets.QFrame(self.project_frame)
        self.tree = ProjectTree(self.project_frame)
        self.title = QtWidgets.QLabel(self)
        self.arrange()

    def arrange(self):
        self.project_frame.setLayout(self.stacked)

        self.stacked.addWidget(self.blank)
        self.stacked.addWidget(self.tree)

        self.setTitleBarWidget(self.title)
        self.setWidget(self.project_frame)


class ProjectTree(QtWidgets.QTreeView):
    def __init__(self, parent):
        super().__init__(parent)
        self.tree_model = QtGui.QStandardItemModel()
        self.arrange()

    def arrange(self):
        self.setModel(self.tree_model)
        self.header().hide()

    def add_channel(self, item: QtGui.QStandardItem):
        self.tree_model.appendRow(item)
