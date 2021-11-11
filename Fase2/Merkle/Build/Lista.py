from Merkle.Build.Nodo import Nodo
import hashlib
class Lista:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0
    
    def Insertar(self, Nuevonodo):
        nuevo = Nuevonodo
        if(self.first == None):
            self.first = nuevo
            self.last = nuevo
        else:
            aux = self.last
            aux.siguiente = nuevo
            self.last = nuevo
        self.size += 1
        return nuevo
    
    def VerificarLista(self,i):
        ntam = 2*(2**i)

        if ntam < self.size:
            return self.VerificarLista(i+1)
        else:
            return ntam
    def rellenar(self):
        tamanio = self.VerificarLista(1)
        relleno =""
        for i in range(tamanio-self.size):
            relleno +="0"
            nodo = Nodo(relleno)
            
            self.Insertar(nodo)
    def QuitarCeros(self):
        if(self.last==None):
            print()
        else:
            aux = self.first
            c = 0
            while aux != None:
                c +=1
                if(aux.siguiente.data[0] == '0'):
                    aux.siguiente = None
                    self.size = c    
                    break
                aux = aux.siguiente

    def print(self):
        aux = self.first
        c = 0
        while aux != None:
            c+=1
            print(str(c)+"  "+aux.data)
            aux = aux.siguiente
    def Encrypt (self, lista):
        aux = lista.first

        while aux != None:

            data = aux.data
            h = hashlib.sha256(str(data).encode())
            aux.data = h.hexdigest()

            aux = aux.siguiente
        
        
    def clone(self,newlista):
        aux = self.first
        while  aux != None:
            nodo =Nodo(aux.data)
            aux.arriba =  newlista.Insertar(nodo)
            aux = aux.siguiente
        
        return newlista
