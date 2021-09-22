'''from Avl.Avl import*
from Avl.Students import*

studen1 = Student(201700404,3063391290315,'Elder','Ciencias y Sistemas','el.ariel2296@gmail.com','brC123abc',106,24)
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






avl.print()
avl.createTree()
print("arbol created")'''

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
        print("Carnet: "+students[x].getName())

        
