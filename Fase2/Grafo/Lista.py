from Grafo.Nodo import Nodo
from Grafo.Requisitos.Lista import Lista as Aux
class Lista:
    def __init__(self) :
        self.first = None
        self.last = None
        self.listaaux = Aux()
        self.bodyline =""
        pass
    def InsertarCurso(self,curso):
        nuevo = Nodo(curso)

        if (self.first == None):
            self.first = nuevo
            self.last = nuevo
        else:
            aux = self.last
            aux.siguiente = nuevo
            self.last = nuevo
    def PrintAllCourses(self):
        aux = self.first

        while aux != None:
            print("Codigo curso: "+str(aux.curso.Codigo)+"  Nombre: "+aux.curso.nombre)
            aux.curso.PrintCodigos()
            aux = aux.siguiente
    
    def GenerateBodyDot(self, codigo):
        aux = self.first

        while aux!=None:
            if aux.curso.Codigo == codigo:
                self.bodyline +="node [ shape= box label= \""+aux.curso.Codigo+"\\n"+aux.curso.nombre+"\"] "+str(aux.curso.Codigo)+"\n"
                
                
                temp = aux.curso.requisitos.first

                while temp != None:
                    self.GenerateBodyDot(temp.id)
                    temp = temp.siguiente
                

            aux = aux.siguiente

        return self.bodyline
    def GenerateDirection(self,codigo):
        aux = self.first

        while aux!=None:
            
            if aux.curso.Codigo == codigo:
                    
                    
                temp = aux.curso.requisitos.first

                while temp != None:
                    direccion = str(codigo)+"--"+str(temp.id)
                    self.listaaux.Insertar(direccion)
                    self.GenerateDirection(temp.id)
                    temp = temp.siguiente
                

            aux = aux.siguiente
        self.getdireciones()
        return self.bodyline

    def getdireciones(self):
        aux = self.listaaux.first

        while aux != None:
            self.bodyline+= aux.id+"\n"
            aux = aux.siguiente
        
        self.listaaux = Aux()

    