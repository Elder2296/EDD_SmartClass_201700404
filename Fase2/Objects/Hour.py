from Struct.Nodo import Nodo

class Hour(Nodo):
    def __init__(self,hour):
        Nodo.__init__(self)
        self.hour = hour
    def imprimir(self):
        return 'la hora es:' + str(self.hour)

    def getValue(self):
        return self.hour