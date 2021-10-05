from Avl.Avl import *
from Avl.Students import *
from Homeworks.homework import Homework
from Analizer.parser import parser,types
from Graficadora.Graficadora import Grafo
class Load():
    avl = AVL()    
    def __init__(self):
        print("Cargas")
    
    def loadStudents(self, path):
        #print("desde la carga"+path)
        file = open(path,'r', encoding= 'utf-8')
        message = file.read()
        file.close()
        #print(message)
        parser.parse(message)
        students = list()
        homewors = list()
        character = "\""
        #Load students and homeworks to Lists
        for i in range(len(types)):
            if types[i] == "\"user\"":
                
                student = Student(types[i+1].replace(character,""),types[i+2].replace(character,""),types[i+3].replace(character,""),types[i+4].replace(character,""),types[i+5].replace(character,""),types[i+6].replace(character,""),types[i+7],types[i+8])
                students.append(student)
            if types[i] == "\"task\"":
                homework = Homework(types[i+1].replace(character,""),types[i+2].replace(character,""), types[i+3].replace(character,""), types[i+4].replace(character,""), types[i+5].replace(character,""), types[i+6].replace(character,""), types[i+7].replace(character,""))
                homewors.append(homework)
        

        #Add students to AVL
        for a in range(len(students)):
            self.avl.Insert(students[a])
            #print(students[a].getCarnet())
        #Add years to Student
        for b in range(len(homewors)):
            
            if (self.avl.search(homewors[b].carnet)):
                self.avl.getStudent(homewors[b].carnet).addYear(homewors[b].date.year)
        #Add mounths to years list
        contador =0
        for c in range(len(homewors)):
            if(self.avl.search(homewors[c].carnet)):
                if(self.avl.getStudent(homewors[c].carnet).FindYear(homewors[c].date.year)):
                    #first insert mounth on years list
                    self.avl.getStudent(homewors[c].carnet).getYear(homewors[c].date.year).addMounth(homewors[c].date.mounth)
                    #despues se inserte la tarea en la matriz
                    hour = homewors[c].hour
                    day = homewors[c].date.day
                    homewors[c].putId(contador)
                    contador = contador+1
                    self.avl.getStudent(homewors[c].carnet).getYear(homewors[c].date.year).getMounth(homewors[c].date.mounth).insertMatriz(hour, day, homewors[c])
        
        print("\nCARNET TASKS")
        for b in range(len(homewors)):
             print (homewors[b].carnet)
        print("\n STUDENTS")    
        self.avl.print()
        print("\n")
        self.avl.PrintYears() 
        '''if(self.avl.search(int(201900405))):

            print(self.avl.getStudent(201900405).getName())
        else:
            print("Not found")'''
        
        #self.avl.createTree()
    def Reports(self, type, peticion):
        if(type == 0):
            self.avl.createTree()
        elif(type == 1):
            #print("la peticion es: "+str(peticion[0])+" tipo: " +str(type(peticion[0]))) 
            carnet = int(peticion[0])
            anio = int(peticion[1])
            mounth = int(peticion[2])
            if self.avl.search(carnet):
                if self.avl.getStudent(carnet).SearchYear(anio):
                    if self.avl.getStudent(carnet).getYear(anio).SearchMounth(mounth):
                        print("Sí hay coincidencias")
                        g = Grafo()
                        g.generarMatriz(self.avl.getStudent(carnet).getYear(anio).getMounth(mounth).matriz)

        elif(type == 2):
            carnet = int(peticion[0])
            anio = int(peticion[1])
            mounth = int(peticion[2])
            day = int(peticion[3])
            hour = int(peticion[4])
            if self.avl.search(carnet):
                if self.avl.getStudent(carnet).SearchYear(anio):
                    if self.avl.getStudent(carnet).getYear(anio).SearchMounth(mounth):
                        print("Sí hay coincidencias")
                        #g = Grafo()
                        #g.generarMatriz(self.avl.getStudent(carnet).getYear(anio).getMounth(mounth).matriz)
                        if self.avl.getStudent(carnet).getYear(anio).getMounth(mounth).matriz.SearchHeader(hour,day):
                            g = Grafo()
                            g.generarLista(self.avl.getStudent(carnet).getYear(anio).getMounth(mounth).matriz.getNodoTareas(hour, day))
                               