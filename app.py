from flask import Flask, render_template
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/producto/<int:producto_id>')
def mostrar_producto(producto_id):
    producto = {
        'id': producto_id,
        'nombre': 'Producto',
        'precio': 9.99,
        'descripcion': 'ejemplo de producto'
    }
    return render_template('producto.html', producto=producto)

if __name__ == '__main__':
    app.run()
