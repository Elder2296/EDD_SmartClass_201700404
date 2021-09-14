from Avl.Avl import*
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



'''avl.insertar(21)
avl.insertar(12)
avl.insertar(36)
avl.insertar(9)
avl.insertar(24)'''


avl.print()
avl.createTree()
print("arbol created")