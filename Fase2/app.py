from multiprocessing import Process
from flask import Flask, json, jsonify, request
from flask_cors import CORS

from Homeworks.Date import Date
from Grafo.Curso import Curso
from Homeworks.homework import Homework


app = Flask(__name__)

from products import products
from Loads  import *

principal = Load()
'''
@app.route('/ping')
def ping():
    return jsonify({"message": "pong!!!"})
@app.route('/products')
def getProducts():
    return jsonify({"products": products, "xmessage": "products"})

@app.route('/products/<string:product_name>')
def getProduct(product_name):
    productsFound = [
        product for product in products if product['name'] == product_name.lower()]
    if (len(productsFound) > 0):
        return jsonify({'product': productsFound[0]})
    return jsonify({'message': 'Product Not found'})'''




@app.route('/carga', methods=['POST'])
def Load():
    tipo = request.json['tipo'],
    path =request.json['path']
    print("tipo: "+str(tipo))
    principal.loadStudents(str(path))
    #print()
    
    return jsonify({'message':'Load succesfully'})

@app.route('/reporte', methods=['POST'])
def getGrafo():
    
    tipo = request.json['tipo']
    if tipo == 0:
        peticion =[request.json['opcion']]
        principal.Reports(tipo,peticion)
    elif tipo == 1:
        peticion =[
            request.json['carnet'],
            request.json['año'],
            request.json['mes']
        ]
        principal.Reports(tipo,peticion)

    elif tipo== 2:
        peticion = [
            request.json['carnet'],
            request.json['año'],
            request.json["mes"],
            request.json["dia"],
            request.json["hora"]
        ]
        principal.Reports(tipo,peticion)
    elif tipo == 3:
        principal.Reports(tipo,None)
    elif tipo == 4:
        peticion = [
            request.json['carnet'],
            request.json['año'],
            request.json['semestre']
        ]
        principal.Reports(tipo,peticion)
    elif tipo == 5:
        peticion = request.json['Codigo']
        principal.Reports(tipo,peticion)
    elif tipo ==6:
        principal.Reports(tipo,None) 

    elif tipo == 7:
        principal.Reports(tipo,None)
    elif tipo == 8:
        principal.Reports(tipo,None)
    elif tipo == 9:
        principal.Reports(tipo,None)
    elif tipo == 10:
        principal.Reports(tipo,None)
       
    print("tipo de reporte: "+str(tipo))
    return jsonify({'message': 'report type'})

@app.route('/cursosPensum', methods = ['POST'])
def LoadPensum():
    cursos = request.json['Cursos']
    for curso in cursos:
        materia = Curso(curso['Codigo'],curso['Nombre'],curso['Creditos'],curso['Prerequisitos'],curso['Obligatorio'])
        principal.LoadCursos(materia)
        #print("Codigo: ", curso['Codigo'])
        #print("Nombre: ", curso['Nombre'])
    return jsonify({'message':'load succes'})
@app.route('/cursosEstudiante', methods=['POST'])
def LoadCoursesStudent():
    students = request.json['Estudiantes']
    for student in students:
        print("\n\nCarnet: "+student['Carnet'])
        
        years = student['Años']
        for year in years:
            print('Year: '+ year['Año'])
            semesters = year['Semestres']
            for semester in semesters:
                print('Semestre: '+ semester['Semestre'])
                cursos = semester['Cursos']
                for curso in cursos:
                    print('Codigo Curso: '+curso['Codigo'])
                    course = Curso(curso['Codigo'],curso['Nombre'],curso['Creditos'],curso['Prerequisitos'],curso['Obligatorio'])
                    #principal.AddCourseToStudent(student['Carnet'],year['Año'],semester['Semestre'],course)
        
    
    
    return jsonify({'message': 'Load courses succesfuly'})

@app.route('/estudiantes',methods=['POST'])
def createStudent():
    estudiantes = request.json['estudiantes']
    for estudiante in estudiantes:

        carnet = int(estudiante['carnet'])
        dpi = str(estudiante['DPI'])
        nombre = estudiante['nombre']
        carrera = estudiante['carrera']
        email = estudiante['correo']
        pas = estudiante['password']
        creditos = 0
        edad = estudiante['edad']
        
        data = str(carnet)+"--"+dpi+"--"+nombre
        principal.createStudent(carnet,dpi,nombre,carrera,email,pas,creditos,edad,data)
    
    return jsonify({'message':'create student succesfuly'})


@app.route('/estudiante',methods=['POST'])
def createStuden():
    carnet = int(request.json['carnet'])
    dpi = str( request.json['DPI'])
    nombre = request.json['nombre']
    carrera = request.json['carrera']
    email = request.json['correo']
    pas = request.json['password']
    creditos = 0
    edad = request.json['edad']
    
    data = str(carnet)+"--"+dpi+"--"+nombre
    principal.createStudent(carnet,dpi,nombre,carrera,email,pas,creditos,edad,data)
    return jsonify({'message':'create student succesfuly'})

@app.route('/estudiante',methods = ['PUT'])
def updateStudent():
    carnet = int(request.json['carnet'])
    dpi = request.json['DPI']
    nombre = request.json['nombre']
    carrera = request.json['carrera']
    email = request.json['correo']
    pas = request.json['password']
    creditos = request.json['creditos']
    edad = request.json['edad']
    student = Student(carnet,dpi,nombre,carrera,email,pas, creditos,edad)
    principal.updateStudent(student)
    return jsonify({'message':'update student succesfuly'})

@app.route('/estudiante', methods = ['GET'])
def getStudent():
    carnet = request.json['carnet']
    student = principal.getStudent(int(carnet))
    carnet = student.carnet
    dpi = student.dpi
    nombre= student.name
    carrera = student.carrera
    email = student.email
    pas = student.password
    credits = student.credits
    age = student.age 

    return jsonify({'carnet':carnet,'dpi':dpi,'nombre':nombre,'carrera':carrera,'email':email,'password': pas,'creditos':credits,'edad':age})

@app.route('/recordatorio',methods = ['POST'])
def AddHomework():
    carnet = request.json['Carnet']
    name = request.json['Nombre']
    desc = request.json['Descripcion']
    materia = request.json['Materia']
    date = request.json['Fecha']
    hour = request.json['Hora']
    state = request.json['Estado']
    task = Homework(carnet,name,desc,materia,date,hour,state)

    principal.AddHomework(task)
    return jsonify({'message':'sucess'})


@app.route('/recordatorio', methods = ['GET'])
def getHomework():
    carnet = request.json['Carnet']
    f = request.json['Fecha']
    h = request.json['Hora']
    position = request.json['Posicion']
    arreglo = f.split(sep='/')
    day = int(arreglo[0])
    mounth = int(arreglo[1])
    year = int(arreglo[2])
    date = Date(day,mounth,year)
    arreglo2 = h.split(sep = ':')
    hour = int(arreglo2[0])
    if principal.getHomework(int(carnet),date,hour,position) != None:

        task = principal.getHomework(int(carnet),date,hour,position)
        carnet = task.carnet
        name = task.name
        desc = task.description
        materia = task.materia
        date2 = task.date.getDate()
        hour2 = task.hour
        state = task.state
        return jsonify({'carnet':carnet, 'name':name,'description':desc,'materia': materia,'fecha':date2,'hora':hour2,'estado':state})
    else:
        return jsonify({'message':'Not found'})

@app.route('/recordatorio', methods = ['PUT'])
def updateHomework():
    carnet = request.json['Carnet']
    nombre = request.json['Nombre']
    desc = request.json['Descripcion']
    materia = request.json['Materia']
    fecha = request.json['Fecha']
    hora = request.json['Hora']
    estado = request.json['Estado']
    posicion = request.json['Posicion']
    task = Homework(int(carnet),nombre,desc,materia,fecha,hora,estado)
    principal.updateTask(task,posicion)
    return jsonify({'message':'success'})
@app.route('/recordatorio', methods = ['DELETE'])
def deleteHomework():
    carnet = request.json['Carnet']
    f = request.json['Fecha']
    hour = request.json['Hora']
    position = request.json['Posicion']


    arreglo = f.split(sep='/')
    day = int(arreglo[0])
    mounth = int(arreglo[1])
    year = int(arreglo[2])
    date = Date(day,mounth,year)
@app.route('/Autentication', methods ={'POST'})
def Autentication():
    carnet = request.json['CARNET']
    password = request.json['PASS']
    user = principal.Autentication(carnet,password)
    return jsonify({'found':user.found,'tipo': user.type,'name':user.nameDES,'carnet':user.carnet})

@app.route('/Apuntes', methods = {'POST'})
def createNote():
    carnet = request.json['CARNET']
    title = request.json['TITULO']
    content = request.json['CONTENIDO']
    print("Carnet:"+ str(carnet)+"\nTITULO: "+str(title)+"\nCONTENIDO: "+str(content))
    data = str(carnet) +"--"+title+"--"+content
    principal.loadApunte(carnet,title,content,data)
    return jsonify({'server message':'succesfully'})


@app.route('/cargarapuntes', methods ={'POST'})
def loadapuntes():
    usuarios = request.json['usuarios']
    for usuario in usuarios:
        carnet = usuario['carnet']
        apuntes = usuario['apuntes']
        for apunte in apuntes:
            titulo = apunte['Título']
            contenido = apunte['Contenido']
            data = str(carnet) +"--"+titulo+"--"+contenido
            principal.loadApunte(carnet,titulo,contenido,data)
    

    return jsonify({'server message':'succesfully'})


@app.route('/listaapuntes', methods = {'POST'})
def Arryapuntes():
    carnet = request.json['carnet']
    result=[]
    lista = principal.getNotes(carnet)

    aux = lista.first

    while aux!= None:
        nota = {
            'titulo':aux.note.title,
            'contenido': aux.note.content,
        }
        result.append(nota)
        aux = aux.siguiente



    return jsonify({'Notas':result})
@app.route('/cursos',methods = {'POST'})
def getCursos():    
    lista = principal.getAllCursos()
    result = []
    aux = lista.first
    while aux != None:
        curso ={
            'curso': str(aux.curso.Codigo)+'--'+aux.curso.nombre
        }
        result.append(curso)
        aux = aux.siguiente
    
    return jsonify({'Cursos':result})
    
@app.route('/Asignar',methods ={'POST'})
def Asignar():
    carnet = request.json['Carnet']
    semestre = request.json['Semestre']
    año = request.json['Anio']
    cursos = request.json['Cursos']
    codigos=""
    print(semestre)
    array = semestre.split(sep='-')
    print("Carnet: "+str(carnet)+" semestre: "+str(array[1])+" Año: "+ año)
    for curso in cursos:
        arreglo= curso.split(sep='--')
        codigo = arreglo[0]
        codigos+=codigo+"//"
        print("codigo de curso: "+codigo)
        id = int(codigo)
        curso = principal.GetCurso(id)
        principal.AddCourseToStudent(carnet,año,str(array[1]),curso)
    data = str(carnet)+"--"+str(año)+"--"+str(semestre)+"--"+str(codigos)
    principal.loadDataToAsignacion(data)
    return jsonify({'message':'succesfully'})

'''

@app.route('/products', methods=['POST'])
def addProduct():
    new_product = {
        'name': request.json['name'],
        'price': request.json['price'],
        'quantity': request.json['quantity']
    }
    products.append(new_product)
    return jsonify({'message':'product added succesfully','products': products})
# Update Data Route
@app.route('/products/<string:product_name>', methods=['PUT'])
def editProduct(product_name):
    productsFound = [product for product in products if product['name'] == product_name]
    if (len(productsFound) > 0):
        productsFound[0]['name'] = request.json['name']
        productsFound[0]['price'] = request.json['price']
        productsFound[0]['quantity'] = request.json['quantity']
        return jsonify({
            'message': 'Product Updated',
            'product': productsFound[0]
        })
    return jsonify({'message': 'Product Not found'})

@app.route('/products/<string:product_name>', methods=['DELETE'])
def deleteProduct(product_name):
    productsFound = [product for product in products if product['name'] == product_name]
    if len(productsFound) > 0:
        products.remove(productsFound[0])
        return jsonify({
            'message': 'Product Deleted',
            'products': products
        })'''
if __name__ == '__main__':
    

    
    CORS(app)
    

    app.run(debug=True, port = 3000)
    
    



"""
Enable CORS. Disable it if you don't need CORS
https://parzibyte.me/blog
"""
