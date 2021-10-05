from Homeworks.Date import Date
class Homework():
    def __init__(self,carnet, name, description,materia,date, hour, state):
        self.carnet = int(carnet)
        self.name = name 
        self.description = description
        self.materia = materia
        arreglo = date.split(sep='/')
        day = int(arreglo[0])
        mounth = int(arreglo[1])
        year = int(arreglo[2])
        self.date = Date(day,mounth,year)
        arreglo2 = hour.split(sep = ':')
        self.hour = int(arreglo2[0])
        self.state = state
    def putId(self, id):
        self.id = id