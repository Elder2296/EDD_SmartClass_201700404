import os
from PIL import Image
class GraphTableHash:
    def __init__(self) -> None:
        
        pass
    def graficar(self, tabla):
        lineas ="digraph tabla{\n"
        lineas+= "node [shape = box]\n\n"
        lineas += self.recorrerColumnaPrincipal(tabla)
        lineas += self.recorrerApuntes(tabla)
        lineas+="\n\n}"
        self.createFile(lineas)
    def recorrerApuntes(self,tabla):
        temp = tabla.first
        lineas =""
        while temp != None:
            aux = temp.notes.first
            while aux != None:
                lineas+="node [label = \""+aux.note.title+"\\n"+aux.note.content+"\" width = 1.5] "+"NT"+str(aux.id)+str(temp.carnet)+"\n"
                
                aux = aux.siguiente
            temp = temp.siguiente
        


        temp = tabla.first
        lineas2 =""
        lineas3 =""
        while temp != None:
            aux = temp.notes.first
            if aux !=None:
                lineas2+= str(temp.carnet)+" -> "+"NT"+str(aux.id)+str(temp.carnet)+"\n"
            while aux.siguiente != None:
                lineas2+= "NT"+str(aux.id)+str(temp.carnet)+" -> "+"NT"+str(aux.siguiente.id)+str(temp.carnet)+"\n"
                
                aux = aux.siguiente
            
            aux = temp.notes.first
            if aux !=None:
                lineas3+= "{ rank = same;"+str(temp.carnet)+"; "
            while aux != None:
                lineas3+= "NT"+str(aux.id)+str(temp.carnet)+"; "
                
                aux = aux.siguiente
            lineas3+="}\n"
            lineas+=lineas3
            temp = temp.siguiente
        lineas += "\n\n"
        lineas+=lineas2
        
        return lineas
    def recorrerColumnaPrincipal(self,tabla):
        temp = tabla.first
        lineas =""
        while temp!= None:
            lineas+= "node [ label=\""+str(temp.carnet)+ "\" width = 1.5 style = filled, fillcolor = bisque ] "+str(temp.carnet)+"\n"

            temp = temp.siguiente
        temp = tabla.first

        while temp.siguiente != None:
            lineas+= str(temp.carnet)+" -> "+str(temp.siguiente.carnet)+"\n"
            temp = temp.siguiente

        return lineas
    def createFile(self, lineas):
        f = open('/home/losa/Escritorio/Reportes_F3/tablaHash.dot','w')
        try:
            f.write(lineas)
        finally:
            f.close()        
        prog = "dot -Tpng  /home/losa/Escritorio/Reportes_F3/tablaHash.dot -o /home/losa/Escritorio/Reportes_F3/tablaHash.png"
        os.system(prog)
        img = Image.open('/home/losa/Escritorio/Reportes_F3/tablaHash.png')
        img.show()