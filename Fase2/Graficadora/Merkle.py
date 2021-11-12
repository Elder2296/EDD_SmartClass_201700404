import os
from Merkle.ListaLimpia.ListaLimpia.ListaLimpia import ListaLimpia
class Merkle:
    def __init__(self,data, namefile  ):
        self.namefile = namefile
        self.listaAux = ListaLimpia()
        self.listaAuxDirecciones = ListaLimpia() 
        self.lineas ="digraph G{\n\nrankdir = BT\n\n"
        self.direcciones=""
        self.buildbody(data)
        
        
    def buildbody(self, data):
        aux = data.first
        while aux !=None:
            self.BuildToTop(aux)
            
            aux = aux.siguiente
    def BuildToTop(self,nodo):
        if nodo.arriba != None:

            linea="node [shape = box label=\""+nodo.data+"\"] "+str(nodo.id)
            self.listaAux.Insertar(linea)
            direccion= str(nodo.id)+" -> "+str(nodo.arriba.id)+"\n"
            self.listaAuxDirecciones.Insertar(direccion)
            self.BuildToTop(nodo.arriba)

        linea ="node [shape = box label=\""+nodo.data+"\"] "+str(nodo.id)
        self.listaAux.Insertar(linea)        
    def generarFile(self):
        self.verifyExist(self.listaAux.first)
        self.verifyExist(self.listaAuxDirecciones.first)
        self.getBodyHeaders()
        self.getBodyDirections()
        self.lineas += "\n\n}"
        f = open('/home/losa/Escritorio/Reportes_F3/Merkle'+self.namefile+'.dot','w')
        try:
            f.write(self.lineas)
        finally:
            f.close()
        prog = 'dot -Tpng  /home/losa/Escritorio/Reportes_F3/Merkle'+self.namefile+'.dot -o /home/losa/Escritorio/Reportes_F3/Merkle'+self.namefile+'.png'
        os.system(prog)

    def getBodyHeaders(self):
        aux = self.listaAux.first

        while aux != None:
            self.lineas+=aux.id+"\n"
            aux = aux.siguiente
        
        self.listaAux = ListaLimpia()
    def getBodyDirections(self):
        aux = self.listaAuxDirecciones.first

        while aux != None:
            self.lineas+=aux.id+"\n"
            aux = aux.siguiente
        
        self.listaAux = ListaLimpia()
        
    def verifyExist(self,nodo):
        
        aux = nodo.siguiente

        while aux!= None:
            if aux.id == nodo.id:
                aux.anterior.siguiente = aux.siguiente

                if aux.siguiente != None:
                    aux.siguiente.anterior = aux.anterior
            
            aux = aux.siguiente
        
        if nodo.siguiente != None:
            return self.verifyExist(nodo.siguiente)
        
        return