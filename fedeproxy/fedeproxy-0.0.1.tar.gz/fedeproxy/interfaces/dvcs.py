import abc


class DVCS(abc.ABC):
    @abc.abstractmethod
    def clone(self, branch):
        ...

    @abc.abstractmethod
    def pull(self, branch):
        ...

    @abc.abstractmethod
    def push(self, branch):
        ...
