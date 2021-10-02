from abc import ABC, abstractmethod

class Nodo(ABC):
    def __init__(self):
        self.left  = None
        self.right = None
        self.up = None
        self.down = None


        self.next = None
        self.back = None

    @abstractmethod
    def imprimir(self):
        pass

    @abstractmethod
    def getValue(self):
        pass