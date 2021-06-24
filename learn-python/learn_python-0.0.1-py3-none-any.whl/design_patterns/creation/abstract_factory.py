from abc import ABC, abstractmethod


class ObjectA:
    def __init__(self):
        print("Hello from Object A")


class ObjectB:
    def __init__(self):
        print("Hello from Object B")


class AbstractFactory(ABC):

    @abstractmethod
    def create_object_a(self):
        pass

    @abstractmethod
    def create_object_b(self):
        pass


class ConcreteFactory(AbstractFactory):

    def create_object_a(self):
        return ObjectA()

    def create_object_b(self):
        return ObjectB()