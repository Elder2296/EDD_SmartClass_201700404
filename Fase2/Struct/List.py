from abc import ABC, abstractmethod

class Lista(ABC):
    def __init__(self):
        self.first = None
        self.last = None

    @abstractmethod
    def insert(self):
        pass

    '''@abstractmethod
    def Print(self):
        pass'''