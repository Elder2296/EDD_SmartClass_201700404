from semesters.Nodo import Nodo
class Semester():
    def __init__(self) -> None:
        self.first = None
        self.last = None
        self.size = 0
    def Insert(self, semester):
        nuevo = Nodo(semester)
        if(self.first == None and self.last == None):
            self.first = nuevo
            self.last = nuevo
        else:
            aux = self.last
            nuevo.next = None
            aux.next = nuevo
            self.last = nuevo
        
        self.size = self.size +1
    def Print(self):
        aux = self.first
        while (aux != None):
            print(aux.semester)
            aux = aux.next
    def SearchSemester(self, semester):
        found = False
        aux = self.first
        while aux != None:
            if(aux.semester == semester):
                found = True
                break
        return found
    
    def getSemester(self, semester):
        aux = self.first

        while (aux != None):
            if(aux.semester == semester):
                return aux
            
        return 0