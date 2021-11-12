from os import PRIO_PGRP
from Avl.Avl import *
from Avl.Students import *
from Homeworks.homework import Homework
from Analizer.parser import parser,types
from Graficadora.Graficadora import Graficadora
from Graficadora.Grafo  import Grafo
from Graficadora.Graph_TableHash import GraphTableHash
from TreeB.TreeB import Arbol_B
import hashlib
from TablaHash.TablaHash import TablaHash
from TablaHash.Note import Note
from Graficadora.Graph_TableHash import GraphTableHash
from Grafo.Lista import Lista
from Graficadora.Red import Red
from Graficadora.Merkle import Merkle as GraphMerkle
from cryptography.fernet import Fernet
from Merkle.Build.Lista import Lista as Merkle
from Merkle.Build.Nodo import Nodo as NodoMerkle





class Load():
    avl = AVL()
    treeB = Arbol_B(5)   
    tablaHash = TablaHash(7)
    contador = 0 
    listacursos = Lista()
    listaasignaciones = Merkle()
    listaApuntes = Merkle()
    listaEstudiantes = Merkle()
    
    def __init__(self):
        print("Cargas")
        self.clave = Fernet.generate_key()
        self.capa = Fernet(self.clave)
        self.id =1
    
    def loadApunte(self,carnet,title, content,data):
        
        note = Note(title,content)
        nodo = NodoMerkle(data)
        self.listaApuntes.Insertar(nodo)
        self.tablaHash.Insert(carnet,note)
    
    def CreateGraphTableHash(self):
        graficator = GraphTableHash()
        graficator.graficar(self.tablaHash)
        
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
                dpi = str(types[i+2]).replace(character,"")
                carnet = types[i+1].replace(character,"")
                name = types[i+3].replace(character,"")
                email =types[i+5].replace(character,"")
                contrasenia = types[i+6].replace(character,"")
                age = types[i+8]
                pa = hashlib.sha256(str(contrasenia).encode())
                passEncript = pa.hexdigest()
                
                
                
                nuevodpi = self.capa.encrypt(str(dpi).encode())
                nuevoname = self.capa.encrypt(str(name).encode())
                nuevoemail = self.capa.encrypt(str(email).encode())
                nuevopass = self.capa.encrypt(str(passEncript).encode())
                nuevaedad = self.capa.encrypt(str(age).encode())
                

                #print(h.hexdigest())  

                student = Student(carnet,nuevodpi,nuevoname,types[i+4],nuevoemail,nuevopass,types[i+7],nuevaedad)
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

    def createStudent(self, carnet, dpi,nombre,carrera,email, pas, creditos,edad,data):
        nodo = NodoMerkle(data)
        self.listaEstudiantes.Insertar(nodo)
        age = edad
        pa = hashlib.sha256(str(pas).encode())
        passEncript = pa.hexdigest()
                
                
                
        nuevodpi = self.capa.encrypt(str(dpi).encode())
        nuevoname = self.capa.encrypt(str(nombre).encode())
        nuevoemail = self.capa.encrypt(str(email).encode())
        nuevopass = self.capa.encrypt(str(passEncript).encode())
        nuevaedad = self.capa.encrypt(str(age).encode())
                

                #print(h.hexdigest())  

        student = Student(carnet,nuevodpi,nuevoname,carrera,nuevoemail,nuevopass,creditos,nuevaedad)

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
            
            
            


    ##REPORTES


    def Reports(self, type, peticion):
        if(type == 0):
            tipo = peticion[0]
            if tipo == "Encrypt":
                self.avl.createTree(self.clave)
            else:
                self.avl.createTreeDes(self.clave)
                print("ARBOL DESENCRIPTADO")
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
                print("Encontro estudiante")
                if self.avl.getStudent(carnet).SearchYear(anio):
                    print("Encontro año")
                    if self.avl.getStudent(carnet).getYear(anio).searchSem(sem):
                        print("encontro semestre")
                        g = Grafo()
                        g.generarGrafo(self.avl.getStudent(carnet).getYear(anio).getSemester(sem).tree.raiz)
                        print("Debe generar el reporte 4")
                    else:
                        print("No encontro el semestre")
                else:
                    print("No encontro el año")
            else:
                print("No encontro Estudiante")
        elif type ==5:
            red = Red()
            red.Graficar(self.listacursos,peticion)
            #self.listacursos.PrintAllCourses()
        elif type == 6:
            graficartabla = GraphTableHash()
            graficartabla.graficar(self.tablaHash)
            
        elif type == 7:
            red = Red()
            red.GraficarTodo(self.listacursos)
        elif type == 8:
            #Recuperacion de estado
            self.id = 1
            self.listaApuntes.rellenar()
            #lista que llevara los encabezados encriptados
            listaEncrypt = Merkle()
            #se hace un clon de la lista principal de data
            self.listaApuntes.clone(listaEncrypt)
            #se encrypta la lista de headers
            self.listaApuntes.Encrypt(listaEncrypt)
            self.putId(self.listaApuntes, listaEncrypt)

            
            self.BuildTreeMerkle(listaEncrypt,Merkle())

            buildTree = GraphMerkle(self.listaApuntes,'apuntes')
            buildTree.generarFile()
            self.listaApuntes.QuitarCeros()
        elif type == 9:
            self.id =1
            #Recuperacion de estado
            self.listaasignaciones.rellenar()
            #lista que llevara los encabezados encriptados
            listaEncrypt = Merkle()
            #se hace un clon de la lista principal de data
            self.listaasignaciones.clone(listaEncrypt)
            #se encrypta la lista de headers
            self.listaasignaciones.Encrypt(listaEncrypt)
            self.putId(self.listaasignaciones, listaEncrypt)

            
            self.BuildTreeMerkle(listaEncrypt,Merkle())

            buildTree = GraphMerkle(self.listaasignaciones,'Asignaciones')
            buildTree.generarFile()
            self.listaasignaciones.QuitarCeros()
        elif type == 10:
            self.id =1
            #Recuperacion de estado
            self.listaEstudiantes.rellenar()
            #lista que llevara los encabezados encriptados
            listaEncrypt = Merkle()
            #se hace un clon de la lista principal de data
            self.listaEstudiantes.clone(listaEncrypt)
            #se encrypta la lista de headers
            self.listaEstudiantes.Encrypt(listaEncrypt)
            self.putId(self.listaEstudiantes, listaEncrypt)

            
            self.BuildTreeMerkle(listaEncrypt,Merkle())

            buildTree = GraphMerkle(self.listaEstudiantes,'Estudiantes')
            buildTree.generarFile()
            self.listaEstudiantes.QuitarCeros()
            
            




    #CARGA DE CURSOS AL GRAFO   
    def putId(self,lista1,lista2):
        aux = lista1.first
        
        while aux != None:
            aux.id = self.id
            self.id +=1
            aux = aux.siguiente
        
        
        temp = lista2.first
        while temp != None:
            temp.id = self.id
            self.id+= 1
            temp = temp.siguiente


    def BuildTreeMerkle(self,listInit,finalList):
        if listInit.size == 1:
            return
        else:
            aux = listInit.first
            while aux != None:
                aux.data
                aux.siguiente.data
                data = aux.data + aux.siguiente.data
                h = hashlib.sha256(str(data).encode())
                nodo = NodoMerkle(h.hexdigest())
                nodo.id = self.id
                self.id += 1
                aux.arriba = nodo
                aux.siguiente.arriba = nodo
                finalList.Insertar(nodo)

                aux = aux.siguiente.siguiente
            self.BuildTreeMerkle(finalList,Merkle())


    def LoadCursos(self, curso):
        self.listacursos.InsertarCurso(curso)

    def GetCurso(self, codigo):
        return self.listacursos.getCurso(codigo)
        #self.treeB.insertar(curso)
    def AddCourseToStudent(self,carnet, anio, semester, course):

        if self.avl.search(int(carnet)):
            if self.avl.getStudent(int(carnet)).SearchYear(int(anio)):
                print("Inserto el año: "+str(anio))
                if self.avl.getStudent(int(carnet)).getYear(int(anio)).SearchSemester(int(semester)):
                    self.avl.getStudent(int(carnet)).getYear(int(anio)).getSemester(int(semester)).tree.insertar(course)
                    print('I maked to insertion')
                else:
                    print("No encontro el mes")
    def loadDataToAsignacion(self,data):
        nodo = NodoMerkle(data)
        self.listaasignaciones.Insertar(nodo)
        
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
    def getHomework(self,carnet,date,hour, position):

        if self.avl.search(carnet):
            if self.avl.getStudent(carnet).yearsList.SearchYear(date.year):
                if self.avl.getStudent(carnet).yearsList.getYear(date.year).SearchMounth(date.mounth):  
                    print("encontro el Mes:")
                    if self.avl.getStudent(carnet).yearsList.getYear(date.year).getMounth(date.mounth).matriz.getNodoTareas(hour, date.day) != None:

                        return self.methodaux(self.avl.getStudent(carnet).yearsList.getYear(date.year).getMounth(date.mounth).matriz.getNodoTareas(hour, date.day),position)
                    else:
                        return None
                    
        
    def methodaux(self, nodo,posicion):
        c = 1
        aux = nodo.first
        while aux != None:
            if c == posicion:
                return aux.getValue() 
            aux = aux.next
        
        return None
    def updateTask(self, task, position):
        if self.avl.search(task.carnet):
            if self.avl.getStudent(task.carnet).yearsList.SearchYear(task.date.year):
                if self.avl.getStudent(task.carnet).yearsList.getYear(task.date.year).SearchMounth(task.date.mounth):  
                    print("encontro el Mes:")
                    if self.avl.getStudent(task.carnet).yearsList.getYear(task.date.year).getMounth(task.date.mounth).matriz.getNodoTareas(task.hour, task.date.day) != None:
                        
                        self.methodaux(self.avl.getStudent(task.carnet).yearsList.getYear(task.date.year).getMounth(task.date.mounth).matriz.getNodoTareas(task.hour, task.date.day),position).name = task.name
                        self.methodaux(self.avl.getStudent(task.carnet).yearsList.getYear(task.date.year).getMounth(task.date.mounth).matriz.getNodoTareas(task.hour, task.date.day),position).description = task.description
                        self.methodaux(self.avl.getStudent(task.carnet).yearsList.getYear(task.date.year).getMounth(task.date.mounth).matriz.getNodoTareas(task.hour, task.date.day),position).materia = task.materia
                        self.methodaux(self.avl.getStudent(task.carnet).yearsList.getYear(task.date.year).getMounth(task.date.mounth).matriz.getNodoTareas(task.hour, task.date.day),position).state = task.state

    def deleteTask(self, carnet, date, hour, position):
        if self.avl.search(carnet):
            if self.avl.getStudent(carnet).yearsList.SearchYear(date.year):
                if self.avl.getStudent(carnet).yearsList.getYear(date.year).SearchMounth(date.mounth):  
                    print("encontro el Mes:")
                    if self.avl.getStudent(carnet).yearsList.getYear(date.year).getMounth(date.mounth).matriz.getNodoTareas(hour, date.day)!=None:
                        print()        
    def Autentication(self, carnet, pas):
        user = Student(0,"","","","","",0,0)
        user.userFound()
        user.usertype('None')
        if(carnet == "Admin" and pas =="Admin"):
            user.found = True
            user.usertype('Admin')
            return user
        else:
            carnet = int(carnet)
        
        
            if self.avl.search(carnet):
            #Arreglar condicional 
                print("FOUND STUDENT")
                h = hashlib.sha256(str(pas).encode())
                
                password = self.capa.decrypt(self.avl.getStudent(carnet).password).decode('utf-8')
                print("AVL: "+password+" Login: "+str(h.hexdigest()))
                if password == str(h.hexdigest()):
                #print("entro")
                    print("FOUND PASSWORD")
                    user.nameDES = self.capa.decrypt(self.avl.getStudent(carnet).name)
                    user = self.avl.getStudent(carnet)
                    user.usertype('Student')
                    user.found = True
                    return user
                return user
        
            return user
    
        
    def getNotes(self,carnet):
        return self.tablaHash.getLista(carnet)
    
    def createApunteMerkle(self, data):
        nuevo = NodoMerkle(data)
        self.listaApuntes.Insertar(nuevo)
    def getAllCursos(self):
        return self.listacursos
        
