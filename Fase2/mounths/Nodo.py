from matriz.Matriz import Matriz
class Nodo():
    def __init__(self, mounth):
        self.mounth = mounth
        self.next = None
        self.back = None
        self.matriz = Matriz()
        #Aqui debe ir una matriz
    def insertMatriz(self,hour,day,homework):
        #print('LLEGO A CASI INSERTAR')
        self.matriz.insert(hour,day,homework)
    def getTask(self, hour,day,position):
        self.matriz.getTask(hour,day,position)