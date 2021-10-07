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
        if semester == 1 or semester == 2:
            if not(self.semesters.SearchSemester(semester)):
                self.semesters.Insert(semester)
    def getSemester(self, semester):
        return self.semesters.getSemester(semester)
    def getMounth(self, mounth):
        return self.mounths.getMounth(mounth)
    def SearchMounth(self, mounth):
        return self.mounths.SearchMounth(mounth)
    def SearchSemester(self,semester):
        if self.semesters.SearchSemester(semester):
            return True
        else:
            self.InsertSemester(semester)
            return True
    def searchSem(self,semester):
        return self.semesters.SearchSemester(semester)