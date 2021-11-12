from Years.Nodo import *

class Years():
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0
    def Insert(self, year):
        nuevo = Nodo(year)

        if(self.first == None and self.last == None ):
            self.first = nuevo
            self.last = nuevo
            self.first.next = None
            self.last.next = None
        else:
            aux = self.last
            nuevo.next = None
            aux.next = nuevo
            self.last = nuevo
        
        self.size = self.size+1
    




    def Print(self):
        aux = self.first
        while aux != None:
            print(aux.year)
            aux.mounths.Print()
            aux = aux.next
    def SearchYear(self, year):
        found = False
        aux = self.first
        while aux != None:
            if(aux.year == year):
                found = True
                return found
            aux = aux.next
        self.Insert(year)
        return self.SearchYear(year)
    def getYear(self, year):
        aux = self.first
        while aux != None:
            if(aux.year == year):
                return aux
            
            aux = aux.next
        return 0

    
