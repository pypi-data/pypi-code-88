from PySide2 import QtWidgets, QtCore, QtGui
import threading
import webbrowser

import RashSetup
from RashSetup import JsonHandler, TempHandler, Launcher
import os
import sys
import pathlib

__all__ = [
    "QtWidgets",
    "QtCore",
    "QtGui",
    "Misc",
    "StatusBar",
    "ClickLabel",
    "LAUNCHER",
    "JsonHandler"
]


class Misc:
    Media = pathlib.Path(__file__).parent / "Media"
    Gifs = Media / "Gifs"
    Icons = Media / "Icons"
    Logs = Media / "Logs"
    Settings = os.path.join(os.path.dirname(sys.executable), "settings.json")
    CMD = os.path.join(os.path.dirname(sys.executable), "RashCMD.exe")

    @staticmethod
    def ensure_paths():
        None if Misc.Logs.exists() else Misc.Logs.mkdir()


class SafeThread(threading.Thread, QtCore.QObject):
    progress = QtCore.Signal(object)
    finished = QtCore.Signal(object)

    def __init__(self, parent, name, target, with_progress=False, *args):
        threading.Thread.__init__(self)
        QtCore.QObject.__init__(self, parent)

        self.setName(name)
        self.target = target
        self.args = args
        self.with_progress = with_progress

    def run(self):
        return self.finished.emit(
            self.target(self.progress, *self.args) if self.with_progress else self.target(*self.args))


class QPixMovie(QtGui.QMovie):
    def __init__(self, gif, parent, ratio=None):
        super().__init__(str(gif))
        self.setParent(parent)
        self.ratio = ratio
        self.frameChanged.connect(self.release_pix)
        self.start()

    def release_pix(self):
        play = self.currentPixmap()
        play.setDevicePixelRatio(self.ratio if self.ratio else 1)
        self.parent().setPixmap(play)

    def running(self):
        return QtGui.QMovie.Running == self.MovieState


class ClickLabel(QtWidgets.QLabel):
    clicked = QtCore.Signal()
    double_clicked = QtCore.Signal()
    enter = QtCore.Signal()
    leave = QtCore.Signal()

    def __init__(self, parent):
        super().__init__(parent)
        self._movie = None
        self._ratio = StatusBar.Ratio
        self.setObjectName("ClickLabel")

    def mousePressEvent(self, event):
        self.clicked.emit()
        return super().mousePressEvent(event)

    def mouseDoubleClickEvent(self, event) -> None:
        self.double_clicked.emit()

        return super().mouseDoubleClickEvent(event)

    def enterEvent(self, event):
        self.enter.emit()

        return super().enterEvent(event)

    def leaveEvent(self, event):
        self.leave.emit()

        return super().leaveEvent(event)

    def load_gif(self, gif: str, ratio=None):
        self._movie = self._movie.setFileName(gif) if self._movie else QPixMovie(gif, self, ratio)

    def movie(self):
        return self._movie


class ReloadButton(ClickLabel):
    def __init__(self, parent, gif):
        super().__init__(parent)

        self.normal = gif, 19
        self.load_gif(*self.normal)

        self.movie().stop()

        self.mode = 0
        # 0 means free
        # 1 means loading
        # 2 means ready if there's an update

        self.enter.connect(lambda: self.toggle(1))
        self.leave.connect(lambda: self.toggle(0))
        self.clicked.connect(self.take_action)

        self.set_tips()

    def set_tips(self, normal=True):
        self.setStatusTip("Checks for updates !" if normal else "Checking for Updates!")
        self.setToolTip("Check update ?" if normal else "Scraping!")

    def toggle(self, result):
        if self.mode != 0:
            return

        self.movie().start() if result else self.movie().stop()

    def load(self):
        self.mode = 1
        self.set_tips(False)

        self.load_gif(str(Misc.Gifs / "loading.gif"), 6)
        crawler = SettingsCrawler()
        handler = JsonHandler(Misc.Settings).load()

        thread = SafeThread(
            self,
            "UpdaterCheckerThread",
            crawler,
            False,
            True,
            {
                handler["general"]["name"]: [handler["general"]["hosted"], str(Misc.Settings)]
            },
            lambda x: self.collect(x, crawler.close)
        )

        thread.start()

    def collect(self, meta, close_it):
        open("test.txt", "w").write(meta["Rash"]["update"])

        self.mode = 1
        self.set_tips()
        self.load_gif(*self.normal)

    def display_results(self, meta):
        self.setStatusTip(meta["title"])
        self.setToolTip(
            f"<h1> {meta['title']} </h1>"
            f"{meta['']}"
        )

    def take_action(self):
        try:
            self.load() if self.mode == 0 else None if self.mode == 1 else None
        except Exception as error:
            print(error)
            self.mode = 0


class StatusBar(QtWidgets.QStatusBar):
    Size = 40, 40
    Ratio = 26.0

    def __init__(self, parent):
        super().__init__(parent)

        self.refresh = ReloadButton(self, str(Misc.Gifs / "searching.gif"))
        self.git = ClickLabel(self)
        self.stay_safe = QtWidgets.QLabel(self)
        self.force_update = QtWidgets.QAction(self)
        self.searching = None
        self.working = threading.Lock()

        self.arrange()

    def arrange(self):
        self.addPermanentWidget(self.refresh)
        self.addPermanentWidget(self.git)
        self.addPermanentWidget(self.stay_safe)
        self.setSizeGripEnabled(False)

        self.git.clicked.connect(lambda x=True: webbrowser.open("https://github.com/RahulARanger/Rash"))

        resized = QtGui.QPixmap(str(Misc.Icons / "stay_safe.png"))
        resized.setDevicePixelRatio(StatusBar.Ratio)

        self.stay_safe.setPixmap(resized)
        self.stay_safe.setToolTip("Stay Safe")
        self.stay_safe.setStatusTip("Stay Safe and wear mask")

        self.refresh.setToolTip("Checks for update!")
        self.git.setStatusTip("Redirect to https://github.com/RahulARanger/Rash")
        self.git.setToolTip("Redirects to Github Page")
        self.git.load_gif(str(Misc.Gifs / "github.gif"), 20)


#%%%%%%%%%%%%%%%%%% SETTING UP %%%%%%%%%%%%%%%%%%%%%%%%%%

threading.current_thread().setName("Rash")  # setting the name of the Main Thread

LAUNCHER = RashSetup.Launcher(__file__)

