from mounths.Nodo import *
class Mounths():
    def __init__(self) :
        self.first = None
        self.last = None
        self.size = 0
    def Insert(self, mounth):
        nuevo = Nodo(mounth)
        if(self.first == None and self.last == None):
            self.first = nuevo
            self.last = nuevo
            
        else:
            aux = self.last
            aux.next = nuevo

            nuevo.next = None
            nuevo.back = aux
            self.last = nuevo

        self.size = self.size +1
    def Print(self):
        aux = self.first
        print("Mounths")
        while aux != None:
            print(aux.mounth)
            aux = aux.next
    def SearchMounth(self, mounth):
        found = False 
        aux = self.first
        while aux != None:
            if(aux.mounth == mounth):
                found = True
                break
            aux = aux.next
        return found
    def getMounth(self, mounth):
        aux = self.first
        while aux != None:
            if(aux.mounth == mounth):
                return aux
            
            aux = aux.next
        return 0



