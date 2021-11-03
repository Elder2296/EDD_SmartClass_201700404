from TablaHash.Nodo import Nodo
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
                self.Insert(carnet1, apunte)
                
    
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
            