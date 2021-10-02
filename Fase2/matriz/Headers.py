from Struct.List import Lista


class Header(Lista):
    def __init__(self):
        Lista.__init__(self)
    
    def insert(self, nuevo):
        if self.first == None: # inserta al principio y devuelve el primero
            self.first = nuevo
            self.last = nuevo
            return self.first

        elif  nuevo.getValue() < self.first.getValue(): #insercion al inicio y lo retorna
            self.first.back = nuevo
            nuevo.next = self.first
            self.first = nuevo
            return self.first

        elif nuevo.getValue() == self.first.getValue(): #nuevo es igual a primero, retorna primero
            return self.first

        elif nuevo.getValue() > self.last.getValue(): # insercion al ultimo, returna ultimo
            self.last.next = nuevo
            nuevo.back = self.last
            self.last = nuevo
            return self.last

        else: # INSERCION AL MEDIO
            tmp = self.first
            while tmp.next != None:
                if nuevo.getValue() > tmp.getValue() and nuevo.getValue() < tmp.next.getValue():
                    tmp.next.back = nuevo
                    nuevo.next = tmp.next
                    tmp.next = nuevo
                    nuevo.back = tmp
                    return nuevo

                elif nuevo.getValue() == tmp.getValue(): #devuleve el valor que es igual
                    return tmp
                tmp = tmp.next

            if nuevo.getValue() == tmp.getValue():  # devuleve el valor que es igual
                return tmp


    def imprimir(self):
        tmp = self.first
        while tmp != None:
            print(tmp.getValue())
            tmp = tmp.next