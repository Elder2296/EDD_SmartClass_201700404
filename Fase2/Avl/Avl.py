from Avl.Nodo import *
import os
from PIL import Image
from cryptography.fernet import Fernet

class AVL():
    def __init__(self):
        self.root = None
        self.find = False  
        self.find2 = 0  
    def Max(self, carnet1, carnet2):
        if carnet1 > carnet2:
            return carnet1
        else:
            return carnet2
    def Insert(self, student):
        #print("NAME STUDENT: "+student.name)
        self.root = self.Insert2(student, self.root)
    

    def Insert2(self, student, root):


        if root == None:
            return Nodo(student)
        else:
            if student.getCarnet() < root.getStudent().getCarnet():

                root.left = self.Insert2(student,root.left)

                if(self.Heigth(root.right)- self.Heigth(root.left)==-2):

                    if student.getCarnet() < root.left.getStudent().getCarnet():

                        root = self.RotationLeft(root)
                    else:
                        root = self.RotationDoubleLeft(root)

            elif student.getCarnet() > root.getStudent().getCarnet():
                root.right = self.Insert2(student,root.right)

                if(self.Heigth(root.right)- self.Heigth(root.left)==2):
                    if student.getCarnet() > root.right.getStudent().getCarnet():
                        root = self.RotationRight(root)
                    else:
                        root = self.RotationDoubleRight(root)
            else:
                root.student = student
        root.heigth = self.Max(self.Heigth(root.left), self.Heigth(root.right))+1
        return root


    def Heigth(self, nodo):
        if nodo != None:
            return nodo.heigth
        return -1


    def RotationLeft(self, nodo):
        aux = nodo.left
        nodo.left = aux.right
        aux.right = nodo
        nodo.heigth = self.Max(self.Heigth(nodo.right), self.Heigth(nodo.left))+1
        aux.heigth = self.Max(self.Heigth(aux.left),nodo.heigth)+1
        return aux


    def RotationRight(self, nodo):
        aux = nodo.right
        nodo.right = aux.left
        aux.izq = nodo
        nodo.heigth = self.Max(self.Heigth(nodo.right), self.Heigth(nodo.left))+1
        aux.heigth = self.Max(self.Heigth(aux.right), nodo.heigth)+1
        return aux
    


    def RotationDoubleLeft(self,nodo):
        nodo.left = self.RotationRight(nodo.left)
        return self.RotationLeft(nodo)
    
    def RotationDoubleRight(self,nodo):
        nodo.right = self.RotationLeft(nodo.right)
        return self.RotationRight(nodo)


   
    def search(self,carnet):
        self.encontrarStudiante(self.root, carnet)
        #print("Resultado de la busqueda: "+str(self.find))
        return self.find
    def encontrarStudiante(self, nodo,carnet1):
        #print("from avl")
        #print(str(nodo.getStudent().carnet)+"---"+str(type(nodo.getStudent().carnet))+" *** " +str(carnet1)+"---"+str(type(carnet1)))
        
        if(nodo.getStudent().carnet == carnet1):
            #print("ENCONTRO A ESTUDIANTES CON CARNET: "+str(nodo.getStudent().carnet))
            
            self.find = True
            
        
        if(nodo.getStudent().carnet < carnet1):
            if (nodo.right == None):
                self.find = False
            else:
                self.encontrarStudiante(nodo.right, carnet1)
        if(nodo.getStudent().carnet > carnet1):
            if (nodo.left == None):
                self.find = False
            else:
                self.encontrarStudiante(nodo.left, carnet1)

    
    def searchStudent(self,nodo, carnet):
        
        if(nodo.getStudent().getCarnet() == carnet):
            #print("FIND STUDENT  type: "+str(type(nodo.getStudent())))
            return nodo.getStudent()
            
        elif (nodo.getStudent().getCarnet() < carnet):
            return self.searchStudent(nodo.right,carnet)
        elif (nodo.getStudent().getCarnet() > carnet):
            return self.searchStudent(nodo.left,carnet)
        '''if(self.find2 == 1):
            print("SE LE AGREGARAN ANIOS A EL CARNET: "+str(nodo.getStudent().carnet))
            self.find2 = 0
            return nodo.getStudent()'''

    def getStudent(self,carnet):
        #print("from method GETSTUDENT *** "+str(type(self.searchStudent(self.root,carnet))))
        return self.searchStudent(self.root,carnet)
            
    


    


    def print(self):
        self.__in(self.root)

    def __in(self,nodo):
        if nodo:
            self.__in(nodo.left)
            print(nodo.getStudent().getCarnet())
            self.__in(nodo.right)


    def PrintYears(self):
        self.Enorden(self.root)    


    def Enorden(self, nodo):
        if nodo:
            self.Enorden(nodo.left)
            print("LIST YEARS of "+str(nodo.getStudent().carnet)+" size: "+str(nodo.getStudent().yearsList.size))
            nodo.getStudent().yearsList.Print()
            
            self.Enorden(nodo.right)
    def createTree(self,clave):
        file = open("/home/losa/Escritorio/Reportes_F3/avl.dot","w")
        file.write("digraph AVL{\n")
        # file.write("node [shape = circle label = \""+str(self.raiz.valor)+"\"] "+str(self.raiz.valor)+"\n")
        self.__inOrden(self.root,file,clave)
        self.mappear(self.root,file)
        file.write("\n}")
        file.close()
        prog = "dot -Tpng /home/losa/Escritorio/Reportes_F3/avl.dot -o /home/losa/Escritorio/Reportes_F3/avl.png"
        os.system(prog)
        im = Image.open('/home/losa/Escritorio/Reportes_F3/avl.png')
        im.show()

    def createTreeDes(self,clave):
        file = open("/home/losa/Escritorio/Reportes_F3/avlDES.dot","w")
        file.write("digraph AVL{\n")
        # file.write("node [shape = circle label = \""+str(self.raiz.valor)+"\"] "+str(self.raiz.valor)+"\n")
        self.__inOrdenDES(self.root,file,clave)
        self.mappear(self.root,file)
        file.write("\n}")
        file.close()
        prog = "dot -Tpng /home/losa/Escritorio/Reportes_F3/avlDES.dot -o /home/losa/Escritorio/Reportes_F3/avlDES.png"
        os.system(prog)
        im = Image.open('/home/losa/Escritorio/Reportes_F3/avlDES.png')
        im.show()

    def __inOrdenDES(self, nodo, file,clave):
        if nodo:
            self.__inOrdenDES(nodo.left,file,clave)
            self.capa = Fernet(clave)

            dpi =self.capa.decrypt(nodo.getStudent().dpi)
            name = self.capa.decrypt(nodo.getStudent().getName())
            password = (self.capa.decrypt(nodo.getStudent().password))
            file.write("node [shape = box label = \""+str(nodo.getStudent().carnet)+"\\n"+dpi.decode('utf-8')+"\\n"+name.decode('utf-8')+"\\n"+nodo.getStudent().getCarrera()+"\\n"+password.decode('utf-8')+"\"] "+str(nodo.getStudent().getCarnet())+"\n")
            #print("Valor:", nodo.valor)
            self.__inOrdenDES(nodo.right,file,clave)

        

        


    def __inOrden(self, nodo, file,clave):
        if nodo:
            self.__inOrden(nodo.left,file,clave)
            self.capa = Fernet(clave)
            id = self.capa.encrypt(str(nodo.getStudent().getCarnet()).encode())
            carnet =id.decode('utf-8')[0:10]
            dpi = nodo.getStudent().dpi.decode('utf-8')[0:10]
            name = nodo.getStudent().getName().decode('utf-8')[0:10]
            carrera = nodo.getStudent().getCarrera()
            pasword = nodo.getStudent().password.decode('utf-8')[0:10]
            file.write("node [shape = box label = \""+carnet+"\\n"+dpi+"\\n"+name+"\\n"+carrera+"\\n"+pasword+"\"] "+str(nodo.getStudent().getCarnet())+"\n")
            #print("Valor:", nodo.valor)
            self.__inOrden(nodo.right,file,clave)
    def mappear(self, nodo, file):
        if nodo.left:
            file.write(str(nodo.getStudent().getCarnet())+" -> "+str(nodo.left.getStudent().getCarnet())+" \n")
            self.mappear(nodo.left,file)
        if nodo.right:
            file.write(str(nodo.getStudent().getCarnet())+" -> "+str(nodo.right.getStudent().getCarnet())+" \n")
            self.mappear(nodo.right,file)