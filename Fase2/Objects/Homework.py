from Struct.Nodo import Nodo
class Homework(Nodo):
    def __init__(self,homework):
        Nodo.__init__(self)
        self.homework = homework
    def imprimir(self):
        pass

    def getValue(self):
        return self.homework