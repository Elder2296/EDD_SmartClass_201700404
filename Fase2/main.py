from Avl.Avl import*
from Avl.Students import*
from Analizer.parser import parser,types
from Homeworks.homework import Homework
import hashlib
from TablaHash.Note import Note
from TablaHash.TablaHash import TablaHash
from Graficadora.Graph_TableHash import GraphTableHash
note = Note("titulo1","contenido1")
note2 = Note("titulo2","contenido2")
note3 = Note("titulo3","contenido3")
note4 = Note("titulo4","contenido4")
note5 = Note("titulo5","contenido5")
note6 = Note("titulo6","contenido6")
note7 = Note("titulo7","contenido7")
note8 = Note("titulo8","contenido8")

table = TablaHash(7)
table.Insert("201700404",note)
table.Insert("201700603",note2)
table.Insert("201981256",note3)
table.Insert("202032564",note4)
table.Insert("201800256",note5)
table.Insert("201800256",note3)
table.Insert("201538322",note6)
table.Insert("201700404",note7)
table.Insert("201700404",note8)
grafica = GraphTableHash()
grafica.graficar(table)
table.printNodos()



'''from TreeB.Curso import Curso
from TreeB.TreeB import Arbol_B
from Graficadora.Grafo import Grafo
curso = Curso(101,"Matemática Básica 1",7,"","true")
curso2 = Curso(39,"Deportes 1",7,"","true")
curso3 = Curso(348,"Quimica General 1",7,"","true")
curso4 = Curso(103,"Matemática Básica 2",7,"","true")
curso5 = Curso(5,"Tecnicas de Estudio",7,"","true")

arbol = Arbol_B(5)
arbol.insertar(curso)
arbol.insertar(curso2)
arbol.insertar(curso3)
arbol.insertar(curso4)
arbol.insertar(curso5)

g = Grafo()
g.generarGrafo(arbol.raiz)'''
'''path = "/home/losa/Ciencias_y_Sistemas/2021/Segundo_Semestre/Lab_Estructuras/Fase1/EDD_SmartClass_201700404/Fase2/Estudiantes.txt"
file = open(path,'r', encoding= 'utf-8')
message = file.read()
file.close()
print(message)
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
avl =AVL()
for a in range(len(students)):
    #print("NAME STUDENT: "+students[a].name)
    avl.Insert(students[a])
avl.createTree()'''

#h = hashlib.sha256("brC123abc".encode())
#print(h.hexdigest())



'''studen1 = Student(201700404,3063391290315,'Elder','Ciencias y Sistemas','el.ariel2296@gmail.com','brC123abc',106,24)
studen2 = Student(201700603,3063391290315,'Selvin','Quimica','el.ariel2296@gmail.com','brC123abc',106,24)
studen3 = Student(201700111,3063391290315,'Ariel','Ciencias y Sistemas','el.ariel2296@gmail.com','brC123abc',106,24)
studen4 = Student(201709063,3063391290315,'María','Electronica','el.ariel2296@gmail.com','brC123abc',106,24)
studen5 = Student(201700505,3063391290315,'Cindy','Mecanica','el.ariel2296@gmail.com','brC123abc',106,24)
studen6 = Student(201700396,3063391290315,'Obed','Ciencias y Sistemas','el.ariel2296@gmail.com','brC123abc',106,24)
studen7 = Student(201700146,3063391290315,'Isabel','Ambiental','el.ariel2296@gmail.com','brC123abc',106,24)
studen8 = Student(201700893,3063391290315,'Jeny','Electronica','el.ariel2296@gmail.com','brC123abc',106,24)
studen9 = Student(201700115,3063391290315,'Delmi','Ciencias y Sistemas','el.ariel2296@gmail.com','brC123abc',106,24)


avl = AVL()
avl.Insert(studen1)
avl.Insert(studen2)
avl.Insert(studen3)
avl.Insert(studen4)
avl.Insert(studen5)
avl.Insert(studen6)
avl.Insert(studen7)
avl.Insert(studen8)
avl.Insert(studen9)

if(avl.search(201700404)):
    print(avl.getStudent(201700404).getName())
else:
    print("No encontrado.")




avl.print()
avl.createTree()
print("arbol created")'''




'''
from Avl.Students import Student
from Analizer.parser import parser, types

if __name__ == '__main__':
    f = open('Estudiantes.txt','r', encoding= 'utf-8')
    message = f.read()
    f.close()
    #print(message)
    parser.parse(message)
    students = list()
    homeworks = list()
    print("largo de types: "+str(len(types)))
    for i in range(len(types)):
        
        if types[i] == "\"user\"":
            character = "\""
            student = Student(types[i+1].replace(character,""),types[i+2].replace(character,""),types[i+3].replace(character,""),types[i+4].replace(character,""),types[i+5].replace(character,""),types[i+6].replace(character,""),types[i+7],types[i+8])
            students.append(student)
        if types[i] == "task":
            task = "tarea "+ str(i+1)
            homeworks.append(task)

    print("ESTUDIANTES") 
    for x in range(len(students)):
        print("Carnet: "+students[x].getCarnet())
        print("Carnet: "+students[x].getName())'''

'''from Years.Years import *

anios = Years()

anios.Insert(2019)
anios.Insert(2014)
anios.Insert(2015)
anios.Insert(2016)

anios.Print()'''
def nextCousin(numero):
    nLimite = numero+10

    for c  in range(numero,nLimite,1):
        if(c>numero):
            lista = list()
            for div in range(c+1):
                if(div!=0):
                    if(c%div)==0:
                        lista.append(div)

            if(lista.__len__())==2:
                return c
                
    return nextCousin(nLimite)


number = 6000
#print("el siguiente numero primo de: "+str(number)+" ES: " + str(nextCousin(number)))
