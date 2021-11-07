from Grafo.Nodo import Nodo
from Grafo.Requisitos.Lista import Lista as Aux
class Lista:
    def __init__(self) :
        self.first = None
        self.last = None
        self.listaaux = Aux()
        self.listaAuxbody = Aux()
        self.bodyline =""
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
                cabezas ="node [shape=box label=\""+aux.curso.Codigo+"\\n"+aux.curso.nombre+"\"] "+str(aux.curso.Codigo)
                  
                self.listaAuxbody.Insertar(cabezas)
                    
                temp = aux.curso.requisitos.first

                while temp != None:
                    self.GenerateBodyDot(temp.id)
                    temp = temp.siguiente
                

            aux = aux.siguiente

        
        

    

    def GenerateDirection(self,codigo,tipo):
        aux = self.first

        while aux!=None:
            
            if aux.curso.Codigo == codigo:
                    
                    
                temp = aux.curso.requisitos.first

                while temp != None:
                    direccion=""
                    if(tipo =="ponderado"):
                        direccion = str(temp.id)+"->"+str(codigo)+" [label =\""+str(self.getCreditos(temp.id))+"\"]"
                    else:
                        direccion = str(codigo)+"--"+str(temp.id)      
                    self.listaaux.Insertar(direccion)
                    self.GenerateDirection(temp.id,tipo)
                    temp = temp.siguiente
                

            aux = aux.siguiente
    def getCreditos(self, codigo):
        aux = self.first
        while aux != None:
            if aux.curso.Codigo == codigo:
                return aux.curso.creditos
            aux = aux.siguiente
        

    def getdireciones(self):
        aux = self.listaaux.first

        while aux != None:
            self.bodyline+= aux.id+"\n"
            aux = aux.siguiente
        
        self.listaaux = Aux()
        return self.bodyline
    def getBody(self):
        aux = self.listaAuxbody.first

        while aux != None:
            self.bodyline+=aux.id+"\n"
            aux = aux.siguiente
        
        self.listaAuxbody = Aux()
        return self.bodyline
    def GenerateRedCompleta(self):
        aux = self.first

        while aux!=None:

            cabeza = "node [shape=box label=\""+aux.curso.Codigo+"\\n"+aux.curso.nombre+"\"] "+str(aux.curso.Codigo)
            self.listaAuxbody.Insertar(cabeza)
            if not(aux.curso.requisitos.first ==None):
                
                temp = aux.curso.requisitos.first

                while temp != None:
                    self.GenerateBodyDot(temp.id)
                    temp = temp.siguiente
                

            aux = aux.siguiente


        

    def GenerateAllDirections(self):
        aux = self.first

        while aux!=None:
            
                
            temp = aux.curso.requisitos.first

            while temp != None:
                direccion = str(aux.curso.Codigo)+"--"+str(temp.id)
                self.listaaux.Insertar(direccion)
                self.GenerateDirection(temp.id,"")
                temp = temp.siguiente
      
            aux = aux.siguiente
            
        
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


    