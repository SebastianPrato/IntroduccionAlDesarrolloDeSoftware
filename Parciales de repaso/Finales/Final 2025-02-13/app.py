#Parte 1:

from pydoc import text
from flask import Flask, jsonify, render_template, request
import requests

app = Flask(__name__)


#a i
@app.route('/articles', methods=["GET"])
def listar_art():
    conn = engine.connect()

    query = "FROM products SELECT *"

    try:
        result = conn.execute(text(query))
        conn.close()
    except SQLAlchemyError as err:
        return jsonify(str(err.__cause__))
    
    #se preparan los datos para ser mostrados como json
    data = []
    for row in result:
        entity = {}
        entity['id_art'] = row.id_art
        entity['description'] = row.description
        entity['price'] = row.price
        entity['stock'] = row.stock
        data.append(entity)
    
    return jsonify(data), 200
#a ii
#Esta linea devuelve los datos que fueron recopilados en data en forma de Json, el 200 es un código de estado HTTP que refleja que resultado de la solicitud fue ok

#b) decorador y sentencia para eliminar productos:
@app.route('/articulos/<int: id>', methods=['DELETE'])
def eliminar_art(id):
    conn = engine.connect()

    query = f"DELETE FROM products WHERE id_art = {id}"

    try:
        result = conn.execute(text(query))
        conn.close()
    except SQLAlchemyError as err:
        return jsonify(str(err.__cause__))
    return jsonify({"message": "Se ha eliminado el producto con éxito"}),200

#c i)
@app.route('/new_article', methods=['POST'])
def new_article():
    conn = engine.connect()
    new_user = request.get_json()

    query = f"""
            INSERT INTO products (description, price, stock)
            VALUES ({new_user['description']}, {new_user['price']}, {new_user['stock']})"""
    try: 
        result = conn.execute(text(query))
        conn.commit()
        conn.close()
    except SQLAlchemyError as err:
        print("error", err.__cause__)
        return jsonify({'message': 'Se ha producido un error' + str(err.__cause__)})
    return jsonify({'message': 'Se ha cargado correctamente' + query}), 201

# c ii) Las lineas 62 y 63 son para comitear la ejecución de la query, es decir, volvera efectiva, y para cerrar la conexión.

#d i)
@app.route('/articles/<id_art>', methods=["PUT"])
def actualizar_articulo(id, precio, stock, descripcion):
    conn = engine.connect()

    #d ii)
    query = f"""
            UPDATE products 
            SET descripcion = {descripcion}, 
                precio = {precio}, 
                stock = {stock}
            WHERE id_art = {id}
            """
    try:
        result = conn.execute(text(query))
        conn.close()
    except SQLAlchemyError as err:
        return jsonify(str(err.__cause__))
    return jsonify({"message": "Se ha actualizado el producto exitosamente"}), 200


#Ejericio 2:

@app.route("/producto/<id_art>", methods=["GET"])
def detail(id_art):
    try:
        response = request.get(f"{API_URL}/article/{id_art}")
        response.raise_for_status()
        data = response.json()
    except requests.exception.RequestException as e:
        print(f"Error fetching data: {e}")
        data = []
    return render_template('detail.html', data=data)
"""
Explicación general:

El try intenta hacer una petición a la API para obtener los datos del artículo.
El except captura errores (como que no exista el ID o haya problemas de red) y permite mostrar un mensaje de error o redirigir sin que la app se caiga.
"""                    
#c el codigo necesario para que el precio sea de color rojo es ' style="color: red" como atributo dentro de la etiqueta span que contiene el precio en el html'


"""
Ejercicio 3:

a) git fetch: 
Comando usado para traer los cambios del repositorio remoto al repositorio local

b) git branch testing:
Esta sentencia sirve para crear una rama testing

c) git push origin master
Esta sentencia sirve para subir la rama master local al repositorio remoto origin
"""

if __name__ == '__main__':
    app.run(debug=True)