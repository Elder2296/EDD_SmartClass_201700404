from Struct.List import Lista
from Struct.Nodo import Nodo
from Objects.Homework import Homework

class Homeworks(Lista, Nodo):
    def __init__(self):
        Nodo.__init__(self)
        Lista.__init__(Nodo)
        self.row = 0
        self.column = 0
        self.size = 0
    def insert(self,row,column, homework):
        task = Homework(homework)
        self.row = row
        self.column = column
        if self.first == None:
            self.first = task
            self.last = task
        else: #insertando al ultimo
            self.last.next = task
            task.back = self.last
            self.last = task
        self.size = self.size+1
    def Insert(self,homework):
        task = Homework(homework)
        if self.first == None:
            self.first = task
            self.last = task
        else: #insertando al ultimo
            self.last.next = task
            task.back = self.last
            self.last = task
        self.size = self.size+1
        

    def imprimir(self):
        tmp = self.first
        while tmp != None:
            print(tmp.getValue())
            tmp = tmp.next
    def getValue(self):
        tmp = self.first
        acum = ""
        while tmp != None:
            acum += str(tmp.getValue()) +" "
            tmp = tmp.next
        return acum