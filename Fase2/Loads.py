from Avl.Avl import *
from Avl.Students import *
from Analizer.parser import parser,types
class Load():
    avl = AVL()    
    def __init__(self):
        print("Cargas")
    
    def loadStudents(self, path):
        print("desde la carga"+path)
        file = open(path,'r', encoding= 'utf-8')
        message = file.read()
        file.close()
        #print(message)
        parser.parse(message)
        students = list()
        for i in range(len(types)):
            if types[i] == "\"user\"":
                character = "\""
                student = Student(types[i+1].replace(character,""),types[i+2].replace(character,""),types[i+3].replace(character,""),types[i+4].replace(character,""),types[i+5].replace(character,""),types[i+6].replace(character,""),types[i+7],types[i+8])
                students.append(student)
        for a in range(len(students)):
            self.avl.Insert(students[a])
            print(students[a].getCarnet())    
            

        self.avl.print()
        self.avl.createTree()