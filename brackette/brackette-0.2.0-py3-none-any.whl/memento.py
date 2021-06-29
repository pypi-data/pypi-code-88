from __future__ import annotations
from brackette.time import generateUTCTimestamp, tsToHuman
from abc import ABC, abstractmethod
from diff_match_patch import diff_match_patch
from hashlib import sha256

import json


class Originator:
    def __init__(self):
        self._state = ''

    def apply_diff(self, diff):
        dmp = diff_match_patch()
        patches = dmp.patch_fromText(diff)
        self._state, _ = dmp.patch_apply(patches, self._state)
        self.hash()

    def revert(self, memento: Memento) -> None:
        diff = memento.get_diff()
        self.apply_diff(diff)
        return self._state

    def backup(self):
        self.hash()
        return self._state

    def hash(self):
        self._hash = sha256(bytes(self._state, 'ascii')).digest().hex()

    def do_stuff(self, something):
        self._state = something


class OriginatorJSON(Originator):
    def __init__(self, object_state={}):
        super().__init__()
        self._object_state = object_state
        self._state = self.backup()

    def revert(self, memento: Memento):
        state = super().revert(memento)
        self._object_state = json.loads(state)
        return state

    def backup(self):
        self._state = json.dumps(self._object_state)
        return super().backup()


# https://refactoring.guru/design-patterns/memento/python/example
class Memento(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_date(self) -> str:
        pass


class ConcreteMemento(Memento):
    def __init__(self, diff: str) -> None:
        self._diff = diff
        self._date = generateUTCTimestamp()
        self._hash = sha256(bytes(diff, 'ascii')).digest().hex()

    def get_diff(self) -> str:
        return self._diff

    def get_name(self) -> str:
        return f"{tsToHuman(self._date)} {self._hash}"

    def get_date(self) -> str:
        return self._date


class Caretaker():
    def __init__(self, originator: Originator) -> None:
        self._past = []
        self._future = []
        self._originator = originator
        self._state = originator._state

    def backup(self) -> None:
        self._future = []
        original = self._state
        revision = self._originator.backup()
        diff = self.get_diff(revision, original)
        memento = ConcreteMemento(diff)
        self._past.append(memento)
        self._state = revision

    def get_diff(self, original, revision):
        dmp = diff_match_patch()
        patches = dmp.patch_make(original, revision)
        diff = dmp.patch_toText(patches)
        return diff

    def undo(self) -> None:
        if not len(self._past):
            return
        memento = self._past.pop()
        reverted = self._originator.revert(memento)
        current = self._state
        diff = self.get_diff(reverted, current)
        self._future.append(ConcreteMemento(diff))
        self._state = reverted

    def redo(self) -> None:
        if not len(self._future):
            return
        memento = self._future.pop()
        reverted = self._originator.revert(memento)
        current = self._state
        diff = self.get_diff(reverted, current)
        self._past.append(ConcreteMemento(diff))
        self._state = reverted

    def show_history(self) -> None:
        print("Caretaker: Here's the list of past mementos:")
        for memento in self._past:
            print(memento.get_name())
        print("Caretaker: Here's the list of future mementos:")
        for memento in self._future:
            print(memento.get_name())
