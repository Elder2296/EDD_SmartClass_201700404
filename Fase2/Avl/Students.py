from Years.Years import Years
class Student():
    def __init__(self, carnet,dpi,name, carrera, email,password,credits, age):
        self.carnet = int(carnet)
        self.dpi = dpi
        self.name = name
        self.carrera = carrera
        self.email = email
        self.password = password
        self.credits = credits
        self.age = age
        self.yearsList= Years()

    def getCarnet(self):
        return self.carnet
    def getName(self):
        return self.name
    def getCarrera(self):
        return self.carrera
    def addYear(self, year):
        yearfound = 0
        if not( self.yearsList.SearchYear(year)):
            self.yearsList.Insert(year)
        
        



        