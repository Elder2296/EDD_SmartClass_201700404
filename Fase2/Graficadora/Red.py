
from Grafo.Lista import Lista
import os
from PIL import Image

class Red:
    def __init__(self):
        self.listacursos = Lista()
        pass
    def Graficar(self, lista, codigo):
        self.listacursos = lista
        
        linesToFile ="graph {\n"
        linesToFile+= "rankdir = RL\n\n"
        self.listacursos.GenerateBodyDot(codigo)
        #Se debe eliminar todos los repetidos antes
        self.listacursos.verifyExist(self.listacursos.listaAuxbody.first)

        linesToFile+= self.listacursos.getBody()

        self.listacursos.bodyline=""
        linesToFile+="\n\n"
        
        self.listacursos.GenerateDirection(codigo)
        self.listacursos.verifyExist(self.listacursos.listaaux.first)
        linesToFile+= self.listacursos.getdireciones()
        self.listacursos.bodyline=""
        linesToFile+="\n\n\n}"
        

        

        f = open('/home/losa/Escritorio/Reportes_F3/Red.dot','w')
        try:
            f.write(linesToFile)
        finally:
            f.close()


        prog = "dot -Tpng  /home/losa/Escritorio/Reportes_F3/Red.dot -o /home/losa/Escritorio/Reportes_F3/Red.png"
        os.system(prog)
        img = Image.open('/home/losa/Escritorio/Reportes_F3/Red.png')
        img.show()
    def GraficarTodo(self, lista):
        self.listacursos = lista
        
        linesToFile ="graph {\n"
        linesToFile+= "rankdir = RL\n\n"
        
        
        
        self.listacursos.GenerateRedCompleta()
        self.listacursos.verifyExist(self.listacursos.listaAuxbody.first)

        linesToFile+= self.listacursos.getBody()

        self.listacursos.bodyline=""

        self.listacursos.GenerateAllDirections()
        self.listacursos.verifyExist(self.listacursos.listaaux.first)
        linesToFile+= self.listacursos.getdireciones()
        self.listacursos.bodyline=""
        linesToFile+="\n\n"
        
        linesToFile+="\n\n\n}"
        

        

        f = open('/home/losa/Escritorio/Reportes_F3/RedCompleta.dot','w')
        try:
            f.write(linesToFile)
        finally:
            f.close()
        
        prog = "dot -Tpng  /home/losa/Escritorio/Reportes_F3/RedCompleta.dot -o /home/losa/Escritorio/Reportes_F3/RedCompleta.png"
        os.system(prog)
        img = Image.open('/home/losa/Escritorio/Reportes_F3/RedCompleta.png')
        img.show()

        