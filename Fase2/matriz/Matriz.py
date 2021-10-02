from Objects.Day import Day
from Objects.Hour import Hour
from matriz.Headers import Header
from matriz.Homeworks import Homeworks

class Matriz():
    def __init__(self):
        self.Rows = Header()
        self.Columns = Header()
    
    def insert(self, _hour, _day, homework):
        hour = Hour(_hour)
        responseRow = self.Rows.insert(hour)

        day = Day(_day)

        responseColumn = self.Columns.insert(day)

        if responseRow.right == None and responseColumn.down == None:
            nuevolc = self.newHomeworkList(_hour,_day,homework)
            #ASOCIANDO CABECERAS
            responseRow.right = nuevolc
            responseColumn.down = nuevolc
        elif responseRow.right != None and responseColumn.down == None: #FILA EXISTE  COLUMNA NO
            # enlazamos la nueva cabecera
            nuevolc = self.newHomeworkList(_hour,_day,homework)
            responseColumn.down = nuevolc
            # trabajo con el valor de las columnas
            #insercion al inicio
            if nuevolc.column < responseRow.right.column:
                nuevolc.right = responseRow.right
                responseRow.right.left = nuevolc
                responseRow.right = nuevolc
            else:
                tmp = responseRow.right
                flagInsercion = False
                while tmp.right != None:
                    if nuevolc.column > tmp.column and nuevolc.column < tmp.right.column: #INERCION AL MEDIO
                        nuevolc.right = tmp.right
                        tmp.right .left = nuevolc
                        tmp.right = nuevolc
                        nuevolc.left = tmp
                        flagInsercion = True
                    tmp = tmp.right

                if not flagInsercion:  #INSERCION AL FINAL
                    tmp.right = nuevolc
                    nuevolc.left = tmp

        elif responseRow.right == None and responseColumn.down != None: #COLUMNA EXISTE ; FILA NO
            # enlazamos la nueva cabecera
            nuevolc = self.newHomeworkList(_hour, _day, homework)
            responseRow.right = nuevolc
            # trabajo con el valor de las columnas
            # insercion al inicio
            if nuevolc.row < responseColumn.down.row:
                nuevolc.down = responseColumn.down
                responseColumn.down.up = nuevolc
                responseColumn.down = nuevolc
            else:
                tmp = responseColumn.down
                flagInsercion = False
                while tmp.down != None:
                    if nuevolc.row > tmp.row and nuevolc.row < tmp.down.row:  # INERCION AL MEDIO
                        nuevolc.down = tmp.down
                        tmp.down.up = nuevolc
                        tmp.down = nuevolc
                        nuevolc.up = tmp
                        flagInsercion = True
                    tmp = tmp.down

                if not flagInsercion:  # INSERCION AL FINAL
                    tmp.down = nuevolc
                    nuevolc.up = tmp
        else: # aca si existen las cabeceras
            nuevolc = self.newHomeworkList(_hour, _day, homework)
            flagInsFila = False
            flagInsCol = False


            #VALIDACIONES DEL INICIO
            #filas
            if nuevolc.column < responseRow.right.column:
                nuevolc.right = responseRow.right
                responseRow.right.left = nuevolc
                responseRow.right = nuevolc
                flagInsFila = True
            if nuevolc.row < responseColumn.down.row:
                nuevolc.down = responseColumn.down
                responseColumn.down.up = nuevolc
                responseColumn.down = nuevolc
                flagInsCol = True

            if not flagInsFila and flagInsCol:
                #encontrar el nulo de la fila
                tmpFila = responseRow.right
                find = False
                while tmpFila.right != None:
                    if nuevolc.column > tmpFila.column and nuevolc.column < tmpFila.right.column:
                        nuevolc.right = tmpFila.right
                        tmpFila.right.left = nuevolc
                        tmpFila.right = nuevolc
                        nuevolc.left = tmpFila
                        find = True
                    tmpFila = tmpFila.right

                if not find:
                    tmpFila.right = nuevolc
                    nuevolc.left = tmpFila

            elif not flagInsCol and flagInsFila:
                tmpCol = responseColumn.down
                find = False
                while tmpCol.down != None:
                    if nuevolc.row > tmpCol.row and nuevolc.row < tmpCol.down.row:
                        nuevolc.down = tmpCol.down
                        tmpCol.down.up = nuevolc
                        tmpCol.down = nuevolc
                        nuevolc.up = tmpCol
                        find = True
                    tmpCol = tmpCol.down

                if not find:
                    tmpCol.down = nuevolc
                    nuevolc.up = tmpCol
            else:
                columFound = False
                #encontrar el nulo de la fila
                #Primero busca en columnas
                tmpFila = responseRow.right
                find = False
                while tmpFila.right != None:
                    if nuevolc.column > tmpFila.column and nuevolc.column < tmpFila.right.column:
                        nuevolc.right = tmpFila.right
                        tmpFila.right.left = nuevolc
                        tmpFila.right = nuevolc
                        nuevolc.left = tmpFila
                        find = True
                    if tmpFila.column == _day:
                        columFound = True
                    tmpFila = tmpFila.right

                if not find and not columFound:
                    tmpFila.right = nuevolc
                    nuevolc.left = tmpFila
                


                rowFound = False
                tmpCol = responseColumn.down
                found = False
                while tmpCol.down != None:
                    if nuevolc.row > tmpCol.row and nuevolc.row < tmpCol.down.row:
                        nuevolc.down = tmpCol.down
                        tmpCol.down.up = nuevolc
                        tmpCol.down = nuevolc
                        nuevolc.up = tmpCol
                        found = True
                    if tmpCol.row == _hour and columFound:
                        tmpCol.Insert(homework)                        
                        rowFound = True

                    tmpCol = tmpCol.down

                if not found and not rowFound:
                    tmpCol.down = nuevolc
                    nuevolc.up = tmpCol

            
        



    def newHomeworkList(self,_hour, _day, homework):
        homeworklist = Homeworks()
        homeworklist.insert(_hour,_day, homework)
        return homeworklist



    