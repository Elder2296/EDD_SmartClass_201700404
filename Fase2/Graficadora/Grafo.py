import os
import queue

from PIL import Image

class Grafo:
    def __init__(self):
        pass

    def generarGrafo(self, raiz):

        # [ ACUMULADOR, ACUMULADORE DE ENLACES, CONTADOR PAGINA, CONTADOR AUX ]
        acumulador = ["digraph G\n{\nnode[shape = record, height= .1];\n", "", 0, 0]

        if raiz != None:
            cola = queue.Queue()
            cola.put(raiz)

            while not(cola.empty()): # Mientras la cola no este vacia
                tmpPagina = cola.get()
                self.imprimir(tmpPagina, acumulador)
                i = 0
                while i <= tmpPagina.cuenta:
                    if tmpPagina.ramas[i] != None:
                        cola.put(tmpPagina.ramas[i])
                    i += 1
                acumulador[2] += 1 #contador de pagina
            acumulador[0] += "\n" + acumulador[1]

        acumulador[0] += "}\n"

        f = open('/home/losa/Escritorio/Reportes_F3/treeB.dot', 'w')
        try:
            f.write(acumulador[0])
        finally:
            f.close()

        prog = "dot -Tpng  /home/losa/Escritorio/Reportes_F3/treeB.dot -o /home/losa/Escritorio/Reportes_F3/treeB.png"
        os.system(prog)
        img = Image.open('/home/losa/Escritorio/Reportes_F2/treeB.png')
        img.show()

    def imprimir(self, actual, acumulador):
        acumulador[0] += 'node{}[label="<r0>'.format(str(acumulador[2]))

        if actual.ramas[0] != None:
            acumulador[3] += 1 # contador auxiliar
            acumulador[1] += '"node{}":r0 -> "node{}"\n'.format(str(acumulador[2]) , str(acumulador[3]))

        i = 1
        while i <= actual.cuenta:
            acumulador[0] += '|<c{}> {} |<r{}>'.format(str(i),str(actual.claves[i].Codigo)+'\\n'+str(actual.claves[i].nombre),str(i))

            if actual.ramas[i] != None:
                acumulador[3] += 1 # contador auxiliar
                acumulador[1] += '"node{}":r{} -> "node{}"\n'.format(str(acumulador[2]) ,str(i), str(acumulador[3]))
            i += 1
        acumulador[0] += '"];\n'