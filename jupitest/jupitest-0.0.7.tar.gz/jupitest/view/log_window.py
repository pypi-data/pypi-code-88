from viewable import Viewable
import tkinter as tk


class LogWindow(Viewable):
    def __init__(self, master, message):
        super().__init__()
        self._master = master
        self._message = message
        self._text = None

    def _build(self):
        self._body = tk.Toplevel()
        self._body.title("Log")
        scrollbar = tk.Scrollbar(self._body)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self._text = tk.Text(self._body, name="logWindow",
                             width=75, height=25)
        self._text.pack(side=tk.RIGHT, expand=1, fill=tk.BOTH)
        scrollbar.config(command=self._text.yview)
        self._text.config(yscrollcommand=scrollbar.set)

    def _on_map(self):
        super()._on_map()
        self._text.insert("0.0", self._message)
        self._text.config(state="disabled")

    def _on_destroy(self):
        pass
