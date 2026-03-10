import time
from flask import Flask, jsonify, render_template, request


app = Flask(__name__)

@app.route('/ping')
def ping():
    return jsonify("pong")

@app.route('/ping_con_delay/<int:delay>')
def ping_con_delay(delay):
    time.sleep(delay)
    return jsonify('pong')

data = {
    "nombre": None,
    "apellido": None,
}

@app.route('/estudiantes')
def estudiantes():
    return jsonify({
        "nombre": data["nombre"],
        "apellido": data["apellido"]
    }), 200

@app.route('/estudiantes', methods=['POST'])
def crear_estudiantes():
    body = request.get_json( )
    data["nombre"] = body['nombre']
    data["apellido"] = body['apellido']
    return jsonify({
        "nombre": data["nombre"],
        "apellido": data["apellido"]
    }), 201

@app.route('/estudiantes/<nombre>', methods=['GET'])
def estudiantes_nombre(nombre):
    if nombre != data["nombre"]:
        return jsonify({"error": "no existe el estudiante"}), 404
    return jsonify({
        "nombre": data["nombre"],
        "apellido": data["apellido"],
    }),200


@app.route('/response')
def response():
    return jsonify("Datos adquiridos con éxito"),200

if __name__ == '__main__':
    app.run(port=8080, debug=True)