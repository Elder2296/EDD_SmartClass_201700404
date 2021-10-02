from Struct.Nodo import Nodo

class Day(Nodo):
    def __init__(self,num):
        Nodo.__init__(self)
        self.number = num
    def imprimir(self):
        return self.number

    def getValue(self):
        return self.number