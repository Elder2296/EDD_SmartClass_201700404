from mounths.mounths import Mounths
class Nodo():
    def __init__(self, year) :
        self.year = year
        self.mounths = Mounths()
        self.next = None
    def addMounth(self, mounth):
        find = False
        for i in range(len(self.mounths)):
            if (self.mounths[i].SearchYear(mounth)):
                find = True
        
        if find == False:
            self.mounths.Insert(mounth)
        