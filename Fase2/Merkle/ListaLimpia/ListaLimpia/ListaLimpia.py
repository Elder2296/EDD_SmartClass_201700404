from Merkle.ListaLimpia.ListaLimpia.Nodo import Nodo

class ListaLimpia:
    def __init__(self) -> None:
        self.first = None
        self.last = None
        self.size = 0
    def Insertar(self, codigo):
        
        nuevo = Nodo(codigo)

        if self.first == None:
            self.first = nuevo
            self.last = nuevo
            self.size += 1

        else:
            
            aux = self.last
            aux.siguiente = nuevo
            nuevo.anterior = aux
            
            self.last = nuevo
            self.size += 1
    

    def PrintCodigo(self):
        aux = self.first

        while aux!=None:
            print("        "+str(aux.id))
            aux = aux.siguiente