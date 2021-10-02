from Hours.Nodo import Nodo 
class Header():
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0
    def Insert(self, hour):
        nuevo = Nodo(hour)
        if(self.first == None and self.last == None):
            self.first = nuevo
            self.last = nuevo
            return self.first
        elif nuevo.value < self.first.value:
            self.first.back = nuevo
            nuevo.next = self.first
            self.first = nuevo
            return self.first
        elif nuevo.value == self.first.value:
            return self.first
        
        elif nuevo.value > self.last.value:
            self.last.next = nuevo
            nuevo.back = self.last
            self.last = nuevo
            return self.last
        else:
            aux = self.first

            while aux.next != None:
                if nuevo.value > aux.value and nuevo.value < aux.next.value:
                    aux.next.back = nuevo
                    nuevo.next = aux.next
                    aux.next = nuevo
                    nuevo.back = aux
                    return nuevo
                elif nuevo.value == aux.value:
                    return aux
                aux = aux.next
            if nuevo.value == aux.value:
                return aux


        
        self.size = self.size + 1
    def SearchHour(self, hour):
        aux = self.first

        while (aux != None):
            if(aux.value == hour):
                return True
            
            aux = aux.next
        
        return False
    def getHour(self, hour):
        aux = self.first

        while aux != None:
            if(aux.value == hour):
                return aux
            
            aux = aux.next
        
        return None
    def Print(self):
        aux = self.first

        while aux != None:
            print(aux.value)
            aux = aux.next

        
