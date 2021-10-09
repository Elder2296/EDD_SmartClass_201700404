from Avl.Avl import *
from Avl.Students import *
from Homeworks.homework import Homework
from Analizer.parser import parser,types
from Graficadora.Graficadora import Graficadora
from Graficadora.Grafo  import Grafo
from TreeB.TreeB import Arbol_B
class Load():
    avl = AVL()
    treeB = Arbol_B(5)   
    contador = 0 
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
        
        print("Usuarios encontrados: "+str(len(students)))
        print("tareas encontradas: "+str(len(homewors)))
        #Add students to AVL
        for a in range(len(students)):
            #print("NAME STUDENT: "+students[a].name)
            self.avl.Insert(students[a])
            #print(students[a].getCarnet())
        #Add years to Student
        for b in range(len(homewors)):
            
            if (self.avl.search(homewors[b].carnet)):
                self.avl.getStudent(homewors[b].carnet).addYear(homewors[b].date.year)
        #Add mounths to years list
        
        for c in range(len(homewors)):
            if(self.avl.search(homewors[c].carnet)):
                if(self.avl.getStudent(homewors[c].carnet).FindYear(homewors[c].date.year)):
                    #first insert mounth on years list
                    self.avl.getStudent(homewors[c].carnet).getYear(homewors[c].date.year).addMounth(homewors[c].date.mounth)
                    #despues se inserte la tarea en la matriz
                    hour = homewors[c].hour
                    day = homewors[c].date.day
                    homewors[c].putId(self.contador)
                    self.contador = self.contador+1
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

    def createStudent(self, student):
        self.avl.Insert(student)
    def updateStudent(self, student):
        if self.avl.search(student.carnet):
            self.avl.getStudent(student.carnet).setDpi(student.dpi)  
            self.avl.getStudent(student.carnet).setName(student.name)
            self.avl.getStudent(student.carnet).setCarrera(student.carrera)
            self.avl.getStudent(student.carnet).setEmail(student.email)
            self.avl.getStudent(student.carnet).setPassword(student.password)
            self.avl.getStudent(student.carnet).setCredits(student.credits)
            self.avl.getStudent(student.carnet).setAge(student.age)
            print("Se actualizaron los datos")
        else:
            print("NO SE PUDO ACTUALIZAR")
            
            
    def getStudent(self, carnet):
        if self.avl.search(carnet):
            return self.avl.getStudent(carnet)
        return 0
            
            
            
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
                        g = Graficadora()
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
                            g = Graficadora()
                            g.generarLista(self.avl.getStudent(carnet).getYear(anio).getMounth(mounth).matriz.getNodoTareas(hour, day))
        elif type == 3:
            g = Grafo()
            g.generarGrafo(self.treeB.raiz)
        elif type == 4:
            carnet = int(peticion[0])
            anio = int(peticion[1])
            sem = int(peticion[2])
            if self.avl.search(carnet):
                if self.avl.getStudent(carnet).SearchYear(anio):
                    if self.avl.getStudent(carnet).getYear(anio).searchSem(sem):
                        g = Grafo()
                        g.generarGrafo(self.avl.getStudent(carnet).getYear(anio).getSemester(sem).tree.raiz)
            print("Debe generar el reporte 4")
    def LoadCursos(self, curso):
        self.treeB.insertar(curso)
    def AddCourseToStudent(self,carnet, anio, semester, course):

        if self.avl.search(int(carnet)):
            if self.avl.getStudent(int(carnet)).SearchYear(int(anio)):
                if self.avl.getStudent(int(carnet)).getYear(int(anio)).SearchSemester(int(semester)):
                    self.avl.getStudent(int(carnet)).getYear(int(anio)).getSemester(int(semester)).tree.insertar(course)
                    print('I maked to insertion')
                else:
                    print("No encontro el mes")  
    def AddHomework(self,homework):
        homework.putId(self.contador)
        self.contador = self.contador +1
        if self.avl.search(homework.carnet):
            if self.avl.getStudent(homework.carnet).yearsList.SearchYear(homework.date.year):
                if self.avl.getStudent(homework.carnet).yearsList.getYear(homework.date.year).SearchMounth(homework.date.mounth):  
                    self.avl.getStudent(homework.carnet).yearsList.getYear(homework.date.year).getMounth(homework.date.mounth).insertMatriz(homework.hour,homework.date.day,homework)
                
                    print('Insertion Perfect')
            else:
                self.avl.getStudent(homework.carnet).yearsList.addYear(homework.date.year)
                if self.avl.getStudent(homework.carnet).yearsList.getYear(homework.date.year).SearchMounth(homework.date.mounth):  
                    self.avl.getStudent(homework.carnet).yearsList.getYear(homework.date.year).getMounth(homework.date.mounth).insertMatriz(homework.hour,homework.date.day,homework)
                    print("Insertion Perfect")