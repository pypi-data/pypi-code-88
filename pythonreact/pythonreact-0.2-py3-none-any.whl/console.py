from rich import print
import os
from sys import platform


class Component:
    def __init__(self):
        if not hasattr(self, "state"):
            self.state = {}
        self.__mounted = False

    def mount(self):
        self.__mounted = True
        self.__output()

    def render(self) -> list:
        return []

    def __clear(self):
        if platform.lower() in ["win32", "win64", "windows"]:
            os.system("cls")
        else:
            os.system("clear")

    def set_state(self, new_state):
        for key in new_state:
            if key in self.state:
                self.state[key] = new_state[key]

        self.__output()

    def __build(self):
        text = ""

        for item in self.render():
            new_text = item
            if issubclass(type(item), Component):
                new_text = item.__build()
            text += str(new_text) + "\n"

        return text[:-1]

    def __output(self):
        if not self.__mounted:
            return

        self.__clear()
        print(self.__build())
