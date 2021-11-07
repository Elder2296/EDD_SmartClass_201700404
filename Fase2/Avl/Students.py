from Years.Years import Years
import hashlib
class Student():
    def __init__(self, carnet,dpi,name, carrera, email,password,credits, age):
        self.carnet = int(carnet)
        character = "\""
        self.dpi = dpi
        self.name = name
        self.nameDES =""
        self.carrera = carrera.replace(character,"")
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
        if not( self.yearsList.SearchYear(year)):
            self.yearsList.Insert(year)
    def FindYear(self,year):
        return self.yearsList.SearchYear(year)
    def getYear(self, year):
        return self.yearsList.getYear(year)
    def SearchYear(self,year):
        return self.yearsList.SearchYear(year)
    def setDpi(self, dpi):
        self.dpi = dpi
    def setName(self, name):
        self.name = name
    def setCarrera(self, carrera):
        self.carrera = carrera
    def setEmail(self, email):
        self.email = email
    def setPassword(self, pas):
        self.password = pas
    def setCredits(self,credits):
        self.credits = credits
    def setAge(self, age):
        self.age = age  
    def usertype(self, type):
        self.type = type
    def userFound(self):
        self.found = False



        