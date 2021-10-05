from io import TextIOWrapper
from flask import Flask, json, jsonify, request

app = Flask(__name__)

from products import products
from Loads  import *

principal = Load()
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
    return jsonify({'message': 'Product Not found'})




@app.route('/carga', methods=['POST'])
def Load():
    tipo = request.json['tipo'],
    path =request.json['path']
    print("tipo: "+str(tipo))
    principal.loadStudents(str(path))
    #print()
    
    return jsonify({'message':'Load succesfully'})

@app.route('/reporte', methods=['GET'])
def getGrafo():
    tipo = request.json['tipo']
    if tipo == 0:
        principal.Reports(tipo,None)
    elif tipo == 1:
        peticion =[
            request.json['carnet'],
            request.json['año'],
            request.json['mes']
        ]
        principal.Reports(tipo,peticion)

    print("tipo de reporte: "+str(tipo))
    return jsonify({'message': 'report type'})




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
        })
if __name__ == '__main__':
    app.run(debug=True, port = 3000)