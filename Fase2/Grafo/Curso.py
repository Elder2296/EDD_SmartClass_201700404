
from Grafo.Requisitos.Lista import Lista
class Curso:

    def __init__(self, Codigo, Nombre, creditos, prerequisitos, obligatorio):
        self.Codigo = Codigo
        self.nombre = Nombre
        self.creditos = int(creditos)
        self.requisitos = Lista()
        self.AddRequisitos(prerequisitos)
        self.obligatorio = obligatorio
        pass
    def AddRequisitos(self,lista):
        character ="\""
        arreglo = lista.replace(character,"")
        if arreglo == "":
            pass
        else:
            lista2 = arreglo.split(sep=',')
            for n in range(len(lista2)):
                identificador = lista2[n]
                self.requisitos.Insertar(identificador)
        
    def PrintCodigos(self):
        self.requisitos.PrintCodigo()
        

        