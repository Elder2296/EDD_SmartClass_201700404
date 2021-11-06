from Grafo.Requisitos.Nodo import Nodo
class Lista:

    def __init__(self) -> None:
        self.first = None
        self.last = None
        self.size = 0
    def Insertar(self, codigo):
        
        nuevo = Nodo(codigo)

        if self.first == None:
            self.first = nuevo
            self.last = nuevo
        else:
            if self.verifyEquals(codigo):
                #Sí encuentra uno repetido, no lo agrega
                pass
            else:
                aux = self.last
                aux.siguiente = nuevo
                self.last = nuevo
        self.size += 1
    def verifyEquals(self,codigo):
        aux = self.first

        while aux!=None:
            #print("EXISTENTE: "+str(aux.id)+" NUEVO: "+str(codigo))
            if(aux.id is codigo):
                print("ENCONTRO IGUALES")
                return True

            aux = aux.siguiente

        
        return False
    def PrintCodigo(self):
        aux = self.first

        while aux!=None:
            print("        "+str(aux.id))
            aux = aux.siguiente
