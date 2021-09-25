from mounths.mounths import Mounths
from semesters.Semester import Semester
class Nodo():
    def __init__(self, year) :
        self.year = year
        self.mounths = Mounths()
        self.semesters = Semester()
        self.next = None
    def addMounth(self, mounth):
        if not(self.mounths.SearchMounth(mounth)):
            self.mounths.Insert(mounth)
        else:
            print("Mes repetido en el anio")
    def InsertSemester(self, semester):
        if not(semester < 1 and semester > 2):
            if not(self.semesters.SearchSemester(semester)):
                self.semesters.Insert(semester)