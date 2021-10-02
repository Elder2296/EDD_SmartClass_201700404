from Homeworks.Nodo import Nodo
class Homeworks():
    
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0
    def  Insert(self,row,column, homework):
        self.row = row
        self.column = column
        nuevo = Nodo(homework)
        if(self.first == None and self.last == None):
            self.first = nuevo
            self.last = nuevo
        else: 
            aux = self.first
            nuevo.next = None
            nuevo.back = aux
            
            aux.next = nuevo

            self.last = nuevo
        
        self.size = self.size + 1 
    