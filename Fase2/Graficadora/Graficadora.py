import os
from matriz.Matriz import Matriz

class Grafo:
    def __init__(self):
        pass
    def generarLista(self, nodo):
        info = "digraph List{\n"
        info = info +"rankdir = LR;\n"
        aux = nodo.first
        while aux != None:
            decla= 'node [shape = box label = \"Carnet: '+str(aux.getValue().carnet)+'\\nNombre: '+str(aux.getValue().name)+'\\nDescripcion: '+str(aux.getValue().description)+'\\nFecha: '+str(aux.getValue().date.getDate())+'\\nHora: '+str(aux.getValue().hour)+'\\nEstado: '+str(aux.getValue().state)+'\"]'+str(aux.getValue().id)+'\n'
            info = info + decla
            aux = aux.next

        aux2 = nodo.first

        while aux2.next != None:
            apuntar = str(aux2.getValue().id)+" -> "+str(aux2.next.getValue().id)+ '\n'
            #print(apuntar)
            info = info+ apuntar
            aux2 = aux2.next
        info = info +"}"

        f = open('/home/losa/Escritorio/Reportes_F2/Lista.dot','w')
        try:
            f.write(info)
        finally:
            f.close()

        prog = "dot -Tpng  /home/losa/Escritorio/Reportes_F2/Lista.dot -o /home/losa/Escritorio/Reportes_F2/Lista.png"
        os.system(prog)


    def generarMatriz(self, matriz):
        acumInfo = """digraph G{
                    node[shape=box, style=filled, color=deepskyblue3];
                    edge[color=black];
                    rankdir=UD;\n"""
        idCabeceraFila = ""
        cabeceraFila = ""

        idCabeceraCol = ""
        cabeceraCol = ""

        alineacionCol = "{rank=min; Matriz;"
        alineacionElementosFila = ""
        alineacionElementosColumna= ""

        cabeceraElementosFila = ""
        enlacesElementosFila = ""

        cabeceraElementosColumna = ""
        enlacesElementosColumna= ""

        # RECORRIDO DE FILAS
        eFila = matriz.Rows.first
        if eFila != None:
            cabeceraFila += 'Matriz -> "{}";\n'.format(str(hash(eFila)))
            #RECORRER TODAS LAS FILAS DE LA MATRIZ

            while eFila != None:
                #elemntos fila
                alineacionElementosFila += '{{rank=same; {};'.format(str(hash(eFila)))
                infoFilas = self.recorrerFilasMatriz(eFila)
                alineacionElementosFila += infoFilas[0] + "}\n"
                cabeceraElementosFila += infoFilas[1] + "\n"
                enlacesElementosFila += infoFilas[2] + "\n"


                idCabeceraFila += '"{}"[label = "{}"];\n'.format(str(hash(eFila)),str(eFila.getValue()))
                if eFila.next != None:
                    #filas
                    cabeceraFila += '"{}" -> "{}";\n'.format(str(hash(eFila)),str(hash(eFila.next)))
                eFila = eFila.next

            # idCabeceraFila += '"{}"[label = "{}"];\n'.format(str(hash(eFila)), str(eFila.getValue()))
            # # elemntos fila
            # alineacionElementosFila += '{{rank=same; {};'.format(str(hash(eFila)))
            # infoFilas = self.recorrerFilasMatriz(eFila)
            # alineacionElementosFila += infoFilas[0] + "}\n"
            # cabeceraElementosFila += infoFilas[1] + "\n"
            # enlacesElementosFila += infoFilas[2] + "\n"



        # RECORRIDO DE COLUMNAS
        eCol = matriz.Columns.first
        if eCol != None:
            cabeceraCol += 'Matriz -> "{}";\n'.format(str(hash(eCol)))
            while eCol != None:
                # elemntos Columna
                # alineacionElementosColumna += '{{rank=same; {};'.format(str(hash(eCol)))
                infoCols = self.recorrerColumnasMatriz(eCol)
                # alineacionElementosColumna += infoCols[0] + "}\n"
                # cabeceraElementosColumna += infoCols[1] + "\n"
                enlacesElementosColumna += infoCols[2] + "\n"

                #COLUMNAS
                alineacionCol += '"{}";'.format(str(hash(eCol)))
                idCabeceraCol += '"{}"[label="{}"];\n'.format(str(hash(eCol)),str(eCol.getValue()))
                if eCol.next != None:
                    cabeceraCol += '"{}" -> "{}";\n'.format(str(hash(eCol)),str(hash(eCol.next)))
                else:
                    alineacionCol += '}\n\n'
                eCol = eCol.next

            # alineacionCol += '"{}";}};\n\n'.format(str(hash(eCol)))
            # idCabeceraCol += '"{}"[label="{}"];\n'.format(str(hash(eCol)), str(eCol.getValue()))
            # elemntos Columna
            # alineacionElementosColumna += '{{rank=same; {};'.format(str(hash(eCol)))
            # infoCols = self.recorrerColumnasMatriz(eCol)
            # alineacionElementosColumna += infoCols[0] + "}\n"
            # cabeceraElementosColumna += infoCols[1] + "\n"
            # enlacesElementosColumna += infoCols[2] + "\n"

        acumInfo += alineacionCol + alineacionElementosFila  + alineacionElementosColumna\
                    + idCabeceraCol + idCabeceraFila  + cabeceraElementosFila +\
                     cabeceraElementosColumna + cabeceraCol + \
                    cabeceraFila +  enlacesElementosFila + \
                    enlacesElementosColumna + "\n}\n"

        f = open('/home/losa/Escritorio/Reportes_F2/grafo.dot','w')
        try:
            f.write(acumInfo)
        finally:
            f.close()

        prog = "dot -Tpng  /home/losa/Escritorio/Reportes_F2/grafo.dot -o /home/losa/Escritorio/Reportes_F2/grafo.png"
        os.system(prog)

    def recorrerFilasMatriz(self,nodoFila):
        rank = ""
        enlaces = ""
        cabeceras = ""
        tmp = nodoFila.right
        enlaces += '"{}" -> "{}";\n'.format(str(hash(nodoFila)), str(hash(tmp)))
        while tmp != None:
            rank += '"{}";'.format(str(hash(tmp)))
            cabeceras += '"{}"[label = "{}"];\n'.format(str(hash(tmp)), str(tmp.size))
            if tmp.right != None:
                enlaces += '"{}" -> "{}";\n'.format(str(hash(tmp)), str(hash(tmp.right)))
            tmp = tmp.right
        # cabeceras += '"{}"[label = "{}"];\n'.format(str(hash(tmp)), str(tmp.getValue()))
        return [rank,cabeceras,enlaces]

    def recorrerColumnasMatriz(self,nodoCol):
        rank = ""
        enlaces = ""
        cabeceras = ""
        tmp = nodoCol.down
        enlaces += '"{}" -> "{}";\n'.format(str(hash(nodoCol)), str(hash(tmp)))
        while tmp != None:
            rank += '"{}";'.format(str(hash(tmp)))
            cabeceras += '"{}"[label = "{}"];\n'.format(str(hash(tmp)), str(tmp.size))
            if tmp.down != None:
                enlaces += '"{}" -> "{}";\n'.format(str(hash(tmp)), str(hash(tmp.down)))
            tmp = tmp.down
        # cabeceras += '"{}"[label = "{}"];\n'.format(str(hash(tmp)), str(tmp.getValue()))
        return [rank,cabeceras,enlaces]