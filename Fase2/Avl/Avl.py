from Avl.Nodo import *
import os
from PIL import Image
'''class Nodo:
    def __init__(self,valor):
        self.valor = valor
        self.altura = 0
        self.izq = self.der = None*/'''
'''
class AVL:
    def __init__(self):
        self.raiz = None
    
    def MAX(self, val1, val2):
        if val1>val2:
            return val1
        else:
            return val2

    def insertar(self, valor):
        self.raiz = self.__insertar(valor, self.raiz)
    
    def __insertar(self, valor, raiz):
        if raiz == None:
            return Nodo(valor)
        else:
            if valor < raiz.valor:
                raiz.izq = self.__insertar(valor, raiz.izq)
                if(self.Altura(raiz.der) - self.Altura(raiz.izq) == -2):
                    if valor < raiz.izq.valor:
                        raiz = self.RI(raiz)
                    else:
                        raiz = self.RDI(raiz)
            elif valor > raiz.valor:
                raiz.der = self.__insertar(valor, raiz.der)
                if(self.Altura(raiz.der)- self.Altura(raiz.izq) == 2):
                    if valor > raiz.der.valor:
                        raiz = self.RD(raiz)
                    else:
                        raiz = self.RDD(raiz)
            else:
                raiz.valor = valor
        
        raiz.altura = self.MAX(self.Altura(raiz.izq), self.Altura(raiz.der))+1
        return raiz

    def Altura(self, nodo):
        if nodo != None:
            return nodo.altura
        return -1

    def RI(self, nodo):
        aux = nodo.izq
        nodo.izq = aux.der
        aux.der = nodo
        nodo.altura = self.MAX(self.Altura(nodo.der), self.Altura(nodo.izq))+1
        aux.altura = self.MAX(self.Altura(aux.izq), nodo.altura)+1
        return aux
    
    def RD(self, nodo):
        aux = nodo.der
        nodo.der = aux.izq
        aux.izq = nodo
        nodo.altura = self.MAX(self.Altura(nodo.der), self.Altura(nodo.izq))+1
        aux.altura = self.MAX(self.Altura(aux.der), nodo.altura)+1
        return aux

    def RDI(self, nodo):
        nodo.izq = self.RD(nodo.izq)
        return self.RI(nodo)
    
    def RDD(self, nodo):
        nodo.der = self.RI(nodo.der)
        return self.RD(nodo)

    def print(self):
        print ("el valor de la raiz: "+str(self.raiz.valor))
        self.__in(self.raiz)
    
    def __in(self, nodo):
        if nodo:
            self.__in(nodo.izq)
            print("Valor:", nodo.valor)
            self.__in(nodo.der)
    def __inOrden(self, nodo, file):
        if nodo:
            self.__inOrden(nodo.izq,file)
            file.write("node [shape = circle label = \""+str(nodo.valor)+"\"] "+str(nodo.valor)+"\n")
            #print("Valor:", nodo.valor)
            self.__inOrden(nodo.der,file)
    def mappear(self, nodo, file):
        if nodo.izq:
            file.write(str(nodo.valor)+" -> "+str(nodo.izq.valor)+" \n")
            self.mappear(nodo.izq,file)
        if nodo.der:
            file.write(str(nodo.valor)+" -> "+str(nodo.der.valor)+" \n")
            self.mappear(nodo.der,file)

    def createTree(self):
        file = open("avl.dot","w")
        file.write("digraph AVL{\n")
        # file.write("node [shape = circle label = \""+str(self.raiz.valor)+"\"] "+str(self.raiz.valor)+"\n")
        self.__inOrden(self.raiz,file)
        self.mappear(self.raiz,file)
        file.write("\n}")
        file.close()
'''
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
    def createTree(self):
        file = open("/home/losa/Escritorio/Reportes_F2/avl.dot","w")
        file.write("digraph AVL{\n")
        # file.write("node [shape = circle label = \""+str(self.raiz.valor)+"\"] "+str(self.raiz.valor)+"\n")
        self.__inOrden(self.root,file)
        self.mappear(self.root,file)
        file.write("\n}")
        file.close()
        prog = "dot -Tpng /home/losa/Escritorio/Reportes_F2/avl.dot -o /home/losa/Escritorio/Reportes_F2/avl.png"
        os.system(prog)
        im = Image.open('/home/losa/Escritorio/Reportes_F2/avl.png')
        im.show()
    def __inOrden(self, nodo, file):
        if nodo:
            self.__inOrden(nodo.left,file)
            file.write("node [shape = circle label = \""+str(nodo.getStudent().getCarnet())+"\\n"+nodo.getStudent().getName()+"\\n"+nodo.getStudent().getCarrera()+"\"] "+str(nodo.getStudent().getCarnet())+"\n")
            #print("Valor:", nodo.valor)
            self.__inOrden(nodo.right,file)
    def mappear(self, nodo, file):
        if nodo.left:
            file.write(str(nodo.getStudent().getCarnet())+" -> "+str(nodo.left.getStudent().getCarnet())+" \n")
            self.mappear(nodo.left,file)
        if nodo.right:
            file.write(str(nodo.getStudent().getCarnet())+" -> "+str(nodo.right.getStudent().getCarnet())+" \n")
            self.mappear(nodo.right,file)