class Date():
    def __init__(self,day, mounth, year) :
        self.day = day
        self.mounth = mounth
        self.year = year
    def getDate(self):
        return str(self.day)+"/"+str(self.mounth)+"/"+str(self.year)
    
    