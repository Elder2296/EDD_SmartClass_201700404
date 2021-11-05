from TablaHash.Nodo import Nodo
from TablaHash.NodoNote import NodoNote
class TablaHash:
    def __init__(self,_size) -> None:
        self.size = _size
        self.first = None
        self.factorCarga = 0.0 
        self.id = 0
    

    def Insert(self, carnet1, apunte):
        carnet = int(carnet1)
        self.factorCarga = (self.id/self.size)*100
        if self.buscarCarnet(carnet,apunte):
            pass
        else:

            if self.factorCarga < 50 and self.factorCarga >=0:
                llv = carnet % self.size
                self.InsertarHash(carnet,apunte,llv)
            else:
                #aqui va el codigo, para aumentar el tamaño la siguiente numero primero
                self.size = self.nextCousin(self.size)
                self.recargar()
                self.first = self.firstaux
                self.id = self.idaux
                self.Insert(carnet1, apunte)
                
    def recargar(self):
        temp = self.first
        self.firstaux = None
        self.idaux = 0
        while temp != None:
            llv = temp.carnet % self.size
            #Declarar un nodo nuevo
            nodo = Nodo(None,None,None)
            nodo.key = llv
            nodo.notes = temp.notes
            nodo.carnet = temp.carnet
            self.recargarHash(nodo,llv)
            temp = temp.siguiente


    def recargarHash(self, nodo,key):
        nodo.key = key
        if self.firstaux == None:
           
            self.firstaux = nodo
            self.idaux +=1
            return
               
        if self.buscarLlvAux(nodo.key):
            i=1
            pos = self.buscarPosaux(nodo,i)
            self.recargarHash(nodo,pos)
            
        else:
            tmp = self.firstaux 
            
            if nodo.key < tmp.key:
                nodo.siguiente = tmp
                self.firstaux= nodo
                self.idaux += 1
            else:
                
                while tmp.siguiente != None:
                    tmp2 = tmp.siguiente
                    if nodo.key <tmp2.key:
                        tmp.siguiente = nodo
                        nodo.siguiente = tmp2
                        self.idaux +=1
                        break
                    tmp = tmp.siguiente
                if tmp.siguiente == None:
                    tmp.siguiente = nodo
                    self.idaux += 1
        
    def buscarPosaux(self, nodo,i):
        pos = nodo.key + i*i
        n_pos = pos % self.size
        if self.buscarLlv(n_pos):
            i+=1
            return self.buscarPos(nodo,i)
        return n_pos
        
    def buscarLlvAux(self, llv):
        tmp = self.firstaux
        while tmp != None:
            if llv == tmp.key:
                return True
            tmp = tmp.siguiente
        return False

    def InsertarHash(self,carnet, apunte, llv):
        nuevo = Nodo(llv, carnet, apunte)

        if self.first == None:
            self.first = nuevo
            self.id += 1
            return

        if self.buscarLlv(llv):
            i=1
            pos = self.buscarPos(nuevo,i)
            self.InsertarHash(carnet,apunte,pos)
        else:
            tmp = self.first 
            if nuevo.key < tmp.key:
                nuevo.siguiente = tmp
                self.first= nuevo
                self.id += 1
            else:
                
                while tmp.siguiente != None:
                    tmp2 = tmp.siguiente
                    if nuevo.key <tmp2.key:
                        tmp.siguiente = nuevo
                        nuevo.siguiente = tmp2
                        self.id +=1
                        break
                    tmp = tmp.siguiente
                if tmp.siguiente == None:
                    tmp.siguiente = nuevo
                    self.id += 1




    def buscarPos(self, actual,i):
        pos = actual.key + i*i
        n_pos = pos % self.size
        if self.buscarLlv(n_pos):
            i+=1
            return self.buscarPos(actual,i)
        return n_pos

        
    def buscarLlv(self, llv):
        tmp = self.first
        while tmp != None:
            if llv == tmp.key:
                return True
            tmp = tmp.siguiente
        return False
    def buscarCarnet(self, carnet, apunte):
        tmp = self.first
        while tmp != None:
            if carnet == tmp.carnet:
                tmp.Insert(apunte)
                return True
            tmp = tmp.siguiente
        return False
    def nextCousin(self,numero):
        nLimite = numero+10

        for c  in range(numero,nLimite,1):
            if(c>numero):
                lista = list()
                for div in range(c+1):
                    if(div!=0):
                        if(c%div)==0:
                            lista.append(div)

                if(lista.__len__())==2:
                    return c
                    
        return self.nextCousin(nLimite)
    def printNodos(self):
        temp = self.first
        while temp != None:
            print("Llave: "+str(temp.key)+" Carnet: "+str(temp.carnet))
            temp = temp.siguiente


class ListaAux():
    def __init__(self):
        self.first = None
        pass

            