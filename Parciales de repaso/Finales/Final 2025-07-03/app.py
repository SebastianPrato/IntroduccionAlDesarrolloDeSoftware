#Ejericio 1

from pydoc import text
from flask import Flask, jsonify, request
import requests

app = Flask(__name__)


#a)
@app.route('/socios', methods=["GET"])
def listar_socios():
    conn = engine.connect()

    query = f"""
            SELECT *
            FROM socios
            """
    
    try: 
        result = conn.execute(text(query))
        conn.close()
    except SQLAlchemyError as err:
        return jsonify(str(err.__cause__))
    #Se preparan los datos para ser mostrados como json
    data = []
    for row in result:
        entity = {}
        entity['id_socio'] = row.id_socio
        entity['nombre'] = row.nombre
        entity['apellido'] = row.apellido
        entity['categoria'] = row.categoria
        entity['deuda'] = row.deuda
        data.append(entity)
    
    return jsonify(data), 200

#b) El try Except es correcto, intenta ejecutar una query a la bbdd y captura los posibles errores en caso de que hayan problemas con la ejecución de la misma. Por su parte, en la linea 36 (seguramente el exámen se equivoco con el número de linea, pues preguntan por el 200 que es el código de la response html) se encarga de devolver los datos recopilados en formato de json, el 200 es un código de status http que significa el resultado de la solicitud fue ok

#c)
@app.route('/socios', methods=["POST"])
def agregar_socios():
    conn = engine.connect()
    body_data = requests.get_json()

    query = f"""
            INSERT INTO socios (nombre, apellido, categoria, deuda)
            VALUES ({body_data[nombre]}, {body_data[apellido]}, {body_data[categoria]}, {body_data[deuda]})
            """
    
    try: 
        conn.execute(text(query))
        conn.commit()
        conn.close()
    except SQLAlchemyError as err:
        return jsonify(str(err.__cause__))
    #Se preparan los datos para ser mostrados como json
    return jsonify({"message": "Se ha añadido un nuevo socio"}), 201

#d)
@app.route('/socios/<int:id>', methods=['PUT'])
def update_socio(id):
    conn = engine.connect()
    body_data = requests.get_json()
    query = f"""
            UPDATE socios
            SET nombre = {body_data["nombre"]}, 
                apellido = {body_data["apellido"]}, 
                categoria = {body_data["categoria"]}, 
                deuda = {body_data["deuda"]}
            WHERE id_socio = {id}
            """
    query_validation = f"SELECT * FROM socios WHERE id_socio = {id}"

    try: 
        val_result = conn.execute(text(query_validation))
        if val_result.rowcount!=0:
            result = conn.execute(text(query))
            conn.commit()
            conn.close()
        else:
            conn.close()
            return jsonify({"message": "Error: El id ingresado no pertenece a ningún socio del registro"}), 404
    except SQLAlchemyError as err:
        return jsonify({"message": str(err.__cause__)})
    return jsonify({"message": "Se ha modificado el registro correctamente" + query}), 200

#La linea 76 el comit confirma los cambios realizados por el update y los guarda en la base
#La linea 77 cierra la conexión, es importante para evitar problemas de rendimiento y seguridad y para liberar los recursos del servidor.

#Ejercicio 2:
#No tengo mucho tiempo asi que lo haré corto escribiendo las respuestas directamente:
#Teniendo API_URL="http:127.....:5001"
#response = request.get("http:localhost:5001/socios/")
#y el render_template debe cargar index.html

{% for socio in socios %}
    {{socio.id_socio}}
    {{socio.nombre}}
    {{socio.apellido}}
    {{socio.categoria}}
    {{socio.deuda}}
{% endfor %}

# para que deuda apareza en rojo hay que agregar ' style="color:red' dentro de la etiqueta td de deuda

"""
ejercicio 3:
Git branch testing crea una nueva rama llamada testing
Git checkout testing cambia nuestra ubicación de la rama en la que estemos a la rama testing
Docker es una herramienta que se usa para poder hacer que nuestro código sea legible en diferentes ordenadores y sistemas de forma tal que se encarga de lo que es el manejo de dependencias y servidores para facilitar los deeploys y la integración a otros sistemas mediante un sistema de imagenes y contenedores
"""
if __name__ == '__main__':
    app.run(port=5001)