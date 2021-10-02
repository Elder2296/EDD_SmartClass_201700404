from Struct.List import Lista
from Struct.Nodo import Nodo

class Homeworks(Lista, Nodo):
    def __init__(self):
        Nodo.__init__(self)
        Lista.__init__(Nodo)
        self.row = 0
        self.column = 0
    def insert(self,row,column, homework):
        self.row = row
        self.column = column
        if self.first == None:
            self.first = homework
            self.last = homework
        else: #insertando al ultimo
            self.last.next = homework
            homework.back = self.last
            self.last = homework
    def Insert(self,homework):
        if self.first == None:
            self.first = homework
            self.last = homework
        else: #insertando al ultimo
            self.last.next = homework
            homework.back = self.last
            self.last = homework
        

    def print(self):
        tmp = self.first
        while tmp != None:
            print(tmp.getValue())
            tmp = tmp.next
    def getValue(self):
        tmp = self.first
        acum = ""
        while tmp != None:
            acum += tmp.getValue() +" "
            tmp = tmp.next
        return acum