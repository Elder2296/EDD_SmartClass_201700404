from Struct.Nodo import Nodo
class Homework(Nodo):
    def __init__(self,homework):
        Nodo.__init__(self)
        self.homework = homework
    def print(self):
        pass

    def getValue(self):
        return self.homework