from TablaHash.NodoNote import NodoNote
class Lista:
    def __init__(self) -> None:
        self.first= None
        self.last = None
        self.size = 0
    
    def Insert(self, note):
        nuevo = NodoNote(note,self.size)

        if self.first == None:
            self.first = nuevo
            self.last = nuevo
        else:
            aux = self.last
            aux.siguiente = nuevo

            nuevo.siguiente = None
            self.last = nuevo
        self.size = self.size +1
    
    def Print(self):
        aux = self.first
        
        while aux != None:
            print(aux.note.title)
            aux = aux.siguiente