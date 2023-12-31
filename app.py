from flask import Flask, render_template
from flask import Flask, jsonify
import requests
import json


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/comprar/<int:producto_id>')
def mostrar_producto(producto_id):
    producto = {
        'id': producto_id,
        'nombre': 'Producto',
        'precio': 50000,
        'descripcion': 'producto tipo'
    }
    return render_template('producto.html', producto=producto)

@app.route('/productos')
def productos():
    response = requests.get('https://musicpro.bemtorres.win/api/v1/bodega/producto')
    if response.status_code == 200:
        data = response.json()
        return render_template('productos.html', productos=data)
    else:
        return 'Error al obtener datos de la API'

if __name__ == '__main__':
    app.run()
