from typing import List
from Grafo.Lista import Lista


class Red:
    def __init__(self):
        self.listacursos = Lista()
        pass
    def Graficar(self, lista, codigo):
        self.listacursos = lista
        
        linesToFile ="graph {\n"
        linesToFile+= "rankdir = RL\n\n"
        linesToFile+=self.listacursos.GenerateBodyDot(codigo)
        self.listacursos.bodyline=""
        linesToFile+="\n\n"
        linesToFile+= self.listacursos.GenerateDirection(codigo)
        self.listacursos.bodyline=""
        linesToFile+="\n\n\n}"
        

        

        f = open('/home/losa/Escritorio/Reportes_F2/Red.dot','w')
        try:
            f.write(linesToFile)
        finally:
            f.close()

        